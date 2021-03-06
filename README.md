# Prefix-Number

Given a very large number N, you need to count the total ways such that if we divide the number into two parts a and b then number a can be obtained by integral division of number b by some power p of 10 and p≥0.
For example: Let 220 be a number then, if you divide the number into two parts 2 and 20 then, if 20 is divided by 101 gives the number 2. 

# Important Notes:

1. You cannot perform any irregular division of the number i.e the original number should be formed after concatenation of the two parts a and b. Example of irregular division is 289 divided as 29 and 8

2. Both the numbers a and b should not contain any leading zeros

3. Integral division of any two numbers a,b is F(a/b) where F is the floor function

# Input Format

A line that contains a very large number N(string of digits 0−9).

# Output Format
Total number of ways to divide the string such that it follows the above constraints.
Input Constraints
1≤|N|≤105 where |N| is length of the number N

# Sample Input
5 <br>
7 21 18 3 12

# Sample Output
7 3 <br>
12 18 21 
