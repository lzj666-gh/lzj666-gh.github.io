# P1313 题解

大佬们没搞错吧，这题这么难？（快速幂之类的蒟蒻表示完全不会）

看到像这样的多项式，想必都可以想到杨辉三角

1

1 1

1 2 1

1 3 3 1

1 4 6 4 1

……

但这只有~~50分~~

因为啊，a,b可以不是1

这样我们就看一下杨辉三角

举个例子：第3行到第4行

(x^2+2·x·y+y^2)(x+y)

看一下x^2 · y 这一项是怎么来的

是 (x^2 · y)+(2xy · x)=3·x^2·y

就是杨辉三角x[4][2]=x[3][1]·1+x[3][2]·1

当a,b,不为1时呢，相加的两个相的系数乘的便不是1,1 ，而是y的系数与x的系数

既 x[4][2]=x[3][1]·b+x[3][2]·a

可得到递推公式 x[i][j]=x[i-1][j-1]·b+x[i-1][j]·a

假设当a=2,b=3时,杨辉三角为

1

2 3

4 12 9

8 36 54 27

16 96 216 216 81

……

杨辉三角的行数便是(k+1),最后输出的是(m+1)【是y的m次方相】pas:这里数组不能从0开始哈


----------------------------------萌萌哒的分割线----------------------------------



    #include<iostream>
    using namespace std;
    long long x[1010][1010];
    int main()
    {
	    long long a,b,k,n,m;
	    cin>>a>>b>>k>>n>>m;
	    x[1][1]=1;
	    for(int i=2;i<=k+1;i++) for(int j=1;j<=i;j++)
	    x[i][j]=(x[i-1][j-1]*b+x[i-1][j]*a)%10007;
	    cout<<x[k+1][m+1];
	    return 0;
    }
    
13行，可能比较玄学,~~不符合day2第一题~~