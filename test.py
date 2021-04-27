#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def test():
	print(webgram.getPost('social_justice_watch', 5847).getIndex())

if __name__=='__main__':
	test()