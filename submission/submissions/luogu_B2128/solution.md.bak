# B2128 题解

```cpp
#include<cstdio>
using namespace std;
int n,pri[50005]={},cnt=0;
int main(){
	scanf("%d",&n);//输入
	for(int i=2;i<=n;i++){//埃氏筛法
		if(pri[i])continue;
		for(int j=i+i;j<=n;j+=i)pri[j]=1;//质数的几倍是合数
	}
	for(int i=2;i<=n;i++)if(!pri[i])cnt++;//统计质数
	printf("%d",cnt);//输出
	return 0;
}

```
