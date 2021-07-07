lst = [1,3,5,2,6,4,8,9]

start = 0
for i in range(0,7):
    var = []
    for i in range(0,3):;
        if start == len(lst):
            start = 0
        var.append(lst[start])
        start +=1
    print(var)
