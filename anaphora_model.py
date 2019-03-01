
import e2eCoref as e2e
from e2eCoref.util import initialize_best_env
from e2eCoref.coref_model import CorefModel
from e2eCoref.demo import print_predictions, make_predictions, make_and_write_predictions_to_file
import tensorflow as tf
import subprocess
import os


class AnaphoraModel():
  """
  Writes out annotations for a document, represented as a list of tokens, in MMAX standoff format, to the path
  identified by the destination argument.
  """


  def __init__(self):
    os.chdir("e2eCoref")
    subprocess("my_setup.sh")
    self.config = initialize_best_env()
    self.model = CorefModel(self.config)
    os.chdir("..")

  def predict_example(self, words: list, destination: str):
    text = AnaphoraModel.wordlist_to_block(words)
    os.chdir("e2eCoref")
    with tf.Session() as session:
      self.model.restore(session)
      make_and_write_predictions_to_file(make_predictions(text, self.model), destination)

      # print_predictions(make_predictions(text, self.model))
      #allen2xml.method(e2e.demo.get_predictions(e2e.demo.make_predictions(text, model))

    os.chdir("..")

  @staticmethod
  def wordlist_to_block(list):
    block = ""
    for word in list:
      block += " " + word
    return block
