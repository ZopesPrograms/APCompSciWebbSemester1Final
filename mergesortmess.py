import math
import time

'''def sort_merge(list1, list2):
  assert type(list1[0]) == float or type(list1[0]) == int, (str(list1) + ' must be numerical list!')
  assert type(list2[0]) == float or type(list2[0]) == int, (str(list2) + ' must be numerical list!')

  result = []
  for i in range(len(list1)):
    for i in range(len(list2)):


def binary_search(x, list):
  assert type(list[0]) == float or type(list[0]) == int, (str(list) + ' must be numerical list!')
  
  partial_lists = []
  divs_num = math.ceil(len(list)/2)
  
  for i in range(divs_num):
    try:
      partial_lists.append([list[2*i], list[(2*i)+1]])
    except IndexError:
      partial_lists.append([list[2*i]])
    print(partial_lists[i])'''

def sorted_merge(list1, list2):
  merged = []

  if len(list1) > len(list2):
    while len(list2) > 0:
      if list2[-1] > list1[-1]:
        merged.append(list1.pop())
      else:
        merged.append(list2.pop())
    
  else:
    while len(list2) > 0:
      if list2[-1] > list1[-1]:
        merged.append(list1.pop())
      else:
        merged.append(list2.pop())

  print('Merged to: ' + str(merged))
  return merged

def equal_lists(list1, list2):
  list1.clear()
  for e in list2:
    list1.append(e)

def binary_search_better(x, listv):
  partial_lists = []
  temp_lists = []

  divs_num = math.ceil(len(listv)/2)

  for i in range(divs_num):
    try:
      if listv[2*i] < listv[(2*i)+1] :
        partial_lists.append([listv[2*i], listv[(2*i)+1]])
      else:
        partial_lists.append([listv[(2*i)+1], listv[2*i]])
    except IndexError:
      partial_lists.append([listv[2*i]])
    print(partial_lists[i])

  while len(partial_lists) < len(listv):
    divs_num = int(len(partial_lists)/2)
    
    for d in range(divs_num):
      print('Merge a ' + str(2*d) + ' and a ' + str((2*d) + 1))
      time.sleep(1)
      temp_lists.append(sorted_merge(partial_lists[(2*d)], partial_lists[(2*d)+1]))
      #print(sorted_merge(partial_lists[2*d], partial_lists[(2*d)+1]))
      #print('On run ' + str(d))
      #print('Temp list: ' + str(temp_lists[:]))

    partial_lists.clear()

    equal_lists(partial_lists, temp_lists)
    print(str(partial_lists))
  print('Concluded')
  return partial_lists

if __name__ == '__main__':
  print('Result is: ' + str(binary_search_better(1, [9, 2, 3, 4, 5, 1, 7, 8])))
