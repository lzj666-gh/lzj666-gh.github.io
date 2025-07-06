# P3833 题解

前置题目：P3384

这道题目是一个模板题（省选考模板？）

作为一个 STL 的忠实拥护者，怎么能只有数组写链式前向星的题解呢？

这道题的数据还是比较水的，因此有两种做法。

第一种做法：倍增跳 LCA，然后用树状数组或者线段树维护一下子树和链就可以了

时间复杂度 $O(n \log n)$，常数较大

（其实数据出好一点这个就真的不行了，不信用这种方法做 P3384）

第二种做法：树链剖分

在这里顺便说一下树链剖分：

树链剖分是把一个树分成若干条链，最常用的是轻重链剖分。一个节点 $u$ 的重链所连接的节点 $v$，有一个特征，就是 $v$ 的子树是最大的，其他的边全都是轻链。通过一些处理（两次dfs）可以求出一个节点的父亲、深度和在线段树上的 $id$，那么就可以很方便地做这道题目了。

时间复杂度 $O(n \log^2 n)$ 常数较小，如果把线段树改成树状数组就最好了


我这里的代码对于输入的数据做了处理，即每个读入的节点的编号加 $1$，当然不这样处理也可以，把第一次处理时的 $fa$ 变成一个很大的数，比如 $n+100$ 之类的。不过一般的题目数据不会卡的。

然后再介绍一个小技巧

```cpp
char c;
scanf("%s",&c);
```
可以有效地去除空格


好了代码如下：

```cpp
#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int n,m,r,father[100050],depth[100050],size[100050],son[100050],top[100050],ide[100050],rid[100050],cnt=0;

long long val[100050],p;

vector <int> graph[100050];

struct SegTree
{
    int left,right;
    long long value,tag;
}t[500050];

void dfs1(int u,int fa)
{
    father[u]=fa;
    depth[u]=depth[fa]+1;
    size[u]=1;
    for (int i=0;i<graph[u].size();i++)
    {
        int v=graph[u][i];
        if (v!=fa)
        {
            dfs1(v,u);
            size[u]+=size[v];
            if (size[v]>size[son[u]])
                son[u]=v;
        }
    }
}

void dfs2(int now,int fir)
{
    cnt++;
    top[now]=fir;
    ide[now]=cnt;
    rid[ide[now]]=now;
    if (!son[now]) 
        return;
    dfs2(son[now],fir);
    for (int i=0;i<graph[now].size();i++)
    {
        int v=graph[now][i];
        if (v!=father[now] && v!=son[now])
            dfs2(v,v);
    }
}

void Push_Up(int id)
{
    t[id].value=t[id<<1].value+t[id<<1|1].value;
}

void Push_Down(int id)
{
    t[id<<1].tag+=t[id].tag;
    t[id<<1|1].tag+=t[id].tag;
    t[id<<1].value+=t[id].tag*(t[id<<1].right-t[id<<1].left+1);
    t[id<<1|1].value+=t[id].tag*(t[id<<1|1].right-t[id<<1|1].left+1);
    t[id].tag=0;
}

void Build(int id,int left,int right)
{
    t[id].left=left;
    t[id].right=right;
    if (left==right)
    {
        t[id].value=val[rid[left]];
        return;
    }
    int mid=(left+right)>>1;
    Build(id<<1,left,mid);
    Build(id<<1|1,mid+1,right);
    Push_Up(id);
}

void Update(int id,int left,int right,long long value)
{
    if (t[id].left>=left && t[id].right<=right)
    {
        t[id].tag+=value;
        t[id].value+=value*(t[id].right-t[id].left+1);
        return;
    }
    Push_Down(id);
    int mid=(t[id].left+t[id].right)>>1;
    if (right<=mid)
        Update(id<<1,left,right,value);
    else if (left>mid)
        Update(id<<1|1,left,right,value);
    else
    {
        Update(id<<1,left,mid,value);
        Update(id<<1|1,mid+1,right,value); 
    }
    Push_Up(id);
}

long long Query(int id,int left,int right)
{
    if (t[id].left>=left && t[id].right<=right)
        return t[id].value;
    else
    {
        int mid=(t[id].left+t[id].right)>>1;
        Push_Down(id);
        if (right<=mid)
            return Query(id<<1,left,right);
        if (left>mid)
            return Query(id<<1|1,left,right);
        else
            return Query(id<<1,left,mid)+Query(id<<1|1,mid+1,right);
    }
}

void SubTreeChange(int id,int value)
{
    int x=ide[id];
    int y=ide[id]+size[id]-1;
    Update(1,x,y,value);
}

long long SubTreeQuery(int id)
{
    int x=ide[id];
    int y=ide[id]+size[id]-1;
    return Query(1,x,y);
}

void LinkChange(int x,int y,int value)
{
    int tx=top[x];
    int ty=top[y];
    while (tx!=ty)
    {
        if (depth[tx]<depth[ty])
        {
            swap(x,y);
            swap(tx,ty);
        }
        Update(1,ide[tx],ide[x],value);
        x=father[tx];
        tx=top[x];
    }
    if (depth[x]>depth[y])
        swap(x,y);
    Update(1,ide[x],ide[y],value);
}

long long LinkQuery(int x,int y)
{
    int tx=top[x];
    int ty=top[y];
    long long ans=0;
    while (tx!=ty)
    {
        if (depth[tx]<depth[ty])
        {
            swap(x,y);
            swap(tx,ty);
        }
        ans+=Query(1,ide[tx],ide[x]);
        x=father[tx];
        tx=top[x];
    }
    if (depth[x]>depth[y])
        swap(x,y);
    ans+=Query(1,ide[x],ide[y]);
    return ans;
}

int main()
{
    scanf("%d",&n);
    for (int i=1;i<n;i++)
    {
        int u,v;
        scanf("%d%d",&u,&v);
        graph[u+1].push_back(v+1);
        graph[v+1].push_back(u+1);
    }
    dfs1(1,0);
    dfs2(1,1);
    scanf("%d",&m);
    Build(1,1,cnt);
    for (int i=1;i<=m;i++)
    {
        int u,v,d;
        char c;
        scanf("%s",&c);
        if (c=='A')
        {
            scanf("%d%d%d",&u,&v,&d);
            LinkChange(u+1,v+1,d);
        }
        else
        {
            scanf("%d",&u);
            printf("%lld\n",SubTreeQuery(u+1));
        }
    }
    return 0;
}
```

倍增+线段树做法

```cpp
#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

struct Seg_Tree
{
    int left,right,add;
    long long value;
}son[400050];

int n,m;

vector <int> graph[100050];

int fa[100050][16],size[100050],depth[100050];

int Time,pos[100050],belong[100050];

long long delta[500050];

bool vis[100050];

int read()
{
    int w=0,c=1; 
    char ch=getchar();
    while (ch<'0' || ch>'9')
    {
        if (ch=='-') 
            c=-1;
        ch=getchar();
    }
    while (ch>='0' && ch<='9')
    {
        w=w*10+ch-'0';
        ch=getchar();
    }
    return w*c;
}

void Build(int id,int left,int right)
{
    son[id].value=son[id].add=0;
    son[id].left=left;
    son[id].right=right;
    if (left==right)
        return;
    Build(id<<1,left,(left+right)>>1);
    Build(id<<1|1,((left+right)>>1)+1,right);
    son[id].value=son[id<<1].value+son[id<<1|1].value;
}

void Change_delta(int id,long long value,int left,int right)
{
    son[id].value+=value*(right-left+1);
    delta[id]+=value;
}

void Push_Up(int id)
{
    son[id].value=son[id<<1].value+son[id<<1|1].value;
}

void Push_Down(int id,int left,int right)
{
    int mid=(left+right)/2;
    Change_delta(id<<1,delta[id],left,mid);
    Change_delta(id<<1|1,delta[id],mid+1,right);
    delta[id]=0;
}

void Update(int id,int left,int right,long long value,int pos1,int pos2)
{
    int mid=(left+right)/2;
    //cout << id << " " << left << " " << right << " " << value << " " << pos1 << " " << pos2 << endl;
    //system("pause");
    if (pos1<=left && pos2>=right)
    {
        Change_delta(id,value,left,right);
        return;
    }
    Push_Down(id,left,right);
    if (pos1<=mid)
        Update(id<<1,left,mid,value,pos1,pos2);
    if (pos2>mid)
        Update(id<<1|1,mid+1,right,value,pos1,pos2);
    Push_Up(id);
}

void getlca(int u)
{
    vis[u]=true;
    size[u]=1;
    for (int i=1;i<=16;i++)
    {
        if (depth[u]<(1<<i))
            break;
        fa[u][i]=fa[fa[u][i-1]][i-1];
    }
    for (int i=0;i<graph[u].size();i++)
    {
        int v=graph[u][i];
        if (vis[v])
            continue;
        depth[v]=depth[u]+1;
        fa[v][0]=u;
        getlca(v);
        size[u]+=size[v];
    }
}

void dfs(int k,int num)
{
    int x=0;
    //cout << k << " " << num << endl;
    //system("pause");
    Time++;
    pos[k]=Time;
    belong[k]=num;
    for (int i=0;i<graph[k].size();i++)
    {
        int v=graph[k][i];
        if (depth[v]>depth[k] && size[v]>size[x])
            x=v;
    }
    if (x==0)
        return;
    dfs(x,num);
    for (int i=0;i<graph[k].size();i++)
    {
        int v=graph[k][i];
        if (depth[v]>depth[k] && x!=v)
            dfs(v,v);
    }
}

void Insert(int x,int y,long long z)
{
    for (;belong[x]!=belong[y];x=fa[belong[x]][0])
    {
        //cout << x << " " << y << endl;
        if (depth[belong[x]]<depth[belong[y]])
            swap(x,y);
        Update(1,1,n,z,pos[belong[x]],pos[x]);
    }
    if (depth[x]<depth[y])
        swap(x,y);
    //cout << x << " " << y << " " << pos[x] << " " << pos[y] << endl;
    Update(1,1,n,z,pos[y],pos[x]);
}

long long Query(int id,int left,int right,int pos1,int pos2)
{
    int mid=(left+right)/2;
    long long ans=0;
    //cout << id << " " << left << " " << right << " " << son[id].value << " " << pos1 << " " << pos2 << endl;
    if (pos1<=left && pos2>=right)
        return son[id].value;
    Push_Down(id,left,right);
    if (pos1<=mid)
        ans+=Query(id<<1,left,mid,pos1,pos2);
    if (pos2>mid)
        ans+=Query(id<<1|1,mid+1,right,pos1,pos2);
    Push_Up(id);
    return ans;
}

int main()
{
    //freopen("tree.in","r",stdin);
    //freopen("tree.out","w",stdout);
    scanf("%d",&n);
    for (int i=1;i<n;i++)
    {
        int u,v;
        scanf("%d%d",&u,&v);
        u++;
        v++;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    getlca(1);
    dfs(1,1);
    Build(1,1,n);
    m=read();
    //for (int i=1;i<=n;i++)
    //    cout << belong[i] << endl;
    for (int i=1;i<=m;i++)
    {
        char chr;
        int x;
        scanf("%s",&chr);
        scanf("%d",&x);
        x++;
        if (chr=='A')
        {
            int y,z;
            scanf("%d%d",&y,&z);
            y++;
            Insert(x,y,z);
        }
        if (chr=='Q')
            printf("%lld\n",Query(1,1,n,pos[x],pos[x]+size[x]-1));
    }
    return 0;
}

/*4
0 1
1 2
2 3
4
A 1 3 1
Q 0
Q 1
Q 2
*/
```
**实测倍增比树链剖分慢1000ms**
