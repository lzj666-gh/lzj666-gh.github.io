# P3531 题解

交换相邻两个数就决定了是求逆序对

对于A中的一个字符在B中的位置，我们可以发现同一个字符肯定是按从前往后的顺序出现在B中的。

比如A串ABABA，B串BAABA

我们肯定是把A中的第一个A放在B中的第一个A上，依次类推。

因为如果第一个A放在了后面，那么就有可能产生更对逆序对（因为你把大的数放在了前面）。由此得证。

好吧其实也挺显然的，我也是无聊才来水水题解的。

下面是代码（楼上那位ZJa队爷不放真是可惜了）

```cpp
#include<bits/stdc++.h>
using namespace std;
int c[26][1000001],n,a[1000001],d[26];
long long f[1000001];
int lowbit(int x){
	return x&(-x);
}
void insert(int x){
	int i;
	for(i=x;i<=n;i+=lowbit(i))f[i]++;
}
long long query(int x){
	int i;
	long long ans=0;
	for(i=x;i;i-=lowbit(i))ans+=f[i];
	return ans;
}
int main(){
	long long ans=0;
	int i;
	char s[1000001],s1[1000001];
	scanf("%d",&n);
	scanf("%s",s);
	scanf("%s",s1);
	for(i=0;i<n;i++)
		c[s[i]-'A'][++c[s[i]-'A'][0]]=i;
	for(i=0;i<n;i++){
		a[i+1]=c[s1[i]-'A'][++d[s1[i]-'A']]+1;
	}	
	for(i=1;i<=n;i++){
		//printf("%d\n",i);
		ans+=query(n)-query(a[i]-1);
		//printf("%d\n",i);
		insert(a[i]);
	}
	printf("%lld",ans);
}
```