# P10997 题解

# D. Partition 官方题解

本题考察的主要知识点：

- 【4】动态规划的基本思路

### 读题

对于这题，读明白题是成功的一半。

结合给出的图形，我们不难发现，这个图的“红橙/黄绿分割线”和“红黄/橙绿分割线”分别单调。换言之，简单的染色方案应当满足：

1. 红色或橙色的格子的右边和上方都是红色或橙色。
2. 红色或黄色的格子的左边和上方都是红色或黄色。

---

上面两个条件的必要性是显然的，下面证明上面命题是题目要求的充分条件。

使用反证法不难证明如下两个结论：

3. 黄色或绿色的格子的左边和下方都是黄色或绿色。
4. 橙色或绿色的格子的右边和下方都是橙色或绿色。

接下来，使用结论 1,2 可推出题目要求的第 1 条，结论 1,4 可推出题目要求的第 2 条，结论 2,3 可推出题目要求的第 3 条，结论 3,4 可推出题目要求的第 4 条。

---

因此大概思路也就有了——红橙/黄绿分割线是从左上角，每次向右或向下走一步，走到右下角得到的路径，红黄/橙绿分割线是从右上角开始，每次向左或向下走一步，走到左下角得到的路径。我们 DP 这两条路径即可得到答案。

### 55 分做法

从上往下 DP。本题解中，我们规定网格交叉点 $(i,j)$ 表示的是格子 $(i,j)$ **左上角**的那个交叉点，特别地，最右侧的一排交叉点用 $(x,m+1)$ 表示，最下面一排用 $(n+1,y)$ 表示。

设 $f(i,l,r)$ 表示当前在第 $i$ 行，红橙/黄绿分割线在第 $l$ 列，红黄/橙绿分割线在第 $r$ 列的最大总和。同时设 $s_{i,x}$ 表示 $a_{i,1}+a_{i,2}+\ldots + a_{i,x}$，那么有转移方程：

- 当 $l\le r$ 时，分割线从左到右把网格分成黄、红、橙三块。$f(i,l,r)=\max(f(i,l-1,r), f(i,l,r+1), f(i-1,l,r)+2s_{i,m}-s_{i,r-1}+2s_{i,l-1})$。

- 当 $l>r$ 时，分割线从左到右把网格分成黄、绿、橙三块。

  $f(i,l,r)=\max(f(i,l-1,r), f(i,l,r+1), f(i-1,l,r)+2s_{i,m}+2s_{i,l-1}-s_{i,r-1})$。

### 100 分做法

我们把“红色、橙色、黄色、绿色的权值分别为 $1,2,3,4$”拆分成三步：

- 所有格子自动获得 $1$ 权值。
- 橙色、绿色格子增加 $1$ 权值。
- 黄色、绿色格子增加 $2$ 权值。

红黄/橙绿分界线和红橙/黄绿分界线是分别独立的。

使用 $s_{i,j}$ 表示 $(i,j)$ 以及其下方格子数字和。我们可以分别用一个二维 DP 来求出两个部分贡献的增加量最大值。时间复杂度 $O(nm)$，可以通过。

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,m;
long long s[2005][2005],f[2005][2005],g[2005][2005];
int main(){
	scanf("%d%d",&n,&m);
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			scanf("%lld",&s[i][j]);
	for(int i=n;i;i--)
		for(int j=1;j<=m;j++)
			s[i][j]+=s[i+1][j];
	long long S=0;
	for(int j=1;j<=m;j++)
		S+=s[1][j];
	memset(f,-0x3f,sizeof f);
	memset(g,-0x3f,sizeof g);
	f[0][1]=g[0][m+1]=0;
	for(int i=1;i<=n+1;i++){
		for(int j=1;j<=m+1;j++)
			f[i][j]=max(f[i-1][j],f[i][j-1]+s[i][j-1]);
		for(int j=m+1;j;j--)
			g[i][j]=max(g[i-1][j],g[i][j+1]+s[i][j]);
	}
	cout<<S+2*f[n+1][m+1]+g[n+1][1];
	return 0;
}
```