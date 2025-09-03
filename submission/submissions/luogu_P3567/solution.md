# P3567 题解

看到大家的做法好正经啊~~不要被数据结构懵逼了双眼~~

向大(神)家(仙)推荐一种超好(幼)写(稚)的做法：区间随机化

注意到区间出现次数严格大于一半，根据概率相关知识，我们有大概在$\frac{1}{2}$的概率随机到这个数字，如果我们随机的次数较大，那么将会有较大概率随机到答案

考虑如何判断无解，当随机化次数达到阈值还没有得到答案，就可以近似认定为无解，下面定义阈值为$k=30$

假设我们最终得到的是有解，那么$\frac{1}{2^k}$次判断失误，概率相当小

于是我们得到了一个算法：

小范围区间直接暴力，大范围区间随机区间内的一个数字进行检验

于是问题就变成了如何检验一个数字在区间内出现的次数，神仙说：善用$STL$

直接把每个数字出现的位置丢进$vector$之后查询用$upper_bound-lower_bound$即可

于是做完了，但是同时需要一些其他的优化，尽量减少二分的次数

```cpp
#include <bits/stdc++.h>

using namespace std;

inline int R_int(){
	register int n=0;
	register char ch=getchar();
	register bool I=false;
	while(ch<'0'||ch>'9')I=(ch=='-'?1:0),ch=getchar();
	while(ch>='0'&&ch<='9')n=(n<<1)+(n<<3)+(ch^'0'),ch=getchar();
	return I?-n:n;
}

const int maxn=1000000+10;

vector<int>p[maxn];
int sta[100],top;
bool vis[maxn];
int v[maxn];
int M[maxn];
int n,m;

signed main(){
	srand((long long)new char);
	n=R_int(),m=R_int();
	for(int i=1;i<=n;i++)v[i]=R_int(),p[v[i]].push_back(i);
	for(int c=1,L,R,len;c<=m;c++){
		L=R_int(),R=R_int();len=R-L+1;
		if(len<=100){
			int tag=0;
			len=len>>1;
			for(int i=L;i<=R;i++){
				if(++M[v[i]]>len){
					tag=v[i];
					while(i>=L)--M[v[i--]];
					break;
				}
			}
			if(!tag)for(int i=L;i<=R;i++)--M[v[i]];
			printf("%d\n",tag);
		}
		else {
			int tag=0;
			for(int i=1;i<=30;i++){
				int tmp=v[rand()%len+L];
				sta[++top]=tmp;
				if(!vis[tmp]&&p[tmp].size()>(len>>1)&&std::upper_bound(p[tmp].begin(),p[tmp].end(),R)-std::lower_bound(p[tmp].begin(),p[tmp].end(),L)>(len>>1)){
					tag=tmp;break;
				}
				vis[tmp]=1;
			}
			while(top)vis[sta[top--]]=0;
			printf("%d\n",tag);
		}
	}
	return 0;
}
```