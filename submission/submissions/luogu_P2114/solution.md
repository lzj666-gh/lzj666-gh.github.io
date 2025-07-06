# P2114 题解

比较方便的，我用了a1和a2两个变量表示二进制全0和全1经过门之后的样子。

之后的和其他人都差不多。可能是比较短的代码了。

贪心时就能用0换1就一定换，能用1换1也换，不能换别换就好了。

```cpp
#include<bits/stdc++.h>
int n,m,ans,x,a1=0,a2=-1;
char str[5];
int main(){
	scanf("%d%d",&n,&m);
	while(n--){
		scanf("%s%d",str,&x);
		if(str[0]=='A') a1&=x, a2&=x;
		if(str[0]=='X') a1^=x, a2^=x;
		if(str[0]=='O') a1|=x, a2|=x;
	}
	for(int j=29;~j;--j){
		if(a1>>j&1) ans+=1<<j;
		else if(a2>>j&1&&(1<<j)<=m) ans+=1<<j, m-=1<<j;
	} printf("%d",ans);
	return 0;
}
```