# P3174 题解

近乎一年后的纠错：

感谢 @tommy0103 指出了本题解的一个小错误（

原本的代码在根节点时因为没有父亲节点所以原本的代码没法准确得到父亲节点的 cnt。然后现在改过来了。

---


树形 DP

记 $f_u$ 为在 $u$ 子树中，以 $u$ 为毛毛虫的头的最大毛毛虫。这是一个由下向上的树形 $dp$。

那么我们从叶节点看。

首先看叶节点（即最基础的状态）。

![image.png](https://i.loli.net/2020/05/05/uaA6eT8lJjYcbV1.png)

显然答案肯定为 $1$。

然后我们把一个向上推的过程看作毛毛虫增长的过程。最简单的比如只有一个节点，那么它这个毛毛虫与世无争，自己一个人在这里生长即可。

![image.png](https://i.loli.net/2020/05/05/pWq2mC8OGobnYhf.png)

如果不止这一个，那么这些生长的毛毛虫就需要面临残酷的竞争，选出一个儿子继续存活（成为这个子树的以 $u$ 为头的毛毛虫），其他儿子只能沦落成这个毛毛虫的脚。（绿色为原来的小毛毛虫加上父节点，黄色为新的脚。）

![image.png](https://i.loli.net/2020/05/05/sh7B1r4lmZ6SetW.png)

于是我们发现对于非叶节点的点，我们只要找到最大的子毛毛虫即可，然后再加上其他叶节点的个数。

$f_u=\max_{v\in son_u}{f_v+1}+(cnt_u-1)$，其中 $cnt$ 指儿子数量。

其实我们发现，如果我们的转移方程改为 $f_u=\max_{v\in son_u}{f_v+1}+\max(0,cnt_u-1)$，那么就不需要叶节点的特判。

~~但这真的是个很简单的转移方程。~~

但一条最大的毛毛虫可能是趴在一个节点上的，比如：

![image.png](https://i.loli.net/2020/05/05/Y1CyBIEXVljtJ4D.png)

但由于最多是两条链组成这样一个大的毛毛虫。所以我们~~乱搞一番~~计算答案时找出最大和次大，然后更新答案即可。

```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=300009;
vector<int>e[N];
int f[N],ans; 
void dfs(int u,int fa) {
	int mx0=0,mx1=0;
	for(int i=0,v;i<e[u].size();i++)
		if((v=e[u][i])!=fa){
			dfs(v,u);
			f[u]=max(f[u],f[v]);
			if(f[v]>mx0) mx1=mx0,mx0=f[v];
			else if(f[v]>mx1) mx1=f[v];
		}
	int cnt=e[u].size()-(fa!=-1);
	f[u]+=(1+max(0,cnt-1));
	ans=max(ans,mx0+mx1+1+max(0,cnt-1-(fa==-1)));
}
int main() {
	int n,m; scanf("%d%d",&n,&m);
	for(int i=1,u,v;i<=m;i++)
		scanf("%d%d",&u,&v),e[u].push_back(v),e[v].push_back(u);
	dfs(1,-1);
	printf("%d",ans);
	return 0;
}
```

