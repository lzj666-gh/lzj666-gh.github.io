# P10244 题解

# A. String Minimization

本题涉及的主要知识点：

- 【2】字符串
- 【3】贪心法

### 题意分析

题目要在 $a$ 字典序尽量小的前提下求 $b$ 字典序最小值，所以先考虑 $a$ 什么时候字典序最小。

不难发现 $a$ 的两个不同位置之间没什么关系（$a_i$ 不管是否进行操作都不会产生 $a_j$，如果 $i\ne j$），所以我们只需要把**每个字符**都求出最小值即可。

总而言之：

- 若 $a_i<c_i$，则不能对 $i$ 操作。
- 若 $a_i>c_i$，则必须对 $i$ 操作。
- 若 $a_i=c_i$，则是否操作都可以。

接下来考虑最小化 $b_i$。若 $a_i\ne c_i$ 则是否操作已经确定，只有 $a_i=c_i$ 时，才会考虑“若 $b_i>d_i$ 则交换"。

总之，若 $a_i>c_i$，或者 $a_i=c_i$ 且 $b_i>d_i$，则必须交换 $b_i,d_i$。


### 参考程序

以下为 C++ 参考代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
int n;
string a,b,c,d;
int main(){
	cin>>n>>a>>b>>c>>d;
	for(int i=0;i<n;i++)
		if(a[i]>c[i] || a[i]==c[i] && b[i]>d[i])
			b[i]=d[i];
	cout<<b<<endl;
	return 0;
}
```

以下为 Python 3 参考代码。注意 Python 的字符串不能原地修改，必须转化成列表。

```python
n=int(input())
a=input()
b=list(input())
c=input()
d=input()
for i in range(n):
    if a[i]>c[i] or a[i]==c[i] and b[i]>d[i]:
        b[i]=d[i]
print("".join(b))
```