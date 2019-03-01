
import anaphora_model
import extras


example = extras.doc2words("WikiCoref/Annotation/Barack_Obama/Basedata/Barack Obama_words.xml")
destination = 'test_output.txt'

anaphora_model.AnaphoraModel.predict_example(example, destination)