def merge(l,start,mid,end):
    a = []
    p = start
    q = mid + 1
    for i in range(start, end+1):
        if (p>mid):
            a.append(l[q])
            q += 1
        elif (q>end):
            a.append(l[p])
            p += 1
        elif (l[p]< l[q]):
            a.append(l[p])
            p += 1
        else:
            a.append(l[q])
            q += 1

    for i in a:
        l[start] = i
        start += 1
def merge_sort(l, start, end):
    if(start<end):
        mid = (start+end)/2
        merge_sort(l,start, mid)
        merge_sort(l,mid+1, end)
        merge(l,start, mid, end)

print "Enter no of elements"
l = []
for i in range(int(raw_input())):
    l.append(int(raw_input()))
merge_sort(l,0,len(l)-1)
print l
