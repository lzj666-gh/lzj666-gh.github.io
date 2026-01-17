# P4597 题解

表示完全看不懂楼下的大佬们说啥……特别是某绿……某c姓大佬

来说说个人的理解吧

大佬们说：考虑当前的数$x$和之前的最大数$y$，（默认$x<y$，因为如果$x>=y$已经满足非降了）为了让它非降，我们要在区间$[x,y]$里找到一个数$z$，使$y$减小到$z$,$x$增大到$z$，那么可以发现，不管取的数是什么，代价都是$y-x$

不难看出，$y$减小的越多，后面的序列越容易变成非降，那么只要让$y$减小到$x$就好了

看到这里，我一直有一个疑问，如果令$y$减小到$x$之后，序列不满足非降了怎么办？

仔细想了想，实际上应该是这样的：为了让序列非降，$y$不能小于$y$之前的最大值。而由于$y$是整个序列的最大值，如果它之前的最大值$z$小于等于$x$，那么将$y$减小到$x$仍能保证序列是非降的。否则的话，$z$大于$x$小于$y$，仍是在区间$[x,y]$内，那么移动的代价是$y-x$，所以用于更新答案是没有问题的

那么这里为什么要让$y$减到最小呢？这是因为$x$和$y$不论如何调整，他们的代价之和都已经不变了，但问题是他们目前选的最优方案并不是之后的最优。为了满足他们在之后最优，只有把$y$减小到$x$，才能保证之后更有可能非降。

概括一下，对于当前的数，无论最优解如何，对答案的贡献是一定的。而为了保证之后的解也最优，令$y$减小到$x$，可以保证之后的解最优，且不会影响当前的最优解

代码好短……
```
//minamoto
#include<cstdio>
#include<iostream>
#include<queue>
using namespace std;
#define getc() (p1==p2&&(p2=(p1=buf)+fread(buf,1,1<<21,stdin),p1==p2)?EOF:*p1++)
char buf[1<<21],*p1=buf,*p2=buf;
inline int read(){
    #define num ch-'0'
    char ch;bool flag=0;int res;
    while(!isdigit(ch=getc()))
    (ch=='-')&&(flag=true);
    for(res=num;isdigit(ch=getc());res=res*10+num);
    (flag)&&(res=-res);
    #undef num
    return res;
}
priority_queue<int> q;
int n;long long ans;
int main(){
	n=read();
	while(n--){
		int x=read();q.push(x);
		if(x<q.top()){
			ans+=q.top()-x;
			q.pop();q.push(x);
		}
	}
	printf("%lld\n",ans);
	return 0;
}
```