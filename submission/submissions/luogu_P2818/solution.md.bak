# P2818 题解

极简代码
```cpp
#include<cstdio>
#include<iostream>
char s[1010];
long long ans,n;//long long 保险 
int main(){
    scanf("%lld%s",&n,s);
    for(int i=0;s[i];i++) ans=(ans*10+s[i]-'0')%n;//边读取 边计算 
    printf("%lld",ans ? ans:n);//ans==0输出n 
}
```