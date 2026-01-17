# P1376 题解

很简单的一道题，时间O（n）,空间O（1），注意ans用long long！否则会错。并且注意循环的其实值！！！

```cpp
#include<iostream>
using namespace std;
int main()
{
    int c,y;
    long long n,ans=0;
    int k,lastweek;
    cin>>n>>k;
    for(int i=1;i<=n;i++)
    {
        cin>>c>>y;
        if(i==1) lastweek=c;
        else lastweek=min(lastweek+k,c);
        ans+=lastweek*y;
    }
    cout<<ans;
    //system("pause");
    return 0;
}

```