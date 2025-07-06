# P3152 题解

Upd on 2020.7.29：修正 Latex。

---

#### 所有正整数都可以被表示为 $2$ 的次方相加的形式。

例如 : 

$10=2^1+2^3$。

$24=2^3+2^4$。

$59=2^0+2^1+2^3+2^4+2^5$。

$127=2^0+2^1+2^2+2^3+2^4+2^5+2^6$。

通过观察，我们可以发现:

#### 所有正整数都可以被拆成不大于 $\log_2 n+1$ 个互不相同的 $2$ 的次方相加。

解决这个题目主要就是根据这个定理。

当 $n=8$ 时，序列是这样的:

$1\quad 2\quad 3\quad 4\quad 5\quad 6\quad 7\quad 8$

把这个序列的所有数按照上面的方法表示出来。

$2^0\quad 2^1\quad 2^0+2^1\quad 2^2\quad 2^0+2^2\quad 2^1+2^2\quad 2^0+2^1+2^2\quad 2^3$

#### 这样操作的方法就一目了然了吧？

Step 1：将所有 " $2^0$ " 减去，得到序列：

$0\quad 2^1\quad 2^1\quad 2^2\quad 2^2\quad 2^1+2^2\quad 2^1+2^2\quad 2^3$。

Step 2：将所有 " $2^1$ " 减去，得到序列：

$0\quad 0\quad 0\quad 2^2\quad 2^2\quad 2^2\quad 2^2\quad 2^3$。

Step 3：将所有 " $2^2$ " 减去，得到序列：

$0\quad 0\quad 0\quad 0\quad 0\quad 0\quad 0\quad 2^3$。

$step4$ : 将所有 " $2^3$ " 减去，得到序列：

$0\quad 0\quad 0\quad 0\quad 0\quad 0\quad 0\quad 0$。

这样，我们就把这个序列里的所有数全部变成了 $0$。

总共 $\log_2 n+1=\log_2 8+1=3+1=4$ 次操作。

#### 所以，对于所有的 $n$ ，操作的次数为 $\log_2 n+1$。

代码如下

```cpp
#include<bits/stdc++.h>
using namespace std;
int n;
int main(){
    cin>>n;
    cout<<(int)log2(n)+1;
    return 0;
}
```

求赞 (〃'▽'〃) 。