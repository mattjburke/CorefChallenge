
import allennlp


class AnaphoraModel():
  """
  Writes out annotations for a document, represented as a list of tokens, in MMAX standoff format, to the path
  identified by the destination argument.
  """
  model = allennlp.models.coreference_resolution.coref


  #ba_words = WikiCoref/Annotation/Barack_Obama/Barack Obama.txt

  predictor = allennlp.predictors.coref

  def dict_to_mmax(dict):
    return dict

  def predict_example(words: list, destination: str):
    dict = predictor.predict_tokenized(words)
    mmax = dict_to_mmax(dict)
    return mmax
