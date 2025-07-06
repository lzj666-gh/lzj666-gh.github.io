# P5710 题解

看到没有用位运算的我就来发篇题解。

我们可以写出判断是否满足条件的两个函数：

```
int a(int x) {return !(x%2);}
int b(int x) {return x>4&&x<=12;} 
```

小A想要两个都满足 $\Rightarrow$ ```a(x)&b(x)=1;```

Uim想要至少一个满足 $\Rightarrow$ ```a(x)|b(x)=1;```

八尾勇想要刚好一个满足 $\Rightarrow$ ```a(x)^b(x)=1;```

正妹想要两个都不满足 $\Rightarrow$ ```!a(x)&!b(x)=1.```

由于符合想要的就输出1，不符合想要的就输出 0，那我们直接输出表达式的值就好了，后面可以不判断是否等于1.

```cpp
#include<cstdio>
using namespace std;
int x;
int a(int x) {return !(x%2);}//判断第一个条件
int b(int x) {return x>4&&x<=12;} //判断第二个条件
int main()
{
	scanf("%d",&x);//输入
	return !printf("%d %d %d %d",a(x)&b(x),a(x)|b(x),a(x)^b(x),!a(x)&!b(x));//分别判断
 } //结束awa
```
