# P7173 题解

增广路算法由于实现中存在最短路算法，无法处理存在费用负圈的最小费用流问题。

消圈算法本身就有消除负圈的过程，但由于效率低下，在 OI 中并不实用。

我们考虑利用上下界网络流的技术来解决负圈的问题。

对于网络中的负费用边 $x\rightarrow y$，我们先让其直接满流。然后加入一条边 $y\rightarrow x$，费用为原来费用的相反数，用于退流。

满流直接用上下界费用流的技术解决，跑一个有源汇上下界最小费用最大流即可。

代码如下：
```cpp
#include<bits/stdc++.h>
using namespace std;

typedef long long LL;

const int N=200,M=10000,INF=(1<<30)-1;

int n,m,st0,td0,df[N+9];
int ans[2];
struct side{
  int y,next,f,v;
}e[M*2+N*2+9];
int lin[N+9],cs;

void Ins(int x,int y,int f,int v){e[++cs].y=y;e[cs].f=f;e[cs].v=v;e[cs].next=lin[x];lin[x]=cs;}
void Ins_flow(int x,int y,int f,int v){Ins(x,y,f,v);Ins(y,x,0,-v);}

void into(){
  scanf("%d%d%d%d",&n,&m,&st0,&td0);
  cs=1;
  for (int i=1;i<=m;++i){
    int x,y,f,v;
    scanf("%d%d%d%d",&x,&y,&f,&v);
    if (v>=0) Ins_flow(x,y,f,v);
    else{
      df[x]-=f;df[y]+=f;ans[1]+=f*v;
      Ins_flow(y,x,f,-v);
    }
  }
}

int st,td,cn;

void Get_graph(){
  st=n+1;td=cn=n+2;
  for (int i=1;i<=cn-2;++i){
    if (!df[i]) continue;
    df[i]>0?Ins_flow(st,i,df[i],0):Ins_flow(i,td,-df[i],0);
  }
  Ins_flow(td0,st0,INF,0);
}

int flow,value;
int dis[N+9],vis[N+9],pre[N+9],f[N+9];
queue<int>q;

bool Spfa(int st,int td){
  for (int i=1;i<=cn;++i) dis[i]=INF,vis[i]=0;
  dis[st]=0;vis[st]=1;f[st]=INF;q.push(st);
  for (;!q.empty();){
    int t=q.front();q.pop();
    vis[t]=0;
    for (int i=lin[t];i;i=e[i].next)
      if (e[i].f&&dis[t]+e[i].v<dis[e[i].y]){
        dis[e[i].y]=dis[t]+e[i].v;
        pre[e[i].y]=i;
        f[e[i].y]=min(f[t],e[i].f);
        if (!vis[e[i].y]) vis[e[i].y]=1,q.push(e[i].y);
      }
  }
  return dis[td]^INF;
}

void Max_flow(int st,int td){
  flow=0;value=0;
  for (;Spfa(st,td);flow+=f[td],value+=f[td]*dis[td])
    for (int k=td;k^st;k=e[pre[k]^1].y) e[pre[k]].f-=f[td],e[pre[k]^1].f+=f[td];
}

void Get_ans(){
  Max_flow(st,td);
  ans[1]+=value;
  Max_flow(st0,td0);
  ans[0]=flow;ans[1]+=value;
}

void work(){
  Get_graph();
  Get_ans();
}

void outo(){
  printf("%d %d\n",ans[0],ans[1]);
}

int main(){
  into();
  work();
  outo();
  return 0;
}
```