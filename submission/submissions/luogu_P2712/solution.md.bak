# P2712 题解

# P2712
[传送门](https://www.luogu.com.cn/problem/P2712)

## 题目分析
一个摄像头只有在没有其它摄像头照到它的时候才可以被砸，这就是一个[拓扑排序](https://baike.so.com/doc/6172557-6385797.html)的过程。

## 实现思路

1. 存一个有向图（森林），我使用的是领接表存图。并记录每个节点的入度。
1. 扫描所有节点，将入度为0的节点放入队列中。
1. 取出队首并将计数器+1（计数器记录可以砸掉的摄像头数量），扫描队首的所有出边。如果出边指向的是一个摄像头，那么将这个摄像头的入度减一（队首被砸了，那么监视到这个摄像头的摄像头就少了一个）。判断该摄像头入度是否为0，如果为0，则将该摄像头加入队列。
1. 重复过程3，直到队列为空。
1. 如果计数器==n，输出“YES”，否则输出(n - 计数器）。

## 易错点
- 摄像头照到的地方不一定有摄像头，应该用一个数组记录一个位置是否有摄像头。
- 数组开大一点！（我因为这个WA了10次）

## 代码

内带实现思路中各个功能的注释。

```cpp
#include<bits/stdc++.h>
#define INF 0x3f3f3f3f
using namespace std;
int to[200002],ne[200002],head[10002],edge[10002],a[10002];
int n,tot,ans;
bool v[50002];
queue< int > q;
void add(int x,int y){
	to[++tot]=y,ne[tot]=head[x],head[x]=tot,edge[y]++;//edge存入度数量 
}
void read(int &x) {//快读 
    int f = 1; x = 0;
    char ch = getchar();
    while (ch < '0' || ch > '9')   {if (ch == '-') f = -1; ch = getchar();}
    while (ch >= '0' && ch <= '9') {x = x * 10 + ch - '0'; ch = getchar();}
    x *= f;
}
int main()
{
    read(n);
    for(int i=1;i<=n;i++){
    	int m,y;
    	read(a[i]),read(m);
    	v[a[i]]=1;//记录a[i]处有摄像头 
    	for(int j=1;j<=m;j++){
    		read(y);
    		add(a[i],y);//建有向森林 
		}
	}
	for(int i=1;i<=n;i++){
		if(!edge[a[i]]) q.push(a[i]);//过程2，加入入度为0节点 
	}
	while(!q.empty()){
		ans++;//计数器 
		int x=q.front();q.pop();//取出队首 
		for(int i=head[x];i;i=ne[i]){
			int y=to[i];
			edge[y]--;//入度减一 
			if(!edge[y]&&v[y]) q.push(y);//如果这个地方有摄像头且入度为0 
		}
	}
	if(ans==n) printf("YES\n");
	else printf("%d\n",n-ans);
	return 0;
}
	
```

~~**写题解不易，点个赞呗**~~
