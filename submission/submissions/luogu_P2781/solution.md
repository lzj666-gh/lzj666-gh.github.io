# P2781 题解

### 题解 P2781 【传教】

题意很明了，我就不多说了。这道题的难点在于如何累加。由于数据范围很大，所以我们可以先把l,r,k都存下来等到询问的时候再计算。

首先我们先把简单的（传教时的操作）写出来，代码就不放了。

好了，接下来就是计算询问的结果（询问，重点）

如果一段区间在l~r，那么就将其间的所有元素都加上k。由此我们得到式子：

$ans+=(long long)k[j]*(min(rx,r[j])-max(lx,l[j])+1)$

解释：这里还要判断只有一部分重叠的情况，如果两段区间不是完全重合的那就取重合的部分，尾部肯定要取最小，头部肯定要取最大。如果是完全重合这段代码也适用。这里要强制转换成long long。

完整代码：

```cpp
#include<iostream>
using namespace std;
int n,m,l[1010],r[1010],k[1010],cnt=0,f=0;//l，r，k3个数组是题目中所说的传教的范围和增加的信仰值，cnt是l,r,k3个数组的下标，f是判断是传教还是询问。
int main(){
	cin>>n>>m;
	for(int i=1;i<=m;i++){
		cin>>f;
		long long ans=0;//和，记得开long long
		if(f==1){//如果是传教
			cnt++;
			cin>>l[cnt]>>r[cnt]>>k[cnt];//这里不能直接用i，因为f可能是2，就会出错
		}else{//如果不是传教，是询问
			int lx,rx;//询问区间的头和尾
			cin>>lx>>rx;
			for(int j=1;j<=cnt;j++){
				if(lx<=r[j]&&rx>=l[j]){//如果有重叠
					ans+=(long long)k[j]*(min(rx,r[j])-max(lx,l[j])+1);//累加，记得强制转换成long long，不然只有80分
				}
			}
			cout<<ans<<endl;
		}
	}
	return 0;//拜拜！
}
```
