import random
def bubblesort(arr):
  #travel through the array and avoid index error range (0, len(arr)-1)
  for i in range (0, len(arr)-1):
    #for every number at index(idx) perfrom the comparison and swap the numbers
    for idx in range(0, len(arr)-1):
      if arr[idx] > arr[idx+1]:
        arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
  print(arr)
#generate random array for testing
def gen_rand_arr(leng):
  rand_arr =[]
  for number in range(0,leng):
    number = random.randint(0,101)
    rand_arr.append(number)
  return rand_arr

bubblesort(gen_rand_arr(5))