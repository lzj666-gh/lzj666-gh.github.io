# P5116 题解

按照题意纯模拟即可。

这一题是 $\mathrm{for}$ 循环小练。

---

具体思路见代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
int c[4],m[4];//c数组是容量，m数组是桶里牛奶的数量 
int main()
{
	for(int x=1;x<=3;x++)cin>>c[x]>>m[x];//输入 
	for(int x=1;x<=100;x++){//循环模拟100次
		int f=(x-1)%3+1,s;//f是要将牛奶倒出的桶，s则是倒入的桶
		if(f==3)s=1;//桶3要倒给桶1
		else s=f+1;//否则就倒给下一个桶
		int mi=min(c[s]-m[s],m[f]);//mi是倒牛奶的数量，取桶s剩余容积和桶f牛奶数量的最小值 
		m[f]-=mi;//桶f倒出 
		m[s]+=mi;//桶s倒入 
	}
	cout<<m[1]<<endl<<m[2]<<endl<<m[3];//输出 
	return 0;
}
```
$\mathrm{Upd:2019.12.11:}$ 添加 $\mathrm{Latex}$，美化文章。