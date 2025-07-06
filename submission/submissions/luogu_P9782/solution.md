# P9782 题解

[博客食用观感更佳](https://www.luogu.com.cn/blog/Czel-X/ti-xie-7-post)
# 简要题意
有两个字符串 $s$ 和 $t$，代表 26 进制下的数字，求同样用字符串表示的他们的和。
# 分析
我的思路是先将输入的字符串转化为数字相加，再转化为输出结果。

由于输入的只能是两个一位数，所以只有两种情况：结果为一位数或以 $B$ 开头的两位数，分别判断就好。
# 代码
```cpp
#include<bits/stdc++.h>
using namespace std;
string a,b;
int x,y;
int main(){
	cin>>a>>b;
	x=a[0]-'A';
	y=b[0]-'A';
	x+=y;
	if(x<=25){
		char ans='A'+x;
		cout<<ans;
	}
	else{
		cout<<'B';
		char ans='A'+x-26;
		cout<<ans;
	}
}
```
感谢阅读！