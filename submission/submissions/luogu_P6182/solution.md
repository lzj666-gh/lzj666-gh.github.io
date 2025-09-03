# P6182 题解

这道题的标签是可持久化和栈，那我们就拿他们的思想来解这道题吧 QAQ 。

# 前置数组

- $num(i)$： 表示添加的第 $i$ 个奶牛编号。

- $t(i)$：表示第 $i$ 次操作最新的奶牛在 $num$ 数组中的位置（即 $top$ 值）。

- $pre(i)$：表示在 $num$ 数组中位置为 $i$ 的奶牛在其所对应的操作里前一个奶牛的位置（为 $s$ 操作服务）。

# 逐步解析

### 添加操作：

这个十分容易理解，用 $top$ 记录新增的奶牛位置，$t(i)$ 即为 $top$ ，$pre(i)$ 即为上一次操作的 $top$ 值。

代码段如下：

```cpp
if(ch=='a'){                 
    scanf("%d",&x);
    num[++top]=x;
    t[i]=top;pre[t[i]]=t[i-1];
}
```

### 跳转操作：

这里需要注意了，题目描述里面说的是回到第 $x$ 次操作 __前__ 的状态，即第 $x-1$ 次操作的结束状态。我们只需将第 $x-1$ 次操作的状态复制到当前即可。

代码段如下：

```cpp
if(ch=='t'){
    scanf("%d",&x);
    t[i]=t[x-1];
    //pre[t[i]]=pre[t[x-1]];（这一段等价直接省略）
}
```

### 删除操作：

这个操作非常简单 ~~（但因为想错重构了不下亿次）~~ ，$pre$ 数组的作用就来了。我们只需将上一次操作的最新奶牛的前一个奶牛的位置复制到当前即可。

代码段如下：

```cpp
if(ch=='s'){
  t[i]=pre[t[i-1]];
  //pre[t[i]]=pre[pre[t[i-1]]];（这一段也等价，可直接省略）
}
```

20行代码AC！

全段如下：

```cpp
#include<cstdio>
#include<iostream>
using namespace std;
const int N=8e4+10;
int n,num[N],t[N],pre[N],top;
int main(){
    scanf("%d",&n);
    char ch;int x;
    for(int i=1;i<=n;i++){
        scanf(" %c",&ch);
        if(ch=='a'){ 
          scanf("%d",&x);num[++top]=x;
            t[i]=top;pre[t[i]]=t[i-1];
        }else if(ch=='t'){
            scanf("%d",&x);t[i]=t[x-1];
        }else t[i]=pre[t[i-1]];
        printf("%d\n",t[i]?num[t[i]]:-1);
    }
    return 0;
}
```