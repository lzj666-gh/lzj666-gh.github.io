# P1640 题解

# ~~这题为什么要二分图呢？~~

太大了好像划不住

这题我们bfs一下就好了。二分图又不好写，还慢的要死，~~还丑~~，不如~~好写~~稳定的bfs。

说是bfs其实就是乱搞。

以下几段通俗易懂~~可爱~~面向萌新。大佬可以直接跳过看总结。

一个装备只能提供一个属性。我们把两个属性值当做两个点来连线，那么我们可以感性地想象这条线上有一只猫，这只猫要不然趴在一头，要不然趴在另一头，哪个值被覆盖代表着这个装备提供哪个属性值。如果将属性值来这样建一张图，对于每一个连通图，因为每一只猫都能覆盖旁边的一个点，我们可以很轻松的想象到，如果说这个图中有m条边，n个点，那么一定可以有min(n,m)个点被覆盖。

除了一个树以外，图上的边数一定大于等于点数。显然吧！那么说明图中的所有点都是可以被猫猫搞到的，树中有且只有一个点无法被覆盖。根据贪心的思想我们当然是让那个最大的值的那个点无法被覆盖。我们可以用bfs 通过对遍历到的边数和点数的比较 来维护这个过程，(不知道怎么维护可以看代码我会尽量的！写的非常！详细  ~~毕竟我想过审核~~)

而对于树中最大的点如何处理呢？每一次bfs都会遍历整个连通块，其他的bfs是够不到这个最大点的。所以最大的那个点无法被其他的bfs覆盖。那么我们将它的状态视为cant，即它绝对无法被覆盖。

没有与任何点相连的点，也可以看做一个树。

于是我们可以从1开始，向10000遍历。每一个值都是属性值，将每一个值都看做点。如果当前这个点没有被bfs过就bfs它 ~~废话~~，要不然就判断是否是cant点。

 ## 总结在这
 总结：将属性值连边，每一个强联通分量内的所有点都可选，每一个树内最大点不可选，用bfs判断。根本就不用缩点。(并查集可能会更快？我写不明白..)每一条边与每一个点都至多会被判断一次，上界复杂度O(n+m) (要是2就cant了，那么当然后面全不用判了)。
 
 多简单...

说实话，处理结果的思路与楼下用并查集的大佬们的思路很像，但是又略有不同。严格地说并不是同一种方法。

代码！
```cpp
#include <bits/stdc++.h> //我就好这一口
#define rap(i,s,n) for(int i=s;i<=n;i++)//同上
#define drap(i,s,n) for(int i=s;i>=n;i--)//同上
#define N 23333
#define M 2333333
using namespace std;
char xB[1<<15],*xS=xB,*xTT=xB;//读优 原因同上
#define getc() (xS==xTT&&(xTT=(xS=xB)+fread(xB,1,1<<15,stdin),xS==xTT)?0:*xS++)
#define isd(c) ((c>='0'&&c<='9')||(c=='-'))
template<typename T>
inline void rd(T & xaa){
    char xchh; T f=1; xaa=0; while(xchh=getc(),!isd(xchh));
    if(xchh=='-'){f=-1; xchh=getc();} xaa=xchh-'0';
    while(xchh=getc(),isd(xchh)) xaa=xaa*10+xchh-'0';
    xaa*=f; return;
}
int m,to[M],nxt[M],head[N],cnt;//存图
bool vis[N],cant[N];//bfs用的
void add(int a,int b){cnt++; to[cnt]=b; nxt[cnt]=head[a]; head[a]=cnt; return;}
bool bfs(int k){//返回是否能覆盖
	//printf("bfs(%d)\n",k); 
    if(!vis[k]){
        vis[k]=1; int maxp=k,nump=0,nume=0; queue<int>q; q.push(k);
        //maxp:涉及到的最大的点。设成0不会影响结果。
        //nump:点数 nume:边数
        while(!q.empty()){
            int u=q.front(); q.pop(); maxp=max(maxp,u); nump++;
            for(int i=head[u];i;i=nxt[i]){nume++; if(!vis[to[i]]) vis[to[i]]=1,q.push(to[i]);}
        }
        //每bfs一个点都让nump++(显然),每碰到一条边都让nume++。
        //但是因为是双向图，每条边都碰到了两遍。所以/2
        nume>>=1; if(nume<nump) cant[maxp]=1;
        //rap(i,1,maxp) printf("%d ",vis[i]); printf("\n");
    	//rap(i,1,maxp) printf("%d ",cant[i]); printf("\n");
    }
    return (!cant[k]);//判断当前点是否不可覆盖(其实只有它自己孤零零不和其他点相连才是0...
}
int main(){
    //freopen("1640.in","r",stdin);
    rd(m); int a,b; rap(i,1,m){rd(a),rd(b); add(a,b); add(b,a);}
    int k=1; while((vis[k]&&!cant[k])||bfs(k)) k++; printf("%d\n",k-1);
    //注意while中的判断。只有vis过才能判断cant值，否则cant值没有意义。没有vis过就会bfs。
    return 0;
}
```

点个赞吧 ^^（用一个PAFF酱的表情）