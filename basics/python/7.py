#def matrix ()
tmp = []
arr = []
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in a:
        arr.append(j[i])
for k in range(len(a)):
    tmp.append(arr[:len(a)])
    arr = arr[len(a):]
print (tmp)



