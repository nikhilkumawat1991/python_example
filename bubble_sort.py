



lst1 = ["nikhil","kumawat"]


def bubble_sort(lst):
    for i in range(0,len(lst)):
        if lst[i] > lst[i+1]:
            swap = lst[i]
            lst[i] = lst[i+1]
            lst[i+1]  = swap




lst = [4,2,7,1,9,0]
bubble_sort(lst)
print(lst)