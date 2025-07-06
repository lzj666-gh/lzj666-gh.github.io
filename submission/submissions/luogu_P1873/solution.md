# P1873 题解

然而这题并不需要什么二分法。。。

用sort排序再从后往前查找就可以。

只需优化一下当前砍去多少米的算法就可以。

假设已砍过了i棵树（树由高到低排），那此时被砍过的i棵树的高度均等于第i+1棵树的高度。

再砍一棵树（砍第i+1棵）后获得的新高度为（第i+1棵树的高度-第i+2棵树的高度）\*（i+1）。

so  时间复杂度仅为 n

```cpp
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int tree[1000001];
int n,m;
int main()
{
    int i,num,ans;
    long long sum;
    scanf("%d%d",&n,&m);
    for(i=1;i<=n;i++)
        scanf("%d",&tree[i]);
    sort(tree+1,tree+n+1);
    sum=0;
    num=n;
    while(sum<m)
    {
        sum+=(tree[num]-tree[num-1])*(n-num+1);
        num--;
    }
    num++;
    ans=tree[num-1]+(sum-m)/(n-num+1);
    printf("%d\n",ans);
    return 0;
}
```