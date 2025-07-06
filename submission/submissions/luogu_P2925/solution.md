# P2925 题解

##### 很简单的01背包，每件物品的价值和重量相同，直接套就行了。还有其中有个点要优化，在中途进行判断就好了，当然开O2优化也行

`

```cpp
    #include<bits/stdc++.h>
    using namespace std;
    int f[111111];
    int main()
    {
        int n,m,i,j,a[111111];
        cin>>m>>n;
        for (i=1;i<=n;i++) scanf("%d",&a[i]);
        for (i=1;i<=n;i++)
        {
            for (j=m;j>=a[i];j--)
            f[j]=max(f[j],f[j-a[i]]+a[i]);
            if (f[m]==m) {printf("%d",m); return 0;}//优化，如果已经达到最好的结果（装满），就直接退掉
        }
        printf("%d",f[m]);
}
```