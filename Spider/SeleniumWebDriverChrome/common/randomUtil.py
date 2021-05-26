import random
import time

def time_sleep(second):
    '''
    从1秒开始，最长睡眠second秒
    '''
    i_sleep = random.randint(1, second)
    print('sleep: '+ str(i_sleep) + ' second')
    time.sleep(i_sleep)