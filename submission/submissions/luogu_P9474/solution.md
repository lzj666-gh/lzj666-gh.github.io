# P9474 题解

## 题目大意
在长度为 $n$ 的，元素互不相同的数列 $a$ 中选出一个长度为 $m$ 的元素互不相邻的子列，使得子列的极差最小。

$1\le n\le 10^5$。

## 题目分析

- 我会暴力！

枚举每个数是否被选，然后判断是否合法，合法就求个极差，记录过程中的最小值，复杂度 $O(2^n n)$。

期望得分 $12$ 分。

- 我会 dp！

设状态 $dp_{i,j,k,0/1}$ 表示前 $i$ 个数中，已经选了 $j$ 个数，最小值为 $a_k$，且没选（$0$）或者选了（$1$）$a_i$ 时，被选数的最大值的最小值，转移只需要按照题意转移一下就行了，复杂度 $O(n^2m)$。

期望得分 $36$ 分。

- 我会枚举！

首先一个显然的结论是，如果最大最小值都被固定，则其它数肯定就是值在其中间的数。所以当最大最小值固定时，我们就把不在这个范围内的数忽略，然后看看剩下的数能不能选到 $m$ 个。判断很简单，在没被忽略的数中，会形成若干连续的段，对于长度为 $len$ 的一段，显然可以选 $\lceil \frac{len}{2}\rceil$ 个数，总的数就是每一段可取的数之和。

所以我们可以枚举最大值和最小值，然后遍历一遍数组看看可不可行，在所有可行的方案中找到最小的极差即可，复杂度 $O(n^3)$。

期望得分 $36$ 分。

- 我会二分！

我们可以发现，对于一个最小值，满足条件的最大值是连续的，所以我们可以枚举最小值，然后二分查找满足条件的最小的最大值，统计答案即可，复杂度 $O(n^2\log n)$。

期望得分 $76$ 分。

- 我会线段树和双指针！~~但线段树和双指针好像不是普及组算法，不管了。~~

考虑在 $76$ 分算法上优化。显然，当最小值不断增大时，满足条件的最小的最大值也会跟着增大或不变。因为最小值变大了，就会有更多的数不再能选，这时候就需要更多的数来满足条件。所以，我们可以将数组排好序，用一个左指针从小到大枚举最小值，然后用一个右指针维护最大值，在枚举的过程中，我们先不断右移右指针并不断的添加可选的元素，直到满足条件或者全部选完。然后，删除左指针的元素，同时右移左指针。这个过程中，每个元素最多只会被右指针指到一次，被左指针指到一次，也就最多只会被添加一次与删除一次。

现在要考虑如何添加与删除。借助上述结论，对于长度为 $len$ 的连续段，可以选 $\lceil \frac{len}{2}\rceil$ 个数。在添加一个数时，我们考虑对可选数目的影响。首先考虑添加。

1. 当左右两边都空着时，可选数多一个。

2. 当左右两边有且只有一边已经有一段时，添加一个数会使其 $len$ 增加 $1$。由于对 $2$ 向上取整，所以这一段是偶数时可选数多一个，否则没有影响。

3. 当左右两边都有一段时，设左边长 $l$，右边长 $r$，则这一段变成了 $l+r+1$。通过简单的分类讨论可以得到，只有当 $l$ 和 $r$ 都是偶数时，可选数才能加一。

对于删除，其实就是这三点倒过来。


通过枚举可以使这一部分的复杂度变为 $O(n)$，不过可以用线段树维护一个数所在的段的左右端点，然后支持区间覆盖和单点查询，使其复杂度降到 $O(\log n)$。

总复杂度 $O(n\log n)$。

期望得分 $100$ 分。

~~写得如此全面，留个赞吧 awa。~~

```cpp
#include<bits/stdc++.h>
#define ll long long
#define L x<<1
#define R x<<1|1
#define mid (l+r>>1)
#define lc L,l,mid
#define rc R,mid+1,r
#define OK l>=Ll&&r<=Rr
#define rep(x,y,z) for(int x=(y);x<=(z);x++)
#define per(x,y,z) for(int x=(y);x>=(z);x--)
#define pb push_back
#define e(x) for(int i=h[x];i;i=nxt[i])
inline int read(){int s=0,w=1;char c=getchar();while(c<48||c>57) {if(c=='-') w=-1;c=getchar();}while(c>=48&&c<=57) s=(s<<1)+(s<<3)+c-48,c=getchar();return s*w;}
inline void pf(ll x){if(x<0) putchar('-'),x=-x;if(x>9)pf(x/10);putchar(x%10+48);}
const int N =1e5+5,M=4e7+5,inf=2147000000;
const ll mod=998244353;
using namespace std;
int n,m,ans=inf,now;
struct node{
	int x,id;
}a[N];
struct seg{
	int l,r,lazl,lazr;
}xd[N*4];
inline void covl(int x,int k){
	xd[x].l=xd[x].lazl=k;
}
inline void covr(int x,int k){
	xd[x].r=xd[x].lazr=k;
}
inline void pushdown(int x){
	if(xd[x].lazl)covl(L,xd[x].lazl),covl(R,xd[x].lazl);
	if(xd[x].lazr)covr(L,xd[x].lazr),covr(R,xd[x].lazr);
	xd[x].lazl=xd[x].lazr=0;
}
inline void modify(int x,int l,int r,int Ll,int Rr,int k,int t){
	if(Ll>Rr)return;
	if(OK){
		if(t==1)covl(x,k);
		else covr(x,k);
		return;
	}
	pushdown(x);
	if(Ll<=mid&&Rr>=l)modify(lc,Ll,Rr,k,t);
	if(Rr>mid&&Ll<=r)modify(rc,Ll,Rr,k,t);
}
inline seg query(int x,int l,int r,int p){
	if(p<1||p>n)return seg{0,0,0,0};
	if(l==r)return xd[x];
	pushdown(x);
	if(p<=mid)return query(lc,p);
	return query(rc,p);
}
inline void insert(int x){
	seg l,r;
	l=query(1,1,n,x-1),r=query(1,1,n,x+1);
	int Ll=l.l,Rr=r.r;
	if(!Ll){
		if(!Rr)modify(1,1,n,x,x,x,1),modify(1,1,n,x,x,x,2),now++;
		else {
			if((Rr-x)%2==0)now++;
			modify(1,1,n,x,x,Rr,2),modify(1,1,n,x,Rr,x,1);
		}
		return;
	}
	if(!Rr){
		if((x-Ll)%2==0)now++;
		modify(1,1,n,x,x,Ll,1),modify(1,1,n,Ll,x,x,2);
		return;
	}
	bool fl=(x-Ll)&1,fr=(Rr-x)&1;
	if(fl==0&&fr==0)now++;
	modify(1,1,n,Ll,Rr,Ll,1),modify(1,1,n,Ll,Rr,Rr,2);	
}
inline void del(int x){
	seg nw=query(1,1,n,x);
	int Ll=nw.l,Rr=nw.r;
	bool fl=(x-Ll)&1,fr=(Rr-x)&1;
	if(fl==0&&fr==0)now--;
	modify(1,1,n,Ll,x-1,x-1,2),modify(1,1,n,x+1,Rr,x+1,1);
	modify(1,1,n,x,x,0,1),modify(1,1,n,x,x,0,2);
}
inline bool cmp(node a,node b){
	return a.x<b.x;
}
int main(){
	n=read(),m=read();
	rep(i,1,n)a[i].x=read(),a[i].id=i;
	sort(a+1,a+n+1,cmp);
	int Rr=1;
	rep(i,1,n){
		while(Rr<=n&&now<m)insert(a[Rr++].id);
		if(now>=m)ans=min(ans,a[Rr-1].x-a[i].x);
		del(a[i].id);
	}
	cout <<ans;
	return 0;
}
```