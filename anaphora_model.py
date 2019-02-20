
import allennlp


class AnaphoraModel():
  """
  Writes out annotations for a document, represented as a list of tokens, in MMAX standoff format, to the path
  identified by the destination argument.
  """





  def predict_example(words: list, destination: str):
    predictor = allennlp.predictors.coref
    #dict = predictor.predict_tokenized(words)
    #mmax = dict_to_mmax(dict)
    file = open(destination, "a")
    clusters = predictor.predict_tokenized(words)
    file.write(clusters)

'''
  def __init__(self):
    self.model = allennlp.models.coreference_resolution.coref
    self.predictor = allennlp.predictors.coref

  def dict_to_mmax(dict):
    return dict
'''