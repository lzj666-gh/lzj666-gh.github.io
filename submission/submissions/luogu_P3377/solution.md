# P3377 题解

左偏树是 **一种** 支持在 $O(\log_2 n)$ 的时间复杂度内进行合并的 **堆式** 数据结构。

### 一些定义

**外结点** ：左儿子或右儿子是空结点的结点。

**距离** ： 一个结点 $x$ 的距离 $dist_x$ 定义为其子树中与结点 $x$ 最近的外结点到 $x$ 的距离。特别地，定义空结点的距离为 $-1$ 。

### 左偏树的基本性质

左偏树具有 **堆性质** ，即若其满足小根堆的性质，则对于每个结点 $x$ ，有 $v_x\le v_{lc},v_x\le v_{rc}$ 。

左偏树具有 **左偏性质** ，即对于每个结点 $x$ ,有 $dist_{lc}\ge dist_{rc}$ 。

### 基本结论

1. 结点 $x$ 的距离 $dist_x=dist_{rc}+1$ 。

2. 距离为 $n$ 的左偏树至少有 $2^{n+1}-1$ 个结点。此时该左偏树的形态是一棵满二叉树。

3. 有 $n$ 的结点的左偏树的根节点的距离是 $O(\log_2 n)$ 的。

### 基本操作：合并操作

左偏树最基本的操作是合并操作。

定义 `merge(x,y)` 为合并两棵分别以 $x,y$ 为根节点的左偏树，其返回值为合并之后的根节点。

首先不考虑左偏性质，我们描述一下合并两个具有堆性质的树的过程。假设我们要合并的是小根堆。

1. 若 $v_x\le v_y$ ，以 $x$ 作为合并后的根节点；否则以 $y$ 作为合并后的根节点。为避免讨论，若有 $v_x>v_y$ ，交换 $x,y$ 。

2. 将 $y$ 与 $x$ 的其中一个儿子合并，用合并后的根节点代替与 $y$ 合并的儿子的位置，并返回 $x$ 。

3. 重复以上操作，如果 $x$ 和 $y$ 中有一个为空节点，返回 $x+y$ 。

令 $h$ 为树高， $h_x+h_y$ 每次都减少了 $1$  ，上述过程的时间复杂度是 $O(h)$ 的，当合并的树退化为一条链时，这样做的复杂度是 $O(n)$ 的。要使时间复杂度更优，就要使树合并得更 **平衡** 。我们有两种方式：

1. 每次随机选择 $x$ 的左右儿子进行合并。（有没有感觉这很像 FHQ Treap ？）

2. 左偏树。

由于左偏树中左儿子的距离大于右儿子的距离，我们 **每次将 $y$ 与 $x$ 的右儿子合并** 。由于左偏树的树高是 $O(\log_2 n)$ 的，所以单次合并的时间复杂度也是 $O(\log_2 n)$ 的。

但是，两棵左偏树按照上述方法合并后，可能不再保持左偏树的左偏性质。在每次合并完之后，判断对结点 $x$ 是否有 $dist_{lc}\ge dist_{rc}$ ，若没有则交换 $lc,rc$ ，并维护 $x$ 的距离 $dist_x=dist_{rc}+1$ ，即可维护左偏树的左偏性质。

由于合并后的树既满足堆性质又满足左偏性质，所以合并后的树仍然是左偏树。

```cpp
int merge(int x,int y)
{
    if(!x||!y)return x+y;
    if(v[y]<v[x])swap(x,y);
    rc[x]=merge(rc[x],y);
    if(dist[lc[x]]<dist[rc[x]])swap(lc[x],rc[x]);
    dist[x]=dist[rc[x]]+1;
    return x;
}
```

### 左偏树的其他基本操作

#### 插入给定值

新建一个值等于插入值的结点，将该节点与左偏树合并即可。时间复杂度 $O(\log_2 n)$ 。

#### 求最小值

由于左偏树的堆性质，左偏树上的最小值为其根节点的值。

#### 删除最小值

等价于删除左偏树的根节点。合并根节点的左右儿子即可。记得维护已删除结点的信息。

#### 给定一个结点，求其所在左偏树的根节点

我们可以记录每个结点的父亲结点 $fa_i$ ，然后暴力跳父亲结点。

```cpp
int findrt(int x)
{
    if(fa[x])return findrt(fa[x]);
    return x;
}
```

注意，虽然左偏树的距离是 $O(\log_2 n)$ 的，但是左偏树的深度最大可以是 $O(n)$ 的，这种做法的复杂度也是 $O(n)$ 的。

上面的代码让你想到了什么？并查集。我们同样可以用 **路径压缩** 的方式，求一个结点所在左偏树的根节点。

```cpp
int find(int x){return rt[x]==x?x:rt[x]=find(rt[x]);}
```

使用这种写法，需要维护 `rt[x]` 的值。

在合并两个结点 $x,y$ 时，令 `rt[x]=rt[y]=merge(x,y)` 。

在删除左偏树中的最小值时，令 `rt[lc[x]]=rt[rc[x]]=rt[x]=merge(lc[x],rc[x])` ，因为 $x$ 是之前左偏树的根节点，在路径压缩时可能有 `rt` 的值等于 $x$ ，所以 `rt[x]` 也要指向删除后的根节点。

由于 $x$ 已经被作为中间量使用得不成样子，如果之后还要用到结点 $x$ ，需要新建一个值相同的结点。

路径压缩后，可以在 $O(\log_2 n)$ 的优秀时间复杂度内找到一个点所在左偏树的根节点。

### 代码展示

```cpp
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int maxn=100010;
int n,m,op,x,y;
int lc[maxn],rc[maxn],dist[maxn],rt[maxn];
bool tf[maxn];
struct node
{
    int id,v;
    bool operator<(node x)const{return v==x.v?id<x.id:v<x.v;}
}v[maxn];
int find(int x){return rt[x]==x?x:rt[x]=find(rt[x]);}
int merge(int x,int y)
{
    if(!x||!y)return x+y;
    if(v[y]<v[x])swap(x,y);
    rc[x]=merge(rc[x],y);
    if(dist[lc[x]]<dist[rc[x]])swap(lc[x],rc[x]);
    dist[x]=dist[rc[x]]+1;
    return x;
}
int main()
{
    dist[0]=-1;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)scanf("%d",&v[i].v),rt[i]=i,v[i].id=i;
    while(m--)
    {
        scanf("%d%d",&op,&x);
        if(op==1)
        {
            scanf("%d",&y);
            if(tf[x]||tf[y])continue;
            x=find(x);y=find(y);
            if(x!=y)rt[x]=rt[y]=merge(x,y);
        }
        if(op==2)
        {
            if(tf[x]){printf("-1\n");continue;}
            x=find(x);
            printf("%d\n",v[x].v);
            tf[x]=true;
            rt[lc[x]]=rt[rc[x]]=rt[x]=merge(lc[x],rc[x]);
            lc[x]=rc[x]=dist[x]=0;
        }
    }
    return 0;
} 
```