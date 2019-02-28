import logging
import warnings
import anaphora_model
from lxml import etree

## Just to ignore warning messages:
#logging.getLogger("allennlp").setLevel(logging.CRITICAL)
#warnings.filterwarnings("ignore")
'''
predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/coref-model-2018.02.05.tar.gz")
results = predictor.predict(
    document="My sister and I met her friends, and then she left with them and left me alone."
)
'''

def clustersToString(pred_results):
    top_spans = pred_results.get('top_spans')
    doc = pred_results.get('document')
    clusters = pred_results.get('clusters')
    # top_spans from list of lists to list of strings:
    top_spans_dict = {}
    for span in top_spans:
        span_as_str = str(span)
        a = span[0]  # span is a tuple, so extract its components
        b = span[-1]
        temp = ''
        for i in range(a, b + 1):
            temp = temp + doc[i] + ' '
        temp = temp[0:-1]
        top_spans_dict[span_as_str] = temp

    # clusters from list of lists of lists to dict of lists of strings:
    clusters_dict = {}
    i = 0
    for cluster in clusters:
        temp = list()
        for span in cluster:
            temp.append(top_spans_dict.get(str(span)))
        clusters_dict[i] = temp
        i += 1

    return clusters_dict




def doc2words(filename):
    if filename.lower().endswith('xml'):
        try:
            root = etree.parse(filename).getroot()
            words = []
            for element in root:
                words.append(element.text)
            return words
        except:
            raise ValueError('File not found.')
    elif filename.lower().endswith('txt'):
        try:
            words = []
            with open(filename, encoding="utf8") as f:
                for line in f:
                    line = line.strip()
                    if line != '':
                        words.append(line)
            if words[-1] == '</markables>':
                words.pop() # remove '</markables>' from last line
            return words
        except:
            raise ValueError('File not found.')
    else:
        raise ValueError('Please input xml or txt.')


#print("Clusters: " + str(clustersToString(results)))

example = doc2words("WikiCoref/Annotation/Barack_Obama/Basedata/Barack Obama_words.xml")
print(example[2])
destination = 'test_output.txt'

#anaphora_model.predict_example(example, destination)

#model = allennlp.models.coreference_resolution.coref.CoreferenceResolver()
#predictor = allennlp.predictors.coref.CorefPredictor(model, )
#predictor = CorefPredictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/coref-model-2018.02.05.tar.gz")
#dict = predictor.predict_tokenized(words)
#mmax = dict_to_mmax(dict)

#file = open(destination, "a")
#clusters = predictor.predict_tokenized(example)
#file.write(clusters)

anaphora_model.AnaphoraModel.predict_example(example, destination)