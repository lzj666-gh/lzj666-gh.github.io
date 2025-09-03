# P3870 题解


大佬们的变量看起来都好冗杂，还一直说简单，说真的对于蒟蒻来说，这个题真的不算简单，本蒟蒻看着题解，苦苦钻研3个小时，才AC。

下面让我站在蒟蒻的角度讲解一下这道所谓的“板子”题。

很多人说这很简单看出来是线段树，那么简单是指什么呢？

我们说，**一般题目涉及到区间修改以及区间查询**的一般采用分块和线段树的思想，希望大家可以铭记。


------------
下面开始本题讲解。

这道题的整体思路就是用某一区间的长度减去这个区间的亮灯数目就是这个区间在一次修改中所需要打开灯的数目，那么打开灯的数目变了，自然会带动这个区间sum的改变，因此我们需要维护父亲和儿子的sum值。

简单的说tag函数主要是维护儿子的sum值，至于他们的懒标记我之后会在代码里具体解释。


**懒标记在此题中主要指这个区间是否需要更改**这是本题重点但恰恰个个题解巧妙的避过了这个问题。

题目中函数中的return是本题所用的最少的return，不能删一个，至于原因可以自己思考。

话不多说看代码。

```c
#include<bits/stdc++.h>
using namespace std;
const int maxn=1000001;
int ans,n,m,a,b,c;
struct tree
{
	int l,r,sum,add;
}t[maxn];
inline void build(int u,int x,int y)
{
    t[u].l=x;
	t[u].r=y;
	if(x==y)
	{
		t[u].sum=0;//题目说每个灯都是关着的。
		return ;
	}
	int mid=(x+y)>>1;
	build(u*2,x,mid);build(u*2+1,mid+1,y);
}//建树不需要过多解释吧？
inline void tag(int u)
{
	if(t[u].add==0)return;//如果这个父亲不需要更改还需要儿子什么事情呢？
    //如果看不懂这句的话，一定要耐心往下看。
	t[u*2].sum=t[u*2].r-t[u*2].l+1-t[u*2].sum;
	t[u*2+1].sum=t[u*2+1].r-t[u*2+1].l+1-t[u*2+1].sum;//维护儿子的sum值。
	if(t[u*2].add==0)//如果左儿子没有懒标记的话
	t[u*2].add=1;//那么他现在有了懒标记，
    //也就是它现在需要修改区间内的值了。
	else t[u*2].add=0;//如果有懒标记的话，那么它现在不用动了
    //因为这个做儿子连着被修改了两次，
    //根据题意这个区间内的灯被开了一次，又被关了一次，
    //是不是相当于最初的形态？
	if(t[u*2+1].add==0)
	t[u*2+1].add=1;
	else t[u*2+1].add=0;//这个是处理右儿子的，解释同上。
	t[u].add=0;//注意进行这部的时候
    //左右儿子的父亲已经被修改过了
    //所以父亲的懒标记要归0，也就是说父亲现在不需要更改。
}
inline void change(int u,int l,int r)
{
	if(l<=t[u].l&&t[u].r<=r)
	{
		t[u].sum=t[u].r-t[u].l+1-t[u].sum;
		if(t[u].add==0)
		t[u].add=1;
		else 
		t[u].add=0;
		return ;//这个地方跟上面解释相同。
	}
	tag(u);
    //此时，区间没有覆盖父亲，那么检查一下这个父亲用改不用
    //如果父亲用改的话，那么由于我们之后需要用到它的儿子
    //并且我们要改的区间没有覆盖父亲，所以现在要修改儿子了。
	int mid=(t[u].l+t[u].r)>>1;
	if(a<=mid)change(u*2,l,r);
	if(b>mid)change(u*2+1,l,r);
    //此处一定是a<=mid,b>mid这个仔细想想吧。
	t[u].sum=t[u*2].sum+t[u*2+1].sum;
}
inline int ask(int u,int l,int r)
{
	if(l<=t[u].l&&r>=t[u].r)return t[u].sum;
	tag(u);
	int mid=(t[u].l+t[u].r)/2;
	int ans=0;
	if(a<=mid)ans+=ask(u*2,l,r);
	if(b>mid)ans+=ask(u*2+1,l,r);
	return ans;
}//这个地方是板子。
int main()
{
	cin>>n>>m;
	build(1,1,n);
	for(int i=1;i<=m;i++)
	{
		cin>>c>>a>>b;
		if(c==0)
		change(1,a,b);
		else
		cout<<ask(1,a,b)<<endl;
	}
	return 0;
}//完美结束。
```
希望本篇题解可以对大家有帮助！
祝大家ak noip

希望管理哥哥通过。
