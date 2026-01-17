# P5708 题解

一道基础计算题，注意所有变量类型都为`double`。

唯一涉及到的知识点就是 $sqrt$：这是一个求根函数，在函数内填上数字或变量，这个函数就会自动返回求根后的值。

最后用`printf`输出，注意用`.1lf`返回，因为是保留一位小数。

$Code$:

```
#include<bits/stdc++.h>
using namespace std;
double a,b,c,p,ans;
int main()
{
	cin>>a>>b>>c;
	p=(a+b+c)/2;
	ans=sqrt(p*(p-a)*(p-b)*(p-c));
	printf("%.1lf",ans);
	return 0;
}
```