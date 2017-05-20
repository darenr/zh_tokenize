# zh_tokenize

Tokenize Chinese using a Trie (prefix-search) based on work done by @kennycason

ZH gzipped file dictionary can be downloaded from:

https://www.mdbg.net/chinese/dictionary?page=cc-cedict

if this file is not in 

./dict/cedict_1_0_ts_utf-8_mdbg.txt.gz

export ZH_DICT=/fully/qualified/path/to/cedict-VERSION.gz

Algorithm:

Walked through sentences character-by-character observing if substrings exist in the dictionary. If so parse as a token. This is self correcting for words not in the dictionary. Unrecognized sequences will be output verbatim.
