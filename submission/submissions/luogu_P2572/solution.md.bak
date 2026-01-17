# P2572 题解

**更棒的线段树操作，尽在本题解中！**

分析一波题意，显然的区间操作，而且信息都是线段树能维护的。

因为有区间取反操作，所以不仅要记录 $1$ 的信息，$0$ 的信息也要记录。

对于一个点，我们考虑维护 $8$ 个信息：

$1/0$ 的个数，左/右边起 $1/0$ 的最长长度，整段区间中 $1/0$ 的连续最长长度。

只有维护至少 $8$ 个信息才能保证能够合并区间（想想为什么）。

使用结构体存储复杂信息是更好的方法：

```cpp
struct d{
    // 分别表示上述的8个信息
    // w: 1(white) , b: 0(black)
    // l: 左边起 , r: 右边起
    // mw, mb 代表整段区间中1/0的最长长度
    int w,b,lw,lb,rw,rb,mw,mb;
    //构造函数，方便赋值
    d(int w=0,int b=0,int lw=0,int lb=0,int rw=0,int rb=0,int mw=0,int mb=0):
    w(w),b(b),lw(lw),lb(lb),rw(rw),rb(rb),mw(mw),mb(mb){}
};
```

而合并两个子区间，需要考虑很多东西：

$1/0$ 的个数直接相加，左右起的 $1/0$ 要考虑左/右的一整个区间是否是同一个数。

整段区间中的 $1/0$ 最长长度为以下两值的较大值
- 左、右区间的 $1/0$ 最长长度；
- 左边的右端、右边的左端的 $1/0$ 最长长度之和。

由此写出合并两个区间的函数：

```cpp
inline d hb(d i,d j){
	return d(
	i.w+j.w, i.b+j.b,
	(i.b?i.lw:i.w+j.lw), (i.w?i.lb:i.b+j.lb),
	(j.b?j.rw:j.w+i.rw), (j.w?j.rb:j.b+i.rb),
	max(max(i.mw,j.mw),i.rw+j.lw),
	max(max(i.mb,j.mb),i.rb+j.lb));
}
```

这个函数在建树，修改和查询的时候都会用到，我写复杂的线段树都会定义这个函数。

然后是对一个区间整体修改，要注意 $3$ 种修改操作的优先顺序：先赋值后取反：

```cpp
inline void P(int i,int typ){
    // tg1(标记1)是区间赋值,没有标记时为-1,有标记时为0或1
    // tg2(标记2)是区间取反,没有标记时为 0,有标记时为1
    // len表示一个区间的长度,在建树时处理
    d&t=dat[i];
    // 区间赋值为 0
    if(typ==0) tg2[i]= 0, tg1[i]=0, t=d(0,len[i],0,len[i],0,len[i],0,len[i]);
    // 区间赋值为 1
    if(typ==1) tg2[i]= 0, tg1[i]=1, t=d(len[i],0,len[i],0,len[i],0,len[i],0);
    // 区间取反
    if(typ==2) tg2[i]^=1, swap(t.w,t.b), swap(t.lw,t.lb), swap(t.rw,t.rb), swap(t.mw,t.mb);
}
```

这个函数会在修改和标记下传（pushdown）时用到。

接下来是标记下传（pushdown），注意顺序：

```cpp
inline void pd(int i){
    // 对两个子区间修改
    if(~tg1[i]) P(i<<1,tg1[i]), P(i<<1|1,tg1[i]);
    if(tg2[i]) P(i<<1,2), P(i<<1|1,2);
    // 把标记清空
    tg1[i]=-1, tg2[i]=0;
}
```

最后是建树，修改和查询函数，有了上面的，这就很简单了：

```cpp
void build(int i,int l,int r){
    len[i]=r-l+1; tg1[i]=-1;
    if(l==r) {int t=a[l]; dat[i]=d(t,t^1,t,t^1,t,t^1,t,t^1); return;}
    build(i<<1,l,l+r>>1);
    build(i<<1|1,(l+r>>1)+1,r);
    dat[i]=hb(dat[i<<1],dat[i<<1|1]);
}
void Mdf(int i,int l,int r,int a,int b,int t){
    // 如果区间没有交集 或者 当前区间完全包含在修改区间内的情况
    if(b<l||r<a) return; if(a<=l&&r<=b) {P(i,t); return;}
    pd(i); Mdf(i<<1,l,l+r>>1,a,b,t), Mdf(i<<1|1,(l+r>>1)+1,r,a,b,t);
    dat[i]=hb(dat[i<<1],dat[i<<1|1]);
}
d Qur(int i,int l,int r,int a,int b){
    // 如果区间没有交集 或者 当前区间完全包含在查询区间内的情况
    if(b<l||r<a) return d(); if(a<=l&&r<=b) return dat[i];
    pd(i); return hb(Qur(i<<1,l,l+r>>1,a,b),Qur(i<<1|1,(l+r>>1)+1,r,a,b));
}
```

下面是完整代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,q,a[100001];
struct d{
	int w,b,lw,lb,rw,rb,mw,mb;
	d(int w=0,int b=0,int lw=0,int lb=0,int rw=0,int rb=0,int mw=0,int mb=0):
    w(w),b(b),lw(lw),lb(lb),rw(rw),rb(rb),mw(mw),mb(mb){}
};
inline d hb(d i,d j){
	return d(
	i.w+j.w, i.b+j.b,
	(i.b?i.lw:i.w+j.lw), (i.w?i.lb:i.b+j.lb),
	(j.b?j.rw:j.w+i.rw), (j.w?j.rb:j.b+i.rb),
	max(max(i.mw,j.mw),i.rw+j.lw),
	max(max(i.mb,j.mb),i.rb+j.lb));
}
d dat[262144]; int len[262144],tg1[262144],tg2[262144];
inline void P(int i,int typ){
	d&t=dat[i];
	if(typ==0) tg2[i]= 0, tg1[i]=0, t=d(0,len[i],0,len[i],0,len[i],0,len[i]);
	if(typ==1) tg2[i]= 0, tg1[i]=1, t=d(len[i],0,len[i],0,len[i],0,len[i],0);
	if(typ==2) tg2[i]^=1, swap(t.w,t.b), swap(t.lw,t.lb), swap(t.rw,t.rb), swap(t.mw,t.mb);
}
inline void pd(int i){
	if(~tg1[i]) P(i<<1,tg1[i]), P(i<<1|1,tg1[i]);
	if(tg2[i]) P(i<<1,2), P(i<<1|1,2);
	tg1[i]=-1, tg2[i]=0;
}
void build(int i,int l,int r){
	len[i]=r-l+1; tg1[i]=-1;
	if(l==r) {int t=a[l]; dat[i]=d(t,t^1,t,t^1,t,t^1,t,t^1); return;}
	build(i<<1,l,l+r>>1);
	build(i<<1|1,(l+r>>1)+1,r);
	dat[i]=hb(dat[i<<1],dat[i<<1|1]);
}
void Mdf(int i,int l,int r,int a,int b,int t){
	if(b<l||r<a) return; if(a<=l&&r<=b) {P(i,t); return;}
	pd(i); Mdf(i<<1,l,l+r>>1,a,b,t), Mdf(i<<1|1,(l+r>>1)+1,r,a,b,t);
	dat[i]=hb(dat[i<<1],dat[i<<1|1]);
}
d Qur(int i,int l,int r,int a,int b){
	if(b<l||r<a) return d(); if(a<=l&&r<=b) return dat[i];
	pd(i); return hb(Qur(i<<1,l,l+r>>1,a,b),Qur(i<<1|1,(l+r>>1)+1,r,a,b));
}
int main(){
	scanf("%d%d",&n,&q);
	for(int i=1;i<=n;++i) scanf("%d",a+i);
	build(1,1,n);
	for(int i=1;i<=q;++i){
		int opt,l,r;
		scanf("%d%d%d",&opt,&l,&r); ++l, ++r;
		if(opt<3) Mdf(1,1,n,l,r,opt);
		else {d t=Qur(1,1,n,l,r); printf("%d\n",opt==3?t.w:t.mw);}
	}
	return 0;
}
```

以上就是我打较复杂线段树操作时的模板，大家可以借鉴一下，形成自己的风格。