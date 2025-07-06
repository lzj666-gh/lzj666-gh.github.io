# P1714 题解

**我发现题解中大多数用单调队列做的都是错的！！**（不仅是用单调队列，题解中其他的方法基本都能被hack）

不信你试试5 2 5 4 3 2 1，题解中大多数输出的都是7或者1 1 5，输出的都是0
~~主要是这道题数据太水了~~

**所以我决定来给出一个用STL做的正确解法，不能误导别人呀**

~~所以管理员你就让我过了吧~~

其他题解之所以会被hack是因为他们光顾着维护队列单调递增（前缀和递增才会保证最大），忘了万一数据是单调递减怎么办。所以我们应该在维护递增之前就判断现在的答案是否为最优。为了达到这个目的我们应该先给队列赋初值0，因为sum[i]-sum[q.front()]这一句，不赋初值就出bug了，正好赋初值之后就可以避免第一个值是最大的，其余都是负的（如5 2 1 -10 -10 -10 -10 -10）这种丧心病狂的数据了。
```c

#include<bits/stdc++.h>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<stdio.h>
#include<cmath>
#include<deque>
#define debug cout<<"ok"<<endl
typedef long long ll;
const int maxn=1e7+10;
const int mod=1e9+7;
using namespace std;
int ans=-233333333,n,m,a,sum[maxn];
deque<int>q;
int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&a);
        sum[i]=sum[i-1]+a;//前缀和
    }
    q.push_back(0);//赋初值
    for(int i=1;i<=n;i++)
    {
        while(q.front()+m<i)
            q.pop_front();//越界就pop
        ans=max(ans,sum[i]-sum[q.front()]);
        while(!q.empty()&&sum[q.back()]>=sum[i])//递减就pop
            q.pop_back();
        q.push_back(i);
    }
    printf("%d\n",ans);
    return 0;
}

```
~~快把我顶上去呀，可不能一直这样误导观众呀~~
