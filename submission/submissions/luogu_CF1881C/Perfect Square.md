# Perfect Square

## 题目描述

Kristina has a matrix of size $ n $ by $ n $ , filled with lowercase Latin letters. The value of $ n $ is even.

She wants to change some characters so that her matrix becomes a perfect square. A matrix is called a perfect square if it remains unchanged when rotated $ 90^\circ $ clockwise once.

Here is an example of rotating a matrix by $ 90^\circ $ :

 ![](https://cdn.luogu.com.cn/upload/vjudge_pic/CF1881C/4b38bf84bcab0c377c4a504ebb049a6239821153.png)In one operation, Kristina can choose any cell and replace its value with the next character in the alphabet. If the character is equal to "z", its value does not change.

Find the minimum number of operations required to make the matrix a perfect square.

For example, if the $ 4 $ by $ 4 $ matrix looks like this:

 $ $$$\matrix{ a & b & b & a \cr b & c & \textbf{b} & b \cr b & c & c & b\cr a & b & b & a \cr } $ $ </p><p>then it is enough to apply  $ 1$$$ operation to the letter b, highlighted in bold.

## 输入格式

The first line of the input contains a single integer $ t $ ( $ 1 \le t \le 10^2 $ ) — the number of test cases.

Then follows the description of each test case.

The first line of each test case contains a single even integer $ n $ ( $ 2 \le n \le 10^3 $ ) — the number of rows and columns in the matrix.

Then follows $ n $ lines, each containing exactly $ n $ lowercase Latin letters.

It is guaranteed that the sum of $ n $ over all test cases does not exceed $ 10^3 $ .

## 输出格式

For each test case, output a single number on a separate line: the minimum number of operations required for Kristina to obtain a perfect square.

## 提示

The first test case is explained in the problem statement.

## 时空限制

时间限制: 2000 ms
内存限制: 250 MB
