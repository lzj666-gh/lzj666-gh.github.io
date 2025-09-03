# P2357 题解

题目描述-->[p2357 守墓人](https://www.luogu.org/problemnew/show/P2357)

~~敲了一遍线段树,水过.~~

感谢 [troubler](https://www.luogu.org/space/show?uid=88089) 给了我树状数组AC此题的机会.

~~水题解的机会~~

## 分析

**主要思路：** 

**差分**

**简单介绍一下差分**(详细概念太麻烦,看下面.

	给定一个数组
    7 8 6 5 1 8 18 20 35 //瞎敲的emmm
    7 1 -2 -1 3 10 2  15//对应得到差分数组.
	我们发现从[1,i]求和,得到的就是我们的原数组对应值.(这就是差分.
    

**为什么用差分+树状数组**?

对应差分,我们修改一个位置都会对应影响一段区间.

差分的话,我们修改一个位置就达到了修改后面区间的效果.

而我们修改一个区间,只需要对于左端点增加k,右端点+1位置减去k即可.
	
对应差分操作,区间修改操作,我们可以推导出下面的式子.

![](https://i.loli.net/2018/09/07/5b91eddb3f89f.png)
图片来源-->[@胡小兔](http://www.cnblogs.com/RabbitHu/p/BIT.html)

学习一下(简单了解)就可以了.

所以我们就可以很简单码出来.

**码量小又简单,树状数组你值得拥有**

### 安利一篇[很好的写树状数组的blog](http://www.cnblogs.com/RabbitHu/p/BIT.html)


--------------------代码---------------------

```cpp
/*
目前树状数组解法rank1(吸氧
Timeuse：214ms
Creator：顾z
Date:2018.09.07
*/
#include<bits/stdc++.h>
#define int long long
#define IL inline
#define RI register int
#define lowbit(x) x&-x 
IL void in(int &x){
    int f=1;x=0;char s=getchar();
    while(s>'9'||s<'0'){if(s=='-')f=-1;s=getchar();}
    while(s<='9'&&s>='0'){x=x*10+s-'0';s=getchar();}
    x*=f;
}
int n,m,last,opt,x,y,z,mian;
int sum1[500002],sum2[500002];
IL void add(int pos,int x)
{
	for(RI i=pos;i<=n;i+=lowbit(i))
		sum1[i]+=x,sum2[i]+=pos*x;
}
IL long long query(int pos)
{
	long long res=0;
	for(RI i=pos;i;i-=lowbit(i))
		res+=(pos+1)*sum1[i]-sum2[i];
	return res;
} 
main(void)
{
	in(n),in(m);
	for(RI i=1;i<=n;i++)in(x),add(i,x-last),last=x;
	for(RI i=1,opt;i<=m;i++)
	{
		in(opt);
		switch(opt)
		{
			case 1:in(x),in(y),in(z),add(x,z),add(y+1,-z);break;
			case 2:in(z),mian+=z;break;
			case 3:in(z),mian-=z;break;
			case 4:in(x),in(y);printf("%lld\n",query(y)-query(x-1)+(x==1)*mian);break;
			case 5:printf("%lld\n",query(1)+mian);
		}
	}
}
```


再粘一下**线段树代码** emm↓

```cpp

/*
线段树就跑的有些慢了 emmm(未吸氧
zkw线段树应该会更快一些.
Timeuse：594ms
Creator：顾z
Date:2018.09.03
*/
#include<bits/stdc++.h>
#define int long long
#define IL inline
#define RI register int
#define ls o<<1
#define rs o<<1|1
#define N 1000008
IL void read(int &x){
    int f=1;x=0;char s=getchar();
    while(s>'9'||s<'0'){if(s=='-')f=-1;s=getchar();}
    while(s<='9'&&s>='0'){x=x*10+s-'0';s=getchar();}
    x*=f;
}
int n,f,tr[N],tg[N],mian,c[N];
IL void up(int o){tr[o]=tr[ls]+tr[rs];return;}
IL void build(int o,int l,int r)
{
	if(l==r)
	{
		read(tr[o]);
		return;
	}
	int mid=(l+r)>>1;
	build(ls,l,mid);
	build(rs,mid+1,r);
	up(o);
	return;
}
IL void down(int o,int l,int r)
{
	if(tg[o])
	{
		int mid=(l+r)>>1;
		tg[ls]+=tg[o];tg[rs]+=tg[o];
		tr[ls]+=tg[o]*(mid-l+1);
		tr[rs]+=tg[o]*(r-mid);
		tg[o]=0;	
	}
}
IL int query(int o,int l,int r,int x,int y)
{
	if(x<=l&&y>=r)return tr[o];
	down(o,l,r);
	int res=0;
	int mid=(l+r)>>1;
	if(x<=mid)res+=query(ls,l,mid,x,y);
	if(y>mid)res+=query(rs,mid+1,r,x,y);
	return res;
}
IL void change(int o,int l,int r,int x,int y,int del)
{
	if(x<=l&&y>=r)
	{
		tg[o]+=del;
		tr[o]+=del*(r-l+1);
		return;
	}
	down(o,l,r);
	int mid=(l+r)>>1;
	if(x<=mid)change(ls,l,mid,x,y,del);
	if(y>mid)change(rs,mid+1,r,x,y,del);
	up(o);
	return;
}
signed main()
{
	read(n),read(f);
	build(1,1,n);
	for(RI i=1,opt,x,y,z;i<=f;i++)
	{
		read(opt);
		switch(opt)
		{
			case 1:read(x),read(y),read(z),change(1,1,n,x,y,z);break;
			case 2:read(z),mian+=z;break;
			case 3:read(z),mian-=z;break;
			case 4:read(x),read(y),printf("%lld\n",query(1,1,n,x,y)+(x==1)*mian);break;
			case 5:printf("%lld\n",query(1,1,n,1,1)+mian);break;
		}
	}
}
```
目前**树状数组解法rank1 **