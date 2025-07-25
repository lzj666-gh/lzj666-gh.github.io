# Sequential Nim

## 题目描述

There are $ n $ piles of stones, where the $ i $ -th pile has $ a_i $ stones. Two people play a game, where they take alternating turns removing stones.

In a move, a player may remove a positive number of stones from the first non-empty pile (the pile with the minimal index, that has at least one stone). The first player who cannot make a move (because all piles are empty) loses the game. If both players play optimally, determine the winner of the game.

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
