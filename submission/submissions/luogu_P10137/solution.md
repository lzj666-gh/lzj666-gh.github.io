# P10137 题解

[$\mathrm{\color{Black}B\color{Red}enq}$](https://codeforces.com/profile/Benq) 出的神奇倍增题。

对于这种细节很多的题，先把边界判掉。于是使用 `lower_bound` 把奶牛放到它第一个走到的交叉路口，再来考虑接下来的行走。

考虑奶牛的走法有什么规律或者性质。不妨设出发点 $(s_x,s_y)$ 满足 $(s_x+s_y)\bmod 2=0$；对于每条路，奶牛再它上面行走时会转向当且仅当遇到一条**方向不同**且**奇偶性不同**的路。由此可以确定的是，当奶牛再次走到与这条路方向相同的路时，**不需**考虑 $s_x+s_y$ 的奇偶性，下一条**同方向**的路的奇偶性一定与这条路**相反**。

于是这个东西可以**倍增**，类比 LCA 来理解，倍增的数组里面记的是“对于一条道路，令其‘父亲’为在它前面且与它奇偶性不同的第一条同方向道路，对于所有 $k$，这条路的 $2^k$ 级‘祖先’”；于是对于一个时间 $d$，就可以求出在 $d$ 秒内奶牛能走到的最远的交叉路口。

最后处理一下奶牛离开所有交叉路口后要走的路程即可。

时间复杂度 $O(n\log n)$。注意判断倍增的边界。

放代码：

```cpp
/*
ID: CrowMatrix
TASK: Walking in Manhattan
LANG: C++
*/
#include<bits/stdc++.h>
using namespace std;
int main(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);
  int n,q; cin>>n>>q;
  vector<int> h,v;
  while(n--){
    char c; int x; cin>>c>>x;
    if(c=='H')h.emplace_back(x);
    else v.emplace_back(x);
  } // 存储所有道路
  sort(h.begin(),h.end());
  sort(v.begin(),v.end());
  h.emplace_back(2e9),v.emplace_back(2e9);
  vector r(h.size(),vector<int>(18)),
    c(v.size(),vector<int>(18)); // 倍增数组
  for(int i=0;i<18;i++){
    r[h.size()-1][i]=h.size()-1;
    c[v.size()-1][i]=v.size()-1;
  } // 倍增数组初始化
  for(int i=h.size()-2;~i;i--){
    r[i][0]=(h[i]+h[i+1]&1?i+1:r[i+1][0]);
    for(int j=1;j<18;j++)
      r[i][j]=r[r[i][j-1]][j-1];
  } // 对于横的道路处理 2^k 级祖先
  for(int i=v.size()-2;~i;i--){
    c[i][0]=(v[i]+v[i+1]&1?i+1:c[i+1][0]);
    for(int j=1;j<18;j++)
      c[i][j]=c[c[i][j-1]][j-1];
  } // 对于竖的道路处理 2^k 级祖先
  auto Q=[&](int x,int y,int d,int t=0){
    int h0=lower_bound(h.begin(),h.end(),y)-h.begin(),
      v0=lower_bound(v.begin(),v.end(),x)-v.begin();
    if(y<h[h0]){
      if(d+y<=h[h0])return make_pair(x,d+y);
      d-=h[h0]-y,t+=h[h0]-y;
    }
    if(x<v[v0]){
      if(d+x<=v[v0])return make_pair(x+d,y);
      d-=v[v0]-x,t+=v[v0]-x;
    } // 找到第一个交叉路口，记得判走不到的情况
    for(int k=17;~k;k--){
      int x=r[h0][k],y=c[v0][k];
      if(h[x]-h[h0]>d||v[y]-v[v0]>d)continue;
      if(v[y]-v[v0]+h[x]-h[h0]>d)continue;
      d-=v[y]-v[v0]+h[x]-h[h0],t+=v[y]-v[v0]+h[x]-h[h0];
      h0=x,v0=y;
    } // 倍增找走最远的点
    if(t&1){
      int a=c[v0][0];
      if(v[a]-v[v0]>=d)return make_pair(v[v0]+d,h[h0]);
      d-=v[a]-v[v0];
      return make_pair(v[a],h[h0]+d);
    }
    int a=r[h0][0];
    if(h[a]-h[h0]>=d)return make_pair(v[v0],h[h0]+d);
    d-=h[a]-h[h0];
    return make_pair(v[v0]+d,h[a]); // 最后一段
  };
  while(q--){
    int x,y,d; cin>>x>>y>>d;
    auto [a,b]=Q(x,y,d);
    cout<<a<<' '<<b<<'\n';
  } // 处理询问
  return 0;
}
```