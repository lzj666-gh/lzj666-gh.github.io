# P11156 题解

题目传送门：[P11156 【MX-X6-T2】もしも](https://www.luogu.com.cn/problem/P11156)

最真诚的提示：Special Judge 的输出样例都没用。

### 题目分析

我们以最后一组样例为例：$a_6=3$，那要让 $\dfrac{a_4}{a_5}=3$，最小的办法就是 $a_4=3,a_5=1$。让 $\dfrac{a_3}{a_4}=1$，同时 $a_4=3$，则 $a_3$ 最小可以等于 $1$。

按照上面的构造方法，我们得到了 $1,3,1,3,1,3$ 的数列。我们可以发现，上述规律对于任意一个 $n$ 为偶数的 $a_n$ 都适用。

如果 $n$ 为奇数呢？

以 $n=5$ 为例，则 $a_4=1,a_3=a_5,a_2=1,a_1=a_5$。

所以我们得到了规律：

当 $n$ 为偶数时，可以构造 $a_1=1,a_2=a_n,a_3=1,a_4=a_n,\dots$ 的数列；

当 $n$ 为奇数时，可以构造 $a_1=a_n,a_2=1,a_3=a_n,a_4=1,\dots$ 的数列。

### 代码实现

当 $n$ 为偶数时，输出 $a_1=1,a_2=a_n$；

当 $n$ 为奇数时，输出 $a_1=a_n,a_2=1$。

```cpp
#include<iostream>
using namespace std;
void doing(int n,int a){
	int a1,a2;
	if(n&1)cout<<a<<' '<<1<<'\n';
	else cout<<1<<' '<<a<<'\n';
	return ;
}
int main(){
	int t;
	cin>>t;
	while(t--){
		int n,a;
		cin>>n>>a;
		doing(n,a);
	}
	return 0;
}
```

[AC 记录](https://www.luogu.com.cn/record/179817728)。