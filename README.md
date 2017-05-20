# zh_tokenize

[![Project status](https://img.shields.io/badge/Project%20Status-Complete-brightgreen.svg)](#status)


Tokenize Chinese using a Trie (prefix-search) based on work done by @kennycason

ZH gzipped file dictionary can be downloaded from:

https://www.mdbg.net/chinese/dictionary?page=cc-cedict

if this file is not in (do not gunzip)

./dict/cedict_1_0_ts_utf-8_mdbg.txt.gz

(dictionary license http://creativecommons.org/licenses/by-sa/3.0/)

export ZH_DICT=/fully/qualified/path/to/cedict-VERSION.gz

Algorithm:

Walk through sentences character-by-character checking if substring exist in the Trie. If so parse as a token. This is self correcting for words not in the dictionary. The output will be utf-8 encoded tokens space separated suitable for using in a search engine.

Example Usage:

```
from tokenizer import ChineseWordTokenizer

tokenizer = ChineseWordTokenizer(verbose=False, includeSimplified=True, includeTraditional=True)
tokens = tokenizer.tokenize(u"国家都有自己的政府。政府是税收的主体，可以实现福利的合理利用。")
print 'Number of Tokens:', len(tokens), 'Tokens:', tokenizer.printable(tokens)
```

Produces:

```
17 [家都] [有] [自] [己的] [政] [府。] [府是] [税] [收的] [主] [体，] [以实] [现福] [利的] [合] [理利] [用。]
```
