from epoch_saver import EpochSaver
import gensim
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('--model', type=str, default='model.model')
args = parse.parse_args()

model = gensim.models.Word2Vec.load(args.model, mmap='r')
acc = model.accuracy('questions-words-fr.txt')
acc_sections = [(el['section'], (len(el['correct'])/(len(el['correct']) + len(el['incorrect'])))) for el in acc]
for el in acc_sections:
    print(el[0]+':', el[1])
