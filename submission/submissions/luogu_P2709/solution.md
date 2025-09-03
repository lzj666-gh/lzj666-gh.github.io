# P2709 题解

upd on 2023.4.19：修缮 $\LaTeX$，同时补充了复杂度证明。

**多次区间查询、不强制在线、$O(n\sqrt{n})$ 能过**。

很显然：这就是**莫队**。以下视 $n,m$ 同阶。

## 一.什么是莫队

莫队其实就是一种优雅的暴力，它十分~~玄学~~巧妙地将**分块和暴力**结合在了一起，主要用来处理**离线区间查询**等问题。

由于莫队算法是由莫涛队长提出的，因此我们称这种算法为莫队。

## 二.莫队的思想

其实很简单：**通过挪动区间的方式按某种顺序离线处理区间查询操作**。

有三个关键词：挪动区间、按某种顺序、离线处理。

### 1.挪动区间

比如说第一次查询的区间是 $[1,3]$，第二次查询的区间是 $[4,6]$。

那我们直接把 $1$ 挪成 $4$，$3$ 挪成 $6$，然后在挪动的过程中修改我们的答案。

写成代码就是这样：

```cpp
//ans1是上一次查询的左端点，ans2是上一次查询的右端点
//lef是当前查询的左端点，rig是当前查询的右端点
while(ans1>lef) ans1--,add(a[ans1]);//add是扩展函数
while(ans2<rig) ans2++,add(a[ans2]);
while(ans1<lef) del(a[ans1]),ans1++;//del是删除函数
while(ans2>rig) del(a[ans2]),ans2--;
```

add 函数和 del 函数：

```cpp
//b是桶，统计每个数出现次数
inline void add(int x){
	c+=2*b[x]+1;
    //b[x]+1对于平方和c的影响（小学数学）
	b[x]++;
}
inline void del(int x){
	c-=2*b[x]-1;//同上
	b[x]--;
}
```

### 2.按某种顺序

最严格的顺序应该是把每次区间求一个曼哈顿距离最小生成树。

但完全没必要（~~毕竟暴力~~）。

这时候分块就派上了用场~

把 $[1,n]$ 均匀分成 $\sqrt{n}$ 块。

我们**先把这些区间按照左端点 $l$ 所在的块从左往右排序**。

**再把 $l$ 所在块相同的区间按 $r$ 从小到大排序**。

可以证明用这种方法最终挪动次数是 $O(n\sqrt n)$ 级别，而且是此类问题下能做到的最优量级，证明详见 [link](https://www.luogu.com.cn/blog/wyxawa/post-xue-xi-bi-ji-mu-dui-jin-jie)。

当然还有其它方式，但这样简单啊（逃）。

于是就有了这样的代码：

```cpp
int block=sqrt(n);
inline bool cmp(node x,node y){
	if((x.l-1)/block==(y.l-1)/block) return x.r<y.r;
	return x.l/block<y.l/block;
}
……
sort(modui+1,modui+1+m,cmp);//modui就是莫队
```

### 3.离线处理

由于莫队是先把询问的区间存储起来再统一处理，当然是离线算法 qwq。

最后把每次询问对应的答案用数组存储起来就好啦。


------------

## 三.莫队的实现

用一个结构体数组存储查询的区间以及下标。

再开一个数组记录答案，一个桶，当然还有原数组（~~废话~~）。

在转移时还要维护答案（~~不然你怎么记录~~）。

```cpp
long long ans[maxn];//ans记录答案
int a[maxn],b[maxn];//a是原数组，b是桶
struct node{
	int l,r,id;//l是左端点，r是右端点，id是下标
}modui[maxn];
```


------------

OK，这就是普通莫队。

话不多说，直接放代码：

```cpp
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#define maxn 50001
#define ll long long
#define fo(x,y) for(register int i=x;i<=y;++i)
using namespace std;
ll ans[maxn],c; //注意longlong哦
int a[maxn],b[maxn],n,m,k,block;
struct node{
	int l,r,id;
}modui[maxn];

inline bool cmp(node x,node y){//上文有解释
	if((x.l-1)/block==(y.l-1)/block) return x.r<y.r;
	return x.l/block<y.l/block;
}

inline int read(){//快读，不多说
	int x=0,fh=1;
	char ch=getchar();
	while(!isdigit(ch)){
		if(ch=='-') fh=-1;
		ch=getchar();
	}
	while(isdigit(ch)){
		x=(x<<1)+(x<<3)+ch-'0';
		ch=getchar();
	}
	return x*fh;
}
inline void add(int x){//上文都解释过了
	c+=2*b[x]+1;//维护答案
	b[x]++;
}
inline void del(int x){
	c-=2*b[x]-1;//维护答案
	b[x]--;
}
int main(){
	int lef,rig,ans1=1,ans2=0;
    //ans1:上次的左端点 ans2:上次的右端点 
	n=read(),m=read(),k=read();
	block=sqrt(n);
	fo(1,n){
		a[i]=read();
	}
	fo(1,m){
		modui[i].l=read();
		modui[i].r=read();
		modui[i].id=i;
	}
	sort(modui+1,modui+1+m,cmp);
	fo(1,m){
		lef=modui[i].l,rig=modui[i].r;
        //挪动操作：
		while(ans1>lef) ans1--,add(a[ans1]);
		while(ans2<rig) ans2++,add(a[ans2]);
		while(ans1<lef) del(a[ans1]),ans1++;
		while(ans2>rig) del(a[ans2]),ans2--;
		ans[modui[i].id]=c;//存储答案
	}
	fo(1,m) printf("%lld\n",ans[i]);
	return 0;
}

```

点个赞再走吧 qwq。