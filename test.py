#!/usr/bin/env python
# -*- coding: utf-8 -*--

from nose.tools import with_setup


def setup_tokenizer():
    tokenizer = ChineseWordTokenizer()


@with_setup(setup_tokenizer)
def test_1:
    words = tokenizer.tokenize("弹道导弹")
    print(words)
    assert words.length == 1


@with_setup(setup_tokenizer)
def test_2:
    words = tokenizer.tokenize("美国人的文化.dog")
    print(words)
    assert words.length == 3


@with_setup(setup_tokenizer)
def test_3:
    words = tokenizer.tokenize("我是美国人")
    print(words)
    assert words.length == 3


@with_setup(setup_tokenizer)
def test_4:
    words = tokenizer.tokenize("政府依照法律行使执法权，如果超出法律赋予的权限范围，就是“滥用职权”；如果没有完全行使执法权，就是“不作为”。两者都是政府的错误。")
    print(words)


@with_setup(setup_tokenizer)
def test_5:
    words = tokenizer.tokenize("国家都有自己的政府。政府是税收的主体，可以实现福利的合理利用。")
    print(words)
