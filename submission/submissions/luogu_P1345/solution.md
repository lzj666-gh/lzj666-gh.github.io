# P1345 题解


#最小の割点 模板题

众所周知， "最小の割边"（也就是最小割）是要求

`为了使原点（记为S）和汇点（记为T）不连通，最少要割几条边`

那么最小の割点要怎么求？

###转化！把最小の割点转为最小の割边！

我们可以通过转化，把最小の割点转为最小の割边。假设原来的点编号为i，总共有n个点，那么我们就把每个点拆成两个点，编号分别为i和i+n。其中点i负责连接原图中连入这个点的边，点i+n负责连原图中连出这个点的边。就像下边这样：

 ![](https://cdn.luogu.com.cn/upload/pic/11779.png) 

通过这种奇怪的手♂段，我们就华丽丽的把 最小の割点 转为 最小の割边

###边权？

由于一个点只能被删一次~~（废话）~~，故点i和点i+n之间有一条边权为1的**有向边**，而原图中的边的边权则为INF

举个例子：

 ![](https://cdn.luogu.com.cn/upload/pic/12142.png) 

（黑边的边权为INF，黄边的边权为1）

###为什么要这样做？

如果一条黄色的边（就是点i和点i+n之间的边）被删了，那么所有进入这个点的边就不能和从这个点出去的边相连，就等价于这个点不存在。

###完整の代码

    
    
    
    
    
    
    
    

```cpp
    #include <bits/stdc++.h>
    #define vc vector
    #define INF ((int)(1e9))
    #define LINF ((ll)(1e18))
    #define pb push_back
    #define mp make_pair
    #define ll long long
    #define _tp template
    #define _tyn typename
    #define sint short int
    #define ull unsigned ll
    #define pii pair<int,int>
    #define uint unsigned int
    #define ms(_data) memset(_data,0,sizeof(_data))
    #define fin(_filename) freopen(_filename,"r",stdin)
    #define fout(_filename) freopen(_filename,"w",stdout)
    #define msn(_data,_num) memset(_data,_num,sizeof(_data))
    using namespace std;
    _tp<_tyn T>void mymax( T &_a , T _b ){ if( _a < _b ) _a = _b; }
    _tp<_tyn T>void mymin( T &_a , T _b ){ if( _a > _b ) _a = _b; }
    void print(int _x){printf("%d\n",_x);}
    void print(ll _x){printf("%I64d ",_x);}
    #define il inline
    il int in(){
        char c = getchar();
        int ret = 0;
        while( c < '0'  ||  c > '9' ) c = getchar();
        while( c >= '0'  &&  c <= '9' ){
            ret *= 10;
            ret += c-'0';
            c = getchar();
        }
        return ret;
    }
    il void read( int &x ){
        x = in();
    }
    il void read( int &x, int &y ){
        x = in(); y = in();
    }
    il void read( int &x1 , int &x2 , int &x3 ){
        x1 = in(); x2 = in(); x3 = in();
    }
    il void read( int &x1 , int &x2 , int &x3 , int &x4 ){
        x1 = in(); x2 = in(); x3 = in(); x4 = in();
    }
    /////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////
    #define MAXN 110
    struct Edge{
        int to,cap,rev;
        Edge(){}
        Edge( int tt , int cc , int rr ){
            to = tt;
            cap = cc;
            rev = rr;
        }
    };
    int n,m,s,t;
    vc<Edge> e[MAXN<<1];
    vc<Edge> inp[MAXN<<1];
    il void addedge( int f , int t , int c ){
        inp[f].pb( Edge(t,c,inp[t].size()) );
        inp[t].pb( Edge(f,0,inp[f].size()-1) );
        e[f].pb(Edge());
        e[t].pb(Edge());
    }
    il void f5(){
        for( int i = 1 ; i <= n+n+1 ; i++ )
            for( uint j = 0 ; j < inp[i].size() ; j++ )
                e[i][j] = inp[i][j];
    }
    int lev[MAXN<<1];    //Level
    il void bfs( int st ){
        ms(lev);
        queue<int> q;
        q.push(st);
        lev[st] = 1;
        while( !q.empty() ){
            int now = q.front();
            q.pop();
            for( uint i = 0 ; i < e[now].size() ; i++ ){
                if( e[now][i].cap <= 0 ) continue;
                int v = e[now][i].to;
                if( !lev[v] ){
                    lev[v] = lev[now]+1;
                    q.push(v);
                }
            }
        }
    }
    bool vis[MAXN<<1];
    il int dfs( int pos , int flow ){
        if( pos == t ) return flow;
        for( uint i = 0 ; i < e[pos].size() ; i++ ){
            Edge x = e[pos][i];
            int u = x.to;
            if( vis[u] ) continue;
            if( x.cap <= 0 ) continue;
            if( lev[u] != lev[pos]+1 ) continue;
            vis[u] = 1;
            int tans = dfs( u , min(flow,x.cap) );
            vis[u] = 0;
            if( tans > 0 ){
                e[pos][i].cap -= tans;
                e[u][x.rev].cap += tans;
                return tans;
            }
        }
        return 0;
    }
    int ans = 0;
    int main(){
        read(n,m,s,t);
        for( int i = 1 ; i <= n ; i++ ){
            addedge(i,n+i,1);
        }
        for( int i = 1 ; i <= m ; i++ ){
            int a,b;
            read(a,b);
            addedge(a+n,b,INF);
            addedge(b+n,a,INF);
        }
        f5();
        while(1){
            bfs(s+n);
            if( !lev[t] ) break;
            ms(vis);
            int tans;
            while( ( tans = dfs(s+n,INF) ) > 0 ){
                ans += tans;
                ms(vis);
            }
            //cout << "[Tans] " << tans << endl;
        }
        printf("%d\n",ans);
        return 0;
    }
###如果对题解有不明白的地方或者感觉题解不对，一定要在“评论区”提出。
```