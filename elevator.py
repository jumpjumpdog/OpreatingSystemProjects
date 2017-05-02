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


    def run(self):
        while True:
            cur_layer = 'lev'+str(self.cur_layer)+'_'+str(self.id)
            up_layer = 'lev'+str(self.cur_layer+1)+'_'+str(self.id)
            down_layer = 'lev'+str(self.cur_layer-1)+'_'+str(self.id)
            if self.status == 'wait':
                #print "thread%d is waiting"%(self.id)
                self.ui.__getattribute__(cur_layer).setText('wait')
            #如果电梯目前状态向上，那么电梯当前层数加1
            #然后分为3中情况
            # 第一种当前电梯内部没人，外部有人等待，则电梯将开向外部等待的乘客，当检测到到达欲乘乘客楼层，那么将乘客想的目的楼层加入in_queue
            #第二种当前电梯内部有人，外部无人等待，则电梯继续沿原来方向前进，当检测到乘客到达目的楼层，将该乘客从in_queue中取出
            #第三种当前电梯内部外部均有人，即对第一种和第二种情况均考虑了一遍
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


