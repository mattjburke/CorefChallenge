from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from six.moves import input
import tensorflow as tf
import coref_model as cm
import util

import nltk
#nltk.download("punkt")
from nltk.tokenize import sent_tokenize, word_tokenize

def create_example(text):
  raw_sentences = sent_tokenize(text)
  sentences = [word_tokenize(s) for s in raw_sentences]
  speakers = [["" for _ in sentence] for sentence in sentences]
  return {
    "doc_key": "nw",
    "clusters": [],
    "sentences": sentences,
    "speakers": speakers,
  }

def print_predictions(example):
    words = util.flatten(example["sentences"])
    # for mention in example["mention_to_predicted"]:
    #     print(mention)
    # for span in example["top_spans"]:
    #     print(span)
    cluster_list = []
    for cluster in example["predicted_clusters"]:
        clust_l = []
        for t in cluster:
            tup_list = list(t)
            clust_l.append(tup_list)
        cluster_list.append(clust_l)

    #cluster_list = list(map(list, example["predicted_clusters"]))

    for cluster in cluster_list:
        print("another cluster")
        print(cluster)
        print(u"Predicted cluster: {}".format([" ".join(words[m[0]:m[1]+1]) for m in cluster]))

    return cluster_list

def get_predictions_list(example):
    cluster_list = []
    for cluster in example["predicted_clusters"]:
        clust_l = []
        for t in cluster:
            tup_list = list(t)
            clust_l.append(tup_list)
        cluster_list.append(clust_l)

    return cluster_list

def make_and_get_predictions_list(text):
    config = util.initialize_from_env()
    model = cm.CorefModel(config)
    with tf.Session() as session:
        model.restore(session)
        return get_predictions_list(make_predictions(text, model))


def make_predictions(text, model):
  example = create_example(text)
  tensorized_example = model.tensorize_example(example, is_training=False)
  feed_dict = {i:t for i,t in zip(model.input_tensors, tensorized_example)}
  _, _, _, mention_starts, mention_ends, antecedents, antecedent_scores, head_scores = session.run(model.predictions + [model.head_scores], feed_dict=feed_dict)

  predicted_antecedents = model.get_predicted_antecedents(antecedents, antecedent_scores)

  example["predicted_clusters"], example["mention_to_predicted"] = model.get_predicted_clusters(mention_starts, mention_ends, predicted_antecedents)
  example["top_spans"] = zip((int(i) for i in mention_starts), (int(i) for i in mention_ends))
  example["head_scores"] = head_scores.tolist()
  return example

if __name__ == "__main__":
  config = util.initialize_from_env()
  model = cm.CorefModel(config)
  with tf.Session() as session:
    model.restore(session)
    text = "Forrest Gump is a 1986 novel by Winston Groom. The title character retells adventures ranging from " \
             "shrimp boating and ping pong championships, to thinking about his childhood love, as he bumbles " \
             "his way through American history, with everything from the Vietnam War to college football becoming " \
             "part of the story. Gump is portrayed as viewing the world simply and truthfully. He does not know what " \
             "he wants to do in life, but despite his low IQ, he is made out to be full of wisdom. He says that he " \
             "can think things pretty good, but when he tries sayin or writin them, it kinda come out like Jello. " \
             "His mathematical abilities, as an idiot savant, and feats of strength lead him into all kinds of " \
             "adventures."
    print_predictions(make_predictions(text, model))
