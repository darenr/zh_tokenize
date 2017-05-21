# zh_tokenize

[![Travis CI](https://travis-ci.org/darenr/zh_tokenize.svg?branch=master)]()

Tokenize Chinese using a Trie (prefix-search) based on work done by @kennycason

ZH gzipped file dictionary can be downloaded from:

https://www.mdbg.net/chinese/dictionary?page=cc-cedict

to use a different dictionary change dictionary_gzfile to the fill path of the
gz file.

(dictionary license http://creativecommons.org/licenses/by-sa/3.0/)

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
>>> from tokenizer import ChineseWordTokenizer
>>>
>>> tokenizer = ChineseWordTokenizer(verbose=False, includeSimplified=True, includeTraditional=True)
>>> tokens = tokenizer.tokenize(u"国家都有自己的政府。政府是税收的主体，可以实现福利的合理利用。")
>>> print 'Number of Tokens:', len(tokens), 'Tokens:', tokenizer.printable(tokens)
Number of Tokens: 17 Tokens: [家都] [有] [自] [己的] [政] [府。] [府是] [税] [收的] [主] [体，] [以实] [现福] [利的] [合] [理利] [用。]
>>>
```
