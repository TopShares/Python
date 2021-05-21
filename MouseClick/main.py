#! python3
import pyautogui, sys
import random, time

print('Press Ctrl-C to quit.')

def timerC(n):
    '''
    一共执行n次
    '''
    while 1 < n:
        funnyX = 1686
        funnyY = 537
        pyautogui.moveTo(funnyX, funnyY)  # 此处为要执行的任务
        pyautogui.click()

        print(time.strftime('%Y-%m-%d %X',time.localtime()))
        print('Mouse to X: %s, Y: %s', funnyX, funnyY)

        time.sleep(0.5)

        funnyX = 938
        funnyY = 588
        pyautogui.moveTo(funnyX, funnyY)  # 此处为要执行的任务
        pyautogui.click()
        n -= 1


def timer(n):
    '''''
    每n秒执行一次
    '''
    while True:
        time.sleep(n)

        # funnyX = random.randint(10,555)
        # funnyY = random.randint(1,233)
        funnyX = 1607
        funnyY = 601
        pyautogui.moveTo(funnyX, funnyY)  # 此处为要执行的任务
        pyautogui.click()

        print(time.strftime('%Y-%m-%d %X',time.localtime()))
        print('Mouse to X: %s, Y: %s', funnyX, funnyY)

        time.sleep(1)


        funnyX = 880
        funnyY = 560
        pyautogui.moveTo(funnyX, funnyY)  # 此处为要执行的任务
        pyautogui.click()


        # pyautogui.dragTo(funnyX,funnyY)
timerC(113)



# timer(2)

# try:
#     # while True:
#     #     x, y = pyautogui.position()
#     #     positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#     #     print(positionStr, end='')
#     #     print('\b' * len(positionStr), end='', flush=True)

# 	pyautogui.move(0, 50)


# except KeyboardInterrupt:
# 	print('\n')