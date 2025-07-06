# B2051 题解

本题是一道结合了几何相关知识与分支结构的题。

根据正方形可知，只要点的横坐标与纵坐标都在范围内，点就在正方形内。

也就是：

+ $-1\le x\le 1$ 且 $-1\le y\le 1$，点在图形内；

+ 否则点在图形外。

代码：
```
#include<bits/stdc++.h>
using namespace std;
int x,y;
int main(){
    scanf("%d%d",&x,&y);
    if(x>=-1&&x<=1&&y>=-1&&y<=1) puts("yes");
    else puts("no");
    return 0;
}

```