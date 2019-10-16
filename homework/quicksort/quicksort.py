
def quicksort(list):
    if len(list) < 2:
        return list
    #如果list長度小於2不用排直接return
    else:
        pivot=list[0]#以list中第0個當基準
        smaller=[i for i in list[1:] if i <= pivot]#比pivot小放smaller[]
        bigger=[i for i in list[1:] if i > pivot]#比pivot大放bigger[]
        return quicksort(smaller)+[pivot]+quicksort(bigger)#若smaller[]跟bigger[]中的數大於2，繼續排列，直到全部都剩1個
