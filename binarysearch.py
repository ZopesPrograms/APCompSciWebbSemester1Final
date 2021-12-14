import math
# lets fix this code

def binarysearch(x, listv, recursive=False, index=None):
    midval = 0
    mid = math.ceil(len(listv)/2)-1

    print(listv)

    if mid == math.floor(len(listv)/2)-1:
        midval = (listv[mid] + listv[mid+1])/2
        if x < midval:
            del listv[mid+1:]
            return binarysearch(x, listv, True, mid)
        elif x > midval:
            del listv[:mid]
            return binarysearch(x, listv, True, mid)
    else:
        midval = listv[mid]
        if midval == x:
            return mid
        elif x < midval:
            del listv[mid:]
            return binarysearch(x, listv, True, mid)
        elif x > midval:
            del listv[:mid+1]
            return binarysearch(x, listv, True, mid)

if __name__ == '__main__':
    print(binarysearch(7, [1,2,3,4,5,6,7,8,9,10]))
