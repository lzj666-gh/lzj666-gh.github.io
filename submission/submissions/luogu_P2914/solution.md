# P2914 题解

由题意可得这是一道单源最短路，从第一个点到第n个点的单源最短路，先在原来有电线的两点之间连一条边，代价为0，再建图，每两点之间先尝试建一条边，如果原来有边或代价大于m，则依然是无穷大，最后建图完成后跑一遍Dijkstra就好。
```cpp
const oo=maxlongint div 2;//常量，定义无穷大
var
n,w,i,j,k,p1,p2:longint;
m:double;
a:array[1..1000,1..1000]of double;
dist:array[1..1000]of double;
vis:array[1..1000]of boolean;
x,y:array[1..1000]of longint;
function calc(a,b,c,d:longint):double;//计算两点距离
  begin exit(sqrt(sqr(a-b)+sqr(c-d)));end;
function min(a,b:double):double;
  begin if a<b then exit(a);exit(b);end;
begin
read(n,w,m);
for i:=1 to n do read(x[i],y[i]);
for i:=1 to n do
  for j:=1 to n do
    a[i,j]:=oo;//初始化a数组，各点之间的距离为无穷大
for i:=1 to w do
  begin
    read(p1,p2);
    a[p1,p2]:=0;a[p2,p1]:=0;//原来如果有电线经过的代价为0
  end;
for i:=1 to n-1 do
  for j:=i+1 to n do
    begin
      a[i,j]:=min(a[i,j],calc(x[i],x[j],y[i],y[j]));
      //原来有电线的不架电线（代价为0）
      //没有电线的架电线（即两点之间的距离）
      if a[i,j]>m then a[i,j]:=oo;
      //如果新的电线大于了m，那么还是无穷大
      a[j,i]:=a[i,j];
    end;
//以下为最基本的最短路——Dijkstra，不解释
//若有疑问，请移步P3371【模板】单源最短路径
for i:=1 to n do dist[i]:=oo;
dist[1]:=0;
for i:=1 to n do
  begin
    k:=-1;
    for j:=1 to n do
      if((k=-1)or(dist[k]>dist[j]))and(not vis[j])then k:=j;
    if k=-1 then break;vis[k]:=true;
    for j:=1 to n do
      if(not vis[j])and(dist[k]+a[k,j]<dist[j])then
        dist[j]:=dist[k]+a[k,j];
  end;
if dist[n]<>oo then write(trunc(dist[n]*1000))else write(-1);
//输出答案的格式别忘了
end.
```