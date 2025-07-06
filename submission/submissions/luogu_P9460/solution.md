# P9460 题解

首先，我们一看这道题，数据范围整整 $10^6$，那就不可能用枚举了，然后思考一下，我能修改 $k$ 个数，那肯定是每一次都挑选最大的，可是由于当前的最大数是实时更新的，不可能慢慢找。于是我们便找到了办法：二分！

二分的时间复杂度是 $O(n \log n)$，而 $10^6$ 刚刚好不会爆。

我们需要每次二分一条“众数线”设为 $mid$，即当一个数出现的次数大于等于 $mid$ 时，他便可能成为众数。

那 check 怎么写这个问题，就简单多了。

每次的 $x$ 首先加 $k$（因为无论选择哪个，最终 $mid$ 都会加 $k$），然后遍历计数数组（计算每个数出现的次数），如果发现大于 $x$，就把多出来的部分记下，最后把记下的数与 $k$ 比较就行了。

注意一下，若最后二分出的数为零，输出正无穷（也就是 `pigstd`）。

好了，直接上代码（赛时写的比较丑，见谅）。
```cpp
#include<bits/stdc++.h>
using namespace std;
int a[1000005],vis[1000005];
int n,k,maxa=0;//maxa为原数组中众数出现的次数
int mp[1000005];//用来存每个数出现的次数
//特殊说明：用map会TLE,int就行
int check(int x) {
	memset(vis,0,sizeof vis);
	x+=k;
	long long m=0;
	for(int i=1;i<=n;i++) {
		if(mp[a[i]]>x && vis[a[i]]==0) {
			vis[a[i]]=1;
			m+=mp[a[i]]-x;
		}
	}
	if(m>k) return 0;
	else return 1;
}
int main() {
	int ans=0;
	scanf("%d%d",&n,&k);
	for(int i=1;i<=n;i++) {
		scanf("%d",&a[i]);
		mp[a[i]]++;
		maxa=max(mp[a[i]],maxa);
	}
	if(k>=maxa) {//并无意义，只是为了方便
		printf("pigstd");
		return 0;
	}
	int l=0,r=1000000,mid;
	while(l<r) {//二分
		mid=(l+r)>>1;
		if(check(mid)) {
			r=mid;
		}
		else {
			l=mid+1;
		}
	}
	if(l==0) {
		printf("pigstd");
		return 0;
	}
	for (int i=1;i<=1e6;i++)
		if(mp[i]>=l) ans++;
	printf("%d",ans);
   return 0;
}
```