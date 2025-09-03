# P1113 题解

简单来说，因为任务可以并发，所以一个任务如果有前驱的话，最优方案便是在它的最晚一个前驱结束后就立即开始，而且任务k的前驱节点一定小于k，所以读入时顺便从它的前驱里挑一个最大的转移即可。同时可以更新最终答案。

*我是仗着代码短才来发的*

---
```
#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int n,l,t,ans[10005],maxans;
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;++i){
        scanf("%d",&i);
        scanf("%d",&l);
        int tmp=0;
        while(scanf("%d",&t)&&t)
            tmp=max(ans[t],tmp);
        ans[i]=tmp+l;
        maxans=max(ans[i],maxans);
    } 
    printf("%d\n",maxans);
    return 0;
 } 
 ```