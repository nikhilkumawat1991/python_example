#Index specific cyclic iteration in list


test_list = [5, 4, 2, 3, 7]

print ("The original list is : " + str(test_list))

K = 3

res = []
for i in range(len(test_list)):
    print(K % len(test_list))
    res.append(test_list[K % len(test_list)])
    print(res)
    K = K + 1

print ("The cycled list is : " +  str(res))