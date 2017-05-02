#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading

#电梯内部乘客队列
class myqueue(object):
    def __init__(self):
        self.mode = False
        self.buf = []
    def insert(self, item):
        self.buf.append(item)
        self.buf.sort(reverse = self.mode)

    def sort(self):
            self.buf.sort(self.mode)

    def front(self):
        temp = self.buf[0]
        return temp

    def pop_front(self):
        self.buf.pop(0)


    def length(self):
        size = len(self.buf)
        return size

    def empty(self):
        size = len(self.buf)
        if size == 0:
            return True
        return False


