# P5719 题解

## 解题分析

小蒟蒻不才，只会用不用循环的方法。

注意到 $1$ 到 $n$ 之间是 $k$ 的倍数的数构成了一个公差为 $k$ 的等差数列。

该数列的项数为 $p = \lfloor \frac{n}{k} \rfloor$，则首项为 $k$，末项为 $p \times k$，和为 $\dfrac{(p+1) \times k \times p}{2}$。

所以被 $k$ 整除的数平均数为 $\dfrac{(p+1) \times k}{2}$，不被 $k$ 整除的数平均数为 $\dfrac{(n+1)\times n - (p+1) \times k \times q}{2 \times (n-p)}$。

因为要求精确到小数点后 $1$ 位，记得乘上 $1.0$，并像如下代码处理精度。


```cpp
#include<bits/stdc++.h>
#define ll long long
using namespace std;
int n,k,p;
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	cin>>n>>k;
	p=n/k;
	cout<<fixed<<setprecision(1)<<(p+1.0)*k/2<<" "<<((n+1)*n/2.0-(p+1)*k*p/2.0)/(n-p)*1.0;
	return 0;
}

```