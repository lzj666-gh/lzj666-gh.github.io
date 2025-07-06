# P1125 题解

#  P1125 【笨小猴】
## 思路
将题目的输入字符中相同的数量存储到一个数组中，然后找出最大和最小，相减后判断是否是质数，输出。
## 实现
废话不多说，上代码：
```cpp
#include<bits/stdc++.h>
using namespace std;
int a[26];//用来储存每一个字母的数量
int main(){
    int le=0,xunhuan=0,maxn=-500,minn=9999;//le 是单词的长度，xunhuan 是临时变量
    string s;
    cin>>s;
    le=s.size();//求出单词的长度
    for(int i=0;i<=le-1;i++){
        xunhuan=s[i];
        a[xunhuan-97]++;//累计字母数量
    }
    int zhishu[25]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};//质数表，100以内足够用了
    for(int i=0;i<=25;i++){
        if(a[i]<minn&&a[i]!=0)minn=a[i];//找出最少的字母
    }
    for(int i=0;i<=25;i++){
        if(a[i]>maxn)maxn=a[i];//找出最多的字母
    }
    int cha=maxn-minn;//相减
    for(int i=0;i<=24;i++){
        if(cha==zhishu[i]){
            cout<<"Lucky Word"<<endl;
            cout<<cha;//如果是质数直接输出并结束程序
            return 0;
        }
    }
    cout<<"No Answer"<<endl;//如果找完了还没有就不是质数
    cout<<"0";
    return 0;
} 
```
3ms AC

最后在推荐一下自己的博客

[](https://www.luogu.org/blog/wozhendexiangbudaole/)点这里
