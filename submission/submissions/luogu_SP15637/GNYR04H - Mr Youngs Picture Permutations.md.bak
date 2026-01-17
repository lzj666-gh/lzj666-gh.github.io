# GNYR04H - Mr Youngs Picture Permutations

## 题目描述

Mr. Young wishes to take a picture of his class. The students will stand in rows, with each row no longer than the row behind it and the left ends of the rows aligned. For instance, 12 students could be arranged in rows (from back to front) of 5, 3, 3 and 1 students.

 ```
X X X X X
X X X
X X X
X
```
In addition, Mr. Young wants the students in each row arranged so that heights decrease from left to right. Also, student heights should decrease from the back to the front. Thinking about it, Mr. Young sees that for the 12-student example, there are at least two ways to arrange the students (numbers represent heights, with 1 meaning the tallest):

 ```
 1  2  3  4  5     1  5  8 11 12
 6  7  8           2  6  9
 9 10 11           3  7 10
12                 4
```
Mr. Young wonders how many different arrangements of the students there might be for a given arrangement of rows. He tries counting by hand starting with rows of lengths 3, 2 and 1 and counts 16 arrangements:

 ```
123 123 124 124 125 125 126 126 134 134 135 135 136 136 145 146
45  46  35  36  34  36  34  35  25  26  24  26  24  25  26  25
6   5   6   5   6   4   5   4   6   5   6   4   5   4   3   3
```
Mr. Young sees that counting by hand is not going to be very effective for any reasonable number of students. He asks you to help out by writing a computer program to determine the number of different arrangements of students for a given set of rows.

   
Input
=====

The input describes a series of test, each described in two lines. The first line gives the number of rows, _k_, as a decimal integer. The second line contains the lengths of the rows from back to front (_n_ $ _{1} $ ,_n_ $ _{2} $ ,..., _n_ $ _{k} $ ) as decimal integers separated by single spaces. The problem set ends with a line with a row count of 0. There will never be more than 5 rows and the total number of students, _N_, (sum of the row lengths) will be at most 30.

   
Output
======

For each test case output a single integer: The number of arrangements of _N_ students into the given rows, so that the heights decrease along each row from left to right and along each column from back to front (assume that all heights are distinct). The results should be in separate lines. The input data will be chosen so that the result will always fit in an unsigned 32-bit integer.

   
Sample
======

Input

 ```
1
30
5
1 1 1 1 1
3
3 2 1
4
5 3 3 1
5
6 5 4 3 2
2
15 15
0
```
Output

 ```
1
1
16
4158
141892608
9694845
```

## 时空限制

时间限制: 562 ms
内存限制: 1500 MB
