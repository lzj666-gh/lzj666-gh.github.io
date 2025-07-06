# P1068 题解

作为蒟蒻，表示不会结构体，用了下标数组

```cpp
#include<bits/stdc++.h>万能头文件
using namespace std;
int i,n,m,f,k[5001],s[5001],sub[5001];f是分数线，sub是下标
bool cmp(int a,int b){sort规则
    if(s[a]==s[b])return k[a]<k[b];成绩相等比编号
    return s[a]>s[b];否则比成绩
}
int main(){
    cin>>n>>m;
    for(i=1;i<=n;i++)cin>>k[sub[i]=i]>>s[i];输入编号和成绩，同时初始化下标
    sort(sub+1,sub+n+1,cmp);对下标排序
    f=s[sub[int(m*1.5)]];算分数线
    for(i=1;s[sub[i]]>=f;i++);算录取人数
    cout<<f<<" "<<i-1<<endl;
    for(i=1;s[sub[i]]>=f;i++)cout<<k[sub[i]]<<" "<<s[sub[i]]<<endl;输出
}
```