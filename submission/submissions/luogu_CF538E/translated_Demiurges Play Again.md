# Demiurges Play Again (翻译版)

## 题目描述

一棵有根树,A,B轮流操作,给每个叶子分配权值(1~叶子节点数)的一个排列.每次每人可以任选一条边走,A希望最后取得的叶子结点的权值最大,B希望最后取得的叶子结点的权值最小,两人都绝对聪明,问若让A分配权值则最后取得的最大权值是多少,若让B分配权值则最后取得的最小权值是多少

## 输入格式

The first line contains a single integer $ n $ — the number of nodes in the tree ( $ 1<=n<=2·10^{5} $ ).

Each of the next $ n-1 $ lines contains two integers $ u_{i} $ and $ v_{i} $ ( $ 1<=u_{i},v_{i}<=n $ ) — the ends of the edge of the tree; the edge leads from node $ u_{i} $ to node $ v_{i} $ . It is guaranteed that the described graph is a rooted tree, and the root is the node 1.

## 输出格式

Print two space-separated integers — the maximum possible and the minimum possible result of the game.

## 提示

Consider the first sample. The tree contains three leaves: 3, 4 and 5. If we put the maximum number 3 at node 3, then the first player moves there and the result will be 3. On the other hand, it is easy to see that for any rearrangement the first player can guarantee the result of at least 2.

In the second sample no matter what the arragment is the first player can go along the path that ends with a leaf with number 3.

## 时空限制

时间限制: 2000 ms
内存限制: 250 MB
