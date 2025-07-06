# P9473 题解

题面中设 $n$ 个数的最大公因数为 $g$，最小公倍数为 $l$。为了方便，这篇题解沿用题面中的变量。

众所周知，$g$ 一定能整除 $a_i$。设 $\Pi a_i=a_1\times a_2\times\dots\times a_n$，将 $a_1,a_2,a_3,\dots,a_{n-1}$ 全部除以 $g$，这 $n$ 个数的 $l$ 仍然不会变。所以 $l$ 不可能大于 $\frac{\Pi a_i}{g^{n-1}}$。又因为题面要让 $l\times g=\Pi a_i$，所以必须要保证 $g\ge g^{n-1}$，也就是 $g^2\ge g^n$。又因为 $n\ge2,g\ge1$，所以[容易解得](https://www.desmos.com/calculator/0twjhc4zdy?lang=zh-CN)在 $g=1$ 或 $n=2$ 的时候，$g\times l$ 才有可能为 $\Pi a_i$。不过，此时还需要保证 $l=\frac{\Pi a_i}{g^{n-1}}$，才能保证 $l\times g=\Pi a_i$。

1. $n=2$ 时，$l=\operatorname{lcm}(a_1,a_2)=\frac{a_1\times a_2}{\gcd(a_1,a_2)}=\frac{\Pi a_i}{g}$，所以 $l\times g$ 必然等于 $\Pi a_i$。所以，当 $n=2$ 时直接输出 `Yes` 即可，不需要更多的运算。
2. $g=1$ 时，要让 $l\times g=\Pi a_i$，必须要 $l=\Pi a_i$。若 $n$ 个数的最小公倍数等于它们的积，则这 $n$ 个数两两互质。所以，当 $g=1$ 时，必须要判断这 $n$ 个数是否两两互质。如果是，则输出 `Yes`，否则输出 `No`。

那么，怎么判断 $n$ 个数是否两两互质呢？

首先，开一个 `bool` 数组，记录 $a$ 中的某一个数是否含有这个质因数。接着，将 $a$ 中的每一个数进行分解质因数。分解出一个新的质因数 $p$，这个 `bool` 数组的第 $p$ 项就设为 $1$。如果发现这一项已经为 $1$，就说明 $a$ 数组前面有一项含有质因数 $p$，而这两项就不是互质的。此时就退出循环，输出 `No`。

如果分解完 $a$ 的每一项都没有发现有两个数不是互质的，则这 $n$ 个数两两互质，输出 `Yes`。

可以提前筛一遍 $10^8$ 以内的质数，把分解质因数的复杂度从 $\sqrt n$ 降到 $\ln n$。

最后注意，输出是 `Yes` 和 `No`，不是 `YES` 和 `NO`。比赛时差点在这里踩坑（这算坑吗？）。

赛时 AC 代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
//当 n=2 时输出 YES
//当 gcd=1 时判断是否两两互质，如果是输出 YES
int p[6000000];//存质数
bool x[100000001];//存是否不是质数
void s(){//筛质数 
	p[1]=2;
	x[1]=0;//1 不是质数 
	int cnt=1;//筛出的质数个数
	for(int i=2;i<100000000;i++){
		if(!x[i]){//是质数 
			p[++cnt]=i;
		}
		for(int j=1;j<=cnt&&(long long)(i)*p[j]<=100000000;j++){
			x[i*p[j]]=1;//x[i*p[j]] 不是质数 
			if(i%p[j]==0){
				break;
			}
		}
	}
}
int main(){
	s();
	ios::sync_with_stdio(false);
	int t;cin>>t;
	while(t--){
		int n;cin>>n;
		int a[n];
		cin>>a[0];
		int gcd=a[0];
		for(int i=1;i<n;i++){
			cin>>a[i];
			gcd=__gcd(gcd,a[i]);
		}//求这 n 个数的 gcd
		if(n==2)cout<<"Yes"<<endl;//e 和 s 是小写 
		else if(gcd==1){
			//判断 n 个数是否两两互质
			bool b[100000000];//记录每个质因数是否出现过 
			for(int i=0;i<100000000;i++)b[i]=0;
			bool f=1;//目前是否两两互质 
			for(int i=0;i<n;i++){
				//分解 a[i] 的质因数
				for(int j=1;p[j]*p[j]<=a[i];j++){
					if(a[i]%p[j]==0){
						if(b[p[j]]==1){//这个质数之前出现过了 
							f=0;//并非两两互质
							break; 
						}
						while(a[i]%p[j]==0){
							a[i]/=p[j];
						}
						b[p[j]]=1;//p[j] 这个质数出现过了 
					}
				}
				if(a[i]!=1){
					if(b[a[i]]==1){
						f=0;
					}else{
						b[a[i]]=1;
					}
				}
				//判断到目前为止是否全部互质 
				if(f==0){
					cout<<"No"<<endl;//o 是小写 
					break;
				}
				//接下来判断下一个数 
			}
			if(f){//n 个数两两互质 
				cout<<"Yes"<<endl;//e 和 s 是小写
			} 
		}else{
			cout<<"No"<<endl;//o 是小写 
		}
	}
	return 0;
}
```