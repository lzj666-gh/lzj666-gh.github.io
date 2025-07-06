# P1138 题解

# 貌似没有用主席树的，我就来一发主席树题解
看见楼下有用线段树的，其实主席树就是可持久的线段树
普通的线段树是对1到n的区间建树，而主席树是在1到n的区间中只插入某个前缀中的值，由于区间和具有可减性所以主席树用来解决区间第k小的问题

~~一开始看见题目直接就打了一个主席树板子~~

首先树中的节点信息需要记录此区间数的数量，然后是两个儿子节点

```cpp
struct pt{
	int sum;
	pt* ch[2];
};
```
然后建树过程因为如果每个前缀都建一棵树，那么每棵树都是O(n)的空间，总空间为$O(n^2)$彻底变为炸同学

我们发现由于每次增加一个数最多会变$O(logn)$个节点
所以我们可以利用当前树和前一个树的公共区间来建树
总空间$O(nlogn)$

```cpp
typedef pt* ptr;
ptr root[maxn];
int n,k;
void add(ptr last,ptr& th,int v,int l=1,int r=n){
	th=new pt;
	*th=*last;
	th->sum=last->sum+1;
	if(l==r)return ;
	int mid=l+r>>1;
	if(v<=mid)add(last->ch[0],th->ch[0],v,l,mid);
	else add(last->ch[1],th->ch[1],v,mid+1,r);
}
```

建树过程也完了，然后是查询，和楼下线段树dalao一样只不过区间$[l,r]$的节点是$root[r]-root[l-1]$（因为root都是前缀）
所以查询的代码也很好写
```cpp
int getid(ptr le,ptr re,int k,int l=1,int r=n){
	if(l==r)return l;
	int tmp=re->ch[0]->sum-le->ch[0]->sum;
	int mid=l+r>>1;
	if(k<=tmp)return getid(le->ch[0],re->ch[0],k,l,mid);
	else return getid(le->ch[1],re->ch[1],k-tmp,mid+1,r);
}
```
然后就是离散化和去重等等

完整代码：
```cpp
#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
const int maxn=1e5+5;
struct pt{
	int sum;
	pt* ch[2];
};
typedef pt* ptr;
ptr root[maxn];
int n,k;
void add(ptr last,ptr& th,int v,int l=1,int r=n){
	th=new pt;
	*th=*last;
	th->sum=last->sum+1;
	if(l==r)return ;
	int mid=l+r>>1;
	if(v<=mid)add(last->ch[0],th->ch[0],v,l,mid);
	else add(last->ch[1],th->ch[1],v,mid+1,r);
}
int getid(ptr le,ptr re,int k,int l=1,int r=n){
	if(l==r)return l;
	int tmp=re->ch[0]->sum-le->ch[0]->sum;
	int mid=l+r>>1;
	if(k<=tmp)return getid(le->ch[0],re->ch[0],k,l,mid);
	else return getid(le->ch[1],re->ch[1],k-tmp,mid+1,r);
}
int a[maxn];
int main(){
	ptr& null=root[0];
	null=new pt;
	null->ch[0]=null->ch[1]=null;null->sum=0;
	cin>>n>>k;
	for(int i=1;i<=n;++i){
		cin>>a[i];
	}
	sort(a+1,a+1+n);
	n=unique(a+1,a+1+n)-a-1;
	if(k>n){
		cout<<"NO RESULT"<<endl;
		return 0;
	}
	for(int i=1;i<=n;++i){
		add(root[i-1],root[i],i);
	}
	cout<<a[getid(root[0],root[n],k)]<<endl;
	return 0;
}
```
让我们一起%dalao @[ghj1222](https://www.luogu.org/space/show?uid=13091)