# P3467 题解

 Solution

1. 考虑如果整个建筑物链是等高的，一张高为链高，宽为整个建筑物宽的海报即可完全覆盖；
2. 若有两个不等高的元素组成建筑物链，那么一定需要两张；
3. 因为题目要求海报不可超出建筑物链，那么我们即可用单调栈维护：初始海报数为建筑物数，入栈建筑物链的高度序列，当栈顶大于即将入栈元素时弹栈，若最后弹栈元素与即将入栈元素等高，需要的海报数-1；
4. 易证明本方法是正确的：当有两个处于一个峰两侧的等高块时，他们可以用一张海报覆盖，所需海报数显然可减少一个；

```
#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<algorithm> 
using namespace std;
long long top=0,n,num=0,i,j,k,stack[250100];
int main(){
    scanf("%lld",&n);
    for(i=1;i<=n;++i){
        scanf("%lld%lld",&j,&k);
        while(top>0&&k<=stack[top]){
            if(k==stack[top])num++;
            --top;
        }
        stack[++top]=k;
    }
    printf("%lld\n",n-num);
    return 0;
}
```
关于单调栈其他问题可以参考我的博客：http://www.cnblogs.com/COLIN-LIGHTNING/p/8474668.html

有什么问题欢迎各位dalao指出