# P1307 题解

#### 这题。。。。。。那么难吗？**[真心的问号][认真严肃脸]**
这题真的太水了，几行代码了事ψ(*｀ー´)ψ

说实在的，我就给几种解法吧，有长有短，自己看哪种适合自己

## 一、死套“暴力”
此暴力非彼暴力哈，就是用数组把数分解了，倒着组合（当年我的做法）

```cpp
#include<bits/stdc++.h>//头文件
using namespace std;//cin，cout必备的
long long s[11]={},n,k=0,a=1;//数组s,n和转换后的k,再加一个a,作用后面讲
int main()//主程序
{
	memset(s,0,sizeof(n));//清零
	cin>>n;//输入不解释
    for(int i=1;i<=10;i++) s[i]=n/a%10,a*=10;//求出位数后存入数组，具体的就不说了
    a=1000000000;//初始化
    for(int i=1;i<=10;i++) k+=s[i]*a,a/=10;//存入k
    while(k%10==0) k/=10;//倒着看，最后有0就除掉
    cout<<k;//输出不解释
    return 0;//好习惯棒棒哒[恶心][恶心][呕吐][呕吐]
}
```

## 二、简短操作
够简短，不用弄数据，直接操作，抛数位再补回去，具体的就看你造化了。

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,s=0;
int main()//以上应该都懂，不解释
{
    cin>>n;//烦死了输入
    while(n) s=s*10+n%10,n/=10;//如果n不是0，就一直s让一位，腾个0出来，n最后一位跟上去，再无情地抛弃了最后一位（突然想对n说：你无情你冷酷你无理取闹！）
    cout<<s;//烦死了输出
    return 0;
}
```

## 三、极简
真的很极简了，就7行，自己看吧。。。。。。（画外音：突然发现楼主只喜欢用六个句号。。。。。。）
```cpp
#include <bits/stdc++.h>
using namespace std;
int n=0,s=0;//定义与归0 
int main(){
	for(cin>>n;n!=0;n/=10)s=s*10+n%10;//同上一种的套路，暴力直接循环搞 
    cout<<numb;return 0;//输出,0会没掉的（自己去试） 
} 
```

## 四、字符串
由于有坑（负数〇），所以用字符串。。。。。。（又来了）就这样吧
```cpp
#include<bits/stdc++.h>
using namespace std;
string s1,s2;
int main()//不解释
{
    cin>>s1;
    if(s1[0]=='-')
    {
        cout<<"-";//输出负号
        for(int i=s1.length()-1,j=0;i>=1;i--,j++) s2=s2+s1[i];//倒着变成正的（好烦）
        if(s2[0]=='0') s2.erase(0,s2.find_first_not_of('0'));//去0
        cout<<s2;//输出
    }
    else //否则为正
    {
        for(int i=s1.length()-1,j=0;i>=0;i--,j++) s2=s2+s1[i];//正着倒序（还是好烦吧）
        if(s2[0]=='0')s2.erase(0,s2.find_first_not_of('0'));//删除0
        cout<<s2;//输出
    }
    return 0;//终于结束了
}
```
## 五、P党福利
我不是P党的，但是呢由于P党的人摆在那里，还是给写一个吧。

```php
var s,t:string; n,i:longint;
begin
  read(n);
  if n>=0 then str(n,s) else str(-n,s);//判断负数，真变为正数字符串
  for i:=1 to length(s) do t:=s[i]+t;//反转
  while t[1]='0' do delete(t,1,1);//删0
  if n>=0 then write(t) else write('-',t);//负数加负号
end.//结束
```

## 六、java来一个！
对，我再来一个java的！
```java
public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        // 将数据存入
        StringBuffer sb=new StringBuffer(br.readLine().trim());
        sb.reverse();   // 反转
        //负号跑到最后
        if(sb.charAt(sb.length()-1)=='-'){
            // 删除负号并且在头插入负号
            sb.delete(sb.length()-1, sb.length());
            sb.insert(0, '-');

        }
        System.out.println(Integer.parseInt(sb.toString()));
    }
```
## 七、栈
注意了最后要转整数呢
```cpp
#include <bits/stdc++.h>
using namespace std;
char a[100001];
int t=0;
int main()
{
    string b,c;
    bool sign=false,flag=false;
    cin>>c;
    for(int i=0;i<=c.length();i++)
    {
        if(c[i]=='-') s=true;
        else a[++t]=c[i];
    }    
    if(s==true)    b+="-";
    t--;
    for(t;t>=0;t--)
    {
        if(a[t]!='0'&&f==false) f=true,b+=a[top];    
        else if(f==true) b+=a[t];
    }
    int i=atoi(b.c_str());
    cout<<i;
    return 0;    
}//用栈的呢应该都懂吧，不需要解释了吧
```
## 八、最后来一下最简（fu）单（za）的一种了
其实很简单，不注释了，看懂就行（如果你有耐心看完的话）[奸笑][贱笑]
```cpp
#include<iostream>
    using namespace std;
    int main(){
        long long i,n,m=0,s1=0,s2=0,s3=0,s4=0,s5=0,s6=0,s7=0,s8=0,s9=0;//s1到s9代表数字的每一位。（最大是九位嘛）
        cin>>i;
        if(i<0){
            n=0-i;}
        else{
            n=i;}
        if(n>=1){
            s1=n%10;}
        if(n>=10){
            s2=n%100/10;}
        if(n>=100){
            s3=n%1000/100;}
        if(n>=1000){
            s4=n%10000/1000;}
        if(n>=10000){
            s5=n%100000/10000;}
        if(n>=100000){
            s6=n%1000000/100000;}
        if(n>=1000000){
            s7=n%10000000/1000000;}
        if(n>=10000000){
            s8=n%100000000/10000000;}
        if(n>=100000000){
            s9=n%1000000000/100000000;}
        if(s9==0){
            if(s8==0){
                if(s7==0){
                    if(s6==0){
                        if(s5==0){
                            if(s4==0){
                                if(s3==0){
                                    if(s2==0){
                                        if(s1==0){
                                            if(i<0){
                                                m=0-m;}
                                            cout<<m;
                                            return 0;}
                                        m=s1;
                                        if(i<0){
                                            m=0-m;}
                                        cout<<m;
                                        return 0;}
                                    m=s1*10+s2;
                                    if(i<0){
                                        m=0-m;}
                                    cout<<m;
                                    return 0;}
                                m=s1*100+s2*10+s3;
                                if(i<0){
                                    m=0-m;}
                                cout<<m;
                                return 0;}
                            m=s1*1000+s2*100+s3*10+s4;
                            if(i<0){
                                m=0-m;}
                            cout<<m;
                            return 0;}
                        m=s1*10000+s2*1000+s3*100+s4*10+s5;
                        if(i<0){
                            m=0-m;}
                        cout<<m;
                        return 0;}
                    m=s1*100000+s2*10000+s3*1000+s4*100+s5*10+s6;
                    if(i<0){
                        m=0-m;}
                    cout<<m;
                    return 0;}
                m=s1*1000000+s2*100000+s3*10000+s4*1000+s5*100+s6*10+s7;
                if(i<0){
                    m=0-m;}
                cout<<m;
                return 0;}
            m=s1*10000000+s2*1000000+s3*100000+s4*10000+s5*1000+s6*100+s7*10+s8;
            if(i<0){
                m=0-m;}
            cout<<m;
            return 0;}
        else{
            m=s1*100000000+s2*10000000+s3*1000000+s4*100000+s5*10000+s6*1000+s7*100+s8*10+s9;
            if(i<0){
                m=0-m;}
            cout<<m;}
        return 0;
}
```
好了可能有一些长（列了这么多），但应该有一种是你喜欢的。顺便说一下，本人还只是一个小~~蒟蒻~~，dalao们呢不喜勿喷吧，希望多多支持我！谢谢！