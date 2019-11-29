import init
import refresh
from globa import *

#初始化地图
init.init()
#启动刷新线程
refresh.start()
#启动窗口
window.mainloop()



