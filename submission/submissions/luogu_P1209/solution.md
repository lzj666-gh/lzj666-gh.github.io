# P1209 题解

典型的贪心题目

我们可以先假设只有一块木板从编号最小的牛棚一直铺到编号最大的牛棚，然后断开m-1处。自然要按相邻牛棚的编号差从大到小断开才能使我们断开的地方可以有效节省木板长度（因为中间省去的要更多）

另外，要将输入的数据排序，数据可能不是按编号从小到大给的

代码：


```cpp
#include<cstdio> 
#include<algorithm> 
#include<iostream> 
#define MAXN 205
using namespace std; 
int m,s,c,ans;
int a[MAXN],C[MAXN];
bool cmp(int x,int y)
{
    return x>y;
}
int main() 
{ 
    scanf("%d %d %d",&m,&s,&c);
    for(int i=1;i<=c;i++)
        scanf("%d",&a[i]);
    if(m>c) { //特判，如果木板数大于牛数，那么每只牛可以有一块木板
        printf("%d\n",c);
        return 0;
    }
    sort(a+1,a+c+1);
    ans=a[c]-a[1]+1;//假设只有一块木板连续地铺着
    for(int i=2;i<=c;i++)
        C[i-1]=a[i]-a[i-1];
    sort(C+1,C+c,cmp);
    for(int i=1;i<=m-1;i++)//减去差最大的//将木板从差最大的地方减去
        ans=ans-C[i]+1;
    printf("%d\n",ans);
} 

```