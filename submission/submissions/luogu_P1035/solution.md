# P1035 题解

## Code

### Force $O(e^k)$

写一个`累加器`和一个`溢出灯`就行。

> 以后可能会将回归性函数称为`器`，分类性函数称为`灯`。

```c++
#include<bits/stdc++.h>
using namespace std;

bool excess(double sn,double k){ //溢出灯
	return sn > k;
}

int main(){
	int i=1;
	double sn=0,k;
	cin>>k;
	while(1){ //累加器
		sn += (double)1/(double)(i++);
		if(excess(sn,k)) {cout<<i-1;break;}
	}
	return 0;
}
```

### 数论优化 $O(logk)$

> https://www.luogu.org/problemnew/solution/P1035
>
> `exp(k)`是指数调用的复杂度，最高可以优化到`log(k)`（相当多项式幂），因此最后得到的复杂度为$O(logk)$。
>
> 值得指出的$O(logk)$仅仅是理论的，**因为最后cout打印的数的宽度已经是O(k)了**！
>
> 运算虽然可以很快，却会被输出所限制。

```c++
#include<bits/stdc++.h>
using namespace std;

bool excess(double sn,double k){
	return sn > k;
}

int main(){
	int i=1;
	double k;
	while(cin>>k){
		cout<<floor(exp(k-0.5772156649) + 0.5)<<endl;
	}
	return 0;
}
```

# 