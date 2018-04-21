def bubble_sort(list):#从大到小
    '''
    1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
    3.针对所有的元素重复以上的步骤，除了最后一个。
    4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    '''
    length=len(list)
    for index in range(length):
        for i in range(1,length-index):
            if list[i-1]<list[i]:
                list[i],list[i-1]=list[i-1],list[i]
    return list

def select_sort(list): #从大到小
    '''
    从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。
    '''
    length=len(list)
    for index in range(length):
        for i in range(index,length):
            if list[index]<list[i]:
                list[index],list[i]=list[i],list[index]
    return list

def quick_sort(list,left,right): #从小到大
    '''
    快速排序
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
    '''
    if left >= right:
        return list
    key = list[left]
    low = left
    high = right
    while left < right:
        while left < right and list[right] >= key:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] <= key:
            left += 1
        list[right] = list[left]
    list[right] = key
    quick_sort(list,low,left-1)
    quick_sort(list,left+1,high)
    return list


def adjust_heap(list,i,size):
    lchild = 2*i+1
    rchild = 2*i+2
    fa=i
    if i<size/2:
        if lchild<size and list[lchild]>list[fa]:
            fa = lchild
        if rchild<size and list[rchild]>list[fa]:
            fa = rchild
        if fa != i:
            list[fa],list[i] = list[i],list[fa]
            adjust_heap(list,fa,size)
def build_heap(list,size):
    for i in range(0,int(size/2))[::-1]:
        adjust_heap(list,i,size)
def heap_sort(list):
    '''
    初始时把要排序的数的序列看作是一棵顺序存储的二叉树，调整它们的存储序，使之成为一个 堆，这时堆的根节点的数最大。然后将根节点与堆的最后一个节点交换。然后对前面(n-1)个数重新调整使之成为堆。依此类推，直到只有两个节点的堆，并对 它们作交换，最后得到有n个节点的有序序列。从算法描述来看，堆排序需要两个过程，一是建立堆，二是堆顶与堆的最后一个元素交换位置。所以堆排序有两个函数组成。一是建堆的渗透函数，二是反复调用渗透函数实现排序的函数。
    '''
    size = len(list)
    build_heap(list,size)
    for i in range(0,size)[::-1]:
        list[0],list[i] = list[i],list[0]
        adjust_heap(list,0,i)
    return list




list=[10,23,1,53,654,54,16,646,65,3155,546,31]
#print bubble_sort(list)
#print(select_sort(list))
#print(quick_sort(list,0,len(list)-1))
print(heap_sort(list))
