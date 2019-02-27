
import e2e-coref as e2e
import tensorflow as tf

class AnaphoraModel():
  """
  Writes out annotations for a document, represented as a list of tokens, in MMAX standoff format, to the path
  identified by the destination argument.
  """




  def wordlist_to_block(words: list):
    block = ""
    for word in list:
      block += " " + word
    return block


  def predict_example(words: list, destination: str):
    text = wordlist_to_block(list)
    config = e2e.util.initialize_from_env()
    model = e2e.coref_model.CorefModel(config)
    with tf.Session() as session:
      model.restore(session)
      e2e.demo.print_predictions(e2e.demo.make_predictions(text, model))
      #e2e.demo.print_predictions_to_file(e2e.demo.make_predictions(text, model), destination)

    # file = open(destination, "a")
    # clusters = predictor.predict_tokenized(words)
    # file.write(clusters)


