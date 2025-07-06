# P6121 题解

## P6121
~~CSP前发篇题解增加一些RP~~

看到这道题，第一眼，~~思路就是跑 n 遍并查集~~，瞅了一眼数据（1≤N,M≤2×$10^5$），if I do that，I will T 的 ~~起飞~~

我觉得这道题的“[弱化版](https://www.luogu.com.cn/problem/P3144)”还是可以过得

~~虽然我没这么写~~

输入的最后n行表示农场关的顺序，那我们倒过来看（从后往前）是不是可以看成农场开的顺序（2-1-4-3）

```
T0:全开着（1 2 3 4） 
T1:关了3 （1 2 4）
T2:关了4 （1 2）
T3:关了1 （2）
T4:关了2 （-）
```
看作
```
T4:全关着（-） 
T3:开了2 （2）
T2:开了1 （1 2）
T1:开了4 （1 2 4）
T0:开了3 （1 2 3 4）
```
### 1.整体思路
也就是说我们可以从$T_{n-1}$搜索到${T_0}$时刻，每次判断加上一个点，还是否与其他点联通。
### 2.理论支持
把 $k$ 个点和并成一个联通图，  
一次合并两个点（即在两个点间加一条边），  
不重复操作（两个点已经联通的就不加了），  
我们只需要操作 $k-1$ 次（加 $k-1$ 条边）即可，  
如果说我们操作不够 $k-1$ 次（边数小于 $k-1$），  
那么这张图一定不连通。

我们需要依靠并查集来实现，  
那用并查集来解释就是所有的点是否在同一个集合，  
如果在，则联通； 反之，则不连通。
### 3.具体实现
我们用一个数组 $ f $ 来存他的祖先节点，  
开始初始化成每个点自己在一个集合，  
如果他们不在一个集合的话，并且有一条边连接他们两个，就把他，们合并起来，操作数 $+1$.  
如果当前有 $k$ 个农场是开着的，记录合并的次数，如果次数等于 $k-1$ 则```YES```;反之，则```NO```.

#### 初始化
```cpp
inline void init(){
    for(register int i=1;i<=n;i++)
        f[i]=i;
}
```
#### 链式前向星存边
```cpp
int tot,head[200010];
inline void add_edge(int from,int to){
    e[++tot].from=from;
    e[tot].to=to;
    e[tot].next=head[from];
    head[from]=tot;
…… …… ……
scanf("%d%d",&u,&v);
        add_edge(u,v);
        add_edge(v,u);
}
```
#### 并查集（路径压缩+合并）
```cpp
inline int _find(int x){
    while(x!=f[x]) x=f[x]=f[f[x]];
    return x;
…… …… ……
int fx=_find(t[i]),fy=_find(e[j].to);
if(fx!=fy)
{
	++k; //合并次数+1
	f[fx]=fy;
}
```

## 完整代码附上~

```cpp
#include<iostream>
#include<cstdio>
using namespace std;
struct _edge{
    int from;
    int to;
    int next;
}e[400010];
int tot,head[200010],k;
bool vis[200010];                        //判断农场是否开着 
inline void add_edge(int from,int to){   //链式前向星存图
    e[++tot].from=from;
    e[tot].to=to;
    e[tot].next=head[from];
    head[from]=tot;
}
int n,m,u,v,t[200010],ans[200010],f[200010];
inline int _find(int x){            //查询+路径压缩
    while(x!=f[x]) x=f[x]=f[f[x]];
    return x;
}
inline void init(){                 //并查集初始化
    for(register int i=1;i<=n;i++)
        f[i]=i;
}
int main()
{
    scanf("%d%d",&n,&m);
    for(register int i=1;i<=m;i++)
    {
        scanf("%d%d",&u,&v);
        add_edge(u,v);              //无向图双向存边
        add_edge(v,u);
    }
    for(register int i=1;i<=n;i++)
        scanf("%d",&t[i]);          //农场关的时间，反着看就是开的时间
    init();                         //定义了函数……记得用
    vis[t[n]]=1;                    //t_n时开了农场 t[n]，标记
    ans[n]=1;                       //只开了一个时图必定是联通的
    for(register int i=n-1;i>=1;i--) //反着搜，第i 时刻开了农场t[i]
    {
        vis[t[i]]=1;                //标记
        for(register int j=head[t[i]];j;j=e[j].next)
        {
            if(vis[e[j].to]==1)      //如果该边终点农场也开了，执行如下语句
            {
                int fx=_find(t[i]),fy=_find(e[j].to);//并查集查询
                if(fx!=fy)     //不在同一个集合的话
                {
                    ++k;       //合并次数 +1 
                    f[fx]=fy;  //合并两个集合
                }
            }
        }
        if(k==n-i) ans[i]=1;   //当前开了n-（i-1）个农场，判断是否连通，储存答案
        else ans[i]=0;
    }
    for(register int i=1;i<=n;i++)
    {
        if(ans[i]==1) printf("YES\n");  //打印答案
        else printf("NO\n");
    }
    return 0;
}

```
**若有地方没看懂可以私信我**  
**若写的不好还请大家的体谅**  
**若有错的地方还望大家指出**  
**谢谢各位的支持~**
**最后，Meteorshower_Y在这里祝福大家RP++，Score++**