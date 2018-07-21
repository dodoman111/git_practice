#1
def count_matches(some_list,value):
    if some_list ==[]:
        return 0
    if some_list[0] == value:
        return 1 + count_matches(some_list[1:],value)
    else:
        return count_matches(some_list[1:],value)



#2
def double_each(some_list):
    a =[]
    if some_list ==[]:
        return a
    return a + [some_list[0]]*2 + double_each(some_list[1:])



#3
a = 0
def sums_to(nums,k):
    global a
    if nums ==[]:
        if a == k:
            return True
        else : return False
    else:
        a = nums[0] + a
        return sums_to(nums[1:],k)



#4
def is_reverse(string1,string2):
    if string1 == '' and string2 == '':
        return True
    if string1 !='' and string2 !='' and string1[0] == string2[-1]:
        return is_reverse(string1[1:],string2[:-1]) 
    else: 
        return False



#5
def sort_repeated(L):
    a = set()
    for j in L:
        if L.count(j) > 1:
            a.add(j)
    return list(a)


def make_Dict_number(lst):
    d = {}
    for k in sorted(lst):
        d[k] = lst.count(k)
    return d


#6
def make_Dict_number(lst):
    s  ={}
    L = sorted(lst) +['']
    count  = 1
    for i in range(len(L)-1):
        if L[i] == L[i+1]:
            count += 1
        else :  
            s[L[i]] = count
            count = 1
    return s


def mostFrequent(lst):
    a =[]
    d = make_Dict_number(lst)
    maxv = max(d.values())
    for i in d.keys():
        if d.get(i) == maxv:
            a.append(i)
    print(*a)
