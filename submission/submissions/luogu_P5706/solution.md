# P5706 题解

第一问：将$t$毫升的快乐水分给$n$人，每人可以分到$n/k$毫升的快乐水。

第二问：一个人需要2个杯子，所以一共需要$2 \times n$个杯子。

注意$t$要是`double`型（`float`也没问题就是咯），结果保留3位小数。

代码：
```cpp
#include<bits/stdc++.h>
using namespace std;

int main(){
	double a;
	int b;
	cin>>a>>b;
	cout<<setprecision(3)<<fixed<<a/b<<endl<<b*2;
	return 0;
}
```
update:感谢某巨佬查出一处错误，感谢。