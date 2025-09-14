# P4087 题解

    一道对萌新非常友好的线段树，简明易懂，虽然用不到lazy tag,但可以丰富线段树的用法
    
#### 首先，我们简化一波题意：
   维护一个区间的最大值，有n个修改操作，记录最大值的变化情况（即更换照片）。
   
   ps:“变化”の意义：rank1的牛不同了（多了/少了/牛变了）
   
   ~~pps：FJ真无聊，竞争使牛透支~~
   
   
   显然，我们可以用线段树来维护这个量
   
   但是，我们要输出的是变化的次数，所以肯定要判定“变化”
   
### 分类讨论：
	由于一次只修改一个值，所以可以直接如下分类
	
##### 1.rk1产奶量变化了（原来的rk1不一定rk1了）
	   （1：rk1还是那头牛（不是变化）
       （2：rk1不是那头牛（显然要换照片！）
       （3：rk1数量变多（rk1掉分了，和后面的牛并列）
   
   显然，我们不能够靠只记录rk1的值来判断变化
   
   针对（1、（2 情况，我们可以记录一下rk1的牛的编号来实现
   
   而（3 情况用前两个值好像并不能维护，所以还是再记录一下rk1的数量cnt即可
 
##### 2.rk1产奶量没变（原来的rk1还是rk1）
	   （1：rk1数量没变（不是变化）
       （2：rk1数量变了（下面的牛奋起直追，要多挂照片，所以变化）
   
   上面两种情况，我们都可以用cnt来搞定
   
所以，我们只要维护三个量 maxn(rk1产奶量)，cnt（rk1的牛数），rank1（rk1的编号）即可！

~~~cpp
struct Point{
	ll maxn,cnt,rank1;
   	//rank1 是 rank1的奶牛编号 
	//maxn 是rank1奶牛的产量，cnt是rank1的数量 
	ll l,r;
}tree[MAXN<<2];

~~~


接下来就是我们熟悉的线段树了，注意要在建树的时候初始化三个值！

##### 每一道线段树都有它的特色：体现在push_down()和push_up()，往往想好要维护的值和这两个函数，这道线段树就没什么问题了

发现题目中都是单点修改，那......

##### ~~push_down()，我要你有何用！！！~~

~~当然，线段树不需要push_down()也是特色~~

所以，核心在于push_up()的操作，建议先自己想，再 ~~结合注释~~ 食用

push_up的代码在这啦

~~~cpp
void push_up(ll x){
	if(tree[x<<1].maxn>tree[x<<1|1].maxn){//左子树的maxn>右子树的maxn，统统接受左孩子
		tree[x].cnt=tree[x<<1].cnt;
		tree[x].maxn=tree[x<<1].maxn;
		tree[x].rank1=tree[x<<1].rank1;
	}
	if(tree[x<<1].maxn<tree[x<<1|1].maxn){//同上
		tree[x].cnt=tree[x<<1|1].cnt;
		tree[x].maxn=tree[x<<1|1].maxn;
		tree[x].rank1=tree[x<<1|1].rank1;
	}
	if(tree[x<<1].maxn==tree[x<<1|1].maxn){//相等的情况，结合取用
		tree[x].cnt=tree[x<<1].cnt+tree[x<<1|1].cnt;
		tree[x].maxn=tree[x<<1].maxn;
		tree[x].rank1=tree[x<<1].rank1;//我们取最左侧的rk1编号，比较方便
	}
}
~~~

线段树板子敲一敲，update()写个单点修改，连query()都不用（直接调用全区间的就行），吃个main包，
~~此题AC!~~ 

回眸一看：

#### 1.奶牛的编号（在整数1...1e9范围内）

~~悄悄算一下，开10^9<<2这么大，完犊子了~~

but,1≤N≤100,000，所以最多也就修改1e5只牛

#### 所以离散化一下，线段树开到1e5<<2就好啦！

#### 突然，我们发现一个 ~~天大的~~ 锅：
	如果第一个操作减少了某个牛的产奶量，不也要修改吗？按我们这种做法，显然会挂
    
   所以，我们想办法把原始的值给放进去
   
   ~~开 无限大<<2 的线段树！~~
   
#####   我们可以给这些初始的牛开一个虚点代表一下
#####   没错，就这个0号牛，你代表了无数牛民的 ~~意志~~ 产奶量！！！

加上这个虚牛，吃一口main包，本题就愉快地AC啦！

ps: 在判定的部分，可以看一看上方的分析，很简单的


代码扔在下面啦
~~你们最喜欢的部分~~
~~~cpp
#include<bits/stdc++.h>
#define ll long long
#define MAXN 100010
using namespace std;

struct node{
	ll x,date,diet,nx;
}change[MAXN];

struct Point{
	ll maxn,cnt,rank1;//rank1 是 rank1的奶牛编号 
	//maxn 是rank1奶牛的产量，cnt是rank1的数量 
	ll l,r;
}tree[MAXN<<2];

ll n,m,ans,len;

bool cmp1(node x,node y){return x.x<y.x;}
bool cmp2(node x,node y){return x.date<y.date;}

void push_up(ll x){
	if(tree[x<<1].maxn>tree[x<<1|1].maxn){
		tree[x].cnt=tree[x<<1].cnt;
		tree[x].maxn=tree[x<<1].maxn;
		tree[x].rank1=tree[x<<1].rank1;
	}
	if(tree[x<<1].maxn<tree[x<<1|1].maxn){
		tree[x].cnt=tree[x<<1|1].cnt;
		tree[x].maxn=tree[x<<1|1].maxn;
		tree[x].rank1=tree[x<<1|1].rank1;
	}
	if(tree[x<<1].maxn==tree[x<<1|1].maxn){
		tree[x].cnt=tree[x<<1].cnt+tree[x<<1|1].cnt;
		tree[x].maxn=tree[x<<1].maxn;
		tree[x].rank1=tree[x<<1].rank1;
	}
}

void build(ll l,ll r,ll x){
	tree[x].l=l,tree[x].r=r;
	len=max(len,x);
	if(l==r){
		tree[x].maxn=m;
		tree[x].cnt=1;
		tree[x].rank1=l;
		return ;
	}
	ll mid=l+r>>1;
	build(l,mid,x<<1);
	build(mid+1,r,x<<1|1);
	push_up(x);
}

void update(ll nl,ll nr,ll l,ll r,ll x,ll k)
{
	if(nl==l&&nr==r){
		tree[x].maxn+=k;//单点修改，暴力改掉就好啦！
		return; 
	}
	ll mid=l+r>>1;
	if(nl<=mid)update(nl,nr,l,mid,x<<1,k);
	if(nr>mid)update(nl,nr,mid+1,r,x<<1|1,k);
	push_up(x);
}

int main(){
	cin>>n>>m;
	for(int i=1;i<=n;i++)
	{
		cin>>change[i].date>>change[i].x>>change[i].diet;
	}
	change[++n].x=0,change[n].date=0;
	change[n].nx=0,change[n].diet=0;//设了一个奇妙的虚牛，从来不变 
	sort(change+1,change+n+1,cmp1);//按序号排序 
	
	int tag=0;
	for(int i=2;i<=n;i++)
	{
		if(change[i].x!=change[i-1].x)
			tag++;
		change[i].nx=tag;//离散化
	}
	build(0,tag,1);
	sort(change+1,change+n+1,cmp2);//按时间排序 
	
	for(int i=1;i<=n;i++)
	{
		int u=tree[1].cnt,v=tree[1].rank1;//先记录一波原来的值
		update(change[i].nx,change[i].nx,0,tag,1,change[i].diet); 
		if(tree[1].cnt!=u)ans++;
		//因为一次只修改一只牛，那么判断 rank1数量变化即可 
		else if(tree[1].rank1!=v)ans++;
       		//rk1换牛了
	}
	cout<<ans;
	return 0;
}

~~~
##### 完结撒花！ \（^~^）/
