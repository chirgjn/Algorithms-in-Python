def partition(l,start, end):
    i = start + 1
    p = l[start]
    for j in range(start+1, end+1):
        if l[j] < p:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[start], l[i-1] = l[i-1], l[start]
    return i-1
def quick_sort(l, start, end):
    if start < end:
        piv_pos = partition(l,start,end)
        quick_sort(l, start, piv_pos-1)
        quick_sort(l, piv_pos+1, end)
print "Enter no of elements"
l = []
for i in range(int(raw_input())):
    l.append(int(raw_input()))
quick_sort(l,0,len(l)-1)
print l
