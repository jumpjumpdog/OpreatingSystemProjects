#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from threading import Thread
from PyQt4 import QtGui
from elevator import elevator
from letMeTry.budianti import MyForm,Temp_Layer


#电梯线程初始化函数
def init_elevator():
    elevator_threads = [elevator(x) for x in range(1,4)]
    return elevator_threads

#调度函数
#调度的准则是在电梯运行方向和乘客所要去的方向一致，并且电梯接乘客是在顺路或者电梯本身闲置的情况下，否则乘客将继续等待
#在对3部电梯遍历检测是否满足条件，得到所有满足条件的电梯之后，从中选择一部最近的电梯，将乘客分配给该电梯
#例如 当电梯运行方向是向上，乘客的目标是向上运行，并且乘客当前所在楼层位于电梯的上侧，则该电梯
#min：电梯与乘客之间的距离
#Temp_Layer: 等待乘客列表
#id  电梯id

def select():
    while True:
        min = 100
        id = -1
        if len(Temp_Layer):
            passenger = Temp_Layer[0]
            Temp_Layer.pop(0)
            for elevator in elevator_threads:
                if passenger.direction == elevator.status:
                    if passenger.direction == 'up' and elevator.cur_layer < passenger.cur_layer:
                        min, id = (min, id) if min < passenger.cur_layer - elevator.cur_layer else (
                        passenger.cur_layer - elevator.cur_layer, elevator.id)
                    elif passenger.direction == 'down' and elevator.cur_layer > passenger.cur_layer:
                        min, id = (min, id) if min < elevator.cur_layer - passenger.cur_layer else (
                        elevator.cur_layer - passenger.cur_layer, elevator.id)
                elif elevator.status == 'wait':
                    print abs(elevator.cur_layer - passenger.cur_layer)
                    min, id = (min, id) if min < abs(elevator.cur_layer - passenger.cur_layer)else(
                    abs(elevator.cur_layer - passenger.cur_layer), elevator.id)

            if id != -1:
                if min != 0:
                    if elevator_threads[id - 1].status == 'wait':
                        if passenger.cur_layer == elevator_threads[id - 1].cur_layer:
                            elevator_threads[id - 1].status = 'wait'
                        elevator_threads[id - 1].status,elevator_threads[id-1].mode  = ('up',False) if passenger.cur_layer > elevator_threads[id - 1].cur_layer else ('down',True)
                    elevator_threads[id - 1].queue.insert(passenger.cur_layer)

            if id == -1:
                Temp_Layer.append(passenger)


#选择线程，将存储在Temp_Layer中的等待乘客分发给各个电梯线程
selectThread = Thread(target=select)
selectThread.start()

#创建PyQt app及app的UI界面，显示UI界面
app = QtGui.QApplication(sys.argv)
myform = MyForm()
myform.show()


elevator_threads = init_elevator()

#将每个电梯线程都与组件关联，同时开启电梯线程
for x in elevator_threads:
    x.ui = myform.ui
    x.start()



if __name__ == "__main__":
    sys.exit(app.exec_())




