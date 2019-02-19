# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:10:34 2019

@author: tseki
"""

import os
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

base_path = './WikiCoref/Annotation/'

xml2words = doc2words(base_path + 'Barack_Obama/Basedata/Barack Obama_words.xml')
txt2words = doc2words(base_path + 'Barack_Obama/Barack Obama.txt')

print('xml2words: size=' + str(len(xml2words)) + ', last element = ' + xml2words[-1])
print('txt2words: size=' + str(len(txt2words)) + ', last element = ' + txt2words[-1])

'''
# check all last lines of txt files:
articles = os.listdir(base_path)
for dir in articles:
    files = os.listdir(base_path + dir)
    for file in files:
        if file.endswith(".txt"):
            print(doc2words(base_path + dir + '/' + file)[-1])
# ok... so all txt files' last line is '</markables>'
'''