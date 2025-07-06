# P2504 题解

题目很水  
代码简单易懂  
~~偷看了一下标签~~  
## 没错就是生成树！！！  
# 思路：
把两个点之间的距离算出来，一边Kruskal，记录下最大的边，和每只猴子的跳跃距离比较一下，如果跳跃距离大就ans++。    

最后附上代码    

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,m,k,ans=0;
double sum=-1;
int a[1000005][3],b[1000005],pre[1000005];//	前面一直RE，开大一点；

struct zzz {
	int x,y;
	double p;
} z[1000005];

int cmp(zzz k,zzz d) {
	return k.p<d.p;
}

int find(int x) {
	if(pre[x]==x)
		return x;
	return pre[x]=find(pre[x]);
}

int main() {
	cin>>m;
	for(int i=1; i<=m; i++) {
		cin>>b[i];
	}
	cin>>n;
	for(int i=1; i<=n; i++) {
		cin>>a[i][1]>>a[i][2];
	}
	for(int i=1; i<=n; i++) {
		for(int j=1; j<=n; j++) {
			if(i!=j) {
				k++;
				z[k].x=i;
				z[k].y=j;
				z[k].p=sqrt((a[i][1]-a[j][1])*(a[i][1]-a[j][1])+(a[i][2]-a[j][2])*(a[i][2]-a[j][2]));
			}
		}
	}	
	int cnt=n;//Kruskal！！！
	sort(z+1,z+k+1,cmp);
	for(int i=1; i<=n; i++) {
		pre[i]=i;
	}
	for(int i=1; i<=k; i++) {
		if(cnt==1)
			break;
		int s1=find(z[i].x),s2=find(z[i].y);
		if(s1!=s2) {
			pre[s1]=s2;
			cnt--;
			sum=z[i].p;
		}
	}
	for(int i=1; i<=m; i++) {//比较
		if(sum<=b[i])
			ans++;
	}
	cout<<ans<<endl;//完美输出
	return 0;
}
```
## 第三次发题解，有错误请各位神犇指点  

最后安利一下我的[博客](https://www.luogu.org/blog/zhaozizhuo/)
