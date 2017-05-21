#!/usr/bin/env python
# -*- coding: utf-8 -*--

from nose.tools import with_setup

from tokenizer import ChineseWordTokenizer

tokenizer = ChineseWordTokenizer()

def test_1():
    words = tokenizer.tokenize(u"弹道导弹")
    print tokenizer.printable(words)
    assert len(words) == 1
    assert words[0] == u"弹道导弹"

def test_2():
    words = tokenizer.tokenize(u"美国人的文化.dog")
    print tokenizer.printable(words)
    assert len(words) == 3
    assert words[0] == u"美国人"
    assert words[1] == u"的"
    assert words[2] == u"文化"

def test_3():
    words = tokenizer.tokenize(u"我是美国人")
    print tokenizer.printable(words)
    assert len(words) == 3
    assert words[0] == u"我"
    assert words[1] == u"是"
    assert words[2] == u"美国人"

def test_5():
    words = tokenizer.tokenize(u"政府依照法律行使执法权，如果超出法律赋予的权限范围，就是“滥用职权”；如果没有完全行使执法权，就是“不作为”。两者都是政府的错误。")
    print tokenizer.printable(words)
    # should be: [ 政府 依照 法律 行使 执法 权 如果 超出 法律 赋予 的 权限 范围 就是 滥用职权 如果 没有 完全 行使 执法 权 就是 不 作为 两者 都 是 政府 的 错误 ]


def test_6():
    words = tokenizer.tokenize(u"国家都有自己的政府。政府是税收的主体，可以实现福利的合理利用。")
    print tokenizer.printable(words)
    # should be [ 国家 都 有 自己 的 政府 政府 是 税收 的 主体 可以 实现 福利 的 合理 利用 ]
