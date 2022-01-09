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

def find_set_bit(n):
	c = 0
	while (n!=0):
		c += 1
		n = n&(n-1)
	return c

def find_bit_num (a, b)->int:
	return (find_set_bit(a^b))

if __name__ == "__main__":
	T = int(input().strip())
	for ti in range(T):
		a, b = map(int, input().strip().split(' '))
		print(find_bit_num(a, b))
    
