import bert #needs Project Interpreter package bert-tensorflow

words = []

train_InputExamples = words.apply(lambda x: bert.run_classifier.InputExample(guid=None,
                                                                   text_a = x,
                                                                   text_b = None,
                                                                   label = None), axis = 1)

