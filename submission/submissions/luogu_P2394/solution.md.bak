# P2394 题解

重要的事情说三遍，小数的精度！小数的精度！小数的精度！
------------
这道题用cin的话你就凉了，long double也回天乏力。
用cin，80分，上代码：
```
#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	long double s;//确保精度 
	cin>>s;
	s=s/23; 
	printf("%.8Lf",s);//"%.8Lf"意思是将一个long double变量s保留8位后输出 
}

```
输入文件不超过5M......![QQ截图20190806132708.png](C:\Users\Administrator\Desktop\QQ截图20190806132708.png)
很明显，**精度**不够

正当本蒟蒻不出来问题的时候，本蒟蒻突然想起scanf可以强制提高精度，于是......
```
#include<cstdio>
int main()
{
	long double s;
	scanf("%15Lf",&s);
    s=s/23;
	printf("%.8Lf",s);
}
```
AC了
点个赞再走啊~~~