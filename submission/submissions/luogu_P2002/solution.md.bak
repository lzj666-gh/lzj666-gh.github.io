# P2002 题解

题解数目好像不多，那么就来写一篇题解吧，顺便来入门一下下午要学的缩点

这道题目和[[HAOI2006]受欢迎的牛](https://www.luogu.org/problem/P2341)很像，我仅仅只是在那个代码上做了小小的修改就过了

如果想要学习tarjan算法的基本思路的话，大家可以看看[这篇文章](https://blog.csdn.net/qq_34374664/article/details/77488976)，

但是我在代码中也会对tarjan的基本思路稍微讲一讲，可能没那么详细

那我就直接在代码上解释了：
```cpp
#include<bits/stdc++.h>
using namespace std;
int num,head[100010],dfn[100010],low[100010],cnt,vis[100010];
/*
dfn[]:时间戳，表示他在dfs(tarjan)中是第几个被搜到的
low[]:以该节点为根的子树中所有起始于该子树中的子孙节点的边所连到的点中dfn的最小值
vis[]:表示该节点是否入栈 
*/
int sum[100010],bj[100010],tot,qwq[100010];
/*
sum[]:该强联通分量中有多少个数(本题用不上，但受欢迎的牛会用到) 
bj[]:表示该节点处于哪一个强连通分量 
qwq[]:表示该强连通分量是否被其他的强连通分量所连起来 
*/
struct Edge{
	int to,next;
}edge[500010];
inline void add(int from,int to){
	num++;
	edge[num].to=to;
	edge[num].next=head[from];
	head[from]=num;
}
//以上为前向星存边 
stack<int>s;	//建栈(也可手写) 
inline void tarjan(int x){
	cnt++;
	dfn[x]=low[x]=cnt;
	s.push(x);
	vis[x]=1;
	//所有点被遍历到时的初始化 
	for(register int i=head[x];i;i=edge[i].next){
		int y=edge[i].to;
		if(dfn[y]==0){	//如果该节点未被访问过 
			tarjan(y);	//则向下遍历 
			low[x]=min(low[x],low[y]);
			//y为x的子节点,所以可以取x与y中low更小的值 
		}
		else if(vis[y]==1){
			low[x]=min(low[x],dfn[y]);
			//y在栈中因此y一定是x的祖先节点
			//low表示的是起始于该子树中的子孙节点的边所连到的点中dfn的最小值
			//所以我们和y比较的是y的dfn值，而不是low
		}
	}
	if(low[x]==dfn[x]){
//当该点的low等于自己本身说明自己就是以x为根节点的子树能到达的dfn最小的节点(在整棵树中能到达的最上方的点) 
		int z;
		tot++;	//tot表示有几个强连通分量 
		while(s.top()!=x){	//把整个强连通分量出栈 
			sum[tot]++;	
			z=s.top();	//取出栈顶 
			vis[z]=0;	//标志其不在栈中 
			bj[z]=tot;	//标志其在哪一个强连通分量 
			s.pop();	//出栈 
		}
		sum[tot]++;
		z=s.top();
		vis[z]=0;
		bj[z]=tot;
		s.pop();
	}
	return;
}
int main(){
	int n,m;
	scanf("%d%d",&n,&m);
	int x,y;
	for(register int i=1;i<=m;i++){
		scanf("%d%d",&x,&y);
		add(x,y);
	}
	for(register int i=1;i<=n;i++){
		if(dfn[i]==0)
			tarjan(i);
	}
	for(register int i=1;i<=n;i++){		//遍历每一条边 
		for(register int j=head[i];j;j=edge[j].next){
			int y=edge[j].to;	
			if(bj[i]!=bj[y]){
//如果有两个强连通分量之间有边，被连的那个强连通分量就不需要再在强连通分量中扩散消息了
//只需要在那个连它的强连通分量中扩散消息，消息就会扩散到它那里来 
				qwq[bj[y]]=1;//标记此强连通分量不需要扩散消息 
			}
		}
	}
	int ans=0;
	for(register int i=1;i<=tot;i++){
		if(qwq[i]==0){
			ans++;
		}
	}
	printf("%d",ans);
	return 0;
}
```
