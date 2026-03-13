# P10567 题解

如果想看赛时解法，从前往后看。如果想看正常解法，从后往前看。

注意是按照板块看而不是整体反过来……

## 赛事做法

赛时给了四组样例，其中偶数都成立，奇数都不成立，产生猜想。

## 题目分析

若 $n$ 为奇数，按照行来看奇数个奇数相加必是奇数，按照列来看奇数个偶数相加必是偶数，所以总数必须又是奇数又是偶数，矛盾。

若 $n$ 为偶数，可以进行构造（见下面【构造方法】）。


## 代码实现

```cpp
#include<bits/stdc++.h>
#define int long long 
using namespace std;
int n;
signed main(){
    cin>>n;
    if(n&1)
        cout<<"No";
    else
        cout<<"Yes";
    return 0;
}
```

下面是构造代码（不支持 $n\le 10^{18}$，不保证代码能够在 1s 时间内运行完）：

```cpp
#include<bits/stdc++.h>
using namespace std;
int n;
int main(){
	cin>>n;
	if(n&1){
		cout<<"-1";
		return 0;
	}
	if(n%4){
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				cout<<(i-1)*n+j<<" \n"[j==n];
		return 0;
	}
	for(int i=1;i<=n;i++){
		for(int j=1;j<n;j++)
			cout<<(i-1)*(n-1)+j<<' ';
		cout<<(n-1)*n+i<<'\n';
	}
	return 0;
}
```

## 构造方法

下文所述 $n$ 为偶数。

首先考虑按照 $\begin{bmatrix}
   1 & 2 &3 & 4 & \dots & n \\
   n+1 & n+2 & n+3 & n+4 & \dots & 2n\\
   \dots & \dots & \dots & \dots & \dots & \dots \\
   (n-1)\times n+1 & (n-1)\times n+2 & (n-1)\times n+3 & (n-1)\times n+4 & \dots & n^2\\
\end{bmatrix}$ 来构造。

然而 $n=4$ 时就不行了，经过观察我们发现是行不满足要求。

对于这个矩阵第 $i$ 列的和是 $[0+1+2+\dots+(n-1)]\times n+n\times i=(n-1)\times n^2\div 2+n\times i$。这个式子第一项是偶数，原因是 $n$ 有因子 $2$，所以 $n^2$ 有因子 $4$，然而 $4\div 2=2$，仍是偶数。第二项也是偶数，因为 $n$ 是偶数。所以式子为偶数。

第 $i$ 行的和是 $(i-1)\times n+(1+2+3+\dots+n)=(i-1)\times n+n\times(n+1)\div 2$。这个式子在 $n$ 是 $4$ 的倍数时也是偶数，否则是奇数。

所以 $n$ 不是 $4$ 的倍数是可以考虑这种构造方案。

其他方案，首先考虑微调（去掉最后一列）。

按照 $\begin{bmatrix}
   1 & 2 &3 & 4 & \dots & n-1 \\
   n & n+1 & n+2 & n+3 & \dots & 2n-2\\
   \dots & \dots & \dots & \dots & \dots & \dots \\
   (n-1)^2+1 & (n-1)^2+2 & (n-1)^2+3 & (n-1)^2+4 & \dots & n^2-n\\
\end{bmatrix}$ 来构造（这是前 $n-1$ 列）。

这样第 $i$ 行和是 $(i-1)\times(n-1)+[1+2+\dots+(n-1)]=(n-1)\times(i-1)+n\times(n-1)\div 2=(n-1)\times[(i-1)+n\div 2]$。由于 $n$ 是偶数，所以 $n\div 2$ 是整数，所以 $(i-1)+n\div 2$ 奇偶性与 $i$ 有关（一奇一偶），又知道 $n-1$ 是奇数，所以不会出现全是偶数。

但是我们需要验证列，第 $i$ 列是 $[0+1+\dots+(n-1)]\times(n-1)+i\times n=(n-1)\times n\div 2\times (n-1)+i\times n$ 是偶数（原因是 $n$ 是 $4$ 的倍数）。

第 $n$ 列的数都是 $(n-1)\times n+1,(n-1)\times n+2,\dots,n^2$。虽然不知道顺序，但是和是 $n\times(n-1)\times n+(1+2+\dots+n)=n\times(n-1)\times n+(n+1)\times n\div 2$ 是偶数。

所以所有列都是偶数，那就需要所有行都是奇数。

行都是奇数的满足方案的微妙之处就在于把最后一列数随便改变顺序不会改变列是偶数的性质，但是可以调节行的奇偶性。

具体做法是：把 $(n-1)\times[(i-1)+n\div 2]$ 是奇数时匹配一个偶数，是偶数时匹配一个奇数，然而因为 $n$ 是偶数，最后一段又是连续的 $n$ 个数，必然一半奇数一半偶数，正好可以匹配。

更具体：$i$ 是奇数时，式子是偶数，需要添加的数是奇数；$i$ 是偶数时，式子是奇数，需要添加的数是偶数。所以最后一列的数按从小到大的顺序排好之后，从上到下一次从最右边加进矩阵（正好满足第一个奇、第二个偶、第三个奇……）。

$n$ 是奇数无法构造，解释见【题目分析】。