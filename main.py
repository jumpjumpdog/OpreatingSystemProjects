#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from time  import sleep
from threading import Thread
from PyQt4 import QtGui
from elevator import elevator
from letMeTry.budianti import MyForm,Temp_Layer


#电梯线程初始化函数
def init_elevator():
    elevator_threads = [elevator(x) for x in range(1,4)]
    return elevator_threads

#选择调度的电梯
#方向一致，相对位置一致
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
                    elevator_threads[id - 1].queue.insert(passenger.cur_layer)
                    if elevator_threads[id - 1].status == 'wait':
                        if passenger.cur_layer == elevator_threads[id - 1].cur_layer:
                            elevator_threads[id - 1].status = 'wait'
                        elevator_threads[id - 1].status = 'up' if passenger.cur_layer > elevator_threads[
                            id - 1].cur_layer else 'down'

            if id == -1:
                Temp_Layer.append(passenger)



selectThread = Thread(target=select)
selectThread.start()


app = QtGui.QApplication(sys.argv)
myform = MyForm()
myform.show()


elevator_threads = init_elevator()

for x in elevator_threads:
    x.ui = myform.ui
    x.start()



if __name__ == "__main__":
    sys.exit(app.exec_())




