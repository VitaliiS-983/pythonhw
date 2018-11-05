def decToBin(n):
   if n > 1:
       decToBin(n//2)
   print (n % 2,end = '')
dec = 77

decToBin(dec)