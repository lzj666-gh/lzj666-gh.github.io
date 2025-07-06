# P5958 题解

**本题解已经通过了，这次是勘误，去掉了反作弊，望管理员通过。**

**感谢 @void_basic_learner dalao 指出的错误。**
# 树形DP入门题

## 题意描述
在一棵以1号节点为根节点的树上，有很多~~纯洁的~~白点，

BUT，突然有一个黑点出现（可能在任意位置）

它要染黑尽可能多的节点，而在一棵子树中，

只有当黑点的比例$>x$才可以染黑根节点（即整棵子树）

求x的最小值，使得整棵树中被染黑的节点数不超过$k$个

如果你看不懂请走[传送门](https://www.luogu.com.cn/problem/P5958)

## 算法分析
一道很裸的树形DP，但思路很巧

显然本题有以下性质：
 1. **最坏情况下，最开始的叛徒是叶子结点**
 2. **因为一个节点被染黑了，一起为根节点的子树将全黑，所以最终被染黑的一定是一颗子树**

先设计状态：**$f(i)$表示使得$i$不变黑的最小$x$**

易得：**$f(i)$也是使得$i$变黑的最大$x$**

可知$f(i)$仅与$f(son{i})$以及$soni$的大小有关（这里的$soni$表示$i$的子节点）

那么我们用$sum(i)$表示**以$i$为根节点的子树的大小**,$sum(i)$是需要提前用dfs预处理的

显然$i$被染黑仅必须满足以下两种情况：

 1. **$f(soni) > x$,即$i$的某棵子树被染黑**
 2. **$sum(soni)/(sum(i)-1) > x$,即$soni$的被染黑足以导致$i$的被染黑**
 
根据以上规律可以推出如下方程：

$f(i)=max(f(i),min(f(soni),sum(soni)/(sum(i)-1)))$~~(不会用LaTeX写公式的蒟蒻瑟瑟发抖)~~

取$min$是因为需要同时满足条件1和条件2，
取$max$是因为需要答案最优

~~（貌似貌似到这里就结束了呢）~~

其实还有以下三点细节需要注意：

1. **对于叶子结点$a$，显然有$f(a)=1$**
2. **对于$ans$当$sum(a)<k$时是不需要考虑的，因为它合法，所以即使它被染黑也无所谓**
3. **针对上一条结论，易得$ans=max(ans,f(a))$,其中$sum(a)>=k$**

然后就去快乐$AC$吧......

## 代码实现

```cpp
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<vector>
#define maxn 500050
using namespace std;

int n,k,sum[maxn];
double f[maxn],ans;
vector<int>v[maxn];//用vector存图笑哈哈

void dfs(int now,int fa){
    sum[now]=1;
    for(int i=0;i<v[now].size();i++){
        int to=v[now][i];
        dfs(to,now);
        sum[now]+=sum[to];
    }//dfs预处理sum[]
    if(sum[now]==1){f[now]=1.0;return;}//叶子结点的处理
    for(int i=0;i<v[now].size();i++){
        int to=v[now][i];
        f[now]=max(f[now],min(f[to],(double)sum[to]/(sum[now]-1)));
    }//dp
    if(sum[now]>k) ans=max(ans,f[now]);//统计答案，注意if
    return;
}

int main(){
    scanf("%d %d",&n,&k);
    int x;
    for(int i=2;i<=n;i++){
        scanf("%d",&x);
        v[x].push_back(i);
    }
    dfs(1,0);
    printf("%.8lf",ans);//注意精度问题
    return 0;
}
```

## 结语
安利[my blog](https://www.cnblogs.com/lpf-666/)
（光速逃...