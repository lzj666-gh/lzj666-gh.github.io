# P3690 题解

博客太长啦！于是将重要的部分留在题解中，LCT的概念、三个基本性质等更多内容可以参考[我的博客LCT总结](http://www.cnblogs.com/flashhu/p/8324551.html)

## $access(x)$
LCT核心操作，也是最难理解的操作。其它所有的操作都是在此基础上完成的。

因为性质3，我们不能总是保证两个点之间的路径是直接连通的（在一个Splay上）。

access即定义为打通根节点到指定节点的实链，使得一条中序遍历以根开始、以指定点结束的Splay出现。

~~蒟蒻深知没图的痛苦qwq~~

所以还是来几张图吧。

下面的图片参考[YangZhe的论文](https://wenku.baidu.com/view/75906f160b4e767f5acfcedb)

有一棵树，假设一开始实边和虚边是这样划分的（虚线为虚边）

![](http://images2017.cnblogs.com/blog/1309909/201801/1309909-20180123095924037-1618037447.png)

那么所构成的LCT可能会长这样（绿框中为一个Splay，可能不会长这样，但只要满足中序遍历按深度递增（性质1）就对结果无影响）

![](http://images2017.cnblogs.com/blog/1309909/201801/1309909-20180123095955350-1680422636.png)

现在我们要$access(N)$，把$A-N$的路径拉起来变成一条Splay。

因为性质2，该路径上其它链都要给这条链让路，也就是把每个点到该路径以外的实边变虚。

所以我们希望虚实边重新划分成这样。

![](http://images2017.cnblogs.com/blog/1309909/201801/1309909-20180123101901740-2118178734.png)

然后怎么实现呢？

我们要一步步往上拉。

首先把$splay(N)$，使之成为当前Splay中的根。

为了满足性质2，原来$N-O$的重边要变轻。

因为按深度$O$在$N$的下面，在Splay中$O$在$N$的右子树中，所以直接单方面将$N$的右儿子置为$0$（认父不认子）

然后就变成了这样——

![](http://images2017.cnblogs.com/blog/1309909/201801/1309909-20180123110136115-1112016464.png)

我们接着把$N$所属Splay的虚边指向的$I$（在原树上是$L$的父亲）也转到它所属Splay的根，$splay(I)$。

原来在$I$下方的重边$I-K$要变轻（同样是将右儿子去掉）。

这时候$I-L$就可以变重了。因为$L$肯定是在$I$下方的（刚才$L$所属Splay指向了$I$），所以I的右儿子置为$N$，满足性质1。

然后就变成了这样——

![](http://images2017.cnblogs.com/blog/1309909/201801/1309909-20180123110156272-1242463729.png)

$I$指向$H$，接着$splay(H)$，$H$的右儿子置为$I$。

![](http://images2017.cnblogs.com/blog/1309909/201801/1309909-20180123110209772-2057141058.png)

$H$指向$A$，接着$splay(A)$，$A$的右儿子置为$H$。

![](http://images2017.cnblogs.com/blog/1309909/201801/1309909-20180123110213709-49169640.png)

$A-N$的路径已经在一个Splay中了，大功告成！

代码其实很简单。。。。。。循环处理，只有四步——
1. 转到根；
2. 换儿子；
3. 更新信息；
4. 当前操作点切换为轻边所指的父亲，转1

```cpp
inline void access(int x){
	for(int y=0;x;y=x,x=f[x])
		splay(x),c[x][1]=y,pushup(x);//儿子变了，需要及时上传信息
}
```
## $makeroot(x)$
只是把根到某个节点的路径拉起来并不能满足我们的需要。更多时候，我们要获取指定两个节点之间的路径信息。

然而一定会出现路径不能满足按深度严格递增的要求的情况。根据性质1，这样的路径不能在一个Splay中。

Then what can we do?

$makeroot$定义为换根，让指定点成为原树的根。

这时候就利用到$access(x)$和Splay的翻转操作。

$access(x)$后$x$在Splay中一定是深度最大的点对吧。

$splay(x)$后，$x$在Splay中将没有右子树（性质1）。于是翻转整个Splay，使得所有点的深度都倒过来了，$x$没了左子树，反倒成了深度最小的点（根节点），达到了我们的目的。

代码
```cpp
inline void pushr(int x){//Splay区间翻转操作
    swap(c[x][0],c[x][1]);
    r[x]^=1;//r为区间翻转懒标记数组
}
inline void makeroot(int x){
    access(x);splay(x);
    pushr(x);
}
```
关于pushdown和makeroot的一个相关的小问题详见下方update（关于pushdown的说明）

## $findroot(x)$
找$x$所在原树的树根，主要用来判断两点之间的连通性（findroot(x)==findroot(y)表明$x,y$在同一棵树中）

代码：
```cpp
inline int findroot(R x){
    access(x); splay(x);
    while(c[x][0])pushdown(x),x=c[x][0];
//如要获得正确的原树树根，一定pushdown！详见下方update（关于findroot中pushdown的说明）
    splay(x);//保证复杂度
    return x;
}
```
同样利用性质1，不停找左儿子，因为其深度一定比当前点深度小。

## $split(x,y)$

神奇的$makeroot$已经出现，我们终于可以访问指定的一条在原树中的链啦！

split(x,y)定义为拉出$x-y$的路径成为一个Splay（本蒟蒻以$y$作为该Splay的根）

代码
```cpp
inline void split(int x,int y){
    makeroot(x);
    access(y);splay(y);
}
```
x成为了根，那么x到y的路径就可以用$access(y)$直接拉出来了，将y转到Splay根后，我们就可以直接通过访问$y$来获取该路径的有关信息

## $link(x,y)$

连一条$x-y$的边（本蒟蒻使$x$的父亲指向$y$，连一条轻边）

代码
```cpp
inline bool link(int x,int y){
    makeroot(x);
    if(findroot(y)==x)return 0;//两点已经在同一子树中，再连边不合法
    f[x]=y;
    return 1;
}
```
如果题目保证连边合法，代码就可以更简单
```cpp
inline void link(int x,int y){
    makeroot(x);
    f[x]=y;
}
```
## $cut(x,y)$

将$x-y$的边断开。

如果题目保证断边合法，倒是很方便。

使$x$为根后，$y$的父亲一定指向$x$，深度相差一定是$1$。当$access(y),splay(y)$以后，$x$一定是$y$的左儿子，直接双向断开连接
```cpp
inline void cut(int x,int y){
    split(x,y);
    f[x]=c[y][0]=0;
    pushup(y);//少了个儿子，也要上传一下
}
```
那如果不一定存在该边呢？

充分利用好Splay和LCT的各种基本性质吧！

正确姿势——先判一下连通性（注意$findroot(y)$以后$x$成了根），再看看$x,y$是否有父子关系，还要看$y$是否有左儿子。

因为$access(y)$以后，假如y与x在同一Splay中而没有直接连边，那么这条路径上就一定会有其它点，在中序遍历序列中的位置会介于$x$与$y$之间。

那么可能$y$的父亲就不是$x$了。

也可能$y$的父亲还是$x$，那么其它的点就在$y$的左子树中

```cpp
inline bool cut(int x,int y){
	makeroot(x);
	if(findroot(y)!=x||f[y]!=x||c[y][0])return 0;
	f[y]=c[x][1]=0;//x在findroot(y)后被转到了根
	pushup(x);
	return 1;
}
```
如果维护了$size$，还可以换一种判断
```cpp
inline bool cut(int x,int y){
    makeroot(x);
    if(findroot(y)!=x||sz[x]>2)return 0;
    f[y]=c[x][1]=0;
    pushup(x);
    return 1;
}
```
解释一下，如果他们有直接连边的话，$access(y)$以后，为了满足性质1，该Splay只会剩下$x,y$两个点了。

反过来说，如果有其它的点，$size$不就大于$2$了么？

 ---

其实，还有一些LCT中的Splay的操作，跟我们以往学习的纯Splay的某些操作细节不甚相同。

包括$splay(x),rotate(x),nroot(x)$（看到许多版本LCT写的是$isroot(x)$，但我觉得反过来会方便些）

这些区别之处详见下面的模板题注释。

### update（关于findroot中pushdown的说明）
蒟蒻真的一时没注意这个问题。。。。。。Splay根本没学好

找根的时候，当然不能保证Splay中到根的路径上的翻转标记全放掉。

所以最好把pushdown写上。

[Candy巨佬的总结](https://www.cnblogs.com/candy99/p/6271344.html)对pushdown问题有详细的分析

只不过蒟蒻后来经常习惯这样判连通性（~~我也不知道怎么养成的~~）
```cpp
makeroot(x);
if(findroot(y)==x)//后续省略
```
这样好像没出过问题，那应该可以证明是没问题的（makeroot保证了x在LCT的顶端，access(y)+splay(y)以后，假如x,y在一个Splay里，那x到y的路径一定全部放完了标记）

导致很久没有发现错误。。。。。。

另外提一下，假如LCT题目在维护连通性的情况中只可能出现合并而不会出现分离的话，其实可以用并查集哦！（实践证明findroot很慢）

这样的例子有不少，比如“维护链上的边权信息”部分的两道题都是的。

甚至听到Julao们说有少量题目还专门卡这个常数。。。。。。[XZY巨佬的博客](https://www.zybuluo.com/xzyxzy/note/1027479)就提到了

### update（关于pushdown的说明）
我pushdown和makeroot有时候会这样写，常数小一点
```cpp
void pushdown(int x){
    if(r[x]){
        r[x]=0;
        int t=c[x][0];
        r[c[x][0]=c[x][1]]^=1;
        r[c[x][1]=t]^=1;
    }
}
void makeroot(int x){
    access(x);splay(x);
    r[x]^=1;
}
```
这种写法等于说当x有懒标记时，x的左右儿子还是反的

~~那么如果findroot里实在要写pushdown，那么这种pushdown就会出现问题~~（参考cnblogs评论区@ zjp_shadow巨佬的指正）

**再次update，蒟蒻发现这种问题还是可以避免的，若用这种pushdown，findroot可以写，这样写就好啦**

```cpp
inline int findroot(int x){
    access(x);splay(x);
    pushdown(x);
    while(lc)pushdown(x=lc);
    splay(x);
    return x;
}
```
所以此总结以及下面模板里的pushdown，常数大了一点点，却是更稳妥、严谨的写法
```cpp
//pushr同上方makeroot部分
void pushdown(int x){
    if(r[x]){
        if(c[x][0])pushr(c[x][0]);//copy自模板，然后发现if可以不写
        if(c[x][1])pushr(c[x][1]);
        r[x]=0;
    }
}
void makeroot(int x){
    access(x);splay(x);
    pushr(x);//可以看到两种写法造成makeroot都是不一样的
}
```
这种写法等于说当x有懒标记时，x的左右儿子已经放到正确的位置了，只是儿子的儿子还是反的

那么这样就不会出问题啦

两种写法差别还确实有点大呢

当题目中维护的信息与左右儿子顺序有关的时候，pushdown如果用这种不严谨写法会是错的

比如[NOI2005]维护数列（这是Splay题）和洛谷P3613 睡觉困难综合征

## 代码
最基本的LCT操作都在这里，也没有更多额外的复杂操作了，确实很模板。
```cpp
#include<bits/stdc++.h>
#define R register int
#define I inline void
#define G if(++ip==ie)if(fread(ip=buf,1,SZ,stdin))
#define lc c[x][0]
#define rc c[x][1]
using namespace std;
const int SZ=1<<19,N=3e5+9;
char buf[SZ],*ie=buf+SZ,*ip=ie-1;
inline int in(){
	G;while(*ip<'-')G;
	R x=*ip&15;G;
	while(*ip>'-'){x*=10;x+=*ip&15;G;}
	return x;
}
int f[N],c[N][2],v[N],s[N],st[N];
bool r[N];
inline bool nroot(R x){//判断节点是否为一个Splay的根（与普通Splay的区别1）
	return c[f[x]][0]==x||c[f[x]][1]==x;
}//原理很简单，如果连的是轻边，他的父亲的儿子里没有它
I pushup(R x){//上传信息
	s[x]=s[lc]^s[rc]^v[x];
}
I pushr(R x){R t=lc;lc=rc;rc=t;r[x]^=1;}//翻转操作
I pushdown(R x){//判断并释放懒标记
	if(r[x]){
		if(lc)pushr(lc);
		if(rc)pushr(rc);
		r[x]=0;
	}
}
I rotate(R x){//一次旋转
	R y=f[x],z=f[y],k=c[y][1]==x,w=c[x][!k];
	if(nroot(y))c[z][c[z][1]==y]=x;c[x][!k]=y;c[y][k]=w;//额外注意if(nroot(y))语句，此处不判断会引起致命错误（与普通Splay的区别2）
	if(w)f[w]=y;f[y]=x;f[x]=z;
	pushup(y);
}
I splay(R x){//只传了一个参数，因为所有操作的目标都是该Splay的根（与普通Splay的区别3）
	R y=x,z=0;
	st[++z]=y;//st为栈，暂存当前点到根的整条路径，pushdown时一定要从上往下放标记（与普通Splay的区别4）
	while(nroot(y))st[++z]=y=f[y];
	while(z)pushdown(st[z--]);
	while(nroot(x)){
		y=f[x];z=f[y];
		if(nroot(y))
			rotate((c[y][0]==x)^(c[z][0]==y)?x:y);
		rotate(x);
	}
	pushup(x);
}
/*当然了，其实利用函数堆栈也很方便，代替上面的手工栈，就像这样
I pushall(R x){
	if(nroot(x))pushall(f[x]);
	pushdown(x);
}*/
I access(R x){//访问
	for(R y=0;x;x=f[y=x])
		splay(x),rc=y,pushup(x);
}
I makeroot(R x){//换根
	access(x);splay(x);
	pushr(x);
}
int findroot(R x){//找根（在真实的树中的）
	access(x);splay(x);
	while(lc)pushdown(x),x=lc;
	splay(x);
	return x;
}
I split(R x,R y){//提取路径
	makeroot(x);
	access(y);splay(y);
}
I link(R x,R y){//连边
	makeroot(x);
	if(findroot(y)!=x)f[x]=y;
}
I cut(R x,R y){//断边
	makeroot(x);
	if(findroot(y)==x&&f[y]==x&&!c[y][0]){
		f[y]=c[x][1]=0;
		pushup(x);
	}
}
int main()
{
	R n=in(),m=in();
	for(R i=1;i<=n;++i)v[i]=in();
	while(m--){
		R type=in(),x=in(),y=in();
		switch(type){
		case 0:split(x,y);printf("%d\n",s[y]);break;
		case 1:link(x,y);break;
		case 2:cut(x,y);break;
		case 3:splay(x);v[x]=y;//先把x转上去再改，不然会影响Splay信息的正确性
		}
	}
	return 0;
}
```