'''
Given two integers n and k. Reset (set to zero) the last k bits in the number n, and print the result. It is recommended to find solution without loops.

Input
Two numbers n (0 ≤ n ≤ 231 - 1) and k (0 ≤ k ≤ 30).

Output
Print the result of resetting k last bits.

Input example #1 content_copy
5 1
Output example #1 content_copy
4

https://mentorpick.com/blog/view/61e04cebf122fe0e00b7984e
'''

def reset_bits(n, k)->int:
	return n & ~((1<<k)-1)
 
 
if __name__ == "__main__":
	n, k = map(int, input().strip().split(' '))
	print(reset_bits(n, k))
