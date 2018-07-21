
def selection_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j], lst[i]
    return lst


def insertion_sort(lst):
    for i in range(1,len(lst)):
        while i >0 and lst[i]<lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i]
            i-=1
    return lst


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(i,len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    return lst


def merge(left,right):
    a = []
    ind_left = 0
    ind_right = 0
    while ind_left <len(left) and ind_right < len(right):
        if left[ind_left] <= right[ind_right]:
            a.append(left[ind_left])
            ind_left += 1
        else:
            a.append(right[ind_right])
            ind_right += 1
    a.extend(left[ind_left:])
    a.extend(right[ind_right:])
    return a       


def merge_sort(lst):
    if len(lst)==0 or len(lst)==1:
        return lst[:len(lst)]
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    newlist1 = merge_sort(left)
    newlist2 = merge_sort(right)
    return merge(newlist1,newlist2)


def quick_sort(lst):
    if len(lst)>1:
        pivot_ind = len(lst)//2
        smal_lst =[]
        larg_lst =[]
        for i,val in enumerate(lst):
            if i != pivot_ind:
                if val<lst[pivot_ind]:
                    smal_lst.append(val)
                else:
                    larg_lst.append(val)
        quick_sort(smal_lst)
        quick_sort(larg_lst)
        lst[:] = smal_lst + [lst[pivot_ind]] +larg_lst
    return lst

