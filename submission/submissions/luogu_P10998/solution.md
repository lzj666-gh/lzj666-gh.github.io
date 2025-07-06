# P10998 题解

## 思路

这个问题研究的是满足条件的四元组个数，那么我们应该研究“满足条件的四元组”的结构，以及如何从题目的三元组找到对应的四元组。

经过一些尝试和观察或者打表，可以发现这个题答案不可能特别大。

因此，考虑如何高效地枚举可能的四元组。

## 算法

考虑一个三元组 $(u,v,w)$ 属于哪些合法四元组。可以发现，$(u,v,w)$ 所属的合法四元组个数，等于满足“ $(u,v,x),(u,w,x),(v,w,x)$ 三个三元组都存在”的 $x$ 的个数。（这里还是有序的 $u\lt v\lt w\lt x$）

所以，我们定义 $S(u,v)$ 表示使得 $(u,v,x)$ 三元组存在的 $x$ 的的集合。

**朴素算法 1** 我们预处理算出所有非空的 $S(u,v)$，然后对于每个三元组 $(u,v,w)$ 直接暴力计算 $S(u,v),S(v,w),S(u,w)$ 的交集大小，累加起来就是答案。

**定理 上述算法的时间复杂度是 $O(m^{4/3})$。**

**证明如下：**

首先注意到，暴力求这三个集合交集大小的时间复杂度同阶于其中**最小的**一个集合大小，只要枚举最小的那个集合里的元素查询在不在其它集合里即可。

所以时间复杂度 $\sim\sum_{(u,v,w)} \min(\lvert S(u,v) \rvert, \lvert S(u,w) \rvert, \lvert S(v,w) \rvert)$

现在只要分析 $S$ 的大小。为了方便，我们之后称 $1$ 到 $n$ 是无向图上的点，称 $S(u,v)$ 是无向图上 $(u,v)$ 的边权。那么：

1. 所有边权和为 $m$
2. 我们要最大化图上前 $m$ 大的三元环边权最小值之和，这是上述算法时间复杂度的上界。

容易证明，如果一个图中有 $i$ 个不同的三元环，那么图里至少有 $\sim i^{2/3}$ 条边。（参见三元环计数的分析。）

所以第 $i$ 大的三元环边权最小值不会超过 $\sim\frac{m}{i^{2/3}}$。

所以，前述朴素算法 1 时间复杂度上界不超过 $\sim\sum_{i=1}^m \frac{m}{i^{2/3}}\sim \int_1^m \frac{m}{i^{2/3}} \mathrm di+O(m) =O(m^{4/3})$。

这个朴素算法 1 就可以通过本题。

## 参考程序

这个 $O(m^{4/3}\log m)$ 程序使用了 `std::map`，改为hash表（散列表）可以去掉复杂度中的 $\log$。

```cpp
#include<bits/stdc++.h>

using namespace std;
typedef pair<int,int> p_t;

const int MX=300005;
map<p_t, set<int>> d;
int n,m;
int u[MX],v[MX],w[MX];

int main(){
    ios::sync_with_stdio(false);
    cin>>n>>m;
    for(int i=1;i<=m;i++){
        cin>>u[i]>>v[i]>>w[i];
        d[make_pair(u[i],v[i])].insert(w[i]);
    }
    int ans=0;
    for(int i=1;i<=m;i++){
        set<int> *W=&d[make_pair(u[i],v[i])], *V=&d[make_pair(u[i],w[i])], *U=&d[make_pair(v[i],w[i])];
        if(U->size()>V->size())swap(U,V);
        if(V->size()>W->size())swap(V,W);
        if(U->size()>V->size())swap(U,V); // 冒泡排序，找到最小的一个集合，保证求交集复杂度
        for(auto j:*U)if(V->find(j)!=V->end()&&W->find(j)!=W->end()){
            ans++;
        }
    }
    cout<<ans<<endl;
    return 0;
}
```