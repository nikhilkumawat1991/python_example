#Find the subarray in a list with given sum
#[10,15,-5,15,-10,5]
#sum=5

lst = [1,15,-5,15,-10,5]
sum = 5

def find_sum_in_subarray(lst,sum):
    for i in range(len(lst)):
        currentsum = lst[i]
        print(f"current element is: {i} and the value is: {currentsum}")
        next_val = i + 1
        while next_val < len(lst):
            if currentsum == sum:
                print(f"value found between: {i} and {next_val}")
                break
            else:
                currentsum = currentsum + lst[next_val]
                print(f"currentsum is: {currentsum}")
                next_val = next_val + 1

    return 0


if __name__ == "__main__":
    find_sum_in_subarray(lst,sum)








if __name__ == '__main__':
    find_sum_in_subarray(lst,5)

