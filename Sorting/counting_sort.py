def counting_sort(l,m):
    aux = [0]*(m+1)
    n = len(l)
    # Calculate frequency of each element
    for i in range(n):
        aux[l[i]] += 1
    # Calculate indexes to insert elements
    for i in range(1,m+1):
        aux[i] += aux[i-1]
    # Initialize output array
    l2 = [0]*n
    # Place each element in it's place in the output array
    for i in range(n):
        l2[aux[l[i]] - 1] = l[i]
        aux[l[i]] -= 1
    return l2
print "Enter no of elements"
l = []
for i in range(int(raw_input())):
    l.append(int(raw_input()))
m = max(l)
l = counting_sort(l,m)
print l
