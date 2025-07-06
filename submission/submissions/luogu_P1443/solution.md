# P1443 题解

# STL大法好！！

## 取百家所长成一家之言！！

介绍一下用STL模板库 <queue>来广搜这道题
  
广搜什么的自然不同我介绍；
我来介绍一下非常好用但没人用的 
### pair

```
queue<pair<int,int> > q;
```

它可以将两种数据类型的值组合成一个值存入  
队列中大体是这样操作：

```
queue<pair<int,int> > q;//定义

q.push(make_pair(x,y));//入队
//取队首
xx=q.front().first;//第一个值
yy=q.front().second;//第二个值

q.pop();//出队
```
个人认为带头文件的33行代码还是很短的(>_<

上代码：
```
#include<iostream>//P1443
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
#include<cmath>
using namespace std;
const int dx[8]={-1,-2,-2,-1,1,2,2,1};
const int dy[8]={2,1,-1,-2,2,1,-1,-2};//8个方向
queue<pair<int,int> > q;
int f[500][500];//存步数
bool vis[500][500];//走没走过
int main()
{
	int n,m,x,y;
	memset(f,-1,sizeof(f));memset(vis,false,sizeof(vis));
	cin>>n>>m>>x>>y;
	f[x][y]=0;vis[x][y]=true;q.push(make_pair(x,y));
	while(!q.empty())
	{
		int xx=q.front().first,yy=q.front().second;q.pop();//取队首并出队
		for(int i=0;i<8;i++)
		{
			int u=xx+dx[i],v=yy+dy[i];
			if(u<1||u>n||v<1||v>m||vis[u][v])continue;//出界或走过就不走
		    vis[u][v]=true;q.push(make_pair(u,v));f[u][v]=f[xx][yy]+1;
		}
	}
	for(int i=1;i<=n;i++)
	 {for(int j=1;j<=m;j++)printf("%-5d",f[i][j]);printf("\n");}//注意场宽！！
	return 0;
}
```

顺手留赞，感谢φ(>ω<*) 