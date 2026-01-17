# P1533 题解

### 思路：

　　先吐槽一般数据较水～～

　　本来想打个暴力，于是码了一个莫队+权值线段树维护，时间复杂度$O(n\sqrt{n}logn)$（显然过不了啊！～），结果$AC$还进了最优解第一页。

　　首先就是常规的莫队离线，记录区间，排序。

　　对原数离散化，再构建权值线段树，每次维护一个数的增减，查询整个区间第$k$大，记录$ans$就$OK$了。
  
$\quad$这里我安利一波权值线段树：
	
$\quad$1、插入操作：其实就是单点修改，对于离散后的数每次找到它所在的叶子节点，使其权值增减$1$（说明这个数出现了一次或者减少了一个），并维护一段区间的数出现的个数（即区间求和）

$\quad$2、查询操作：询问第$k$小的数时，从整个区间$[1,n]$开始递归，当左儿子区间$[l,mid]$中出现的数个数大于等于$k$时，查询左儿子，否则查询右儿子中的第$k-sum[l,mid]$小的数(即左儿子中已有$sum[l,mid]<k$个数，那么整个区间第$k$小的数在右儿子里，且是右儿子中的第$k-sum[l,mid]$小的数)，当查询到$l==r$时返回$l$就$ok$了。

$\quad$欢迎来踩博客[five20](http://www.cnblogs.com/five20/p/8962105.html)（蒟蒻写题解不易，转载请注明出处，万分感谢！）

### 代码：
```cpp
// luogu-judger-enable-o2
#include<bits/stdc++.h>
#define il inline
#define ll long long
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
using namespace std;
const int N=300005;
int tr[N<<2],n,m,pos[N],a[N],ans[N];
struct node{
	int l,r,k,id;
}q[N];
struct numm{
	int v,id;
	bool operator < (const numm a)const{return v<a.v;}
}nm[N];
il bool cmp(node a,node b){return pos[a.l]==pos[b.l]?a.r<b.r:a.l<b.l;}
il int gi(){
	int a=0;char x=getchar();bool f=0;
	while((x<'0'||x>'9')&&x!='-')x=getchar();
	if(x=='-')x=getchar(),f=1;
	while(x>='0'&&x<='9')a=a*10+x-48,x=getchar();
	return f?-a:a;
}
il void pushup(int rt){tr[rt]=tr[rt<<1]+tr[rt<<1|1];}
il void update(int k,int c,int l,int r,int rt){
	if(l==k&&r==k){tr[rt]+=c;return;}
	tr[rt]+=c;
	int m=l+r>>1;
	if(k<=m)update(k,c,lson);
	else update(k,c,rson);
	pushup(rt);
}
il int query(int k,int l,int r,int rt){
	if(l==r)return l;
	int m=l+r>>1;
	if(tr[rt<<1]>=k)return query(k,lson);
	else return query(k-tr[rt<<1],rson);
}
int main(){
	n=gi(),m=gi();
	int s=int(sqrt(n));
	for(int i=1;i<=n;i++)nm[i].v=gi(),nm[i].id=i,pos[i]=(i-1)/s+1;
	sort(nm+1,nm+n+1);
	for(int i=1;i<=n;i++)a[nm[i].id]=i;
	for(int i=1;i<=m;i++)q[i].l=gi(),q[i].r=gi(),q[i].k=gi(),q[i].id=i;
	sort(q+1,q+m+1,cmp);
	for(int i=1,l=1,r=0;i<=m;i++){
		while(r<q[i].r)update(a[++r],1,1,n,1);
		while(r>q[i].r)update(a[r--],-1,1,n,1);
		while(l<q[i].l)update(a[l++],-1,1,n,1);
		while(l>q[i].l)update(a[--l],1,1,n,1);
		ans[q[i].id]=nm[query(q[i].k,1,n,1)].v;
	}
	for(int i=1;i<=m;i++)printf("%d\n",ans[i]);
	return 0;
}
```