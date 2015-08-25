def insetion_sort(l):
    n = len(l)
    for i in range(1,n):
        temp = l[i]
        j = i
        while (j>0 and l[j-1]>temp):
            l[j] = l[j-1]
            j -= 1
        l[j] = temp
print "Enter no of elements"
l = []
for i in range(int(raw_input())):
    l.append(int(raw_input()))
insetion_sort(l)
print l
