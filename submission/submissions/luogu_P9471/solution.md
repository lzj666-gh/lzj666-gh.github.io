# P9471 题解


##### 这道题很简单，要记录数字小写字母和大写字母的个数，可以用 ASCII 值来判断（ 用 ‘ 符号 ’ 就可以了 ）
```cpp
#include<bits/stdc++.h>
using namespace std;
char ch[1005];
int a,b,c;
int main(){
      for(int i=0;i<8;i++){
            cin>>ch[i];
            if(ch[i]>='0'&&ch[i]<='9')a++;
            if(ch[i]>='a'&&ch[i]<='z')b++;
            if(ch[i]>='A'&&ch[i]<='Z')c++;
      }
      cout<<a<<" "<<b<<" "<<c;
}
```
