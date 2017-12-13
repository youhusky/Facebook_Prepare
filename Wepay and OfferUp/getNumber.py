a = "12345"


def breaknumber(a):
    if len(a) <= 1:
        return False
    res = []
    for i in range(len(a)):
        temp = a[0:i] + a[i+1:]
        res.append(temp)
    return res

def getnumber(num):
    res = []
    for i in range(num,-1,-1):
        n1 = i
        n2 = breaknumber(str(n1))
        if n2:
            for each in n2:

                if int(each) + n1 == num:
                    res.append([n1, int(each)])
    return res

print getnumber(999)