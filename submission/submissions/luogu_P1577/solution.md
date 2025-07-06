# P1577 题解

### 题目标签：二分答案
### 主要思路
首先看着道题时，主要是会发现要求的答案只有一个，且有一个可以对应的条件，就可以基本断定是一道二分答案的题了。

不过，，，像我这种什么也不会的蒟蒻，上来就蒙了——
#### 二分答案是什么？？？
大家应该知道二分吧。~~（不知道去找信奥一本通）~~这里的二分答案二分的一种。

我会用这道题为例来讲述二分答案的思想。

这里，我们不知道截成的k个小段每条有多长，却给出了k，也就是说我们可以先假设一个x为每段的长度，判断他是不是正确的、可行的。

判断可以用这种方法判断（假设已经输入了a[i]，即所给的n条绳子）：

```c
int ans=0;
for(int i=1;i<=n;i++){
	ans+=a[i]/x;//直接向下取整，方便了计算，叠加了每一条绳子可以截出的和 
}
```

但是，你假设的x是不是正确的呢？？？

显然可能性很小，可能你所能截的段数少，也可能多。

那就从0.01开始试吧，反正是计算机，，，

但是，看数据条件的话，100000.00……最坏情况要试10000000次才行。这个数量级显然快要超时了，乘上一开始的n的大小就更不可能了。

那么，该怎么找到答案呢？？？这里就可以用到二分了！！

如果一个假设的x所计算出的个数不与题目所给的k段相同，那么就去分析一下这个x是小了还是大了。如果x小了，也就是说，可以截成的段数多了，所计算出的k'就大于k了，如果x大了，则相反。这样，我们就可以根据算出的k'的大小来调整x。

判断大小就可以直接改一下上面的代码：

```
inline int judge(int x){
	int ans=0;
	for(int i=1;i<=n;i++){
		ans+=a[i]/x;//直接向下取整，方便了计算，叠加了每一条绳子可以截出的和 
	}
	if(ans>=k)
		return true;//如果算出的k'大于等于k，则x小于等于正确答案，返回true
	else
		return false;//如果算出的k'小于k，则x大于正确答案，返回false 
}
```

讲到这里。你大概可以知道怎么用二分了。

二分的性质（伪）就是有一定的排列方式，这里，x相对于正确答案的大小就是这个排列方式。我们可以用一个二分来一次一次的寻找答案，直到左右界重合。这样的寻找答案的方式就是二分答案。

二分答案核心代码除了判断大小（如上），就是寻找答案的步骤了。这个代码比较死，大家记住就OK，绝大多数二分答案题可以使用：

```
int l=0,r=100000000;//把左端与右端定义，这个地方有些题范围不能开太大，有一定的要求，不过这里就OK了
while(l<=r){
	int mid=(l+r)/2;
	if(judge(mid))//判断步骤 
		l=mid+1;
	else
		r=mid-1;//有些题这里有微调……不过不影响 
} 
cout<<r; 
```
直到while循环结束，r就是所要找的的不大不小的正确答案了。

### 注意
真正做这道题时，完全可以用所有值乘100的方式全部化成整数进行计算，最后除以100输出。

## 具体全部代码：
~~（有点SAO的宏定义，，，）~~
```
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<queue>
#include<vector>
#include<set>
using namespace std;
#define go(i,j,n,k) for(register int i=j;i<=n;i+=k)
#define fo(i,j,n,k) for(register int i=j;i>=n;i-=k)
#define mn 100010
#define inf 1<<30
inline int read(){
    int x=0,f=1;char ch=getchar();
    while(ch>'9'||ch<'0'){if(ch=='-')f=-f;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
} 
double d[mn];
int a[mn];
int n,m,minn,maxx;
inline bool judge(int x){
    int num=0;
    go(i,1,n,1)
        num+=a[i]/x;
    return num>=m;
}
int main(){
    n=read(),m=read();
    go(i,1,n,1)	scanf("%lf",&d[i]),a[i]=int(d[i]*100);
    int l=0,r=inf;
    while(l<=r){
        int mid=(l+r)>>1;
        if(mid==0)	break;//这里是个特判。至于为什么，作为思考题。（其实也不难理解）
        if(judge(mid))
            l=mid+1;
        else
            r=mid-1;
    }
    printf("%.2f",r/100.0);
    return 0;
}
```

### PS:第四次交稿，若有不足之处，望dalao多多指正