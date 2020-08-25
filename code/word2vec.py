from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import argparse
import logging
import os
from gensim.test.utils import get_tmpfile
from gensim.models.callbacks import CallbackAny2Vec
from epoch_saver import EpochSaver


logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

parse = argparse.ArgumentParser()
parse.add_argument('--model_prefix', type=str, default='model',
                    help='file prefix')
parse.add_argument('--save_path', type=str, default='model',
                    help='directory to save the model(s)')
parse.add_argument('--save_each_epoch', type=str, default='yes',
                    help='whether to save epoch or not')
parse.add_argument('--restore_model', type=str, default='',
                    help='path to  model')
parse.add_argument('--input_path', type=str, default='arabic_text',
                    help='path to the training corpus')
parse.add_argument('--n_epochs', type=int, default=10, help='number of epochs')
parse.add_argument('--n_workers', type=int, default=8, help='number of workers')
parse.add_argument('--size', type=int, default=250, help='embedding size')
parse.add_argument('--window', type=int, default=10, help='window size')
parse.add_argument('--frequency', type=int, default=20, help='the minimum frequency of a word to be considered')

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

args = parse.parse_args()

if not  os.path.isdir(args.save_path):
    os.mkdir(args.save_path)

line_sentence = LineSentence(args.input_path, 99999999999)

if len(args.restore_model) > 0:
    assert os.path.isfile(args.restore_model)
    model = Word2Vec.load(args.restore_model)
else:
    model = Word2Vec(size=args.size, workers=args.n_workers, min_count=args.frequency, window=args.window)
    model.build_vocab(line_sentence)

path_prefix = os.path.join(args.save_path, args.model_prefix)

saver = EpochSaver(path_prefix)
model.train(line_sentence, total_examples=model.corpus_count,
            epochs=args.n_epochs, callbacks=[saver])


