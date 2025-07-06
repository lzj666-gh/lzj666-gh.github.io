# P9459 题解

# 原题链接
[P9459 浴眼盯真](https://www.luogu.com.cn/problem/P9459)

# 题目简述

给定 $t$ 组测试数据，对于每组数据，输入 $4$ 个字符串，如果：

- $a,b$ 的首字母均为 ```y```。
- $c$ 恰好等于 ```ding```。
- $d$ 恰好等于 ```zhen```。

就输出```Yes```，否则就输出```No```。


# 解题思路

对于每组测试数据，只需要将这 $3$ 个条件分别判定结果即可，如果判定的结果都为```true```，就输出```Yes```，否则就输出```No```。

# 参考代码

```cpp
#include<bits/stdc++.h>
using namespace std;
int n;//n组测试数据
string a,b,c,d;//定义a,b,c,d字符串
int main()
{
	cin>>n;//输入测试数据
	for(int i=1;i<=n;i++)
	{
		cin>>a>>b>>c>>d;//输入a,b,c,d四个字符串
		if(a[0]==b[0] && a[0]=='y' && c=="ding" && d=="zhen")//依次判定3个条件
			cout<<"Yes"<<endl;//如果全都满足，输出Yes
		else
			cout<<"No"<<endl;//否则输出No
	}
    return 0;
}

```
