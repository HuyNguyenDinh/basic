
def selection_sort(n):
    for i in range(len(n)):
        min = i
        for j in range(i, len(n)):
            if n[min] > n[j]:
                min = j
        n[i], n[min] = n[min], n[i]
    return n

def interchange_sort(n):
    for i in range(len(n)):
        for j in range(i, len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]
    return n

def insertion_sort(n):
    for i in range(1, len(n)):
        key = n[i]
        pos = i - 1
        while pos >= 0 and key < n[pos]:
            n[pos + 1] = n[pos]
            pos = pos-1
        n[pos+1] = key
    return n

def bubble_sort(n):
    for i in range(len(n)):
        for j in range(len(n)-1, i, -1):
            if n[j] < n[j-1]:
                n[j], n[j - 1] = n[j-1], n[j]
    return n

def quick_sort(n):
    if len(n) <= 1:
        return n
    else:
        left = []
        right = []
        equal = []
        pivot = n[int(len(n)/2)]
        for i in n:
            if i < pivot:
                left.append(i)
            if i > pivot:
                right.append(i)
            if i == pivot:
                equal.append(i)
        return quick_sort(left) + equal + quick_sort(right)

def merge(a, b):
    n = []
    i = j = 0
    while(i < len(a) and j < len(b)):
        if a[i] < b[j]:
            n.append(a[i])
            i = i + 1
        else:
            n.append(b[j])
            j = j + 1
    for h in range(i, len(a)):
        n.append(a[h])
    for k in range(j, len(b)):
        n.append(b[k])
    return n

def merge_sort(n):
    if len(n) <= 1:
        return n
    else:
        mid = int(len(n)/2)
        m1 = merge_sort(n[0:mid])
        m2 = merge_sort(n[mid:])
        kq = merge(m1, m2)
        return kq