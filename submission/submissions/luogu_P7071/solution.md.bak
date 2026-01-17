# P7071 题解

$Update:$ 

- `if` 语句出了大问题，现已修正

- 关于 数组 `a` 长度的问题亦已修正 

---

~~上机时题目标题差点吓死我。~~

## 步入正题

[题目传送门](https://www.luogu.com.cn/problem/P7071)

分析：

**样例输入**

```cpp
6

```

**样例输出**

```cpp
4 2

```

(1) 可以证明：一切奇数都不存在优秀的拆分，因为2的正整数次幂为偶数。

所以一遇到奇数就输出`-1`。

但是也有一个细节要注意：**0也不存在优秀的拆分。**

所以一开始的判断可以这么写：

```cpp
if (n%2==1 || n==0){
    printf("-1");
    return 0;
}
```
(2)观察样例：

$(6)_{10}=(110)_2$

![](https://cdn.luogu.com.cn/upload/image_hosting/pqotn90j.png)

咦？怎么和样例输出一模一样？

再试一个：

$(28)_{10}=(11100)_2$

![](https://cdn.luogu.com.cn/upload/image_hosting/32dxlwht.png)

可以证明：$16\ \ 8\ \ 4$ 是 $28$的优秀的拆分。

所以我们思路来了：

> 把 $n$ 转换为$2$进制，每取到一位"$1$"就变成十进制，再从大到小输出即为 $n$ 优秀的拆分。

具体看核心代码：

```cpp
void change(int b){
    int res=0; //统计a数组里有多少个元素并且作为指数
    while(b){
        if (b&1){  // 从右至左取每一位并判断是否为0
        	a[res]=pow(2,res);  // 变成十进制
        } 
        res++;
        b>>=1;// 右移一位
    }
    idx=res;   // 记录个数，便于主程序输出
}
```

最后贴上代码：

```cpp
#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
int n,a[30],idx;
void change(int b){
    int res=0;
    while(b){
        if (b&1) a[res]=pow(2,res);
        res++;
        b>>=1;
    }
    idx=res;
}

int main(){
    scanf("%d",&n);
    if (n%2==1 || n==0){
    	printf("-1");
    	return 0;
    }
    change(n);
    for(int i=idx;i>=1;i--)
        if (a[i]!=0) printf("%d ",a[i]);
    return 0;
}
```

$P.S$ 有几点要注意一下：

(1) $a$数组的范围其实没必要开很大。

因为$1\le n \le 1\times 10^7$，

而$2^{24}=16777216$，
![](https://cdn.luogu.com.cn/upload/image_hosting/h4yhin8a.png)

所以指数$<24$，所以开到30就够了。

(2) 如果没有`if (a[i]!=0)`，你会发现：输出结果会有很多$0$，所以必须加上这句话。

至于原因：因为`if (b&1)`，所以 $n$ 转换后会有一些 $0$ 没有做处理，又因为 $a$ 定义在主函数外面，所以会有一些未处理的 $0$ 。

当然，如果再想优化的话，也可加上快速幂：

```cpp

#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
int n,a[30],idx;
int qmi(int a,int b){
    int res=1;
    while(b){
        if (b&1) res=1LL*res*a;
        a=1LL*a*a;
        b>>=1;
    }
    return res;
}

void change(int b){
    int res=0;
    while(b){
        if (b&1) a[res]=qmi(2,res);
        res++;
        b>>=1;
    }
    idx=res;
}

int main(){
    scanf("%d",&n);
    if (n%2==1 || n==0){
    	printf("-1");
    	return 0;
    }
    change(n);
    for(int i=idx;i>=1;i--)
        if (a[i]!=0) printf("%d ",a[i]);
    return 0;
}


```

希望管理员大大给通过~~

如果读者们看了觉得有帮助，留个赞再走呗，谢谢辽~~