# P10916 题解

显然，除了修改之外的位置 $x$ ，都可以选 $\left [x,x\right ]$，所以答案至少为 $n-1$。

然后我们考虑什么时候答案为 $n$ ，我们发扬一下智慧，容易发现 $\gcd$ 肯定减小的很快，所以我们只需要维护相邻两个数和三个数的 $\gcd$，即可通过该题。

实际复杂度 $O(n \log n)$。

### code

```cpp
#include<bits/stdc++.h>
#define ll long long
#define fi first
#define se second
#define wang_shi return 0
#define See_Time cerr<<(clock()-Time)*1.0/CLOCKS_PER_SEC<<'\n'
#define See_Memory cerr<<abs(&M2-&M1)/1024.0/1024.0<<"MB\n"
using namespace std;
const int N=5e5+10;
typedef pair<int,int> PII;
bool M1;
int n,a[N],pos[N],d[N];
void solve()
{
	cin>>n;
	for(int i=1;i<=n;++i)
	{
		cin>>a[i];
		pos[a[i]]=i;
		if(i>1) d[__gcd(a[i],a[i-1])]++;
		if(i>2) d[__gcd(a[i],__gcd(a[i-1],a[i-2]))]++;
	}
	for(int i=1;i<=n;++i)
	{
		int ans=n-1;
		if(pos[i]>1) d[__gcd(a[pos[i]],a[pos[i]-1])]--;
		if(pos[i]>2) d[__gcd(a[pos[i]],__gcd(a[pos[i]-1],a[pos[i]-2]))]--;
		if(pos[i]<n) d[__gcd(a[pos[i]],a[pos[i]+1])]--;
		if(pos[i]<n-1) d[__gcd(a[pos[i]],__gcd(a[pos[i]+1],a[pos[i]+2]))]--;
		ans+=(d[i]>0);
		cout<<ans<<" \n"[i==n];
		if(pos[i]>1) d[__gcd(a[pos[i]],a[pos[i]-1])]++;
		if(pos[i]>2) d[__gcd(a[pos[i]],__gcd(a[pos[i]-1],a[pos[i]-2]))]++;
		if(pos[i]<n) d[__gcd(a[pos[i]],a[pos[i]+1])]++;		
		if(pos[i]<n-1) d[__gcd(a[pos[i]],__gcd(a[pos[i]+1],a[pos[i]+2]))]++;
	}
}
bool M2;
int main()
{
//	freopen("1.in","r",stdin);
//	freopen("1.out","w",stdout);
	ios::sync_with_stdio(0); cin.tie(0);
	int Time=clock();
	int t=1; //cin>>t;
	while(t--) solve();
	See_Memory; See_Time;
	wang_shi;
}








```