# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:10:34 2019

@author: tseki
"""

from lxml import etree

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
            with open('Barack Obama.txt', encoding="utf8") as f:
                for line in f:
                    line = line.strip()
                    if line != '':
                        words.append(line)
            return words
        except:
            raise ValueError('File not found.')
    else:
        raise ValueError('Please input xml or txt.')

xml2words = doc2words('Barack Obama_words.xml')
txt2words = doc2words('Barack Obama.txt')