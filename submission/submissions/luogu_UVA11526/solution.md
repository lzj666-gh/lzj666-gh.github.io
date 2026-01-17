# UVA11526 题解

我看题解里没有这么写的，就补一个

![](https://cdn.luogu.com.cn/upload/image_hosting/obdm4joa.png)

一目了然

不言而喻

$$
\sum_{i=1}^n\lfloor {n\over i}\rfloor=2\sum_{i=1}^{\lfloor\sqrt n\rfloor}\lfloor {n\over i}\rfloor-\lfloor\sqrt n\rfloor^2
$$
```cpp
int f(int n){
	int m=sqrt(n),ans=0;
	for(int i=1;i<=m;i++)ans+=n/i;
	return ans*2-m*m;
}
```
