# P9472 题解

按照字典序的定义，对于第 $0$ 项不一样的情况，肯定是第 $0$ 项小的字典序就小，第 $0$ 项大的字典序就大。

如果第 $x,y$ 个数列的第 $0$ 项相同（设都是 $s$），那么它们的第 $1$ 项应该分别是 $x\times s$ 和 $y\times s$。$x$ 和 $y$ 不相等，所以这两个数列的第一项不同。此时通过第 $1$ 项就能给这两个数列排序。

所以，要按字典序排序，只需要知道一个序列的前两项。

排序时，先按两个序列的第 $0$ 项排序，如果相同，再按第 $1$ 项排序即可。

需要注意的是，一个序列的第一项可能超过 `int` 的表示范围，所以要开 `long long`。我在赛时就是因为没开 `long long`，$100pts\to40pts$。

```cpp
#include<bits/stdc++.h>
using namespace std;
struct arr{
	long long a0;//第 0 项
	long long a1;//第 1 项 
	long long n;//编号 / 公比
}a[114514];
bool cmp(arr x,arr y){
	if(x.a0!=y.a0)return x.a0<y.a0;
	else return x.a1<y.a1;
}//按字典序从小到大排序
int main(){
	ios::sync_with_stdio(false);
	long long n,m;cin>>n>>m;
	for(int i=1;i<=n;i++){
		a[i].n=i;//编号为 i 
		cin>>a[i].a0;//输入第 0 项 
		a[i].a1=a[i].a0*i;//计算第 1 项 
	}
	sort(a+1,a+1+n,cmp);//按字典序从小到大排序
	for(int i=1;i<=n;i++){//按字典序排序完成，直接按顺序输出编号 
		cout<<a[i].n<<" ";
	} 
	return 0;
}
```