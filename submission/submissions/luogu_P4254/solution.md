# P4254 题解

## 题解&&李超线段树学习笔记

### 一.李超线段树解决的问题

考虑下面一个问题： 

定义一个坐标系，有m次操作 

操作1：添加一条直线 

操作2：求x=x0这条直线和其他直线的交点的最高纵坐标

要求时间复杂度log级别，**可以用线段树维护**。

### 二.原理

对于一个区间，我们维护该区间的所有直线中，没有被其他直线覆盖的从上往下去看在x轴上的投影最大的直线（称为标记直线）。

其实这条直线的意义就是对这个区间内**大多数点**而言最优的直线，但也**不一定是最优的直线**，更优解可能在更小的区间内。

现在插入一条直线（称为新直线）到了一个区间，尝试更改该区间的标记直线。

分为几种情况：

1.新直线完全覆盖标记直线，直接更新并return，不用继续向下更新。

2.新直线完全被覆盖，那么新直线无用，直接return。

3.不是上面两种情况，判断两条直线哪一个投影大一些，作为新的标记直线，再递归下去处理。

询问时直接整个线段树包含x0的区间所存的线段取max即可。

其实相当于一个标记永久化的思想。

### 三.细节

如何判断两条直线哪一个应该作为标记直线呢？

分类讨论，设原标记直线为y，新直线为x。

1.k[x]>k[y]

如图，蓝色的代表线段中垂线。

![](http://a2.qpic.cn/psb?/V1190t7T1Jiov3/L0EYCRX232UeawP*7LPTk19pqy16r*Rwqh**LgboHJI!/b/dLkAAAAAAAAA&ek=1&kp=1&pt=0&bo=wAMcAgAAAAADF.8!&tl=1&vuin=630449676&tm=1545645600&sce=60-2-2&rf=viewer_4)

可以直观感受到如果斜率更大且在中点所对应的x上y更大，则投影更大。

还可以清楚认识到y直线对右边的区间已经没有贡献了，在右区间内x肯定优于y，但是y对左边可能还有贡献，所以把y放到左区间去更新一波答案就好。

2.k[x]<k[y]

道理同上，结论是如果斜率更小且在中点所对应的x上y更大，则投影更大。

较弱的那条直线对左区间没有贡献。

### 四.练习题

P4254 裸题，唯一的区别是纵截距给的是x==1的。

bzoj4515 听说是树剖+李超线段树



------------



## Code：

```
#include<bits/stdc++.h>
#define ll long long
#define db double
#define in inline
#define rint register int
#define ls (id<<1)
#define rs (id<<1|1)
using namespace std;
int n,t[200010],cnt;
db k[100010],b[100010];
char s[10];
in ll read()
{
    ll x=0,f=1; char ch=getchar();
    while(ch<'0'||ch>'9') { if(ch=='-') f=-1; ch=getchar(); }
    while(ch>='0'&&ch<='9') { x=x*10+ch-'0'; ch=getchar(); }
    return x*f;
}
in db w (int id,int x) { return k[id]*(x-1)+b[id]; }
in void updata(int id,int l,int r,int x)
{
    if(w(x,l)>w(t[id],l)&&w(x,r)>w(t[id],r)) { t[id]=x; return; }//如果完全覆盖 直接return
    if(w(x,l)<=w(t[id],l)&&w(x,r)<=w(t[id],r)) return; //如果完全被覆盖 直接return
    //上面两种情况已经可以解决l==r时候的问题了 所以不用判断 
    int mid=(l+r)>>1;
    if(k[t[id]] < k[x])
    {
    	//如果新加入直线的斜率更大，且中点纵坐标更大，更改标记直线
        if(w(x,mid) > w(t[id],mid)) updata(ls,l,mid,t[id]),t[id]=x; 
        //因为标记直线有可能在左区间还有贡献 所以把以前的标记直线丢到左区间 
        else updata(rs,mid+1,r,x);
        //如果纵坐标更小 那么新加入直线可能在右区间有贡献 
    }
    else //同理 
    {
        if(w(x,mid) > w(t[id],mid)) updata(rs,mid+1,r,t[id]),t[id]=x;
        else updata(ls,l,mid,x);
    }
}
in db query(int id,int l,int r,int x)
{
    if(l==r) return w(t[id],x);
    int mid=(l+r)>>1;
    if(x<=mid) return max(w(t[id],x),query(ls,l,mid,x));
    else return max(w(t[id],x),query(rs,mid+1,r,x));
}
int main()
{
    n=read();
    while(n--)
    {
        scanf("%s",s);
        if(s[0]=='P')
        {
            cnt++;
            scanf("%lf%lf",&b[cnt],&k[cnt]);
            updata(1,1,50005,cnt);
        }
        else
        {
            int x=read();
            printf("%d\n",(int)(query(1,1,50005,x)/100)) ;
        }
    }
    return 0;
}

```
