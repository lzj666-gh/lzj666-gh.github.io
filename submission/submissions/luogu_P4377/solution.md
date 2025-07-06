# P4377 题解

### 这道题所需要的知识点是：01分数规划 背包dp

 首先01分数规划更像是一种数据的转化，相信不少童鞋都试着贪心来着，然额几经波折的你最后也许会发现贪心是彻底错误的，归结到底还是因为这个式子有个“/”号╰（‵□′）╯
 
而01分数规划就是将这样的数据处理需求“可贪心化”，下面看看她是怎么做到的

首先定义一个数组x，x[i]表示的是这一头牛拿不拿，如果拿赋值成1，不拿就是0

那么则有答案R=sigma(t[i]\*x[i])/sigma(w[i]\*x[i])我们需要R最大，现在我们假设有一个没那么优的答案Z满足Z<=R，那么就会有如下的式子：
	sigma(t[i]\*x[i])>=sigma(w[i]\*x[i])\*Z
    
也就是sigma((t[i]-w[i])\*x[i]\*Z)>=0
    
我天！每头牛的贡献竟然变成了(t[i]-w[i])\*x[i]\*Z，与其他牛无关了有木有！这下不久可以贪心了吗！只要在最优选取的状态下可以使总和非负，就说明这个Z是可行的，答案还可以进一步变大！

所以，与二分配合，进行01分数规划就是这题的第一步。

然而在验证的时候也有些小问题，这里要求奶牛们的总质量必须不小于W，这就很难愉快的贪心了啊。。。不过我们还有应对办法，用背包啊！

设f[i]为当前选择的奶牛总质量为i时sigma((t[i]-w[i])\*x[i]\*Z)最大是多少，因为这有可能是负数，所以初值最好弄成负无穷

接下来以零一背包的模式dp就好了，不过要注意，要把所有总质量大于等于W的更新全算在f[W]上。这里如果有点蒙可以详见代码

总之希望这篇题解对你有帮助！d=====(￣▽￣*)b
```cpp
#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int n,W;
int w[300],t[300];
long long f[10000];
bool check(int z){
	memset(f,128,sizeof(f));f[0]=0;
	long long tmp=f[W];
	for(int i=1;i<=n;i++){
		for(int j=W;j>=0;j--)if(f[j]!=tmp){
			int jj=j+w[i];jj=min(jj,W);
			f[jj]=max(f[jj],f[j]+t[i]-(long long)w[i]*z);
		}
	}
	return f[W]>=0;
}
int erfen(){
	int l=0,r=1000000;
	while(l<=r){
		int mid=l+r>>1;
		if(check(mid))l=mid+1;
		else r=mid-1;
	}
	return l-1;
}
int main(){
	scanf("%d%d",&n,&W);
	for(int i=1;i<=n;i++){
		scanf("%d%d",&w[i],&t[i]);
		t[i]*=1000;
	}
	printf("%d",erfen());
	return 0;
}
```