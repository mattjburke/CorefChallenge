#!/usr/bin/env bash

pip install -r requirements.txt

./setup_all.sh

python my_training_dir_setup.py

python minimize.py

python get_char_vocab.py

python filter_embeddings.py glove.840B.300d.txt train.english.jsonlines dev.english.jsonlines

python cache_elmo.py train.english.jsonlines dev.english.jsonlines
