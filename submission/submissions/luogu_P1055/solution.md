# P1055 题解

[题面传送门](https://www.luogu.com.cn/problem/P1055)

用枚举除了最后一位数字之外的数字和，然后模掉 
$11$，在特判一下最后一位是 $10$ 的情况，就好了。

```cpp
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int a,b,c,d,e,f,g,h,i,s1,s2;
	char j;
    scanf("%1d-%1d%1d%1d-%1d%1d%1d%1d%1d-%c",&a,&b,&c,&d,&e,&f,&g,&h,&i,&j);
    s1=(a*1+b*2+c*3+d*4+e*5+f*6+g*7+h*8+i*9)%11;
    if(j=='X')
		s2=10;
    else
		s2=j-'0';
		
    if(s1==s2)
    cout<<"Right";
    else if(s1==10)
    cout<<a<<"-"<<b<<c<<d<<"-"<<e<<f<<g<<h<<i<<"-X";
    else
    cout<<a<<"-"<<b<<c<<d<<"-"<<e<<f<<g<<h<<i<<"-"<<s1;
	return 0;
}


```
也可以这样写

```cpp

#include<bits/stdc++.h>
using namespace std;
int main()
{
char s[14];
int a[14],m=0;
cin>>s;
a[1]=s[0]-'0';
a[2]=s[2]-'0';
a[3]=s[3]-'0';
a[4]=s[4]-'0';
a[5]=s[6]-'0';
a[6]=s[7]-'0';
a[7]=s[8]-'0';
a[8]=s[9]-'0';
a[9]=s[10]-'0';
 if(s[12]=='X')
      a[10]=10;
   else
   a[10]=s[12]-'0';
for(int i=1;i<=9;i++)
    {
       m+=a[i]*i;
     }
    m%=11;
 if(m==a[10])
    cout<<"Right";
 else   
    {for(int i=0;i<12;i++)
        cout<<s[i];
    if(m==10)
       cout<<'X';
    else
       cout<<m;
    }
return 0;
}



```
撒花！！！完美结束！！！

~~这是本蒟蒻第1次写题解，希望管理员大大通过。~~