# P4145 题解

## 思路

[首发于个人博客。](https://www.xgzepto.cn/post/bzoj-3038)


我不会支持区间开方的数据结构，所以我选择暴力单点修改，树状数组区间查询。

因为1e12的数开方6次就变成了1，所以需要修改的次数实际上很少，用并查集可以跳过小于等于1的数，然后。。。树状数组单点修改即可。没开O2，最慢的点大概就是250ms，还是比较快的。

## 代码

非常短。。。

树状数组两行搞定，并查集一行搞定。

修改的时候判断一下是不是小于等于1，是的话就更新一下fa数组，具体看一下注释。

```
#include <bits/stdc++.h>
#define maxn 100100
#define ll long long
using namespace std;
ll tree[maxn*4],a[maxn];int fa[maxn],m,n,q,l,r,t;
int find(int x){return fa[x]==x?x:fa[x]=find(fa[x]);}//并查集，路径压缩
void add(int x,ll y){while(x<=n)tree[x]+=y,x+=(x&-x);}
ll qry(int x){ll r=0;while(x)r+=tree[x],x-=(x&-x);return r;}
int main(){
	scanf("%d",&n);for (int i=1;i<=n;i++)
	scanf("%lld",&a[i]),add(i,a[i]),fa[i]=i;scanf("%d",&m);fa[n+1]=n+1;
	while(m--){scanf("%d%d%d",&q,&l,&r);if (l>r) swap(l,r); 
		if (q==1) printf("%lld\n",qry(r)-qry(l-1));
		else for (int i=l;i<=r;add(i,(t=(int)sqrt(a[i]))-a[i]),a[i]=t,fa[i]=(a[i]<=1)?i+1:i,i=(find(i)==i)?i+1:fa[i]);
	}
    //上面这行信息量很大。。。做了单点修改的操作，a数组保存了每个点的实际值，当a[i]<=1的时候，直接跳到下一个点，结束。可以手算一下，就能很快理解了。
}
```