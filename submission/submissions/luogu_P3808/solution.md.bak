# P3808 题解

膜拜楼下神犇

%%% 这的确是一道裸的AC自动机（写了是模板呀）

所以，就是打一遍AC自动机即可

~~具体的实现可以百度~~

~~或者也可以参考我代码的注释~~

过了这么久，当然要改一下

首先肯定要搞一搞自己的博客对不对。。。

[AC自动机不懂戳这里](http://www.cnblogs.com/cjyyb/p/7196308.html)

AC自动机的难点在于Fail失配指针的构建

自己多画图就可以很容易的弄懂这个问题

```cpp
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<queue>
#include<algorithm>
using namespace std;
struct Tree//字典树 
{
     int fail;//失配指针
     int vis[26];//子节点的位置
     int end;//标记有几个单词以这个节点结尾 
}AC[1000000];//Trie树
int cnt=0;//Trie的指针 
inline void Build(string s)
{
        int l=s.length();
        int now=0;//字典树的当前指针 
        for(int i=0;i<l;++i)//构造Trie树
        {
                if(AC[now].vis[s[i]-'a']==0)//Trie树没有这个子节点
                   AC[now].vis[s[i]-'a']=++cnt;//构造出来
                now=AC[now].vis[s[i]-'a'];//向下构造 
        }
        AC[now].end+=1;//标记单词结尾 
}
void Get_fail()//构造fail指针
{
        queue<int> Q;//队列 
        for(int i=0;i<26;++i)//第二层的fail指针提前处理一下
        {
               if(AC[0].vis[i]!=0)
               {
                   AC[AC[0].vis[i]].fail=0;//指向根节点
                   Q.push(AC[0].vis[i]);//压入队列 
               }
        }
        while(!Q.empty())//BFS求fail指针 
        {
              int u=Q.front();
              Q.pop();
              for(int i=0;i<26;++i)//枚举所有子节点
              {
                        if(AC[u].vis[i]!=0)//存在这个子节点
                      {
                                AC[AC[u].vis[i]].fail=AC[AC[u].fail].vis[i];
                                    //子节点的fail指针指向当前节点的
                                  //fail指针所指向的节点的相同子节点 
                                Q.push(AC[u].vis[i]);//压入队列 
                      }
                      else//不存在这个子节点 
                      AC[u].vis[i]=AC[AC[u].fail].vis[i];
                      //当前节点的这个子节点指向当
                      //前节点fail指针的这个子节点 
              }
        }
}
int AC_Query(string s)//AC自动机匹配
{
        int l=s.length();
        int now=0,ans=0;
        for(int i=0;i<l;++i)
        {
                now=AC[now].vis[s[i]-'a'];//向下一层
                for(int t=now;t&&AC[t].end!=-1;t=AC[t].fail)//循环求解
                {
                         ans+=AC[t].end;
                         AC[t].end=-1;
                } 
        }
        return ans;
}
int main()
{
     int n;
     string s;
     cin>>n;
     for(int i=1;i<=n;++i)
     {
             cin>>s;
             Build(s);
     }
     AC[0].fail=0;//结束标志 
     Get_fail();//求出失配指针
     cin>>s;//文本串 
     cout<<AC_Query(s)<<endl;
     return 0;
}
```