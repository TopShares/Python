'''
快速排序(Quick Sort)使用分治法策略。

它的基本思想是：选择一个基准数，通过一趟排序将要排序的数据分割成独立的两部分；其中一部分的所有数据都比另外一部分的所有数据都要小。然后，再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

快速排序步骤

(1) 从数列中挑出一个基准值。

(2) 将所有比基准值小的摆放在基准前面，所有比基准值大的摆在基准的后面(相同的数可以到任一边)；在这个分区退出之后，该基准就处于数列的中间位置。

(3) 递归地把"基准值前面的子数列"和"基准值后面的子数列"进行排序。
'''
def QuickSort(arr,firstIndex,lastIndex):
    if firstIndex<lastIndex:
        divIndex=Partition(arr,firstIndex,lastIndex)
 
        QuickSort(arr,firstIndex,divIndex)       
        QuickSort(arr,divIndex+1,lastIndex)
    else:
        return
 
 
def Partition(arr,firstIndex,lastIndex):
    i=firstIndex-1
    for j in range(firstIndex,lastIndex):
        if arr[j]<=arr[lastIndex]:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[lastIndex]=arr[lastIndex],arr[i+1]
    return i
 
 
arr=[1,4,7,1,5,5,3,85,34,75,23,75,2,0]
 
print("initial array:\n",arr)
QuickSort(arr,0,len(arr)-1)
print("result array:\n",arr)
