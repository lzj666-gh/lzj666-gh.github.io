# P3115 题解

蒟蒻很菜，请见谅。

题目不是**特别、特别、特别**复杂。有一点要解释一下。

_"输出只有一行。 输出Bessie旅行最少要花的钱以及在此基础上最少的花费（中间用空格隔开）。如果Bessie不能从她的农场到达她的目的地，则直接输出-1"_ 
 
"在此基础上最少的花费"是指：**在花的钱最少时，经过的城市最少。**  ~~这是唯一比较绕的地方。~~
 
## 步入正题
 
分析：
 
1.建图: 此题中每个航线经过的城市数量<=100， 因此，枚举起点城市和终点城市，暴力建图即可。

PS: 若每个航线经过的城市数量经过的城市较多(如<=100000)，我们可以采用“中转点”的思想。即，对于航线中的所有城市$t [1],t[2],.....t[n],$新建一个点$x$，从$t[1],t[2]......t[n-1]$建立到$x$的边（权为题中给定的$cost$），在从$x$建立到$t[2],t[3]......t[n]$的边（权为$0$），即可使其中任意一点到另一点的距离和为$cost$,但相比而言节约了不少空间（**如果存边的话**）。

2.求最短路。**照着SPFA模板打即可，不需优化。**

详见以下代码。

```cpp
// luogu-judger-enable-o2
//吸个氧气(...)
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
//以下为fread(二进制读入)模板，实测相对于getchar应该快点
char ss[1<<17],*A=ss,*B=ss;
inline char gc(){
    return A==B&&(B=(A=ss)+fread(ss,1,1<<17,stdin),A==B)?EOF:*A++;
}
template<typename qRead>
inline void qr(qRead &s){
    char c=gc(); s=0;
    for(;c<'0'||c>'9';c=gc());
    for(;c>='0'&&c<='9';c=gc())
        s=(s<<1)+(s<<3)+(c^48);
}

typedef long long ll;
const int N=1005,M=105;
struct edge{
    int len,cnt;
}Edge[N][N];//邻接矩阵，本题边较多，不宜用邻接表
int City[N],t[M],n,m,i,j,u,v,a,b;
ll Dis[N];//最短距离
bool Inq[N];

void SPFA(int s){
//模板
    for(i=1;i<=n;++i){
        Dis[i]=1e18; City[i]=1e9;
    }
    queue<int> q;
    q.push(s); Inq[s]=1;
    Dis[s]=0; City[s]=0;
    ll x; int y;
    while(!q.empty()){
        u=q.front(); q.pop(); Inq[u]=0;
        for(v=1;v<=n;++v){//用邻接矩阵存储，那么就要枚举点
            if(Edge[u][v].len<1e9){//如果有边的话
                x=Dis[u]+Edge[u][v].len;
                y=City[u]+Edge[u][v].cnt;
                if(x<Dis[v]){
                    Dis[v]=x;
                    City[v]=y;
                    if(!Inq[v]){
                        q.push(v); Inq[v]=1;
                    }
                }
                else if(x==Dis[v] && y<City[v])//同时使城市数量最小
                    City[v]=y;
            }
        }
    }
}

int main(){
    qr(a); qr(b); qr(m);
    int x,y;
    for(i=1;i<N;++i){
        for(j=1;j<N;++j)
            Edge[i][j].len=Edge[i][j].cnt=1e9;
    }
    while(m--){
        qr(x); qr(y);
        for(i=1;i<=y;++i){
            qr(t[i]);
            n=t[i]>n?t[i]:n;
        }
        for(i=1;i<y;++i){
            for(j=i+1;j<=y;++j){
                if(x<Edge[t[i]][t[j]].len){//防止有重边
                    Edge[t[i]][t[j]].len=x;
                    Edge[t[i]][t[j]].cnt=j-i;
                }
                else if(x==Edge[t[i]][t[j]].len && j-i<Edge[t[i]][t[j]].cnt)
                    Edge[t[i]][t[j]].cnt=j-i;
            }
        }
    }
    SPFA(a);
    //输出
    if(Dis[b]<1e18)
        printf("%lld %d\n",Dis[b],City[b]);
    else
        puts("-1 -1");
    return 0;
}
```
//谢谢观看蒟蒻的代码。

//管理员dalao求通过