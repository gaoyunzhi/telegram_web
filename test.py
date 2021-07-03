#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram

def test():
	print(webgram.getPost('douban_read', 63896).hasVideo())

if __name__=='__main__':
	test()