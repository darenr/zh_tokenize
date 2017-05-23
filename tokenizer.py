#!/usr/bin/env python
# -*- coding: utf-8 -*--

import time
import marisa_trie
import gzip


class ChineseWordTokenizer:

    def __init__(self,  verbose=False,
                 includeSimplified=True,
                 includeTraditional=True,
                 dictionary_gzfile='dict/cedict_1_0_ts_utf-8_mdbg.txt.gz'):
        t_start = time.time() * 1000
        with gzip.open(dictionary_gzfile, 'rb') as f:
            words = []
            for line in f.read().decode('utf-8').splitlines():
                if line.startswith('#'):
                    pass
                else:
                    # Format:
                    # Trad Simp [pin1 yin1] /English equiv 1/equiv 2/
                    # 龥 龥 [yu4] /variant of 籲|吁[yu4]/

                    parts = iter(line.split())
                    traditional = parts.next()
                    simplified = parts.next()

                    if includeTraditional:
                        words.append(traditional)

                    if includeSimplified:
                        words.append(simplified)

            self.trie = marisa_trie.Trie(words)

        t_end = time.time() * 1000
        if verbose:
            print ' *', 'dictionary loaded, indexed in', t_end - t_start, 'ms'

    def tokenize(self, u_str):
        MAX_MISSES = 6
        words = []

        i = 0
        while i < len(u_str):
            length = 1
            loop = False
            misses = 0
            lastCorrectLen = 1
            somethingFound = False
            while True:
                word = u_str[i:i + length]
                if self.trie.has_keys_with_prefix(word):
                    somethingFound = True
                    lastCorrectLen = length
                    loop = True
                else:
                    misses += 1
                    loop = misses < MAX_MISSES

                length += 1

                if i + length > len(u_str):
                    loop = False

                if not loop:
                    break

            if somethingFound:
                word = u_str[i:i + lastCorrectLen]
                if word:
                    words.append(word.strip())
                    i += lastCorrectLen - 1

            i += 1

        return words

    def printable(self, list):
        return u', '.join(["[\"" + x + "\"]" for x in list])


if __name__ == "__main__":

    tokenizer = ChineseWordTokenizer(verbose=True)
    words = tokenizer.tokenize(u"国家都有自己的政府。政府是税收的主体，可以实现福利的合理利用。")
    print tokenizer.printable(words)
