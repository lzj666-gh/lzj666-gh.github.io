# P1327 题解

直接o（n）扫过去；

遇到不对的就直接交换就好了；

因为每个东西迟早要到自己的位置上的；

应该不会被hack把

```cpp
#include<bits/stdc++.h>
#define Ll long long
using namespace std;
const int N=1e5+5;
map<int,int>F;
int a[N],b[N];
int n,m,ans;
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)scanf("%d",&a[i]),b[i]=a[i],F[a[i]]=i;
    sort(b+1,b+n+1);
    for(int i=1;i<=n;i++)
        if(a[i]!=b[i]){
            ans++;
            int x=F[b[i]];
            F[a[i]]=x;
            a[x]=a[i];
        }
    printf("%d",ans);
}
```