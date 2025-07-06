# P1265 题解

今天CSP刚报好名，刚好$\color{green}AC$ 这题。听说比赛前写题解可以＋rp，于是就有了这篇题解。

[**原题传送门**](https://www.luogu.com.cn/problem/P1265)

[**博客食用~~不知道会不会~~更佳**](https://www.luogu.com.cn/blog/nizhuan/solution-p1265)

---
## 0.审题
题面前面一大堆有的没的，蛋是

`当所有城市被组合成一个“城市联盟”时，修建工程也就完成了。`

一语道破目的：最小生成树。

~~其实你不分析题面的话也不知道。~~

**最小生成树是什么呢，实际上就是给您一个图，要求把图变成一个由n-1（n为点数）条边组成的图，使得总边权最小。**

~~该不会真的有人不知道最小生成树是什么就来做这题吧，不会吧不会吧（大雾~~
## 1.思路
第一反应Kruskal，于是写完一提交直接爆炸。

### $\color{black}TLE+MLE$

[血的教训](https://www.luogu.com.cn/record/list?user=240191&pid=P1265&page=1)

$\color{black}MLE$：存边数组爆炸

$\color{black}TLE$：$O(mlogm)$爆炸

---
于是Prim大法好啊！！！

**Prim算法流程：**
1. 开始将起点（本题随意）标记为蓝点；
2. 找一条连接**蓝点集合中一点**和白点集合中一点最短的边；
3. 将该边连接的白点加入蓝点；
4. 将该新加入的蓝点所有连接的白点最短边更新；
5. 返回第二步，直到n个点都被选入最小生成树为止。

**注：蓝点为已加入最小生成树的点，白点反之。**
## 2.代码实现
相信大家可以发现，这个算法流程跟`Dijkstra`差不多，于是代码实现也很相似。

因为算法流程已经给出，代码注释将不再赘述。

### code:
```cpp
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;
int n;
typedef double dou;
dou x[5010],y[5010],dis[5010],book[5010],ans;

dou get_e(dou x1,dou y1,dou x2,dou y2)
{//求两点间距离函数
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

void init()//初始化
{
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		scanf("%lf%lf",&x[i],&y[i]);
		dis[i]=1e12*1.0;//double类很大，炸不了
	}
	return ;
}

void Prim()
{
	dis[1]=0.0;
	book[1]=true;
	int curr;
	double minn;
	for(int i=1;i<=n;i++)
	{
		curr=1;
		minn=1e9*1.0;
		for(int j=1;j<=n;j++)//找最短边
			if(!book[j] && dis[j] < minn)
				minn=dis[j],curr=j;
		book[curr]=true;
		ans+=dis[curr];
		for(int j=1;j<=n;j++)//现用现算
			dis[j]=min(dis[j],get_e(x[curr],y[curr],x[j],y[j]));
	}
	printf("%.2lf",ans);
	return ;
}

int main()
{
//	freopen("work.in","r",stdin);freopen("work.out","w",stdout);
	init();
	Prim();
//	fclose(stdin);fclose(stdout);
	return 0;
}
```

## Thank you for your reading!

~~拒绝白嫖，从我做起。点个赞再走嘛。~~