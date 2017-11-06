a = [1,2,3,4,5,5,5,5,5,5,5,6]
#a= [1,2,2,4,5,5]
target = 5
l = 0
r = len(a) - 1
while l +1 < r:
    mid = (l+r)/2
    if a[mid] < target:
        l = mid 
    else:
        r = mid 
print l if a[l] == target else r


l = 0
r = len(a) -1
while l +1 < r:
    mid = (l+r)/2
    if a[mid] <= target:
        l = mid 
    else:
        r = mid 
print r if a[r] == target else l