#!/usr/bin/env python
# -*- coding: utf-8 -*--

import json
import sys
import codecs
import time
import marisa_trie
import gzip
import os
import re
import sys

class ChineseWordTokenizer:

    def __init__(self, verbose=False):
        start_load_time = time.time() * 1000

        dictionary_gzfile = os.environ['ZH_DICT'] if 'ZH_DICT' in os.environ else 'dict/cedict_1_0_ts_utf-8_mdbg.txt.gz'
        with gzip.open(dictionary_gzfile, 'rb') as f:
            words = []
            for line in f.read().decode('utf-8').splitlines():
                if line.startswith('#'):
                    pass
                else:
                    # format is space separated, chinese tokens are followed by pronounciation demarked
                    # with the token surrounded by square brackets, for example:
                    # 龥 龥 [yu4] /variant of 籲|吁[yu4]/
                    # consume tokens until [here]

                    accumulator = []
                    for token in line.split():
                        if token.startswith('['): # we ignore everything after and including this token
                            # add to words list for indexing
                            words.append(''.join(accumulator))
                        else:
                            accumulator += token.strip()

            self.trie = marisa_trie.Trie(words)

        end_load_time = time.time() * 1000
        if verbose:
            print ' *', 'dictionary loaded and indexed in', end_load_time - start_load_time, 'ms'

    def tokenize(self, u_str):
        return u_str.split()


if __name__ == "__main__":
    tokenizer = ChineseWordTokenizer(verbose=True)
    print tokenizer.tokenize(u"hello world")
