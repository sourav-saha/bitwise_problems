'''
Problem link - https://vjudge.net/problem/UVA-12911
also the problem is explained in the .txt file with this same name.

This code also explains how to read all inputs when number of test cases are not defined. 
'''

import sys


def checkBit(n, i):
    return (1 << i) & n

def create_subset(arr):
    n = len(arr)
    #print(arr, n)
    res = []
    for i in range(1, (1<<n)-1):
        sublist = []
        for bitPos in range(n):
            if checkBit(i, bitPos):
                sublist.append(arr[bitPos])
        res.append(sublist)
    return res

def subset_sum(arr, N, T) -> int:
    count = 0
    firstset = create_subset(arr[:(N//2)])
    secondset = create_subset(arr[N//2:])
    
    my_dict = {}
    for item in firstset:
        if sum(item) in my_dict:
            my_dict[sum(item)] += 1
        else:
            my_dict[sum(item)] = 1

    for item in secondset:
        s = sum(item)
        if (T-s) in my_dict:
            count += my_dict[T-s]
    return count

if __name__ == "__main__":
    try:
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break
            # your logic here
            N, T = map(int, line.strip().split(' '))

            line = sys.stdin.readline().strip()
            if not line:
                break
            arr = list(map(int, line.strip().split(' ')))
            print(subset_sum(arr, N, T))

    except EOFError:
        pass
    except Exception as e:
        print(e)

