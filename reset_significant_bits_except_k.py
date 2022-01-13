'''
Given integer а and positive integer k. Find the number that contains only the last k bits of а (i.e. reset all bits of а except the last k bits).

Input
One line contains two numbers a and k (0 ≤ a ≤ 109).

Output
Print the number a with reseted bits except the last k.

Input example #1 
5 1
Output example #1 
1

Creating A Mask
If we want to keep only right most 3 bits of an 8-bit binary number N.  We should do bitwise AND of N with a mask 0000 0111 so 
that only right most 3 bits are preserved and rest all become 0.

To create a mask whose right most 3 bits are set, easiest way is to (1 << 3) - 1.  because 2 power 3 is 8, 
which in binary form is 0000 1000 and subtracting 1 from it makes it 0000 0111

So, in one line, answer is ( n & (1LL<<k)-1) )
'''

#Code : ToDo 
