def buble_sort(alist):
    '''
    冒泡排序
    '''
    n = len(alist)
    for j in range(0, n-1):  # 0 ~ n-2
        # 多少次
        count = 0
        for i in range(0, n-1-j):  # i 下标 0 ~ n-2
            # 从头到尾
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
        if 0 == count:
            return

# i 0 ~ n-2   range(0, n-1)       j=0
# i 0 ~ n-3   range(0, n-1-1)     j=1
# i 0 ~ n-4   range(0, n-1-2)     j=2
# j=n     i  range(0, n-1-j)

if __name__ == "__main__":
    li = [54, 26, 93, 18, 23, 55, 20]
    buble_sort(li)
    print(li)