# P11364 题解

死于交集关系推导。

首先，区间 $\text{LCA}$ 的深度为：

$$\min_{l\le i<r}{\text{dep}_{\text{LCA}(i,i+1)}}$$

可以用虚树的方法证。


我们找出以 $\text{LCA}(i,i+1)$ 为最近公共祖先的最大区间 $[x_i,y_i,v_i]$，$v_i$ 为 $\text{dep}_{\text{LCA}(i,i+1)}$。

显然，查询是求与 $[l,r]$ 交集至少为 $k$，且最大的 $v_i$。可列出两个不等式。

$$
y_i\ge r\land x_i\le r-k+1 \\
l+k-1\le y_i\le r\land y_i-x_i+1\ge k
$$

第一个对 $r$ 扫描线，第二个对 $k$ 扫描线，时间复杂度 $O(n\log n)$。