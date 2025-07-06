# P5745 题解

## Uid 2019-12-27:修改了树状数组代码的时间复杂度的重要性

这题难度不大，但对于新手来说，不算很友好。所以我们循序渐进，慢慢来刨析这道题目

# 10分代码：

很容易想到枚举所有的$i$到$j$,再对$i$到$j$进行求和，再判断是否满足条件，满足就更新答案。

时间复杂度$O(n^3)$

## 代码:

```cpp
#include <bits/stdc++.h>
using namespace std;
int n,m;
int a[4000001];
int ans1,ans2,ans3;
int main(){
	cin>>n>>m;
	for(int i=1; i<=n; i++){//读入
		scanf("%d",&a[i]);
	}
	for(int i=1; i<=n; i++){
		for(int j=i; j<=n; j++){//枚举i与j
			int sum=0;
			for(int k=i; k<=j; k++){//求和
				sum+=a[k];
			}
			if(sum>ans3&&sum<=m){//如果这个答案比以前的更优，则更新答案
				ans1=i;
				ans2=j;
				ans3=sum;
			}
		}
	}
	cout<<ans1<<" "<<ans2<<" "<<ans3;//输出
}
```
# 30分代码：

因为要对区间进行求和，自然就会想到前缀和来维护。

我们记$sum_i=a_1+a_2+......+a_i$

则$a_l+a_{l+1}+......a_r=sum_r-sum{l-1}$

在读入的过程中预处理前缀和

时间复杂度：$O(n^2)$

## 代码:

```cpp
#include <bits/stdc++.h>
using namespace std;
int n,m;
int a[4000001];
int sum[4000001];//用sum数组来记录前缀和
int ans1,ans2,ans3;
int main(){
	cin>>n>>m;
	for(int i=1; i<=n; i++){
		scanf("%d",&a[i]);
		sum[i]=sum[i-1]+a[i];//处理前缀和
	}
	for(int i=1; i<=n; i++){
		for(int j=i; j<=n; j++){
        int cnt=sum[j]-sum[i-1];
			if(cnt>ans3&&cnt<=m){//计算前缀和并更新答案
				ans1=i;
				ans2=j;
				ans3=cnt;
			}
		}
	}
	cout<<ans1<<" "<<ans2<<" "<<ans3;
}
```
# 60分代码:

因为所有的$a_i$都是正整数，故sum单调递增。

所以若的$sum_r-sum_{l-1}>m$,

因为$sum_{r+1}>sum_{r}$

故$sum_{r+1}-sum_{l-1}>m$

后面的$sum_{r+k}-sum_{l-1}>m$

所以就可以break了

时间复杂度:$O(n^2)$+小常数

## 代码：

```cpp
#include <bits/stdc++.h>
using namespace std;
int n,m;
int a[4000001];
int sum[4000001];
int ans1,ans2,ans3;
int main(){
	cin>>n>>m;
	for(int i=1; i<=n; i++){
		scanf("%d",&a[i]);
		sum[i]=sum[i-1]+a[i];
	}
	for(int i=1; i<=n; i++){
		for(int j=i; j<=n; j++){
        int cnt=sum[j]-sum[i-1];
			if(cnt>ans3&&cnt<=m){
				ans1=i;
				ans2=j;
				ans3=cnt;
			}
			if(cnt>m) break;//如果比m大就可以退出了，不必要继续枚举了
		}
	}
	cout<<ans1<<" "<<ans2<<" "<<ans3;
}
```

# 100分代码:

因为sum单调递增。

所以考虑枚举i，再二分确定j

时间复杂度:$O(nlogn)$

## 代码:

```cpp

#include <bits/stdc++.h>
//#include <windows.h>
using namespace std;
long long sum[4000001];
long long n,m;
long long a[4000001];
int ans1,ans2,ans3;
int main(){
	cin>>n>>m;
	for(int i=1; i<=n; i++){//预处理前缀和
		scanf("%d",&a[i]);
		sum[i]=sum[i-1]+a[i];
	}
	for(int i=1; i<=n; i++){
		int l=i,r=n;
		while(l<=r){//二分确定最优的j
			int mid=(l+r)/2;
			if(sum[mid]-sum[i-1]>m){
				r=mid-1;
			} else {
				l=mid+1;
			}
		}
		if(sum[r]-sum[i-1]<=m){//对于当前的i来说，这个j已经是最优的了，所以更新答案
			if(sum[r]-sum[i-1]>ans3){
				ans1=i;
				ans2=r;
				ans3=sum[r]-sum[i-1];
			}
		}
	}
	cout<<ans1<<' '<<ans2<<' '<<ans3;  
	return 0;	
}
```

# $O(n)$的做法:

关注kkksc03的人一定知道，这道题kkksc03曾经提到过!

kkk在最后给出的做法是：

>维护一个队列，让数组中的数依次入队，并记录其的元素和，若大于m,则让对首出列，更新答案，再让后面的数字继续入队，并更新答案，不断的这么操作，直到所有数字都入过队了为止。

我这里采用了STL的deque(双端队列),感兴趣的Oler们可以去了解一下

## 代码:
```cpp
#include <bits/stdc++.h>
using namespace std;
int n,m;
int a[4000001];
deque<int>q;
int sum=0;
int ans1,ans2,ans3;
int main(){
	cin>>n>>m;
	for(int i=1; i<=n; i++){
		scanf("%d",&a[i]);
	}
	int l=1;
	for(int i=1; i<=n; i++){
		q.push_back(a[i]);//插入a[i]
		sum+=a[i];
		while(sum>m){//如果队列中的值大于m,则对队列进行维护
			q.pop_front();//弹去队首
			sum-=a[i];//更新答案
			if(sum>ans3){
				ans3=sum;
				ans2=i-1;
				ans1=l;
			}
			sum+=a[i];//维护队列中的元素的和
			sum-=a[l];
			l++;
		}
	}
	cout<<ans1<<" "<<ans2<<" "<<ans3;
}
```

# $O(nlog^2n)$的做法

还有一种做法是使用树状数组。

我们知道树状数组也能对区间进行求和，所以可以使用在之前二分的代码加上树状数组

不会树状数组也没关系，你可以去洛谷找到树状数组的模板题，对其进行学习。

## 代码:
```cpp
#include <bits/stdc++.h>
//#include <windows.h>
using namespace std;
int c[8000001];
int n,m;
int a[4000001];
int lowbit(int n){//树状数组的核心函数
	return n&(-n);
}
int add(int x,int y){//单点修改
	for(;x<=n; x+=lowbit(x)) c[x]+=y;
}
int sum(int x){//区间求和
	int ans=0;
	for(;x;x-=lowbit(x)) ans+=c[x];
	return ans;
}
int ans1,ans2,ans3;
int main(){
	cin>>n>>m;
	for(int i=1; i<=n; i++){
		scanf("%d",&a[i]);
		add(i,a[i]);
	}
	for(int i=1; i<=n; i++){//二分的步骤
		int l=i,r=n;
		while(l<=r){
			int mid=(l+r)/2;
			if(sum(mid)-sum(i-1)>m){
				r=mid-1;
			} else {
				l=mid+1;
			}
		}
		int cnt=sum(r)-sum(i-1);
		if(cnt<=m){
			if(cnt>ans3){
				ans1=i;
				ans2=r;
				ans3=cnt;
			}
		}
	}
	cout<<ans1<<' '<<ans2<<' '<<ans3;  
	return 0;	
}
```