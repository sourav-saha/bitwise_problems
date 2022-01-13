'''
Given an positive integer A (1 ≤ A≤100), output the lowest bit of A.

For example, given A = 26, we can write A in binary form as 11010, so the lowest bit of A is 10, so the output should be 2.

Another example goes like this: given A = 88, we can write A in binary form as 1011000, so the lowest bit of A is 1000, so the output should be 8.

Input

Each line of input contains only an integer A (1 ≤ A≤100). A line containing "0" indicates the end of input, and this line is not a part of the input data.

Output

For each A in the input, output a line containing only its lowest bit.

Input example #1 content_copy
26
88
0
Output example #1 content_copy
2
8
'''

def lowest_bit(n)->int:
	for bitpos in range(64):
		if (n&(1<<bitpos)):
			break
	
  # we are using this technique, to create a mask whose last n (e.g 3) bits will be set is 2^n -1 i.e. (1<<n)-1
  # e.g. for last 3 bits it is 0000 0111 i.e. 7(2^3 -1)
	n = n&((1<<bitpos+1)-1)
	return n

if __name__ == "__main__":
	while True:
		n = int(input().strip())
		if n == 0:
			break
		print(lowest_bit(n))
    
    
    
