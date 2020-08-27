import gensim
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('--model', type=str, default='model',
                    help='file path')

args = parse.parse_args()

model = gensim.models.Word2Vec.load(args.model, mmap='r')
model.wv.save_word2vec_format('../../models/model.bin', binary=True)
