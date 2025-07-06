# P1085 题解

~~这个题竟然能写题解~~
## 题目大意
输入七组数，分别表示津津在学校上课的时间和妈妈安排她上课的时间。求在学校上课的时间和妈妈安排她上课的时间的和是否会让津津不高兴。
## 题目思路
可以通过遍历数组来求解最大值出现的位置。

输入数据，边输入边统计最不高兴的是周几，也就是上课时间最长的是第几天。

这里要注意，如果上课时间相同，则统计时间靠前的那一天。
## AC code

```cpp
#include <bits/stdc++.h>
using namespace std;
int a[8],n,m,maxn=-1,maxm=-1;
int main(){
    for(int i=1;i<=7;i++){
        scanf("%d%d",&n,&m);
        a[i]=n+m;
        if(a[i]>8 and a[i]>maxn){
            maxn=a[i];
            maxm=i;
        }
    }
    if(maxn==-1)printf("0");
    else printf("%d",maxm);
    return 0;
}
```
~~记得点赞~~