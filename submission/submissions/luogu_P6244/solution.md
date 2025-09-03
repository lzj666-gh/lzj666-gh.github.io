# P6244 题解

贪心。

考虑：结束越早，留给后面的时间就越多，就能参加更多的活动。

思路：将结束时间（即$t_i+l_i$）排序，遍历，如果该活动能参加就参加，不能就拉倒。

```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int n;
struct node{//记录t[i]和l[i] 
	int t,l;
}a[10010];
bool cmp(node a,node b){//结束时间早的优先 
	return a.t+a.l<b.t+b.l;
}
int main(){
	cin>>n;
	for(int i=1;i<=n;i++){//输入 
		cin>>a[i].t>>a[i].l;
	}
	sort(a+1,a+n+1,cmp);//按结束时间早的排序 
	int end=a[1].t+a[1].l,ans=1;//总得参加一个吧 
	//end记录最晚的一项的结束时间 
	for(int i=2;i<=n;i++){
		if(a[i].t>=end){//可以参加，即下一项开始时间比上一项结束时间晚 
			ans++;//可以参加 
			end=a[i].l+a[i].t;//这是最晚的结束时间 
		}
	}
	cout<<ans<<endl;
	return 0;
}

```