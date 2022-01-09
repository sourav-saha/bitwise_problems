'''
Hackerrank: https://www.hackerrank.com/contests/bz-cci-53/challenges/bz-subsets-of-array/problem

Given an array of distinct integers, print all the subsets of the given array in lexicographical order.

For each test case, print all the subsets of given array one-per line (space separated elements).
Between two test cases output, give an empty line.

Sample Input 0

3 1 2
10 82 
Sample Output 0

1 
1 2
1 2 3
1 3
2
2 3
3

10 
10 82 
82 
'''

from functools import cmp_to_key

def checkBit(n, pos):
    if (n&(1<<pos) != 0):
        return True
    else:
        return False 

def compare(a, b):
    str_a = ""
    for n in a:
        str_a += str(n)
    
    str_b = ""
    for n in b:
        str_b += str(n)
        
    if str_a > str_b:
        return 1
    else:
        return -1

def print_subset_array(arr, n):
    res = []
    for i in range(1, (1<<n)): #pow(2,n)
        sublist = []
        for bitPos in range(n):
            if checkBit(i, bitPos):
                sublist.append(arr[bitPos])
        res.append(sublist)
        res = sorted(res, key=cmp_to_key(compare))
    return res

if __name__ == "__main__":
    T = int(input().strip())
    for ti in range(T):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        res = print_subset_array(sorted(arr), n)
        for item in res:
            print(*item)
        print()
	
	
    
