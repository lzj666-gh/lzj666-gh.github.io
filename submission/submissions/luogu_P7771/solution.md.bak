# P7771 题解

upd 2021.8.26：修改评论区指出的代码的错误，实在抱歉，十分感谢 @[mazymaze](https://www.luogu.com.cn/user/33578) 指出我代码的错误。

upd 2021.12.18：修改评论区两位超级大巨佬 @[Dragon_in_Bed](https://www.luogu.com.cn/user/65289) 和 @[ix35](https://www.luogu.com.cn/user/113546) 指出的我的题解中叙述不严谨的地方，十分感谢他们（我咕了好久啊qwq）。

upd 2023.2.6：再次修改评论区指出的代码的错误，十分感谢 @[Tibrella](https://www.luogu.com.cn/user/655192)。

## [题目传送门](https://www.luogu.com.cn/problem/P7771)

## 前置芝士：

$1$. **欧拉路径定义**：

图中经过所有边**恰好一次**的路径叫**欧拉路径**（也就是一笔画）。如果此路径的**起点**和**终点**相同，则称其为一条**欧拉回路**。

$2.$ **欧拉路径判定（是否存在）**：
- **有向图欧拉路径**：图中**恰好**存在 $1$ 个点出度比入度多 $1$（这个点即为 **起点** $S$），$1$ 个点入度比出度多 $1$（这个点即为 **终点** $T$），其余节点出度=入度。

- **有向图欧拉回路**：**所有点**的入度=出度（起点 $S$ 和终点 $T$ 可以为任意点）。
- **无向图欧拉路径**：图中**恰好**存在 $2$ 个点的度数是**奇数**，其余节点的度数为**偶数**，这两个度数为**奇数**的点即为欧拉路径的 **起点** $S$ 和 **终点** $T$。
- **无向图欧拉回路**：**所有点**的度数都是**偶数**（起点 $S$ 和终点 $T$ 可以为任意点）。

注：存在欧拉回路（即满足存在欧拉回路的条件），也一定存在欧拉路径。

当然，一副图有欧拉路径，还**必须满足**将它的有向边视为无向边后它是**连通**的（不考虑度为 $0$ 的孤立点），连通性的判断我们可以使用```并查集```或 ```dfs``` 等。


$3.$ **寻找欧拉路径（默认存在）**：

- 首先根据题意以及判定先确定起点 $S$。
- 从起点 $S$ 开始 ```dfs``` 。

```dfs``` 伪代码如下：
```cpp
void dfs(int now)
{
	枚举now的出边。
		如果该边还未被访问
			标记为已访问
			dfs(该边连向的另一个点)
	now入栈
}
```

- 最后倒序输出栈内的所有节点即可。
	- 感性理解倒序输出的原因：如果是欧拉回路，那么遍历到哪，输出到哪也是对的，因为不管怎么走都会绕某个环走回起点，所以不到最后不会出栈，然而欧拉路径会出现边都被走过了，走不回起点，最后会停留在终点，遇到这种情况这种路径会最先出栈，于是只要把这个路径先走了，前面就和欧拉回路一样随便走就行，不会出栈，于是倒序输出就是对的。

##  $\texttt{Solution}$：
**题意**：给定 $n$ 个点，$m$ 条边，求这副有向图字典序最小的欧拉路径。

**思路**：

本题需要判断 $+$ 找出**有向图**的欧拉路径。

由于本题保证“将有向边视为无向边后图连通”，所以判定时不用判断连通性。

还有一点要注意的是本题需要按照**字典序**输出。

这一点如何解决呢？

法一：

- 直接使用数组存邻接矩阵，枚举点 $x$ 出边时，直接枚举编号从 $1$ 到 $n$ 的点 $y$，再判断 $x$，$y$ 之间是否有未访问边，这样就解决了字典序的问题。 
- dfs 代码（对应伪代码）:
	```cpp
    void dfs(int now)
    {
        for(int i=1;i<=n;i++)
        {
            if(G[u][i]>0)
            {
                G[u][i]--;
                dfs(i);
            }
        }
        st.push(now);
    }
	```

- 但是这样的做法时间复杂度为 $\mathcal{O}(n^2)$，显然会超时。

法二：

- 既然邻接矩阵不行，那我们就用时间复杂度更优的邻接表，将 $now$ 的所有出边排序即可。链式前向星对于排序出边的操作有些困难（是我太菜了qwq），而 ```vector``` 则容易的多，所以我选用了 ```vector```。
- sort 代码：
	```cpp
    for(int i=1;i<=n;i++) sort(G[i].begin(),G[i].end());
    ```
- dfs 代码：
	```cpp
    void dfs(int now)
    {
    	for(int i=del[now];i<G[i].size();i=del[now])
		{
			del[now]=i+1;
			dfs(G[now][i])
		}
		st.push(now);
     }
     //其中 del[now] 表示 G[now][1,2……,del[now]-1] 都已经被标记访问过，下一次要从G[now][del[now]]开始访问。
    ```
  


- dfs 时间复杂度：$\mathcal{O(n)}$。

- sort 时间复杂度：$\mathcal{O(m\log m)}$。

- 总时间复杂度：$\mathcal{O(n+m\log m)}$。

- 足以 AC 本题。

## $\texttt{AC Code}$：

```cpp
#include <bits/stdc++.h>
using namespace std;
const int MAX=100010;
int n,m,u,v,del[MAX];
int du[MAX][2];//记录入度和出度 
stack <int> st;
vector <int> G[MAX];
void dfs(int now)
{
	for(int i=del[now];i<G[now].size();i=del[now])
	{ 
		del[now]=i+1;
		dfs(G[now][i]);
	}
	st.push(now);
}
int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++) scanf("%d%d",&u,&v),G[u].push_back(v),du[u][1]++,du[v][0]++;  
    for(int i=1;i<=n;i++) sort(G[i].begin(),G[i].end());
    int S=1,cnt[2]={0,0}; //记录
    bool flag=1; //flag=1表示,所有的节点的入度都等于出度,
    for(int i=1;i<=n;i++)
	{
        if(du[i][1]!=du[i][0])
        {
            flag=0;
            if(du[i][1]-du[i][0]==1/*出度比入度多1*/) cnt[1]++,S=i;
            else if(du[i][0]-du[i][1]==1/*入度比出度多1*/) cnt[0]++;
            else return puts("No"),0;
        }
    }
    if((!flag)&&!(cnt[0]==cnt[1]&&cnt[0]==1)) return !puts("No"),0;
	//不满足欧拉回路的判定条件，也不满足欧拉路径的判定条件，直接输出"No" 
    dfs(S);
    while(!st.empty()) printf("%d ",st.top()),st.pop();
    return 0; 
}

```


练习：
- [luogu P1341 无序字母对](https://www.luogu.com.cn/problem/P1341)：判定 $+$ 寻找欧拉路径（可用邻接矩阵）。
- [luogu P2731 骑马修栅栏](https://www.luogu.com.cn/problem/P2731)：寻找欧拉路径（可用邻接矩阵）。
- [luogu P1127 词链](https://www.luogu.com.cn/problem/P1127)：判定 $+$ 寻找欧拉路径。

**最后：** 由于本人能力有限，难免出错，欢迎大家指正。