# P1309 题解

大佬路过，萌新参考。

哎呀，本人第一篇题解啦，如果有误，敬请斧正。

首先来看题（~~没看题的看题去！~~），题面应该不难理解，就是每次相邻分数的两个人根据实力值进行比较，然后输赢分治，不断排序罢了。

“肯定要 `sort` 哇！每次更新分数，然后 `sort` 不就得了？”

其实本质上来说，是可以的，但是 `sort` 会爆炸——时间会爆炸。但是无论时间怎样，那都是 `ccf` 的测试点有没有卡 TLE 的问题而已。但如果真从程序设计本身探讨，`sort` 无疑是一个很浪费的算法。

**一、关于 `sort` 的浪费**
 
首先让我们想想，`sort` 其实就是快速排序，而快速排序其实就是二分的思想（~~胡乱在中间立flag~~）。稳定的话 $O(n \log n)$左右。但是仔细想想此题——每次需要更新的值，都是相邻两个人变化后的分数；而相邻的分数，有些是不会改变位置的，而快速排序则是每次全部修改，必然会造成浪费。

**二、关于归并排序**

然后考虑归并排序：归并排序的思想就是合并两个同序数组的线性方式——每次比较两个有序数组指针指向的值，谁更小（大）则放到 `temp` 数组里，然后删掉进入 `temp` 的元素，指针 `++`。

于是归并排序的代码就不难理解了：

```cpp
void merge(int l,int r){
    if(l==r)return 0;
    int mid=(l+r)/2;
    merge(l,mid);
    merge(mid+1,r);
    int i=l,j=mid+1,p=l;
    while(i<=mid&&j<=r){
        if(a[i]>a[j])temp[++p]=a[++i];
        else temp[++p]=a[++j];
	} 
    while(i<=mid)temp[++p]=a[++i];
    while(j<=r)temp[++p]=a[++j];
    for(int i=l;i<=r;i++)a[i]=temp[i];
} 
```

____


在归并排序中，无非就是将“两个有序数组”变成“一个被一分为二的数组（也是两个）”——因为不断二分后，剩下的单个元素必定有序，所以合并相邻相邻元素并使之有序，之后产生两个有序区间等价于合并两个有序数组。但此处仍有值得注意的地方，就是由于两个数组的大小关系具有不确定性，在第一个 `while` 结束后两个原数组中有剩余的元素未参与排序,所以需要再加两个 `while` 来处理剩余元素（此时一定是只会执行其中的一个 `while`，原因不言自明）。最后，**一定要把过程数组 `temp` 覆盖原数组a的值**，保证每次传递到上一级区间（大区间）的数值都有序。

稳定复杂度：$O(n\log n)$ 。

三、关于为何引进归并排序

大家可以发现，归并排序每次的操作只针对相邻区间，或者说合并时是对相邻几个区间的操作，所以这符合只需要修改相邻几个分数的排布状况的题意。即使和快排的复杂度相同，但是省掉了冗杂无用的操作，是一个极大的改良。

最后，附 `ac` 代码：
```cpp
#include<iostream> 
#include<algorithm>    
using namespace std;  
int n,r,q;  
int a[200100],win[200100],lose[200100];  
int s[200100],w[200100];   
bool cmp(int x,int y)  
{  
  if(s[x]==s[y])   return x<y;
  return s[x]>s[y];
}  
void merge()  
{  
  int i,j;  
  i=j=1,a[0]=0;  
  while(i<=win[0] && j<=lose[0])  
    if(cmp(win[i],lose[j]))  
      a[++a[0]]=win[i++];  
    else   
      a[++a[0]]=lose[j++];  
  while(i<=win[0])a[++a[0]]=win[i++];  
  while(j<=lose[0])a[++a[0]]=lose[j++];          
}  
int main()  
{  
  cin>>n>>r>>q;n*=2;  
  for(int i=1;i<=n;i++)a[i]=i;  
  for(int i=1;i<=n;i++)cin>>s[i];  
  for(int i=1;i<=n;i++)cin>>w[i];  
  sort(a+1,a+n+1,cmp);  
  for(int i=1;i<=r;i++)  
    {  
      win[0]=lose[0]=0;  
      for(int j=1;j<=n;j+=2)  
        if(w[a[j]]>w[a[j+1]])  
          {  
            s[a[j]]++;  
            win[++win[0]]=a[j];  
            lose[++lose[0]]=a[j+1];  
          }  
        else  
          {  
            s[a[j+1]]++;  
            win[++win[0]]=a[j+1];  
            lose[++lose[0]]=a[j];  
          }    
      merge();          
    }  
  cout<<a[q];
  return 0;  
}  
```
