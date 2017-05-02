#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from time import sleep
from budianti  import Ui_MainWindow


from myqueue import myqueue


class elevator(threading.Thread):

    def  __init__(self,i,parent = None):
        super(elevator,self).__init__()
        self.ui = Ui_MainWindow()

        self.id = i
        self.status = 'wait'
        self.cur_layer = 1
        self.queue = myqueue()

#线程函数
#原理是每个电梯实时监测自己的status，并将状态实时显示到ui界面


    def run(self):
        while True:
            cur_layer = 'lev'+str(self.cur_layer)+'_'+str(self.id)
            up_layer = 'lev'+str(self.cur_layer+1)+'_'+str(self.id)
            down_layer = 'lev'+str(self.cur_layer-1)+'_'+str(self.id)
            if self.status == 'wait':
                #print "thread%d is waiting"%(self.id)
                self.ui.__getattribute__(cur_layer).setText('wait')
            elif self.status == 'up':
                print self.id
                self.ui.__getattribute__(cur_layer).setText('')
                self.cur_layer += 1
                self.ui.__getattribute__(up_layer).setText('up')

                if self.cur_layer == self.queue.front():
                    print"arrive %d layer"%(self.cur_layer)
                    self.queue.pop_front()

                if self.queue.empty():
                    self.status = 'wait'
                    self.ui.__getattribute__(up_layer).setText('wait')

            elif self.status == 'down':
                #print "thread%d is going down\n" % (self.id)
                self.ui.__getattribute__(cur_layer).setText('')
                self.cur_layer -= 1
                self.ui.__getattribute__(down_layer).setText('down')

                if self.cur_layer == self.queue.front():
                    print "arrive %d layer"%(self.cur_layer)
                    self.queue.pop_front()

                if self.queue.empty():
                    self.status = 'wait'
                    self.ui.__getattribute__(down_layer).setText('wait')
            sleep(0.5)


