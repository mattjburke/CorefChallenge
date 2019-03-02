
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
    """



    Creates a model with predetermined hyperparameters. If the pretrained boolean is true, then the wieghts of
    a model trained by the authors will be stored in logs and can be used to make predictions. Loading word embedding
    to set up the model can take some time.
    :param pretrained: boolean to indicate if a pretrained model will be loaded or a model to be trained will be loaded
    """
    os.chdir("e2eCoref")
    if pretrained:
      subprocess.call(['./my_pretrained_setup.sh']) # correct format?
    else:
      subprocess.call(['./my_pretrained_setup.sh']) # correct format?
    self.config = initialize_best_env()
    self.model = CorefModel(self.config)
    os.chdir("..")

  def predict_example(self, words: list, destination: str):
    """
    Predicts the coref clusters in a document, given as a list of words, and writes these predictions to a file in a
    modified OntoNotes scheme matching the WikiCoref dataset's scheme.
    :param words: The document to predict on, given as a list of tokens.
    :param destination: The filepath of where to output the file with predictions.
    :return: void
    """
    text = AnaphoraModel.wordlist_to_block(words)
    os.chdir("e2eCoref")
    with tf.Session() as session:
      self.model.restore(session)
      make_and_write_predictions_to_file(make_predictions(text, self.model), destination)

    os.chdir("..")


  @staticmethod
  def wordlist_to_block(list):
    """
    Simply turns a list of words into a continuous block of text.
    :param list: words from a document
    :return: the words separated by one space
    """
    block = ""
    for word in list:
      block += " " + word
    return block
