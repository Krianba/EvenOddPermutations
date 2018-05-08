def is_even(p):

  lengthOfNumbers = len(p) - 1
  numOfTranspos = 0
  pivot = 0

  while(pivot < lengthOfNumbers):

    nextToSort = pivot;
    minimal = nextToSort;

    while(nextToSort < lengthOfNumbers):  
      nextToSort = nextToSort  + 1;
      if p[nextToSort ] < p[minimal]:
        minimal = nextToSort;
    
    
    tmp= p[pivot];
    if(p[pivot] != p[minimal]):
      p[pivot] = p[minimal];
      p[minimal] = tmp;
      numOfTranspos = numOfTranspos + 1;
    pivot = pivot + 1;
  
  if(numOfTranspos % 2 == 0):
    return False
  else:
    return True

