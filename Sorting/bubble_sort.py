def bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
print "Enter no of elements"
l = []
for i in range(int(raw_input())):
    l.append(int(raw_input()))
bubble_sort(l)
print l
