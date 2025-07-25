# P4542 题解

感觉题解写的都太简略了，只是告诉你怎么建图，而没有告诉你为什么这样建，这样建为什么对。很反感这种现象，作为读者本来看题解就是因为思维跳跃性不够，到头来题解也要思维跳跃，真正的疑难点也没想通，没有意义。因此写这篇题解来补充一下建图的正确性和原因。


------------

大体先串一下主流做法。

首先我们用最短路算法求出 $dis_{i,j}$ 表示从 $i$ 到 $j$ 只经过编号不大于 $\max(i, j)$ 的点的最短路径。之后我们用 $dis$ 数组建图，跑最小费用最大流以求出一个分配方案使得：
-	每个点都被经过。
-	最后总花费最少。

现在来想一想这个图怎么建。

网络流对时间的概念不很敏感，所以说两个人分着走在网络流里可以一起流，不用太在意两个人的先后顺序会有影响。而且之前的 $dis$ 数组也对时间顺序做了一个保证。

上面的要求也就是说我们要找到若干条路径，以覆盖图中所有点。如果不考虑费用，我们会联想到最大流中的最小路径覆盖问题（每个点只能经过一次）。这个问题是按如下方法解决的：
-	将每个点 $u$ 拆开为 $u_{in}$ 和 $u_{out}$。
-	建立源汇点，对于每个 $u$，连接 $<S, u_{out}>$、$<u_{in}, T>$。
-	对于原图中的边 $<u, v>$，流网络里连 $<u_{out}, v_{in}>$。
-	图中每条边的流量都是 $1$。

然后跑最大流二分图匹配。对于每个匹配 $<u_{out}, v_{in}>$，代表我们在原图中把这两个点合并为一条路径走过。那么最大流就是我们最多能合并的数量。一开始我们用 $n$ 条路径走过 $n$ 个点。跑完最大流我们能合并最多点，每合并两个点需要的路径数就少一个，也就使用了最少的路径覆盖所有点。

我们尝试将上述模型应用到此题中。首先，每个人都从 $0$ 号点出发，所以 $0$ 可以作为 $K$ 条路径的起点，因而它可以与 $K$ 个点匹配。所以 $<S,0_{out}>$ 这条边的流量我们要改成 $K$。此外我们要引进费用的概念，每次匹配就代表使用了这条边，也就要消耗这条边的代价。这样图就建完了，跑费用流即可。

事实证明这样建图是对的，但是初次想到或读到会产生很多疑问，下面我对我疑惑比较深的进行解答，希望对大家也有帮助。

1.	**最小路径覆盖问题中，我们可以以任意点为起点，而此题中所有人都必须从 $0$ 号点出发，这时上述建图方法如何能保证将所有点覆盖？**

	这就要与这题的 $dis$ 数组息息相关了。原图是连通图，因此我们求出来的 $dis$ 数组对于 $\forall u, v$，$dis_{u,v}$ 都有意义。也就是说，**$dis$ 数组相当于一个无向完全连通图**。因此我们不论从哪个点出发，都一定能找到一条不重复的路径以经过所有点（每个点与未覆盖的点都有边相连），只是代价不同的问题。
    
    对应到流网络中，如果一个点还没有跟任何其他点匹配，那么根据上述推论，一定能找到一条增广路，让这个点匹配，最终让所有点都能相互匹配变成一条路径，也就是上面那段的一条路径覆盖所有点。这样可能会让最终代价增加，但要注意的是**费用流它首先是最大流**，有增广路一定会流，最小费用最大流只是通过算法让最大流的代价最小罢了。所以在这个流网络上跑费用流首先就会满足覆盖所有点。
    
    
2.	**$K$ 个人不一定全要用到，这个如何保证？**

	从建图目的上看，流网络中将 $<S,0_{out}>$ 这条边的流量我们要改成 $K$，目的是为了在所有点都匹配的基础上通过提供多种匹配选择以使最终费用尽量的少。如果一条路径就能优雅且代价最小地走过所有点，自然没有必要用到剩下的选择了。
    
    从图本身看，虽然源点 $S$ 的总流出量增加了，但是汇点 $T$ 的总流入量仍然是 $n$。因此最大流仍然是 $n$，也就是说源点流不满。那么这既可能是我们使用了多余的 $K-1$ 个选择，让某些点失配，也可能是我们舍弃了多余的选择保持原状。
    
    总的来说，就是给一个可能更优的选择，算法会自己决定用不用。
    
3. **每个点真的只经过一次吗？**

	很多题解都这么说，但是我**不认同**。在我们建的流网络中，的确每个点最多只能有一个入度一个出度（除了 $0$ 号点）。看似只经过一次，但是要注意我们的流网络是建立在 $dis$ 数组这个看做是无向完全连通图的基础上的。而 $dis_{u, v}$ 本来就会包含不大于 $\max(u,v)$ 的点作为最短路的中转点，只不过流网络保证匹配时这个点第一次出现罢了，因而每个点只经过一次是不准确的。
    
    
------------
    
总而言之，这道题之所以如此建图和上面三个问题的合理解释都是因为我们处理出了 $dis$ 数组这个可以看做一个无向完全连通图的东西。虽然解释这些问题看似很麻烦，但我觉得这题的精华在 $dis$ 数组上。


具体地建图方法可以去参考别的题解，代码也很简单，放在[剪切板](https://www.luogu.com.cn/paste/mfua9amh)，谢谢观看！
    
    
    
    
    