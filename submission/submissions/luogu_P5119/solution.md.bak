# P5119 题解

本题可以采用二分答案的方法解决。

先将牛到达的时间排序，然后二分最长等待时间即可。

详细过程已经在代码里注释说明，这里不再赘述。

```cpp
#include <cstdio>
#include <algorithm>
using namespace std;
int a[100005];
int main()
{
 //freopen("convention.in","r",stdin);
 //freopen("convention.out","w",stdout);
 int n,m,c;
 scanf("%d%d%d",&n,&m,&c);
 for(int i=1;i<=n;i++)
  scanf("%d",&a[i]);
 sort(a+1,a+n+1);
 int l=0,r=a[n]-a[1];
 while(l<r)
 {
  int mid=(l+r)>>1,cnt=1,sta=1;
  for(int i=1;i<=n;i++)
   if(a[i]-a[sta]>mid||i-sta+1>c)
   //如果等待时间超过了二分中点mid或当前车辆已经满载，就重新发一辆车
   {
   	cnt++;
   	sta=i;
   }
  if(cnt<=m)r=mid;//该时间下车辆数充足，等待时间可以更小
  else l=mid+1;//车辆不足，等待时间要更长
 }
 printf("%d\n",l);
 fclose(stdin);
 fclose(stdout);
 return 0;
}
```