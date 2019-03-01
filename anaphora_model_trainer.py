from anaphora_model import AnaphoraModel
import subprocess
import os

class AnaphoraModelTrainer():
  """
  Trains an AnaphoraModel using data located in the provided list of paths, where a path is a string representing
  a path like WikiCoref/Annotation/Barack_Obama.
  """

  def __init__(self, model: AnaphoraModel):
    self.model = model

  def train_model(self, paths: list):
    self.train_model_conll()

  def train_model_conll(self, paths: list):
    os.chdir()

    pass
