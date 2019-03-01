import json
from lxml import etree
import logging
import warnings
from extras import doc2words
#from allennlp.predictors.predictor import Predictor
# For freebase topic detection:
import requests
from SPARQLWrapper import SPARQLWrapper, JSON
import anaphora_model
import e2eCoref as e2e



def run_test(predictor_, rel_path, save2json):
    # save2json: Toggle save to json. Should be True by default.
    # rel_path: Set to the relative path of the article (words xml) you want to test predictions for

    basepath = './WikiCoref/Annotation/'

    xml_path = basepath + rel_path  # concatenate base and relative paths to get total path from current dir to xml
    name = rel_path[:rel_path.find('/')]  # just extracting the article's name

    list_words = doc2words(xml_path)  # reading xml document into list of strings/words

    # Running the predictor on the list of words:
    #results = predictor_.predict_tokenized(list_words)
    text = anaphora_model.wordlist_to_block(list_words)
    results = e2e.demo.make_and_get_predictions_list(text)

    if save2json:
        json.dump(results, open(name + '_AllenPrediction.json', 'w'))


def compare_json2xml(attribute, path2predictedJSON, path2trueXML):
    return (count_in_json(attribute, path2predictedJSON),count_in_xml(attribute, path2trueXML))


def count_in_json(attribute, path2json):
    try:
        loaded_json = json.load(open(path2json, 'r'))
        if attribute == 'coref_class':
            return len(loaded_json['clusters'])
        elif attribute == 'span':
            return len(loaded_json['top_spans'])
        else:
            return 0
    except:
        raise ValueError('File not found.')


def count_in_xml(attribute, path2xml):
    try:
        root = etree.parse(path2xml).getroot()
        if attribute == 'coref_class':
            classes = set()
            for element in root:
                classes.add(element.get(attribute))
            return len(classes)
        elif attribute == 'span':
            return len(list(root))
        else:
            return 0
    except:
        raise ValueError('File not found.')


def spans_w_coref(path2json):
    try:
        loaded_json = json.load(open(path2json, 'r'))
        span_dict = {}
        # placeholder nills to all spans to maintain the order:
        for span in loaded_json['top_spans']:
            span_dict[str(span)] = None
        # add coref_class value to spans/keys in the dictionary:
        clusters = loaded_json['clusters']
        for i in range(len(clusters)):
            # we are exploring the i-th cluster:
            for span in clusters[i]:
                span_label = '[' + str(span[0]) + ', ' + str(span[1]) + ']'
                span_dict[span_label] = str(i)
        # keep only necessary entries, in a new dict:
        _dict = {}
        for key in span_dict:
            if span_dict[key] is not None:
                _dict[key] = span_dict[key]
        return _dict
    except:
        raise ValueError('File not found.')


def export2xml(path2json, destination):
    markables = etree.Element('markables', {'xmlns': "www.eml.org/NameSpaces/coref"})
    id = 0
    spans_dict = spans_w_coref(path2json)
    for span in spans_dict:
        span_label = 'word_' + str(int(span[1:span.find(',')])+1) + '..word_' + str(int(span[span.find(',')+1:-1])+1)
        markable = etree.Element('markable', {'id': str(id), 'span': span_label})
        markable.set('coref_class', "set_"+spans_dict[span])
        # TO-DO: Place here the in-between tags, in order.
        markable.set('mmax_level', 'coref')
        markables.append(markable)
        id += 1
    #with open('./TestOutput/Markables/Barack Obama_coref_level.xml', 'wb') as f:
    with open(destination + 'coref_predictions.xml', 'wb') as f:
        f.write(etree.tostring(markables, pretty_print=True, encoding="utf-8", method="xml", doctype='<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE markables SYSTEM "markables.dtd">'))


# Returns a set with all values that show up for a tag in an xml:
def xml_tag_values2set(tag, path2xml):
    try:
        tag_vals = set()
        root = etree.parse(path2xml).getroot()
        for element in root:
            tag_vals.add(element.get(tag))
        return tag_vals
    except:
        raise ValueError('File not found.')


# Returns an array [wikidata_uri, freebase_uri] of the searched string str:
def str2wikidata_freebase_uri(str):
    url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&search="+str+"&language=en&limit=1&format=json"
    response = requests.get(url).json()
    try:
        result1 = response.get("search")[0] # <-- dict
        wikidata_uri = result1.get("concepturi")
        wiki_id = wikidata_uri[wikidata_uri.rfind('/')+1:]
        # Look for wiki_id's freebase id:
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery("""
        SELECT * WHERE {
            ?item wdt:* wd:%s.
            OPTIONAL { ?item wdt:P646 ?Freebase_ID. }
        }
        LIMIT 1
        """%wiki_id)
        sparql.setReturnFormat(JSON)
        result2 = sparql.query().convert()
        try:
            freebase_id = result2.get('results').get("bindings")[0].get('Freebase_ID').get('value')
            last_char_index = freebase_id.rfind('/') # doing this to convert '/' to '.' in the freebase id.
            freebase_uri = "http://rdf.freebase.com/ns" + freebase_id[:last_char_index] + '.' + freebase_id[last_char_index+1:]
            return [wikidata_uri, freebase_uri]
        except:
            return [wikidata_uri, "nan"]
    except:
        return ["nan", "nan"]


path2json = 'Barack_Obama_AllenPrediction.json'
path2xml = './WikiCoref/Annotation/Barack_Obama/Markables/Barack Obama_coref_level.xml'
#export2xml(path2json)
#print(xml_tag_values2set('coreftype', path2xml))

strings_to_test = ["Angela Merkel",
                   "Western Canada",
                   "Iowa State",
                   "Google"]
for string_to_test in strings_to_test:
    print(string_to_test + ': ' + str(str2wikidata_freebase_uri(string_to_test)))

