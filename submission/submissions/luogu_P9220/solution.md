# P9220 题解

如果 Alice 能够一步胜利，就判 Alice 胜利。如果 Alice 第一步无法胜利，并且 Alice 第一步不论如何操作，Bob 都能在第二步胜利，就判 Bob 胜利。否则直接判平局。

理由：若某个玩家第 $k$ 步不存在必胜方法，而他在第 $(k+2)$ 步存在必胜方法，那么另一个玩家可以在第 $(k+1)$ 步选择抵消该玩家第 $k$ 步的影响，与第 $(k+2)$ 步必胜矛盾。所以该玩家在 $(k+2)$ 步不必胜。显然由数学归纳法可知 $\forall k\geq 3$，第 $k$ 步没有必胜法。

我们可以对这个图跑 Tarjan 算法缩点。如果一个强连通分量内有异色点就可以直接判断平局。否则我们会得到一个 DAG。

### 判断 Alice 必胜局面

对 DAG 跑拓扑排序，直到遇到第一个黑点，显然 Alice 第一步只能对这个点进行操作。那么我们从这个点出发搜索，如果遇到白点，则 Alice 必不胜。如果搜索完成之后有未被访问过的黑点，则 Alice 必不胜。否则 Alice 必胜。

### 判断 Bob 必胜局面

下文将入度为 $0$ 的节点简记为“根节点”。（注意根节点可能不唯一）

若存在至少一个根节点为白色，可以发现 Bob 必胜当且仅当所有节点为白色。这是因为 Alice 先手可以操作这个根节点，Bob 后手为了把它变回白色必定会选择这个点。而这就会使得整个图回到最开始的状态。

若所有根节点均为黑色且存在至少两个根节点，那么 Bob 必胜当且仅当 $n=2$。这是因为如果 $n > 2$，Alice 可以选择两个根节点以外的一个点。Bob 显然无法一步操作把所有根节点全部变白。

若所有根节点均为黑色且只有一个根节点。那么 Alice 一定可以操作某个根节点以外的点，使得整个图不是全黑。因而 Bob 无法胜利。注意一个边界情况：如果只有两个点，一黑一白，黑点连边向白点，则 Bob 必胜。

综上，Bob 必胜的 DAG 共有三种：

1. 两个孤立黑点。

2. 两个点，一条边。其中边的方向自黑点向白点。

3. 所有点均为白点。

---

由此，本题目完成。时空复杂度均为 $O(n+m)$。