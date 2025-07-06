# SP6256 题解

弱弱的问一句：  
是恶意评分咩？


正解：归并排序
这不是裸得手写sort吗  
只需要在分解的时候累加答案即可  
详情请见《信息学奥赛一本通》—— 归并排序


```cpp
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#define int long long
using namespace std;

const int maxn=200005;
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
			ans+=mid-i+1;//就是在这里累加答案，不加的话就是sort
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
	while(T--){
		ans=0;
		memset(a,0,sizeof a);
		cin>>n;
		for(int i=1;i<=n;i++)
			cin>>a[i];
		mosort(1,n);
		cout<<ans<<'\n';
	}
	return 0;
}