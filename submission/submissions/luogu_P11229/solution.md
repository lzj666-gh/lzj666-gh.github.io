# P11229 题解

## 题意概括

给你一个自然数 $N$，使这 $N$ 根木棍能摆出最小得数（不含前导 $0$）

## 思路

分类讨论，其实看特殊性质就知道可以打 $N \bmod 7$ 的余数打表。

- 余数为 $0$：答案为 $N \div 7$ 个 $8$。
  
- 余数为 $1$：
  - $N = 1$ 特判，无答案，输出 $-1$。
  - 剩下答案为 $10$ 拼接 $(N - 8) \div 7$ 个 $8$。

- 余数为 $2$：答案为 $1$ 和 $(N - 2) \div 7$ 个 $8$。

- 余数为 $3$：
  - $N = 3$ 特判，答案为 $7$。
  - $N = 10$ 特判，答案为 $22$。
  - 剩下答案为 $200$ 拼接 $(N - 17) \div 7$ 个 $8$。

- 余数为 $4$：
  - $N = 4$ 特判，答案为 $4$。
  - 剩下答案为 $20$ 拼接 $(N - 11) \div 7$ 个 $8$。

- 余数为 $5$：
  - 答案为 $2$ 拼接 $(N - 5) \div 7$ 个 $8$。

- 余数为 $6$：
  - 答案为 $6$ 拼接 $(N - 6) \div 7$ 个 $8$。

## 代码

```cpp
#include<bits/stdc++.h>
#define sjh0626s return
#define code 0
using namespace std;
long long n,t,ans,stick[10]={6,2,5,5,4,5,6,3,7,6}; 
int main(){
	cin>>t;
	while(t--){
		cin>>n;
		ans=1e9+1;
		if(n==1)cout<<-1;
		else if(n==2)cout<<1;
		else if(n==3)cout<<7;
		else if(n==4)cout<<4;
		else if(n==5)cout<<2;
		else if(n==6)cout<<6;
		else if(n==7)cout<<8;
		else if(n%7==0)for(int i=1;i<=n/7;i++)cout<<8;
		else if(n%7==1){
			cout<<10;
			for(int i=1;i<=(n-8)/7;i++)cout<<8;
		}
		else if(n%7==2){
			cout<<1;
			for(int i=1;i<=(n-2)/7;i++)cout<<8;
		}
		else if(n%7==3){
			if(n==10)cout<<22;
			else {
				cout<<200;
				for(int i=1;i<=(n-17)/7;i++)cout<<8;
			}
		}
		else if(n%7==4){
			cout<<20;
			for(int i=1;i<=(n-11)/7;i++)cout<<8;
		}
		else if(n%7==5){
			cout<<2;
			for(int i=1;i<=(n-5)/7;i++)cout<<8;
		}
		else if(n%7==6){
			cout<<6;
			for(int i=1;i<=(n-6)/7;i++)cout<<8;
		}
		cout<<"\n";
	}
	sjh0626s code;
}
```