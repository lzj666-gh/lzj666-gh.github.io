# P1182 题解

###本题解法：二分答案+贪心###

**思路：**首先，分析题目，求最大值的最小化，直接联想到二分，So我们直接二分答案，关键是要怎么去高效的check，我看了大家基本上使用了前缀和，但实际上这个空间是可以省略的，为什么呢？我们考虑一个贪心的思路，能加的就加上，不能则新开一段，so对于二分的值x，我们从数列a从前往后扫，如果tot大于了x，我们不加而是tot重新赋值并且num++，最后只需判断num是否不小于m就行了。这样判断与前缀和一样是O(n)的复杂度，但是节省了空间且容易思考。

**注意：**二分时的区间取值问题，很明显，对于l的赋值应该取数列中的最大值，而r应该取数列的总和。(亲测，如果l赋值为0或1，第4个点会wa)。

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,m,a[100005],l,r,mid,ans;
inline bool check(int x)
{
    int tot=0,num=0;
    for(int i=1;i<=n;i++)
    {
        if(tot+a[i]<=x)tot+=a[i];
        else tot=a[i],num++;
    }
    return num>=m;
}
int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)scanf("%d",&a[i]),l=max(l,a[i]),r+=a[i];
    while(l<=r)
    {
        mid=l+r>>1;
        if(check(mid))l=mid+1;
        else r=mid-1;
    }
    cout<<l;
    return 0;
}
```