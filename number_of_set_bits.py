## hackerrank: https://www.hackerrank.com/contests/bz-cci-53/challenges/number-of-set-bits-/problem

'''
Given A 32-bit Unsigned Integer N. Return Number Of Set Bits In N.
Set Bits Are Number Of Bits Which are equal to 1 in Binary Representation of N.

Input Format

First Line Of Input Contains Number T Denoting Number Of testcases.
Next N Lines Consists Of A Single Integer N In Each.

Constraints

1 <= N <= 4294967295

For 10% of total marks:
1 <= T <= 104

For 90% of total marks:
1 <= T <= 106

Output Format

Print Number Of Set Bits In N.

Sample Input 0

1
3
Sample Output 0

2
Explanation 0

32 Bit Binary Representation of 3 00000000000000000000000000000011 So Number Of Set Bits Are 2.
'''

def set_bit_number(n)->int:
    c = 0
    while n!= 0:
        c += 1
        n = n&(n-1) #Learning: n&(n-1) -> setd the right most set bit to 0
    return c

if __name__ == "__main__":
    T = int(input().strip())
    for ti in range(T):
        n = int(input().strip())
        print(set_bit_number(n))
        
        
