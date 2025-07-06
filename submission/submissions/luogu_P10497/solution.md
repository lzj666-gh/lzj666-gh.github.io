# P10497 题解

# 基本思路
遵循从已知推出未知的原则，如果从前向后做，第
一个位置前面没有数字，第二个位置上要求有 $1$ 个数字比其小，这时完全没办法确第二个位置的数字为多少，可能性太多了。于是从后向前做。

举个例子：$1$ $2$ $1$ $0$。

它的最后一个位置为 $0$，于是只能填 $1$，因为 $1$ 是最小的，没有数字比它小。确定后则将 $1$ 加入树状数组。

倒数第二个位置为 $1$，由于 $1$ 已使用过了，于是这个位置只能放 $3$ 了。

倒数第三个位置为 $3$，由于 $1$，$3$ 已使用过，于是这个位置只能放 $5$ 了。

# 解法一：暴力做法
## 思路

开一个数组 $vis$，初值均为 $0$。

将读入的数字倒过来做，设当前处理的数字为 $a$，则在 $vis$ 数组中进行查找一个最小的位置，满足前缀和为 $a+1$。

找到这个位置后，将其标为 $1$。

时间复杂度为 $O(n^2)$。

## 代码
```cpp
#include<bits/stdc++.h>
using namespace std;
int n,a[10001],s,st[10001];
bool vis[10001];
int main()
{
  cin>>n;
  for(int i = 2;i <= n;i++) cin>>a[i];
  for(int i = n;i >= 1;i--)
  {
    s = 0;
    for(int j = 1;j <= n;j++)
      if(vis[j] == 0)
      {
        s++;
        if(s == a[i] + 1)
        {
          vis[j] = 1;
          st[i] = j;
        }
      }
  }
  for(int i = 1;i <= n;i++) cout<<st[i]<<'\n';
  return 0;
}
```
# 解法二：二分加树状数组

## 思路

可以发现本题就是在不断找某个前缀和为给定的值，并且其值越小越好。

于是可以二分这个位置，然后统计其前缀和。

时间复杂度为 $O(n\log^2n)$。
## 代码
```cpp
#include<bits/stdc++.h>
using namespace std;
int n,a[5000001],s,st[5000001],c[5000001];
bool vis[5000001];
int lowbit(int x)
{
  return x & (-x);
}
void add(int i,int x)
{
  while(i <= n)
  {
    c[i] += x;
    i += lowbit(i);
  }
}
int query(int i)
{
  int t = 0;
  while(i > 0)
  {
    t += c[i];
    i -= lowbit(i);
  }
  return t;
}
signed main()
{
  cin>>n;
  for(int i = 1;i <= n;i++)
  {
    add(i,1);
  }
  for(int i = 2;i <= n;i++)
  {
    scanf("%d",&a[i]);
  }
  for(int i = n;i >= 1;i--)
  {
    int l = 1,r = n;
    while(l <= r)
    {
      int mid = (l + r) / 2;
      if(query(mid) > a[i]) r = mid - 1;
      else l = mid + 1;
    }
    st[i] = l;
    add(l,-1);
  }
  for(int i = 1;i <= n;i++) printf("%d\n",st[i]);
  return 0;
}
```
# 结语
如果这篇题解对您有帮助，就请点个赞支持一下吧！