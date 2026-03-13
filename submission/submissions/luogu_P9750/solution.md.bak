# P9750 题解

## 题目分析

给你 $a,b,c$ 写出 $ax^2+bx+c=0$ 这个方程最大的解，无解输出 `NO`。

也就是表示出 $\frac{-b\pm \sqrt{b^2-4ac}}{2a}$。我们把 $b^2-4ac$ 记为 $\Delta$。

如果 $\Delta<0$ 无解。

因为 $\Delta\ge 0$ 所以 $\sqrt{\Delta}\ge 0$ 较大的解是 $\frac{-b+ \sqrt{\Delta}}{2a}$。

我们把 $\sqrt{\Delta}$ 变成 $a\sqrt{b}$ 的形式后。如果 $b=0,1$ 说明解是有理数，如果是有理数记得把 $-b+\sqrt{\Delta}$ 当做整体然后除以 $2a$ 最后当做有理数输出。

注意：如果 $\sqrt{\Delta}$ 不是有理数 $\frac{-b+\sqrt{\Delta}}{2a}$ 应该表示成 $\frac{-b}{2a}+\frac{\sqrt{\Delta}}{2a}$。

然后分个体约分，对于有理数直接约分，无理数只约掉 $a\sqrt{b}$ 中的 $a$ 与分母的公因数。

注意：分母永远是正数。

难点是模拟输出，细节比较多，没什么算法，直接写在这里不直观，放在代码注释中。

再说一些常见的错误输出：

```
0+sqrt(5)
+sqrt(5)
sqrt(8)
sqrt(5)/1
1*sqrt(5)
2*sqrt(5)/4
5/-2
-5/-1
-5/2+3/2
```

## 代码实现

```cpp
#include<bits/stdc++.h> 
using namespace std;
int T,m,a,b,c,d,k,t;
int gcd(int a,int b){//最大公因数
	return b?gcd(b,a%b):a;
}
void Main(){
	cin>>a>>b>>c;
	if(a<0)
		a=-a,b=-b,c=-c;//细节1：分母非负
	d=b*b-4*a*c,k=1;//d是delta
	if(d<0){
		cout<<"NO\n";
		return;
	}//无解
	for(int i=2;i*i<=d;i++)
		while(d%(i*i)==0)
			k*=i,d/=(i*i);//k*sqrt(d)
	if(d==0||d==1){//有理数
		t=abs(gcd(2*a,-b+k*d));//细节2：取绝对值
		cout<<(-b+k*d)/t;
		if(2*a/t!=1)//细节3：分母非1
			cout<<'/'<<2*a/t;
		cout<<'\n';
		return;
	}
	//-b/2a+k*sqrt(d)/2a
	t=abs(gcd(-b,2*a));//细节2
	if(-b/t==0)//细节4：不能有0+xxx
		goto g;
	cout<<-b/t;
	if(2*a/t!=1)//细节3
		cout<<'/'<<2*a/t;
	cout<<'+';
	g:
	t=abs(gcd(k,2*a));//细节2
	if(k/t!=1)//细节5：乘数不为1
		cout<<k/t<<'*';
	cout<<"sqrt("<<d<<')';
	if(2*a/t!=1)//细节3
		cout<<'/'<<2*a/t;
	cout<<'\n';
	return;
}
int main(){/*
	freopen("uqe.in","r",stdin);
	freopen("uqe.out","w",stdout);*/
	for(cin>>T>>m;T;--T)
		Main();//根据某人言，多测函数好
	return 0;
}
```