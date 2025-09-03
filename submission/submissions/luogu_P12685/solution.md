# P12685 题解

动态逆序对问题。

逆序对相关问题，考虑交换两个数只会对两个数之间的逆序对产生影响。

分别求出交换前后这两个数在区间内的逆序对数，进而求出答案变化量。

一个数在区间内的逆序对数本质上就是区间内有多少数大于或小于这个数。这是一个典型的树套树问题，用树套树维护答案的变化量即可。

**注意**

1. 序列一开始就存在逆序对。
2. 特殊考虑交换的两个数之间的贡献。
3. 选用常数较小的写法。
4. 答案可达到 $n^2$ 级别，记得开 ```long long``` 。

代码采用了树状数组套权值线段树（带修主席树）维护操作。

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,m,len;
int lowbit(int x){return x&-x;}
int cntl,cntr;
struct SEG{
	int cnt=0,L[(int)5e6],R[(int)5e6];
	int siz[(int)5e7],ls[(int)5e7],rs[(int)5e7];
	void add(int &i,int l,int r,int x,int k){
		if(!i)i=++cnt;siz[i]+=k;
		if(l==r)return ;
		int mid=(l+r)>>1;
		if(x<=mid)add(ls[i],l,mid,x,k);
		else add(rs[i],mid+1,r,x,k);
	}
	int get_rk(int l,int r,int k,int opt){
		int s=0;
		if(l==r){
			for(int i=1;i<=cntl;i++)s-=siz[L[i]];for(int i=1;i<=cntr;i++)s+=siz[R[i]];
			return s*opt;
		}
		int mid=(l+r)>>1;
		for(int i=1;i<=cntl;i++)s-=siz[ls[L[i]]];for(int i=1;i<=cntr;i++)s+=siz[ls[R[i]]];
		if(k<=mid){
			for(int i=1;i<=cntl;i++)L[i]=ls[L[i]];for(int i=1;i<=cntr;i++)R[i]=ls[R[i]];
			return get_rk(l,mid,k,opt);
		}
		else {
			for(int i=1;i<=cntl;i++)L[i]=rs[L[i]];for(int i=1;i<=cntr;i++)R[i]=rs[R[i]];
			return get_rk(mid+1,r,k,opt)+s;
		}
	}
}T;
struct BIT{
	int rt[(int)5e6];
	void add(int i,int x,int k){for(;i<=n;i+=lowbit(i)){T.add(rt[i],1,len,x,k);}}
	int get(int x,int y,int k,int opt){
		cntl=cntr=0;
		for(int i=x-1;i;i-=lowbit(i))T.L[++cntl]=rt[i];
		for(int i=y;i;i-=lowbit(i))T.R[++cntr]=rt[i];
		return T.get_rk(1,len,k,opt);
	}
}t;
int a[(int)5e6],v[(int)5e6],b[(int)5e6];
long long ans;
signed main(){
	ios::sync_with_stdio(0);
	cin.tie(0),cout.tie(0);
	cin>>n;
	for(int i=1;i<=n;i++){cin>>a[i];b[i]=a[i];v[i]=1;}
	sort(b+1,b+n+1);len=unique(b+1,b+n+1)-b-1;
	for(int i=1;i<=n;i++){
		a[i]=lower_bound(b+1,b+len+1,a[i])-b;
		t.add(i,a[i],v[i]);
	}
	for(int i=1;i<=n;i++)ans+=t.get(i,n,a[i],0);
	cout<<ans<<'\n';
	cin>>m;
	for(int i=1;i<=m;i++){
		int x,y;
		cin>>x>>y;
		if(x>y)swap(x,y);
		int num=y-x+1,ax=a[x],ay=a[y],vx=v[x],vy=v[y];
		if(a[y]<a[x])ans++;else if(a[x]<a[y]) ans--;
		int old=t.get(x,y,a[x],0)+num-t.get(x,y,a[y],1);
		t.add(x,ax,-vx),t.add(x,ay,vy);
		t.add(y,ay,-vy),t.add(y,ax,vx);
		swap(a[x],a[y]),swap(v[x],v[y]);
		int nw=t.get(x,y,a[x],0)+num-t.get(x,y,a[y],1);
		ans=ans+nw-old;
		cout<<ans<<'\n';
	}
	return 0;
}
```