
import e2eCoref_old as e2e
from e2eCoref_old.util import initialize_best_env
from e2eCoref_old.coref_model import CorefModel
from e2eCoref_old.demo import print_predictions, make_predictions
import tensorflow as tf


class AnaphoraModel():
  """
  Writes out annotations for a document, represented as a list of tokens, in MMAX standoff format, to the path
  identified by the destination argument.
  """




  @staticmethod
  def wordlist_to_block(list):
    block = ""
    for word in list:
      block += " " + word
    return block


  def predict_example(words: list, destination: str):
    text = AnaphoraModel.wordlist_to_block(words)
    config = initialize_best_env()
    model = CorefModel(config)
    with tf.Session() as session:
      model.restore(session)
      print_predictions(make_predictions(text, model)) #just testing if regular method can be called in submoduel
      #e2e.demo.print_predictions_to_file(e2e.demo.make_predictions(text, model), destination)
      #allen2xml.method(e2e.demo.get_predictions(e2e.demo.make_predictions(text, model))



