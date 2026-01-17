# P5732 题解

杨辉三角主要具有以下性质：

- 每一行的第一个元素和最后一个元素均为 $1$。
- 第 $i$ 行 第 $j$ 列（$i>1,j \le i$）的元素等于第 $i-1$ 行第 $j-1$ 列和第 $i-1$ 行第 $j$ 列之和。

转换成数学语言：

$$a_{i,1}=a_{i,i}=1$$
$$a_{i,j}=a_{i-1,j-1}+a_{i-1,j}$$


利用递推，我们可以得到代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,a[21][21];
int main()
{
    scanf("%d",&n);
    a[1][1]=1;//初始化
    for(int i=2;i<=n;i++)
        for(int j=1;j<=i;j++)
            a[i][j]=a[i-1][j-1]+a[i-1][j];//进行计算
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=i;j++)printf("%d ",a[i][j]);//输出
        printf("\n");//换行
    }
    return 0;
}
```

Python 代码：

```python
n = int(input()) # 输入n，类型为整数
a = [[0 for i in range(0, n + 1)] for j in range(0, n + 1)] # 建立数组
a[1][1] = 1 # 标记a[1][1]的值为1
for i in range(2, n + 1): # range(a,b)表示在[a,b)区间，不包括b
    for j in range(1, i + 1):
        a[i][j] = a[i-1][j-1] + a[i-1][j] # 递推
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(a[i][j], end = ' ') # end=''可以在输出内容后多输出一个字符串，不写end则默认为换行
    print('') # 输出空，因为默认输出后换行，所以达到了换行作用
```