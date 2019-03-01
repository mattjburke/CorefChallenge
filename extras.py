from lxml import etree

@staticmethod
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