# B2005 题解

依照题意即可。

首先定义一个字符类型 ch，用 cin 输入。

第一行的组成：两个空格加一个字符；

第二行的组成：一个空格加三个字符；

第三行的组成：直接输出五个字符。

依照上面的方法模拟即可。

代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
int main(){
	char ch;
	cin>>ch;
	cout<<"  "<<ch<<endl<<" "<<ch<<ch<<ch<<endl<<ch<<ch<<ch<<ch<<ch;
}
```
