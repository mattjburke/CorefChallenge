from anaphora_model import AnaphoraModel
import subprocess
import os

class AnaphoraModelTrainer():
  """
  Trains an AnaphoraModel using data located in the provided list of paths, where a path is a string representing
  a path like WikiCoref/Annotation/Barack_Obama.
  """

  def __init__(self, model: AnaphoraModel):
    """
    The trainer must be initialized with the AnaphoraModel you with to train.
    :param model: the AnaphoraModel to train
    """
    self.model = model

  def train_model(self, paths: list):
    self.train_model_conll()

  def train_model_conll(self, paths: list):
    """
    Replaces the WikiCoref format documents with corresponding CoNLL format documents, and trains the AnaphoraModel
    on these documents.
    :param paths:
    :return:
    """
    os.chdir("e2eCoref")
    subprocess.call(['python', 'train.py', 'best'])
    os.chdir("..")


  def evaluate_tained_model(self):
    """
    Writes the average F1 score, precision, and recall of the trained model to the console.
    :return: void
    """
    os.chdir("e2eCoref")
    subprocess.call(['python', 'evaluate.py', 'best'])
    os.chdir("..")
