# P1250 题解

解题思路

贪心，要种树种得少，就要使一棵树给多个区间使用，这样，尽量在重叠区间种树即可，而重叠位置一定是区间尾部。处理问题时，先按所有区间的结束位置从小到大排序，若结束位置相同，则按开始位置从大到小排序。之后依次处理每个区间，先在第一个区间尾部种满足要求的树，对下一个区间，看差多少棵就在该区间尾部种多少。

步骤：

①先按照b[]从小到大快排

②对每个区间依次处理

a.从前到后扫描这个区间，统计点的个数；

b.若没有超过要求的点数，则从该区间后向前扫描，添加覆盖点。

③输出ans

代码如下：

```cpp
#include<iostream>
using namespace std;
struct line{int s,e,v;}a[5005],mid;
int n,m,used[30005]={0};
void qsort(int L,int r)//快排
{  int i=L,j=r;mid=a[(L+r)/2];
   while(i<=j)
   {  while(a[i].e<mid.e)i++;
      while(a[j].e>mid.e)j--;
      if(i<=j)swap(a[i++],a[j--]);
   }
   if(L<j)qsort(L,j);
   if(i<r)qsort(i,r);
}
void Init()
{  int i;
   cin>>n>>m;
   for(i=1;i<=m;i++)cin>>a[i].s>>a[i].e>>a[i].v;
   qsort(1,m);
}
void Solve()
{  int i,j,k,ans=0;
   for(i=1;i<=m;i++)//依次处理m个区间
   {  k=0;
      for(j=a[i].s;j<=a[i].e;j++)if(used[j])k++;//统计区间内已标记的数
      if(k<a[i].v)
         for(j=a[i].e;j>=a[i].s;j--)
             if(!used[j]){used[j]=1;k++;ans++;if(k==a[i].v)break;}
   }
   cout<<ans<<endl;
}
int main()
{  Init();
   Solve();
}
还有其他算法，例如：树状数组，差分约束系统
```