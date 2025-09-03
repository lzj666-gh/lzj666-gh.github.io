# P4556 题解

线段树合并板子题

 _对了，楼下的题解是假的可以被hack掉_ 
_____________

这里简单介绍一下线段树合并这种神奇的操作了

## 前置芝士：线段树合并

所谓线段树合并就是将两个线段树合并成一颗线段树的算法

下面的合并暂时可以理解成我们使用线段树维护了两个数组的一些信息(比如区间和，区间最大值之类的)，现在我们需要将这两个数组按位相加，同时得到这个数组所对应的线段树

问题来了线段树明明是好好的线段树我们为什么要合并它呢?

显然两个普通的线段树(也就是那种左儿子是p<<1右儿子是p<<1|1的线段树)没有必要专门设计一个算法合并它们，因为他们已经满了，换句话说我们直接把两个数组按位相加然后重新建一遍线段树可能是最快的方法了

但是线段树众所周知有很多的变体，比如说动态开点线段树，这种线段树很有可能不是满的，甚至只有一条链$O(logn)$个节点，这时候我们合并两个动态开点线段树的时候接着用刚才的方法合并可能就有些不妙了

那么当然这里有一个几乎对于所有数据结构都适用的合并算法叫做启发式合并，当我们合并两个动态开点线段树的时候我们就暴力的把小的线段树中的元素插入到大的线段树里面去。

不过我们会觉得其实这个算法也是有点暴力的，通过这种算法把n个仅有一个元素的动态开点线段树合并成一颗完整的大线段树的复杂度是O(nlog^2n)的

那这里就是线段树合并这个算法出场的时候了，这个算法合并两个动态开点线段树的复杂度是O(两个线段树重叠部分)的

那么我们是如何实现两个线段树合并起来的操作呢？

假设我们现在要把线段树2所对应的数组加到线段树1上

那么我们在两个线段树上同时进行dfs，然后我们dfs的时候判断一下左儿子是否同时有两个节点，如果同时有的话就进去dfs，否则我们看一下是线段树1没有左儿子还是线段树2没有左儿子，如果是线段树2没有左儿子的话我们什么事也不用干，因为线段树2对应的这部分区间全是0加了也白加。

然后如果是线段树1没有左儿子的话，我们发现此时的相加操作相当于把这一段区间全部换成线段树2所对应的区间，因此我们直接让线段树1的左儿子等于线段树2的左儿子就可以了(这一部分有点像主席树的工作方式，因为这样合并之后线段树1和线段树2将会共用一些节点)

当然对于右儿子也要采取同样的处理方式了

最后一个问题是这两个节点都是叶子，既没有左儿子也没有右儿子，那么我们直接将节点2加到节点1上然后返回就可以了

最后就是因为线段树1上左右儿子的信息会发生改变，我们需要对这个节点进行一次$update/pushup/merge$操作(不同人起不一样的函数名，但是干的应该都是同一件事情)

于是我们就成功完成了将两个线段树合并的操作辣~

那么我们可以证明的是，通过这种方法将n个只有1个元素的线段树合并成1个有n个元素的线段树的复杂度就是O(nlogn)的

为什么呢？

考虑我们刚才的算法流程，我们每次dfs一个节点，显然我们可以dfs到这个节点就证明这两个位置都有节点,我们发现合并之后属于线段树2的节点就不会被dfs到了(因为线段树1的节点替换了它的位置)，可能被dfs到的属于线段树2的节点是被接到线段树1的那一部分，但是那部分节点根本就没被dfs到，所以每个节点至多被dfs一次，所以总的复杂度就是O(nlogn)了

_____________________

## 本题题解

对于这道题来讲，我们有一个显然的暴力是利用树上差分的思想，把$u,v$上发放一个数字改成u到1发放一个数字，v到1发放一个数字，u,v的lca到1撤回一个数字
，u,v的lca的father到1撤回一个数字这4个操作

接下来我们每个节点上开一个cnt数组$cnt_{i}$表示i这个数字出现了多少次，那么节点i上出现最多的数字就是cnt数组的最大值(这不是废话嘛)

那么我们求i节点的cnt数组可以暴力的把它的所有孩子的cnt数组按位相加起来来进行求解，然后如果这个节点上有插入或者删除数字的操作我们再对cnt数组进行几次操作就行了~

不过这样太慢了……发现这个东西慢主要是数组按位相加这个操作，所以我们可以用线段树合并来实现数组按位相加这个操作

具体来讲，每个点开一颗权值线段树表示这个点上有什么数字，每个数字出现了几次，然后求点i的权值线段树就是将它所有孩子的线段树合并到一起然后再对合并出来的线段树进行一些在这个节点的插入和删除操作

那么我们的线段树需要维护的信息就是区间的最大值，我们最后查找i点最大的数字的时候就在点i的权值线段树上查一下$1-10^5$这个区间的最大值就行了

然后，这题131mb，虽然空间复杂度$O(nlogn)$但是略微算算空间还是可以卡过去的……

上代码~

```C
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;const int N=1e5+10;typedef long long ll;
int n;int m;int v[2*N];int x[2*N];int ct;int al[N];int fa[N][22];int dep[N];int ans[N];
struct data//存最大值的结构体 
{
    int u;int cnt;
    friend bool operator <(data a,data b){return (a.cnt==b.cnt)?a.u>b.u:a.cnt<b.cnt;}
    friend data operator +(data a,data b){return (data){a.u,a.cnt+b.cnt};}
};vector <data> ve[N];
inline void add(int u,int V){v[++ct]=V;x[ct]=al[u];al[u]=ct;}
struct linetree//动态开点线段树合并 
{
    int s[40*N][2];data v[40*N];int ct;
    inline void ih(){ct=n;}
    inline void ins(int p,int l,int r,data va)//插入 
    {
        if(r-l==1){v[p]=va+v[p];return;}int mid=(l+r)/2;
        if(va.u<=mid)ins(s[p][0]=s[p][0]?s[p][0]:++ct,l,mid,va);
        else ins(s[p][1]=s[p][1]?s[p][1]:++ct,mid,r,va);v[p]=max(v[s[p][0]],v[s[p][1]]);
    }
    inline void mg(int p1,int p2,int l,int r)//合并 
    {
        if(r-l==1){v[p1]=v[p1]+v[p2];return;}int mid=(l+r)/2;//分情况讨论下 
        if(s[p1][0]&&s[p2][0])mg(s[p1][0],s[p2][0],l,mid);else if(s[p2][0])s[p1][0]=s[p2][0];
        if(s[p1][1]&&s[p2][1])mg(s[p1][1],s[p2][1],mid,r);else if(s[p2][1])s[p1][1]=s[p2][1];
        v[p1]=max(v[s[p1][0]],v[s[p1][1]]);
    }
}lt;
inline void dfs1(int u)//处理lca 
{
    for(int i=0;fa[u][i];i++)fa[u][i+1]=fa[fa[u][i]][i];dep[u]=dep[fa[u][0]]+1;
    for(int i=al[u];i;i=x[i])if(v[i]!=fa[u][0])fa[v[i]][0]=u,dfs1(v[i]);
}
inline int lca(int u,int v)//求lca 
{
    if(dep[u]<dep[v])swap(u,v);for(int d=dep[u]-dep[v],i=0;d;d>>=1,i++)if(d&1)u=fa[u][i];
    if(u==v)return u;for(int i=18;i>=0;i--)if(fa[u][i]!=fa[v][i])u=fa[u][i],v=fa[v][i];
    return fa[u][0];
}
inline void dfs2(int u)//线段树合并 
{
    for(int i=al[u];i;i=x[i])if(v[i]!=fa[u][0])dfs2(v[i]),lt.mg(u,v[i],0,1e5);
    vector <data> :: iterator it;
    for(it=ve[u].begin();it!=ve[u].end();++it){lt.ins(u,0,1e5,*it);}
    ans[u]=lt.v[u].u;
}
int main()
{
    scanf("%d%d",&n,&m);lt.ih();
    for(int i=1,u,v;i<n;i++){scanf("%d%d",&u,&v);add(u,v),add(v,u);}dfs1(1);
    for(int i=1,u,v,va;i<=m;i++)//拆成4个操作 
    {
        scanf("%d%d%d",&u,&v,&va);int lc=lca(u,v);
        ve[u].push_back((data){va,1});ve[v].push_back((data){va,1});
        ve[lc].push_back((data){va,-1});ve[fa[lc][0]].push_back((data){va,-1});
    }dfs2(1);for(int i=1;i<=n;i++)printf("%d\n",ans[i]);return 0;//拜拜程序~ 
}

```







