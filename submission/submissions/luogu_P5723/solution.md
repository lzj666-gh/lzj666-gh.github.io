# P5723 题解

一道练习筛质数的练手题。

[请先AC此题](https://www.luogu.com.cn/problem/P3383)。

网上有很多关于筛素数的帖子、博文，可以自学一下。

思路：暴力枚举$1-n$的所有素数，如果当前$i$是素数并且$sum+i≤n$，则$sum+=i$，输出$i$，$x+1$。否则，就输出$x$。


$80$分$code$：

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,x;
long long sum=0;
int pd(int y) {
	for(int i=2; i*i<=y; ++i) {
		if(y%i==0) return 0;
	}
	return 1;
}
int main() {
	scanf("%d",&n);
	for(int i=2; i<=n; ++i) {
		if(i%2==0&&i!=2) continue;
		if(sum+i>n) {
			printf("%d\n",x);
			return 0;
		}
		if(pd(i)) {
			printf("%d\n",i);
			sum+=i;
			x++;
		}
	}
	return 0;
}
```

感谢[洛谷万岁](https://www.luogu.com.cn/user/95333)和[死神审判](https://www.luogu.com.cn/user/242984)指正蒟蒻的错误~

错因分析：上述代码$for$循环中，$i$最小为$2$。但是题目里没有保证$n≥2$，所以，当$n≤2$时会出现错误。

解决方法：加两个特判。

$AC$ $Code$：

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,x;
long long sum=0;
int pd(int y) {
	for(int i=2; i*i<=y; ++i) {
		if(y%i==0) return 0;
	}
	return 1;
}
int main() {
	scanf("%d",&n);
	if(n<2) {
		printf("0\n");
		return 0;
	} else if(n==2) {
		printf("2\n1\n");
		return 0;
	}
	for(int i=2; i<=n; ++i) {
		if(i%2==0&&i!=2) continue;
		if(sum+i>n) {
			printf("%d\n",x);
			return 0;
		}
		if(pd(i)) {
			printf("%d\n",i);
			sum+=i;
			x++;
		}
	}
	return 0;
}
```
