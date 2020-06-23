import random

# p概率输出1   1-p输出0
def basic_random(p):
    x = random.random()
    if x/1>=p:
        return 0
    else:
        return 1


# 调用两次basic_random   01 10 出现的概率是(1-p)p  p(1-p)是相同的
# 利用这一点01时返回0  10时返回1   其它情况递归一次获取
def format_random(p):
    x = basic_random(p)
    if x!=basic_random(p):
        return x
    else:
        return format_random(p)
