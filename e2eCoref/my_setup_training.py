import os
import shutil
import random

paths = os.listdir("../WikiCoref/WikiCoref-CoNLL")
random.seed(4) # just for consistency
random.shuffle(paths) 

for i in range(len(paths)):
  paths[i] = "../WikiCoref/WikiCoref-CoNLL/" + paths[i]

percent_taining=80
percent_dev=10

num_paths = len(paths)

train_mark = int(num_paths*percent_taining/100)
dev_mark = train_mark + int(num_paths*percent_dev/100)

try:
  os.mkdir('train')
  os.mkdir('dev')
  os.mkdir('test')
except:
  pass

counter = 0

#Training:
while counter < train_mark:
  shutil.copy(paths[counter], 'train')
  counter += 1

#Development:
while counter < dev_mark:
  shutil.copy(paths[counter], 'dev')
  counter += 1

#Testing:
while counter < num_paths:
  shutil.copy(paths[counter], 'test')
  counter += 1

#Concatenating:
def cat(foldername):
  os.chdir(foldername)
  filenames = os.listdir()
  with open('../'+foldername+'.english.v4_gold_conll', 'w') as outfile:
    for fname in filenames:
      with open(fname) as infile:
        for line in infile:
          outfile.write(line)
  os.chdir('..')
cat('train')
cat('dev')
cat('test')