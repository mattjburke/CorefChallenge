
import anaphora_model




example = doc2words("WikiCoref/Annotation/Barack_Obama/Basedata/Barack Obama_words.xml")
print(example[2])
destination = 'test_output.txt'



anaphora_model.AnaphoraModel.predict_example(example, destination)