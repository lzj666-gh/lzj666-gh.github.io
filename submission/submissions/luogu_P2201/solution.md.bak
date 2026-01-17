# P2201 题解

思路大概是和楼下相同的

不过既然考虑到这个移动是具有一定的先后顺序的，我们可以使用栈来操作

相对于链表来说，还是栈更容易写吧（心虚...）

这里的写法稍微有一点麻烦

首先是读入的序列，可以放入s1的栈

然后光标之后的部分我们设为栈s2

这样
I操作：读入一个数，并放入s1（以及更新相应数值）

D操作：删除s1栈顶

L操作：将s1栈顶放入s2中

R操作：将s2栈顶放入s1中（以及更新相应数值）

Q操作：输出

维护一个s1的前缀和（S）以及一个答案数组（ans），表示i以及i之前的最大值

//写成函数食用更佳

代码
```cpp
#include<iostream>
#define N 1000010
#include<cstdio>
using namespace std;
int s1[N],s2[N];
int ans[N],S[N];
int top1,top2,n;
int main()
{
    scanf("%d",&n);
    ans[0]=-(1<<30);
    for(int i=1;i<=n;i++)
    {
        char fl;cin>>fl;
        if(fl=='I')
        {
            int x;scanf("%d",&x);
            s1[++top1]=x;
            S[top1]=S[top1-1]+x;
            ans[top1]=max(ans[top1-1],S[top1]);
        }
        if(fl=='D') top1--;
        if(fl=='L') s2[++top2]=s1[top1--];
        if(fl=='R')
        {
            int x=s2[top2--];
            s1[++top1]=x;
            S[top1]=S[top1-1]+x;
            ans[top1]=max(ans[top1-1],S[top1]);
        }
        if(fl=='Q')
        {
            int x;scanf("%d",&x);
            printf("%d\n",ans[x]);
        }
    }
    return 0;
}
//今天也依旧没有捞到岛风厌战呢

```