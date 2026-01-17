# SP25784 题解

## 请勿恶意评分 ##  

如果你认真读题  
其实答案已经很明朗了  
人家都告诉你是冒泡排序了  
那就写个冒泡，每次交换的时候ans++不就完了？
真这么简单？  
真的  
不信你看：
```cpp
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#define int long long
using namespace std;

const int mod=10000007;
const int maxn=200005;
int a[maxn];
int n,ans,T;
int cnt;

signed main(){
	cin>>T;
	while(T--){
		cin>>n;
		for(int i=0;i<n;i++) cin>>a[i];
		for(int i=0;i<n-1;i++){
			a[i]%=mod;
			for(int j=0;j<n-i-1;j++)
				if(a[j]>a[j+1]) ans++,ans%=mod,swap(a[j+1],a[j]);
		}
		cout<<"Case "<<++cnt<<": "<<ans%mod<<'\n';
	}
	return 0;
}
```
妥妥的  
![TLE](https://cdn.luogu.com.cn/upload/pic/61448.png)  
多好 

言归真传，说正解    
就是归并排序
二分将每个区间进行排序  
如果你看过《信息学奥赛一本通》 
里面有详细的讲解  
如何拆分和归并  
并且在每次比较时，对满足条件的进行答案的计数  
输出总数量即可

```cpp
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#define int long long
using namespace std;

const int mod = 10000007;
const int maxn=20005;
int a[maxn],r[maxn];
int ans;

inline void mosort(int s,int t){
	if(s==t) return;
	int mid=(s+t)/2;
	mosort(s,mid);
	mosort(mid+1,t);
	int i=s,j=mid+1,k=s;
	while(i<=mid && j<=t){
		if(a[i]<=a[j]){
			r[k]=a[i];
			k++,i++;
		}
		else{
			r[k]=a[j];
			k++,j++;
			ans+=mid-i+1;
			ans%=mod;	
		}
	}
	while(i<=mid){
		r[k]=a[i];
		k++,i++;
	}
	while(j<=t){
		r[k]=a[j];
		k++,j++;
	}
	for(int i=s;i<=t;i++)
		a[i]=r[i];
}

int T,n;
signed main(){
	cin>>T;
	int cnt=0;
	while(T--){
		ans=0;
		memset(a,0,sizeof a);
		cin>>n;
		for(int i=1;i<=n;i++)
			cin>>a[i];
		mosort(1,n);
		cout<<"Case "<<++cnt<<": "<<ans<<'\n';
	}
	return 0;
}
```
SP中有三道题都是这样的归并排序，放福利啦  
[SP25784](https://www.luogu.org/problemnew/show/SP25784)  
[SP9722](https://www.luogu.org/problemnew/show/SP9722)  
[SP6256](https://www.luogu.org/problemnew/show/SP6256)  
记得都要开long long  
注意数组范围，开大开小都会挂掉  
溜了~~~