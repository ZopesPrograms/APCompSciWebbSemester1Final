import math
# lets fix this code

def binarysearch(x, listv, offset=0):
    midval = 0
    mid = math.ceil(len(listv)/2)-1

    print(listv)
    print('Stupid offset is to ' + str(offset))

    if mid == math.floor(len(listv)/2) and mid != 0:
        midval = (listv[mid] + listv[mid+1])/2
        print('Midval to: ' + str(midval))
        if x < midval:
            print('Middle index is ' + str(mid + 1))
            del listv[mid+1:]
            print('Listv to ' + str(listv))
            return binarysearch(x, listv, mid+offset)
        elif x > midval:
            print('Middle index is ' + str(mid))
            del listv[:mid]
            print('Listv to ' + str(listv))
            return binarysearch(x, listv, offset-mid)
    else:
        midval = listv[mid]
        if midval == x:
            return mid+offset
        elif x < midval:
            del listv[mid:]
            return binarysearch(x, listv, mid+offset)
        elif x > midval:
            del listv[:mid+1]
            return binarysearch(x, listv, offset-mid)

if __name__ == '__main__':
    print(binarysearch(7, [0,1,2,3,4,5,7,8,9,10]))
