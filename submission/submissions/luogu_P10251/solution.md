# P10251 题解

# 分析
注意每次给你的是对角两个对角，所以共有四种可能，左上右下，左下右上，两个点交换又会产生两种情况。

我们枚举这四种情况，为了方便，统计最终答案的左下和右上角，输出结果即可。

注意赋初始值。
# 代码
```cpp
#include <bits/stdc++.h>
using namespace std;
long long n,a,b,c,d,e=1000000000,f=1000000000,g=-1000000000,h=-1000000000;
int main(){
	scanf("%lld",&n);
	while(n--){
		scanf("%lld%lld%lld%lld",&a,&b,&c,&d);
		if(a<c&&b<d){
			e=min(e,a);
			f=min(f,b);
			g=max(g,c);
			h=max(h,d);
		}
		else	if(a>c&&b>d){
			e=min(e,c);
			f=min(f,d);
			g=max(g,a);
			h=max(h,b);
		}
		else	if(a<c&&b>d){
			e=min(e,a);
			f=min(f,d);
			g=max(g,c);
			h=max(h,b);
		}
		else{
			e=min(e,c);
			f=min(f,b);
			g=max(g,a);
			h=max(h,d);
		}
	}
	printf("%lld",(g-e)*(h-f));
    return 0;
}
```