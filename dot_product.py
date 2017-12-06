A =[0,2,0,2,0,0,3,0,0,4]
B =[0,0,0,0,5,0,2,0,0,8]
def dot_product_unsorted(A,B):
    # T O(mn)
    # without order
    resA = {}
    resB = {}
    for i in range(len(A)):
        if A[i] != 0:
            resA[i] = A[i]

    for j in range(len(B)):
        if B[j] != 0:
            resB[j] = B[j]
    res = 0
    for each in resA:
        if each in resB:
            res += resA[each] * resB[each]
    print res

def dot_product_sorted(A,B):
    # O(min(m,n))
    # with order
    resA = []
    resB = []
    for i in range(len(A)):
        if A[i]:
            resA.append((i,A[i]))
    for j in range(len(B)):
        if B[j]:
            resB.append((j,B[j]))
    res = 0
    i1 = 0
    i2 = 0
    while i1 < len(resA) and i2 < len(resB):
        if resA[i1][0] == resB[i2][0]:
            res += resA[i1][1] * resB[i2][1]
            i1 += 1
            i2 += 1
        elif resA[i1][0] > resB[i2][0]:
            i2 += 1
        else:
            i1 += 1
    print res

def binarysearch(array, start, end, target):
    while start + 1 < end:
        mid = start + (end - start) / 2
        pair = array[mid]
        if pair[0] == target:
            return mid
        elif pair[0] < target:
            start = mid
        else:
            end = mid
    if array[end][0] == target:
        return end
    return start

def dot_product3(B,A):
    # if A is so large
    # O(mlgn) if resA and resB given
    resA = []
    resB = []
    for i in range(len(A)):
        if A[i]:
            resA.append((i,A[i]))
    for j in range(len(B)):
        if B[j]:
            resB.append((j,B[j]))
    i = 0
    j = 0
    res = 0
    print resA, resB
    while i < len(resA):
        pairA = resA[i]
        i += 1
        j = binarysearch(resB, j, len(resB)-1, pairA[0])
        pairB = resB[j]
        j += 1
        print pairA,pairB
        if pairA[0] == pairB[0]:
            res += pairA[1] * pairB[1]
    print res



dot_product_unsorted(A,B)
dot_product_sorted(A,B)
dot_product3(A,B)


