#!/usr/bin/env python
# -*- coding: utf-8 -*--

from nose.tools import with_setup

from tokenizer import ChineseWordTokenizer

tokenizer = ChineseWordTokenizer()

def test_1():
    assert len(tokenizer.tokenize(u"弹道导弹")) == 1

def test_2():
    assert len(tokenizer.tokenize(u"美国人的文化.dog")) == 3

def test_3():
    assert len(tokenizer.tokenize(u"我是美国人")) == 3

def test_4():
    assert len(tokenizer.tokenize(u"再見")) == 1

def test_5():
    assert len(tokenizer.tokenize(u"請問")) == 1

def test_6():
    assert len(tokenizer.tokenize(u"你會說英語嗎")) == 4
