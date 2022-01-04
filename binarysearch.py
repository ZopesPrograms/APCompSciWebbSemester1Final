import math
# lets fix this code

def binarysearch(x, listv, offset=0):
    midval = 0
    mid = math.floor((len(listv)-1)/2)

    #print(listv)
    #print('Stupid offset is to ' + str(offset))

    if mid == len(listv)/2 and mid != 0:
        midval = (listv[mid-1] + listv[mid])/2
        print('Midval to: ' + str(midval))

        if x < midval:
            #print('Middle index is ' + str(mid + 1))
            del listv[mid+1:]
            #print('Listv to A ' + str(listv))
            return binarysearch(x, listv, offset+mid)
        elif x > midval:
            #print('Middle index is ' + str(mid))
            del listv[:mid]
            #print('Listv to B ' + str(listv))
            return binarysearch(x, listv, offset+mid)
    else:
        midval = listv[mid]
        print('Midval to: ' + str(midval))

        if midval == x:
            return mid+offset
        elif x < midval:
            del listv[mid:]
            return binarysearch(x, listv, offset+mid)
        elif x > midval:
            del listv[:mid+1]
            return binarysearch(x, listv, offset+mid)

if __name__ == '__main__':
    print('Expected 5 got ' + str(binarysearch(7, [0,1,2,3,4,7])) + ' for search 7 in [0,1,2,3,4,7].')
    print('Expected 4 got ' + str(binarysearch(7, [0,1,2,3,7,8])) + ' for search 7 in [0,1,2,3,7,8].')
    print('Expected 3 got ' + str(binarysearch(7, [0,1,2,7,8,9])) + ' for search 7 in [0,1,2,7,8,9].')
    print('Expected 2 got ' + str(binarysearch(7, [0,1,7,8,9,10])) + ' for search 7 in [0,1,7,8,9,10].')
    print('Expected 1 got ' + str(binarysearch(7, [0,7,8,9,10,11])) + ' for search 7 in [0,7,8,9,10,11].')
    print('Expected 0 got ' + str(binarysearch(7, [7,8,9,10,11,12])) + ' for search 7 in [7,8,9,10,11,12].')