#! python3
import pyautogui, sys
import random, time

print('Press Ctrl-C to quit.')

def timer(n):
    ''''' 
    每n秒执行一次 
    '''  
    while True:
        funnyX = random.randint(10,555)
        funnyY = random.randint(1,233)
        print(time.strftime('%Y-%m-%d %X',time.localtime()))
        print('Mouse to X: %s, Y: %s',funnyX,funnyY)
        pyautogui.moveTo(funnyX, funnyY)  # 此处为要执行的任务
        # pyautogui.dragTo(funnyX,funnyY)
        time.sleep(n)

timer(5)

# try:
#     # while True:
#     #     x, y = pyautogui.position()
#     #     positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#     #     print(positionStr, end='')
#     #     print('\b' * len(positionStr), end='', flush=True)

# 	pyautogui.move(0, 50)


# except KeyboardInterrupt:
# 	print('\n')