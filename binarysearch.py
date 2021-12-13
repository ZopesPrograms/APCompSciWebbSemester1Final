def binary_search(x, list):
  assert type(list[0]) == float or type(list[0]) == int, (str(list) + ' must be numerical list!')
  
  partial_lists = []
  divs_num = len(list)/2
