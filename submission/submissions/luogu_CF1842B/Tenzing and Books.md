# Tenzing and Books

## 题目描述

Tenzing received $ 3n $ books from his fans. The books are arranged in $ 3 $ stacks with $ n $ books in each stack. Each book has a non-negative integer difficulty rating.

Tenzing wants to read some (possibly zero) books. At first, his knowledge is $ 0 $ .

To read the books, Tenzing will choose a non-empty stack, read the book on the top of the stack, and then discard the book. If Tenzing's knowledge is currently $ u $ , then his knowledge will become $ u|v $ after reading a book with difficulty rating $ v $ . Here $ | $ denotes the [bitwise OR operation](https://en.wikipedia.org/wiki/Bitwise_operation#OR). Note that Tenzing can stop reading books whenever he wants.

Tenzing's favourite number is $ x $ . Can you help Tenzing check if it is possible for his knowledge to become $ x $ ?

## 输入格式

Each test contains multiple test cases. The first line of input contains a single integer $ t $ ( $ 1 \le t \le 10^4 $ ) — the number of test cases. The description of test cases follows.

The first line of each test case contains two integers $ n $ and $ x $ ( $ 1 \leq n \leq 10^5 $ , $ 0 \leq x \leq 10^9 $ ) — the number of books in each stack and Tenzing's favourite number.

The second line of each test case contains $ n $ integers $ a_1,a_2,\ldots,a_n $ ( $ 0 \leq a_i \leq 10^9 $ ) — the difficulty rating of the books in the first stack, from top to bottom.

The third line of each test case contains $ n $ integers $ b_1,b_2,\ldots,b_n $ ( $ 0 \leq b_i \leq 10^9 $ ) — the difficulty rating of the books in the second stack, from top to bottom.

The fourth line of each test case contains $ n $ integers $ c_1,c_2,\ldots,c_n $ ( $ 0 \leq c_i \leq 10^9 $ ) — the difficulty rating of the books in the third stack, from top to bottom.

It is guaranteed that the sum of $ n $ does not exceed $ 10^5 $ .

## 输出格式

For each test case, output "Yes" (without quotes) if Tenzing can make his knowledge equal to $ x $ , and "No" (without quotes) otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

## 提示

For the first test case, Tenzing can read the following $ 4 $ books:

- read the book with difficulty rating $ 1 $ on the top of the first stack. Tenzing's knowledge changes to $ 0|1=1 $ .
- read the book with difficulty rating $ 1 $ on the top of the third stack. Tenzing's knowledge changes to $ 1|1=1 $ .
- read the book with difficulty rating $ 2 $ on the top of the first stack. Tenzing's knowledge changes to $ 1|2=3 $ .
- read the book with difficulty rating $ 5 $ on the top of the second stack. Tenzing's knowledge changes to $ 3|5=7 $ .

After reading all books, Tenzing's knowledge is $ 7 $ .

For the third test case, Tenzing can read $ 0 $ books to make his final knowledge equals to $ 0 $ .

## 时空限制

时间限制: 1000 ms
内存限制: 250 MB
