# P1644 题解

## 这题只是一道深搜题(异常简单[滑稽])

这题仔细想一想其实连回溯都不用，更不用二维数组

![](https://cdn.luogu.com.cn/upload/pic/450.png)

先是搜索部分，每次枚举可出现的情况

有右上，右下两个位置，每个位置有两种情况[玩过中国象棋的都知道]，看题目，不能往回走，所以：

```cpp
dfs(a+1,b+2);//a是横坐标，b是纵坐标
dfs(a+2,b+1);
dfs(a-2,b+1);
dfs(a-1,b+2);
```

终止部分也是重点！

先是当马到了正确的位置：

```cpp
if (a==n && b==m){
        t++;//找到了总数+1
}        
```

然后是当马越界时：
 
```cpp
if (a<0 || a>n || b>m) return;
//马越界的情况有三种，有行数超(正负两种)，有列数超(只有正)
```

所以深搜部分这么打：

```cpp
void dfs(int a,int b){
    if (a<0 || a>n || b>m) return;
    if (a==n && b==m){
        t++;
    }else{
        dfs(a+1,b+2);
        dfs(a+2,b+1);
        dfs(a-2,b+1);
        dfs(a-1,b+2);
    }
}
```

主程序就不多说了，主要是起始位置要定义：

```cpp
dfs(0,0);
```

下附赠完美代码：
```cpp
#include<bits/stdc++.h>
using namespace std;
int m,n,t;
void dfs(int a,int b){
    if (a<0 || a>n || b>m) return;
    if (a==n && b==m){
        t++;
    }else{
        dfs(a+1,b+2);
        dfs(a+2,b+1);
        dfs(a-2,b+1);
        dfs(a-1,b+2);
    }
}
int main(){
    cin>>n>>m;
    dfs(0,0);
    cout<<t;
    return 0;
}
```
