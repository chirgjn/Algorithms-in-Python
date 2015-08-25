def selection_sort(l):
    n = len(l)
    for i in range(n-1):
        m = i
        for j in range(i+1,n):
            if l[m]>l[j]:
                m = j
        l[i],l[m] = l[m],l[i]
print "Enter no of elements"
l = []
for i in range(int(raw_input())):
    l.append(int(raw_input()))
selection_sort(l)
print l
