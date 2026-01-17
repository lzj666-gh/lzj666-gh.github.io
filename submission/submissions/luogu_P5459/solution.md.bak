# P5459 题解

## ~~这道题为什么是紫题？~~

这道题很明显一开始要先求个前缀和，这个问题就转换成求i< j，s[j]-s[i]>=L且s[j]-s[i]<=R的对数（0<=i< n)。感觉这个形式跟逆序对有点像，于是便想到了归并排序。但有点区别，那就是答案的统计方式就没有那么简单了。 


但其实我们化一下式子，变成s[i]-s[j]>=L,s[i]-s[j]<=R（看代码就能理解了），发现就可以用队列来维护，那这题就解决了，注意开long long。

[cdq分治](https://www.luogu.org/blog/Owencodeisking/post-xue-xi-bi-ji-cdq-fen-zhi-hu-zheng-ti-er-fen)水题

```cpp
#include<bits/stdc++.h>//万能头文件
using namespace std;
long long L,R,ans,s[110000];
void cdq(int l,int r)
{
    if(l==r)return ;
    int mid=(l+r)/2;
    cdq(l,mid),cdq(mid+1,r);
    int head=l,tail=l-1;
    for(int i=mid+1;i<=r;i++)
    {
        while(tail+1<=mid && s[i]>=s[tail+1]+L)tail++;
        while(head<=mid && s[i]>s[head]+R)head++;
        ans+=tail-head+1;
    }
    sort(s+l,s+r+1);
}//cdq分治
int main()
{
    int n;
    scanf("%d%lld%lld",&n,&L,&R);
    for(int i=1;i<=n;i++)
    {
        int x;
        scanf("%d",&x);
        s[i]=s[i-1]+x;//前缀和
    }
    cdq(0,n);
    printf("%lld\n",ans);
    return 0;
}

```

