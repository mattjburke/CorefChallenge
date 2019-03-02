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

