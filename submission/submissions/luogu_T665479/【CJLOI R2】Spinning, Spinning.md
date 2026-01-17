# 【CJLOI R2】Spinning, Spinning

## 题目描述

The Herta has brought $ k $ Herta puppets, holding hands and forming a circle (the $ i $-th puppet is adjacent to the $ (i+1) $-th, and the 1st puppet is adjacent to the $ k $-th). Each puppet is labeled with a number from $ 1 $ to $ k $, and the $ i $-th puppet has a positive integer $ a_i $.

Now, The Herta conducts multiple experiments. Each experiment produces a result, defined as an integer. Every pair of adjacent puppets contributes to the result by adding the greatest common divisor (gcd) of their numbers. Since puppet number 1 is The Herta's assistant, it additionally contributes its own number to the result.

The expected result of the experiment is defined as the sum of all numbers on the puppets. If the actual result equals the expected result, the experiment is successful.

As the experiment must be replicated multiple times, and repeating the same experiment bores The Herta, the assistant—puppet number 1—asks you to calculate, given that its number is fixed, how many different successful experiments you can construct.

Note: Two experiments are considered different if and only if there exists a puppet with the same index having different numbers in the two experiments. For example, $ 1,1,2,3 $ and $ 1,2,3,1 $ are different, while $ 1,1,2,3 $ and $ 1,1,2,3 $ are the same.

## 输入格式

Input one line with two integers: $ k $ and $ a_1 $.

## 输出格式

On the first line, output the total number of experiments $ x $. Then output $ x $ lines, each containing $ k $ numbers representing $ a_1, a_2, \ldots, a_k $.

Note: Although theoretically you can use any positive integer in the $ a $ array, for simplicity, only 32-bit signed integers are allowed in $ a $.

## 提示

### Sample Explanation

The sample solution is not unique; these are just a few possible solutions.

### Scoring Criteria

Only successful experiments are counted. **If you have two or more identical experiments, only one is recorded.**

For each test case, **if your output includes any failed experiment, you score 0 points.**

Otherwise, if your code outputs $ x $ distinct valid schemes, you score $ P(x) \times 100\% $ of the points for that test case, where $ P(x) $ is rounded to two decimal places:

$$
P(\mathrm{cnt}) = 
\begin{cases}
1 & \mathrm{cnt} \geq p_5 \\
0.8 + 0.2 \cdot \dfrac{\mathrm{cnt} - p_4}{p_5 - p_4} & p_4 \leq \mathrm{cnt} < p_5 \\
0.5 + 0.3 \cdot \dfrac{\mathrm{cnt} - p_3}{p_4 - p_3} & p_3 \leq \mathrm{cnt} < p_4 \\
0.3 + 0.2 \cdot \dfrac{\mathrm{cnt} - p_2}{ p_3 - p_2 } & p_2 \leq \mathrm{cnt} < p_3 \\
0.1 + 0.2 \cdot \dfrac{\mathrm{cnt} - 1}{ p_2 - 1 } & p_1 \leq \mathrm{cnt} < p_2 \\
0 & \mathrm{cnt} < p_1
\end{cases}
$$

In other words, outputting $ p_1 $ schemes gives 10% score, $ p_2 $ gives 30%, $ p_3 $ gives 50%, $ p_4 $ gives 80%, and $ p_5 $ gives 100%. Scores between these thresholds are linearly interpolated.

Note: There are 10 test cases, each worth 10 points. The score on Luogu is rounded down.

This problem uses a special judge (SPJ). A checker is provided, which is the same as the one used in final evaluation. You can refer to the testlib documentation to compile and use it.

Although there are many ways to construct solutions, please avoid outputting too many schemes, as the checker may TLE, resulting in 0 points for that test case.

### Test Case Constraints

For all data, $ n \le 20 $ and $ 0 < a_1 < 2^{16} $. The test cases are as follows:

| Test Case ID | $ n= $ | $ a_1= $ | $ p_1 $ | $ p_2 $ | $ p_3 $ | $ p_4 $ | $ p_5 $ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 5 | 24 | 1 | 10 | 20 | 38 | 75 |
| 2 | 5 | 1540 | 1 | 10 | 80 | 118 | 275 |
| 3 | 5 | 21840 | 1 | 10 | 160 | 398 | 715 |
| 4 | 10 | 105 | 1 | 45 | 360 | 1498 | 2805 |
| 5 | 10 | 11352 | 1 | 45 | 360 | 6538 | 7845 |
| 6 | 10 | 32023 | 1 | 45 | 180 | 658 | 1305 |
| 7 | 20 | 132 | 1 | 190 | 760 | 53488 | 58735 |
| 8 | 20 | 2500 | 1 | 190 | 950 | 67983 | 74600 |
| 9 | 20 | 13680 | 1 | 190 | 2280 | 286008 | 301935 |
| 10 | 20 | 21600 | 1 | 190 | 2280 | 344148 | 360075 |

## 时空限制

时间限制: 4000 ms
内存限制: 512 MB
