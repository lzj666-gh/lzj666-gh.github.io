# P1656 题解

解题思路：

即求图中的桥（割边）

可以使用Tarjan算法


由于本题范围很小，枚举即可

枚举一条边，将这条边去掉后随便选一个点进行FloodFill，或者说从这个点开始进行DFS或BFS遍历，看是否能遍历到所有的点。

如果不可以则这条边为割边，否则不是。
