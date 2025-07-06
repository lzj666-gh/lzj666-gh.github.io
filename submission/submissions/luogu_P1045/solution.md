# P1045 题解

注意：下列代码因为作者脸黑常数大，所以不一定能够在不吸氧/改用scanf和printf的情况下AC，见谅

---

首先看数据范围:$1000<P<3100000$，求$2^P-1$的位数及后500位。很明显这是一道高精题目，所以先把vector重载高精度模板搬来。看着模板高兴的交了上去，只有0分。所以我们要考虑优化了。

---

问题拆分成两半，第一问求位数，$2^P(P>1000)$的末尾为$2,4,6,8$，所以绝不会有退位的风险，所以可以直接套用公式得到位数为$log_{10}2*P+1$，转化成int后即可输出（当然打表也可以，但是考场上挂着跑半天不好吧...）

第二问求$2^P-1$的后500位。我们已经求出位数，如果位数小于500，输出500-位数个0，然后直接...?

我们发现我们的高精模板只能整个输出？因为这个是vector，所以还是滋磁vector基本的操作。用迭代器！但是请注意用反向迭代器，因为我们储存数字时是倒序存储的。

暴力连乘$P$次，交上去竟然全部超时！

我们该怎么办呢？

~~我会FFT！我会压位高精！~~

我会快速幂！

这时候我们就可以用高精快速幂来求$2^P$，让我们原来的$\Theta (P)$变成更高效的$\Theta log_2(P)$，__最后取个模就OK啦！__

Tip:如果还不会快速幂的请往[这边](https://www.luogu.org/problemnew/show/P1226)

仍然超时，只有40

~~果然脸黑~~

---

我们发现时间主要出在乘这个部分上，位数都可以乘到几十万，当然常数很大。所以我们要介绍一个性质

$$(a \times b)\text{ }mod\text{ }p=((a\text{ }mod\text{ }p) \text{ }\times \text{ }(b\text{ }mod\text{ }p))\text{ }mod \text{ }p$$

有了这个性质，我们发现我们可以在进行快速幂的同时进行取余运算，位数最大500位，让速度快了许多

注：该代码为C++11标准，不保证不吸氧过的了

```cpp
#include<algorithm>
#include<cstring>
#include<random>
#include<iostream>
#include<vector>
#include<string>
#include<cmath>
using namespace std;
struct Wint:vector<int>
{
    Wint(int n=0)
    {
        push_back(n);
        check();
    }
    Wint& check()
    {
        while(!empty()&&!back())pop_back();
        if(empty())return *this;
        for(int i=1; i<size(); ++i)
        {
            (*this)[i]+=(*this)[i-1]/10;
            (*this)[i-1]%=10;
        }
        while(back()>=10)
        {
            push_back(back()/10);
            (*this)[size()-2]%=10;
        }
        return *this;
    }
};
istream& operator>>(istream &is,Wint &n)
{
    string s;
    is>>s;
    n.clear();
    for(int i=s.size()-1; i>=0; --i)n.push_back(s[i]-'0');
    return is;
}
ostream& operator<<(ostream &os,const Wint &n)
{
    if(n.empty())os<<0;
    else	for(int i=n.size()-1; i>=0; --i)os<<n[i];
    return os;
}
bool operator!=(const Wint &a,const Wint &b)
{
    if(a.size()!=b.size())return 1;
    for(int i=a.size()-1; i>=0; --i)
        if(a[i]!=b[i])return 1;
    return 0;
}
bool operator==(const Wint &a,const Wint &b)
{
    return !(a!=b);
}
bool operator<(const Wint &a,const Wint &b)
{
    if(a.size()!=b.size())return a.size()<b.size();
    for(int i=a.size()-1; i>=0; --i)
        if(a[i]!=b[i])return a[i]<b[i];
    return 0;
}
bool operator>(const Wint &a,const Wint &b)
{
    return b<a;
}
bool operator<=(const Wint &a,const Wint &b)
{
    return !(a>b);
}
bool operator>=(const Wint &a,const Wint &b)
{
    return !(a<b);
}
Wint& operator+=(Wint &a,const Wint &b)
{
    if(a.size()<b.size())a.resize(b.size());
    for(int i=0; i!=b.size(); ++i)a[i]+=b[i];
    return a.check();
}
Wint operator+(Wint a,const Wint &b)
{
    return a+=b;
}
Wint& operator-=(Wint &a,Wint b)
{
    for(int i=0; i!=b.size(); a[i]-=b[i],++i)
        if(a[i]<b[i])
        {
            int j=i+1;
            while(!a[j])++j;
            while(j>i)
            {
                --a[j];
                a[--j]+=10;
            }
        }
    return a.check();
}
Wint operator-(Wint a,const Wint &b)
{
    return a-=b;
}
Wint operator*(const Wint &a,const Wint &b)
{
    Wint n;
    n.assign(a.size()+b.size()-1,0);
    for(int i=0; i!=a.size(); ++i)
        for(int j=0; j!=b.size(); ++j)
            n[i+j]+=a[i]*b[j];
    return n.check();
}
Wint& operator*=(Wint &a,const Wint &b)
{
    return a=a*b;
}
Wint divmod(Wint &a,const Wint &b)
{
    Wint ans;
    for(int t=a.size()-b.size(); a>=b; --t)
    {
        Wint d;
        d.assign(t+1,0);
        d.back()=1;
        Wint c=b*d;
        while(a>=c)
        {
            a-=c;
            ans+=d;
        }
    }
    return ans;
}
Wint operator/(Wint a,const Wint &b)
{
    return divmod(a,b);
}
Wint& operator/=(Wint &a,const Wint &b)
{
    return a=a/b;
}
Wint& operator%=(Wint &a,const Wint &b)
{
    divmod(a,b);
    return a;
}
Wint operator%(Wint a,const Wint &b)
{
    return a%=b;
}
Wint pow(const Wint &n,const Wint &k)//虽然这已经是快速幂，但是因为有问题所以还是不要用啦
{
    if(k.empty())return 1;
    if(k==2)return n*n;
    if(k.back()%2)return n*pow(n,k-1);
    return pow(pow(n,k/2),2);
}//以上皆为重载高精
int main(){
    int p;
    cin>>p;
    Wint ans=1,m=2,k=1;
    cout<<int(log10(2)*p+1)<<endl;//直接输出位数
    for(int i=1;i<=500;++i)	k*=10;
    for(;p;p>>=1,m=m*m%k)	if(p&1)	ans=ans*m%k;//快速幂
    ans-=1;//一定要减1！因为这里没写--这个运算符所以只能这么写
    int sis=500-ans.size();
    int t=0;
    if(sis<0);
    else
	{
		for(int i=1;i<=sis;++i)
	    {
	        cout<<0;
	        if(i%50==0)	cout<<endl;
	    }
		t=sis;
	}//输出0
    for(auto i=ans.rbegin();i!=ans.rend() && t<=500;++i)//rbegin及rend为反向迭代器，其实就是倒着输出
    {
        ++t;
        cout<<*i;//注意输出
        if(t%50==0)	cout<<endl;
    }
    return 0;
}
```

至此，我们得到了一份高精模板，一些关于STL的知识，一个叫做快速幂的优化算法以及一条取余运算的性质，~~同时得到了至理名言：STL和O2更配哦~~

温馨提示：或许还需要一些卡常技巧，毕竟NOIp不开O2嘛