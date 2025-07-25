# SP15637 题解

算法：线性dp

由于题目要求合影的队列每行每列都是单调的，所以我们可以从1-n进行安排。非常明显的是由于每排的身高都是递减的，所以新加入的学生只能站到每排的末尾。我们考虑使用a1，a2...ak来表示每一排安排的学生人数，那么我们在加入一个新的学生时，必定把他放到一个满足这一行暂未放满且这一行人数目前比前一行人数要少（否则把之后身高比较矮的学生放到上一行，不符合单调性）

于是当k=5时，我们使用dp[a1][a2][a3][a4][a5]来表示每排分别站了a1,a2,a3,a4,a5人时的方案数量，依照接下来（我会放在代码的注释里）的规则进行转移，最终得出答案即可。

而当k<5时，我们插入空行把行数补齐，再按k=5进行处理。

注意，如果按dp[30][30][30][30][30]开空间会爆炸，所以我们应该在输入每行人数后再开数组。

代码


------------
```cpp
#include<cstdio>
#include<cstring>
typedef long long ll;
int k;
int n[6];
void work() {
	memset(n,0,sizeof(n));
	for(int i=1;i<=k;i++)
		scanf("%d",&n[i]);
	ll f[n[1]+1][n[2]+1][n[3]+1][n[4]+1][n[5]+1];//输入每行需要人数后再开数组。
	memset(f,0,sizeof(f));
	f[0][0][0][0][0]=1;
	for(int a1=0;a1<=n[1];a1++)
		for(int a2=0;a2<=n[2];a2++)
			for(int a3=0;a3<=n[3];a3++)
				for(int a4=0;a4<=n[4];a4++)
					for(int a5=0;a5<=n[5];a5++) {
						if(a1<n[1]) f[a1+1][a2][a3][a4][a5]+=f[a1][a2][a3][a4][a5];//若第一排没有放满则向第一排增加一个学生方向转移。
						if(a2<n[2]&&a2<a1) f[a1][a2+1][a3][a4][a5]+=f[a1][a2][a3][a4][a5];//若第二排没有放满并且第二排人数比第一排少（至于为何如此上面有提到）就向第二排增加一个学生的方向转移
						if(a3<n[3]&&a3<a2) f[a1][a2][a3+1][a4][a5]+=f[a1][a2][a3][a4][a5];//3,4,5排同理
						if(a4<n[4]&&a4<a3) f[a1][a2][a3][a4+1][a5]+=f[a1][a2][a3][a4][a5];
						if(a5<n[5]&&a5<a4) f[a1][a2][a3][a4][a5+1]+=f[a1][a2][a3][a4][a5];
					}
	printf("%lld\n",f[n[1]][n[2]][n[3]][n[4]][n[5]]);
}
int main() {
	while(scanf("%d",&k)!=EOF&&k) work();
	return 0;
}
```
做题时看了lyd的那本蓝书，因此才搞明白这道题的做法，在此感谢