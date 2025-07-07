# P3755 题解

CDQ分治的题解好少啊，明明是二维偏序，为啥楼下CDQ硬是求了个三维

由于所有基站都是在一开始给出，相当于修改操作的时间戳都在询问前面(即每个基站都有可能对询问产生贡献)，这样其实就可以省略时间戳，直接做二维偏序

具体来说就是，x,y坐标分别为一二关键字排序，**遇到相同坐标令询问排后面**

询问拆成四个的老套路就不讲了，二维偏序不用树状数组，所以也不用离散化，最后注意要开long long

```cpp
#include<iostream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<cstring>
#include<cstdio>
using namespace std;
typedef long long lt;
 
lt read()
{
    lt f=1,x=0;
    char ss=getchar();
    while(ss<'0'||ss>'9'){if(ss=='-')f=-1;ss=getchar();}
    while(ss>='0'&&ss<='9'){x=x*10+ss-'0';ss=getchar();}
    return f*x;
}

const int maxn=1000010;
int n,m,tot;
struct node{lt x,y,p,opt,k,id,ans;}a[maxn],b[maxn];
lt ans[maxn];

bool cmp(node a,node b)
{
    if(a.x!=b.x) return a.x<b.x;
    else if(a.y!=b.y) return a.y<b.y;
    else return a.opt<b.opt;
}

void CDQ(int ll,int rr)
{
    if(ll==rr) return;
    int mid=ll+rr>>1;
    CDQ(ll,mid); CDQ(mid+1,rr);
 
    int t1=ll,t2=mid+1,p=ll; lt cnt=0;
    while(t2<=rr)
    {
        while(a[t1].y<=a[t2].y&&t1<=mid){
            if(a[t1].opt==1) cnt+=a[t1].p;
            b[p++]=a[t1++];
        }
        if(a[t2].opt==2) a[t2].ans+=cnt;
        b[p++]=a[t2++];
    }
 
    while(t1<=mid) b[p++]=a[t1++];
    while(t2<=rr) b[p++]=a[t2++];
    for(int i=ll;i<=rr;++i) a[i]=b[i];
}

int main()
{
    n=read();m=read();
    for(int i=1;i<=n;++i)
    {
        int x=read(),y=read();lt p=read();
        a[++tot]=(node){x,y,p,1,0,0,0};
    }

    for(int i=1;i<=m;++i)
    {
        int aa=read(),b=read(),c=read(),d=read();
        a[++tot]=(node){c,d,0,2,1,i,0};
        a[++tot]=(node){aa-1,b-1,0,2,1,i,0};
        a[++tot]=(node){aa-1,d,0,2,-1,i,0};
        a[++tot]=(node){c,b-1,0,2,-1,i,0};
    }
    
    sort(a+1,a+1+tot,cmp);

    CDQ(1,tot);
    for(int i=1;i<=tot;++i)
    if(a[i].opt==2) ans[a[i].id]+=a[i].k*a[i].ans;
    
    for(int i=1;i<=m;++i)
    printf("%lld\n",ans[i]);
    return 0;
}
```
