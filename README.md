# CorefChallenge
Kingland competition coreference challenge.

## Running MMAX2 (from Git Bash on Windows)

On the terminal while in the MMAX2 directory, run:
`./mmax2.bat`

## Try, for torch (=> allennlp) installation

In no particular order, necessarily:
- `pip uninstall torch==1.0.1` (might wanna use `torch --version` or something, before, just to double-check)
- `pip install https://download.pytorch.org/whl/cu90/torch-1.0.1-cp36-cp36m-win_amd64.whl` (pip instead of pip3)

  `pip install torchvision` (pip instead of pip3)
- On PyCharm, when adding a new virtual python interpreter, check "Inherit global site-packages"

Steps to complete:
1) Implement the class AnaphoraModel() to use the pretrained allennlp CorefPredictor to predict and write out annotations for a document in MMAX standoff format int he method predict_example(words: list, destination: str).

2) Implement the class AnaphoraModelTrainer() to retrain the allennlp CoreferenceResolver model on data from the WikiCoref/Annotation/ folder. Implemented in method train_model(paths: list).

3) Substitute BERT in for context_layer in CoreferenceResolver model.

4) Retrain new model in AnaphoraModelTrainer().

5) Update AnaphoraModel() class to use new CorefPredictor. (Just init CorefPredictor with new model as parameter).

6) Determine F1 score. Write up explanation of model.

## To create a conda environment needed for HuggingFace Neuralcoref
- `conda update conda`
- `conda update anaconda`
- `conda create -n yourenvname python anaconda`
- `source activate yourenvname` The rest of the commands are executed with the environment activated. They will download only in the environment.
- `conda install pytorch -c pytorch`
- `conda install -c conda-forge spacy`
- `conda install pytorch torchvision -c pytorch`
- `conda install -c conda-forge tensorboardx`
- `python -m spacy download en` This will give a prompt "You can now load the model via spacy.load('en')".

The environment is now ready. You type `which python` to see the filepath to the python interpreter. Select this interpreter for the project in your favorite editor such as PyCharm.
