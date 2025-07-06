# P1776 题解

为什么都没有人用单调队列？	
那就补一发单调队列优化多重背包吧。
w表示物品重量，v表示价值，c表示数量，我们知道朴素状态转移方程： 	
```
f[i][j]=max(f[i−1][j−w∗k]+v∗k);(k<=c)
```	
现在我们要把这个方程变成一个单调队列可以优化的形式，于是我们假设:d=j mod w[i],s=⌊j/w[i]⌋ 	
```
f[i][j]=max(f[i−1][d+w∗k]−v∗k)+v∗s(s-k<=c) 
```
之后我们枚举余数d，然后对于每个余数d都用单调队列优化即可。
```cpp
#include<cstdio>
#include<algorithm>
using namespace std;
int n,V,ans,head,tail,q[40010],q2[40010],dp[40010];
int main(){
	scanf("%d%d",&n,&V);
	for(int i=1;i<=n;i++){
		int v,w,c;
		scanf("%d%d%d",&w,&v,&c);
		if(v==0){
			ans+=w*c;
			continue;
		}
		int k=V/v;
		c=min(c,k);
		for(int d=0;d<v;d++){
			head=tail=0;
			k=(V-d)/v;
			for(int j=0;j<=k;j++){
				while(head<tail&&dp[d+j*v]-j*w>=q2[tail-1])
					tail--;
				q[tail]=j;
				q2[tail++]=dp[d+j*v]-j*w;
				while(head<tail&&q[head]<j-c)
					++head;
				dp[d+j*v]=max(dp[d+j*v],q2[head]+j*w);
			}
		}
	}
	printf("%d",ans+dp[V]);
	return 0;
}
  ```