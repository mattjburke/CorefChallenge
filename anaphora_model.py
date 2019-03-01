
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from e2eCoref.util import initialize_best_env
from e2eCoref.demo import print_predictions, make_predictions, make_and_write_predictions_to_file
from e2eCoref.coref_model import CorefModel
import tensorflow as tf
import subprocess
import os


class AnaphoraModel():
  """
  Writes out annotations for a document, represented as a list of tokens, in MMAX standoff format, to the path
  identified by the destination argument.
  """


  def __init__(self, pretrained):
    os.chdir("e2eCoref")
    if pretrained:
      subprocess.call(['./mypretrained_setup.sh']) # correct format?
    else:
      subprocess.call(['./my_pretrained_setup.sh']) # correct format?
    self.config = initialize_best_env()
    self.model = CorefModel(self.config)
    os.chdir("..")

  def predict_example(self, words: list, destination: str):
    text = AnaphoraModel.wordlist_to_block(words)
    os.chdir("e2eCoref")
    with tf.Session() as session:
      self.model.restore(session)
      make_and_write_predictions_to_file(make_predictions(text, self.model), destination)

    os.chdir("..")

  @staticmethod
  def wordlist_to_block(list):
    block = ""
    for word in list:
      block += " " + word
    return block
