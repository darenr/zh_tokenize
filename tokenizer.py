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

    MAX_MISSES = 6

    def __init__(self, verbose=False, includeSimplified = True, includeTraditional = False):
        start_load_time = time.time() * 1000

        dictionary_gzfile = os.environ['ZH_DICT'] if 'ZH_DICT' in os.environ else 'dict/cedict_1_0_ts_utf-8_mdbg.txt.gz'
        with gzip.open(dictionary_gzfile, 'rb') as f:
            words = []
            for line in f.read().decode('utf-8').splitlines():
                if line.startswith('#'):
                    pass
                else:
                    # Format:
                    # Traditional Simplified [pin1 yin1] /English equivalent 1/equivalent 2/
                    # 龥 龥 [yu4] /variant of 籲|吁[yu4]/

                    parts = iter(line.split())
                    traditional = parts.next()
                    simplified = parts.next()

                    if includeTraditional:
                        words.append(traditional)

                    if includeSimplified:
                        words.append(simplified)

            self.trie = marisa_trie.Trie(words)

        end_load_time = time.time() * 1000
        if verbose:
            print ' *', 'dictionary loaded and indexed in', end_load_time - start_load_time, 'ms'

    def tokenize(self, u_str):
        words = []

        i = 0
        while i < len(u_str):
            length = 1
            loop = False
            misses = 0
            lastCorrectLen = 1
            somethingFound = False
            while True:
                word = u_str[i:i+length]
                if self.trie.has_keys_with_prefix(word):
                    somethingFound = True
                    lastCorrectLen = length
                    loop = True
                else:
                    misses += 1
                    loop = misses < ChineseWordTokenizer.MAX_MISSES;

                length += 1

                if i + length > len(u_str):
                    loop = False

                if not loop:
                    break

            i += 1

            if somethingFound:
                word = u_str[i:i+lastCorrectLen]
                if word:
                    words.append(word)
                    i += lastCorrectLen - 1


        return words

    def printable(self, list):
        return u' '.join(["[" + x + "]" for x in list])

if __name__ == "__main__":
    tokenizer = ChineseWordTokenizer(verbose=True)
    tokens = tokenizer.tokenize(u"国家都有自己的政府。政府是税收的主体，可以实现福利的合理利用。")
    print len(tokens), tokenizer.printable(tokens)
