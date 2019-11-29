from globa import *
import random


#随机繁殖规则
def rule_reproduce_random(count):
    if count >= 5:
        return white
    if count >= 4:
        if random.random() <0.1:
            return black
        return white
    if count >= 2:
        if random.random() < 0.4:
            return black
        return white
    else:
        return white

#经典繁殖规则
#繁殖：任何死细胞如果活邻居正好是3个，则活过来。
def rule_reproduce_classic(count):
    if count == 3:
        return black
    else:
        return white


#随机存活规则
def rule_survive_random(count):
    if count >= 6:
        return white
    elif count >= 5:
        if random.random() < 0.7:
            return black
        return white
    elif count >= 3:
        return black
    else:
        return white

#经典存活规则
#人口过少：任何活细胞如果活邻居少于2个，则死掉。
#正常：任何活细胞如果活邻居为2个或3个，则继续活。
#人口过多：任何活细胞如果活邻居大于3个，则死掉。
def rule_survive_classic(count):
    if count > 3:
        return white
    elif count >= 2:
        return black
    else:
        return white
