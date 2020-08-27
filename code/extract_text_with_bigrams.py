from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import argparse
import logging
import os
from gensim.test.utils import get_tmpfile
from gensim.models.phrases import Phrases, Phraser


logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

parse = argparse.ArgumentParser()
parse.add_argument('--in_path', type=str, default='../../../arabic_data/arabic_.txt.segmented',
                    help='file path')
parse.add_argument('--th', type=int, default=12,
                    help='threshold to consider the bigram)')
parse.add_argument('--min_count', type=int, default=16,
                    help='minimum frequency of the bigram to be considered')
parse.add_argument('--out_path', type=str, default='../../../arabic_data/arabic_bigrams.txt.segmented',
                    help='path to write the output')

args = parse.parse_args()

line_sentence = LineSentence(args.in_path, 99999999999)

phrases = Phrases(line_sentence, min_count=args.min_count, threshold=args.th)

file_out = open(args.out_path, 'a')

for sentence in line_sentence:
    file_out.write(' '.join(phrases[sentence])+'\n')

file_out.close()