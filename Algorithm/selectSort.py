def select_sort(alist):
    '''
    选择排序, 不稳定
    '''
    n = len(alist)
    minIndex = 0
    for j in range(n-1): # j 0 ~ n-2
        minIndex = j
        for i in range(j+1, n):
            if alist[minIndex] > alist[i]:
                minIndex = i
        alist[j], alist[minIndex] = alist[minIndex], alist[j]
    

if __name__ == "__main__":
    li = [54, 26, 93, 18, 23, 55, 20]
    select_sort(li)
    print(li)
