
import e2e-coref as e2e
import neuralcoref as nc
import

class AnaphoraModel():
  """
  Writes out annotations for a document, represented as a list of tokens, in MMAX standoff format, to the path
  identified by the destination argument.
  """





  def predict_example(words: list, destination: str):


    file = open(destination, "a")
    clusters = predictor.predict_tokenized(words)
    file.write(clusters)


  def wordlist_to_block(words: list):
    block = ""
    for word in list:
      block += " " + word
    return block