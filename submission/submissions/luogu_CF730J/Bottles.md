# Bottles

## 题目描述

Nick has $ n $ bottles of soda left after his birthday. Each bottle is described by two values: remaining amount of soda $ a_{i} $ and bottle volume $ b_{i} $ ( $ a_{i}<=b_{i} $ ).

Nick has decided to pour all remaining soda into minimal number of bottles, moreover he has to do it as soon as possible. Nick spends $ x $ seconds to pour $ x $ units of soda from one bottle to another.

Nick asks you to help him to determine $ k $ — the minimal number of bottles to store all remaining soda and $ t $ — the minimal time to pour soda into $ k $ bottles. A bottle can't store more soda than its volume. All remaining soda should be saved.

## 输入格式

The first line contains positive integer $ n $ ( $ 1<=n<=100 $ ) — the number of bottles.

The second line contains $ n $ positive integers $ a_{1},a_{2},...,a_{n} $ ( $ 1<=a_{i}<=100 $ ), where $ a_{i} $ is the amount of soda remaining in the $ i $ -th bottle.

The third line contains $ n $ positive integers $ b_{1},b_{2},...,b_{n} $ ( $ 1<=b_{i}<=100 $ ), where $ b_{i} $ is the volume of the $ i $ -th bottle.

It is guaranteed that $ a_{i}<=b_{i} $ for any $ i $ .

## 输出格式

The only line should contain two integers $ k $ and $ t $ , where $ k $ is the minimal number of bottles that can store all the soda and $ t $ is the minimal time to pour the soda into $ k $ bottles.

## 提示

In the first example Nick can pour soda from the first bottle to the second bottle. It will take 3 seconds. After it the second bottle will contain $ 3+3=6 $ units of soda. Then he can pour soda from the fourth bottle to the second bottle and to the third bottle: one unit to the second and two units to the third. It will take $ 1+2=3 $ seconds. So, all the soda will be in two bottles and he will spend $ 3+3=6 $ seconds to do it.

## 时空限制

时间限制: 2000 ms
内存限制: 500 MB
