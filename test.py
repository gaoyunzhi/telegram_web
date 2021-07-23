#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webgram
import time

def test():
	print(int((time.time() - webgram.getPost('douban_read', 66310).time) / 60))

if __name__=='__main__':
	test()