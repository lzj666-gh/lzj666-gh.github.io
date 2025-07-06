# P1135 题解

## 题目分析

这是一道最短路问题，可以理解为每次建两条边，$i(1\le i \le n) \to i-K_i(1\le i-K_i),i+K_i(i+K_i\le n)$。

实现的算法比较多，下面会讲几乎所有方法。

## Dijkstra——单源非负权最短路

[模板题](/problem/P4779)，[关于 Dijkstra](https://oi-wiki.org/graph/shortest-path/#dijkstra-%E7%AE%97%E6%B3%95)。

每次建边，边权为一。

以 $A$ 为出发点，跑最短路最后输出 $D(B)$。

时间复杂度 $O(n \log n)$。

## Dijkstra 代码实现

```cpp
#include<bits/stdc++.h>
#define st first
#define nd second
using namespace std;
typedef pair<int,int> Pair;
int n,s,k,dis[100001],w[200001],tar[200001],nxt[200001],head[200001],tot;
bool u[100001];
priority_queue<Pair,vector<Pair>,greater<Pair> >q;
void add(int u,int v,int d){
    w[++tot]=d,tar[tot]=v,nxt[tot]=head[u],head[u]=tot;//邻接表存储
    return;
}
void dijkstra(int s){//Dijkstra
    q.push({0,s});
    dis[s]=0;
    while(!q.empty()){
        Pair p=q.top();
        q.pop();
        if(dis[p.nd]!=p.st)
            continue;
        for(int i=head[p.nd];i;i=nxt[i]){
            if(dis[tar[i]]>dis[p.nd]+w[i]){
                dis[tar[i]]=dis[p.nd]+w[i];
                q.push({dis[tar[i]],tar[i]});
            }
        }
    }
    return;
}
int main(){
    memset(dis,0x3f,sizeof(dis));//初始化无穷
    cin>>n>>s>>k;
    for(int i=1,v;i<=n;i++){
        cin>>v;
        if(i+v<=n)//判断越界
            add(i,i+v,1);
        if(1<=i-v)
            add(i,i-v,1);
    }
    dijkstra(s);
    cout<<(dis[k]==0x3f3f3f3f?-1:dis[k]);//注意-1
    return 0;
}
```

## SPFA——单源~~已逝~~带负权最短路

[模板 SPFA 判断负环](/problem/P3385)，[关于 SPFA](https://oi-wiki.org/graph/shortest-path/#%E9%98%9F%E5%88%97%E4%BC%98%E5%8C%96spfa "接着上文 Bellman-Ford 写的")。

由于本题目边权均为 $1$（非负），可以不考虑判断负环（但是代码里还是有）。

时间复杂度 $O(n)$（仅限本题特殊边权）。

## SPFA 代码实现

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,a,b,dis[6001],f[6001],w[6001],tar[6001],nxt[6001],head[6001],tot;
bool u[6001];
queue<int>q;
void add(int u,int v,int d){
    w[++tot]=d,tar[tot]=v,nxt[tot]=head[u],head[u]=tot;
    return;
}
bool spfa(){
    q.push(a);
    dis[a]=0;
    u[a]=1;
    while(!q.empty()){
        int p=q.front();
        u[p]=0;
        q.pop();
        for(int i=head[p];i;i=nxt[i]){
            if(dis[tar[i]]>dis[p]+w[i]){
                dis[tar[i]]=dis[p]+w[i];
                if(!u[tar[i]]){
                    u[tar[i]]=1;
                    q.push(tar[i]);
                    if((++f[tar[i]])>=n)
                        return 1;//有负环（本题里不会出现）
                }
            }
        }
    }
    return 0;//无负环（本题里无需判断）
}
signed main(){
    memset(dis,0x3f,sizeof(dis));
    cin>>n>>a>>b;
    for(int i=1,v;i<=n;i++){
        cin>>v;//建图
        if(1<=i-v)
            add(i,i-v,1);
        if(i+v<=n)
            add(i,i+v,1);
    }
    spfa();//SPFA
    cout<<(dis[b]==0x3f3f3f3f?-1:dis[b]);//注意 -1
    return 0;
}
```

## DFS——深度优先搜索

从 $A$ 开始，搜索每一条路，可以更新答案再继续搜索，不然会搜索多余导致 TLE。

时间复杂度 $O(n^2)$。

## DFS 代码实现

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,a,b,k[201],dis[201];
void dfs(int node,int step){
	dis[node]=step;//一定可以更新
	int v=node-k[node];
	if(1<=v&&step+1<dis[v]/*可以更新在搜索*/)//下
		dfs(v,step+1);
	v=node+k[node];
	if(v<=n&&step+1<dis[v])//上
		dfs(v,step+1);
	return;
}
int main(){
	memset(dis,0x3f,sizeof(dis));
	cin>>n>>a>>b;
	for(int i=1;i<=n;i++)
		cin>>k[i];
	dfs(a,0);
	cout<<(dis[b]==0x3f3f3f3f?-1:dis[b]);
	return 0;
}
```

## Floyd——全源最短路

[模板题](/problem/B3647)，[关于 Floyd](https://oi-wiki.org/graph/shortest-path/#floyd-%E7%AE%97%E6%B3%95)。

本体数据范围很小，可以小题大做，求全源最短路。

时间复杂度 $O(n^3)$。

## Floyd 代码实现

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,a,b,f[201][201];
signed main(){
    memset(f,0x3f,sizeof(f));
    cin>>n>>a>>b;
    for(int i=1;i<=n;i++)
        f[i][i]=0;//自己
    for(int i=1,v;i<=n;i++){
        cin>>v;
        if(1<=i-v)//建边
            f[i][i-v]=min(f[i][i-v],1);
        if(i+v<=n)
            f[i][i+v]=min(f[i][i+v],1);
    }
    for(int k=1;k<=n;k++)
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                f[i][j]=min(f[i][j],f[i][k]+f[k][j]);//DP 求 Floyd
    cout<<(f[a][b]==0x3f3f3f3f?-1:f[a][b]);
    return 0;
}
```

## BFS——广度优先搜索

用一个队列，维护节点和步数。

开始入队 $(A,0)$，然后把上、下入队（合法的话），直到第一次出现 $B$，其实就是不记录 $dis$ 还不排序的 Dijkstra，记得打标记。

正确性：由于边权全部相等（都是 $1$），不需要用堆来进行排序（Dijkstra），直接用队列即可。

时间复杂度 $O(n)$，代码几乎同 SPFA（仅实现不同），是 Dijkstra 去掉堆优化（$\log n$）的复杂度。

## BFS 代码实现

```cpp
#include<bits/stdc++.h>
int n,a,b,k[201];
bool f,u[201];//u 是标记
int ri(){
	int x=0;
	char c=getchar(),f=1;
	while(c<'0'||c>'9'){
		if(c=='-')
			f=-f;
		c=getchar();
	}
	while(c<='9'&&c>='0')
		x=(x<<1)+(x<<3)+(c^48),c=getchar();
	return x*f;
}
struct node{
	int x,y;
};
std::queue<node>q;
int bfs(){
	q.push(node{a,0});//入队
	u[a]=1;
	while(!q.empty()){
		int x=q.front().x,y=q.front().y;
		q.pop();
		if(x==b)
			return y;//到了 B
		int xn=x+k[x],yn=y+1;
		if(xn<=n&&xn>0&&!u[xn])//上
			q.push(node{xn,yn}),u[xn]=1;
		xn-=2*k[x];
		if(xn<=n&&xn>0&&!u[xn])//下
			q.push(node{xn,yn}),u[xn]=1;
	}
	return-1;
}
int main(){
	n=ri(),a=ri(),b=ri();
	for(int i=1;i<=n;i++)
		k[i]=ri();
	printf("%d",bfs());
	return 0;
}
```

## Bellman-Ford——单源~~不如已逝算法~~带负权最短路

[模板 Bellman-Ford 判断负环](/problem/P3385 "由于是 SPFA 的原版，模板题相同")，[关于 Bellman-Ford](https://oi-wiki.org/graph/shortest-path/#bellmanford-%E7%AE%97%E6%B3%95)。

## Bellman-Ford 代码实现

```cpp
#include<bits/stdc++.h>
#define st first
#define nd second
using namespace std;
typedef pair<int,int> Pair;
int n,s,k,dis[100001],w[200001],tar[200001],nxt[200001],head[200001],tot;
bool u[100001];
void add(int u,int v,int d){
    w[++tot]=d,tar[tot]=v,nxt[tot]=head[u],head[u]=tot;
    return;
}
bool bellmanford(int s){//Bellman-Ford
    bool f=0;
    memset(dis,0x3f,sizeof(dis));
    dis[s]=0;
    for(int i=1;i<=n;i++,f=0){
        for(int u=1;u<=n;u++){
            if(dis[u]==0x3f3f3f3f)//不能松弛没有算出的点
                continue;
            for(int i=head[u],v,w;i;i=nxt[i]){
                v=tar[i],w=::w[i];
                if(dis[v]>dis[u]+w)
                    dis[v]=dis[u]+w,f=1;
            }
        }
        if(!f)//有负环（在本题中不可能出现）
            return 0;
    }
    return 1;
}
int main(){
    memset(dis,0x3f,sizeof(dis));
    cin>>n>>s>>k;
    for(int i=1,u,v,w;i<=n;i++){//建图
        cin>>v;
        if(i+v<=n)
            add(i,i+v,1);
        if(1<=i-v)
            add(i,i-v,1);
    }
    bellmanford(s);
    cout<<(dis[k]==0x3f3f3f3f?-1:dis[k]);
    return 0;
}
```

