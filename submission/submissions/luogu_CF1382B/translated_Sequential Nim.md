# Sequential Nim (翻译版)

## 题目描述

有 $n$ 堆石子，第 $i$ 堆有 $a_i$ 个。有两个人在玩取石子游戏。

两个人轮流取石子，每次取编号最小且有石子的堆。每个人可以在一堆石子中取走若干个（至少取 $1$ 个），当一个人没有石子可以取了，他就输了。

现在给出每堆石子的数量，假设两人的都采用最优策略，问最后是先手 (first) 胜利还是后手 (second) 胜利。

## 输入格式

The first line contains a single integer $ t $ ( $ 1\le t\le       1000 $ ) — the number of test cases. Next $ 2t $ lines contain descriptions of test cases.

The first line of each test case contains a single integer $ n $ ( $ 1\le n\le 10^5 $ ) — the number of piles.

The second line of each test case contains $ n $ integers $ a_1,\ldots,a_n $ ( $ 1\le a_i\le 10^9 $ ) — $ a_i $ is equal to the number of stones in the $ i $ -th pile.

It is guaranteed that the sum of $ n $ for all test cases does not exceed $ 10^5 $ .

## 输出格式

For each test case, if the player who makes the first move will win, output "First". Otherwise, output "Second".

## 提示

In the first test case, the first player will win the game. His winning strategy is:

1. The first player should take the stones from the first pile. He will take $ 1 $ stone. The numbers of stones in piles will be $ [1, 5, 4] $ .
2. The second player should take the stones from the first pile. He will take $ 1 $ stone because he can't take any other number of stones. The numbers of stones in piles will be $ [0,         5, 4] $ .
3. The first player should take the stones from the second pile because the first pile is empty. He will take $ 4 $ stones. The numbers of stones in piles will be $ [0, 1, 4] $ .
4. The second player should take the stones from the second pile because the first pile is empty. He will take $ 1 $ stone because he can't take any other number of stones. The numbers of stones in piles will be $ [0, 0, 4] $ .
5. The first player should take the stones from the third pile because the first and second piles are empty. He will take $ 4 $ stones. The numbers of stones in piles will be $ [0, 0,         0] $ .
6. The second player will lose the game because all piles will be empty.

## 时空限制

时间限制: 1000 ms
内存限制: 250 MB
