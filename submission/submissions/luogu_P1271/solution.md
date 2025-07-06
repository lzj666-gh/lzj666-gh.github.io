# P1271 题解

本题思路：

简单的快排，直接$sort$即可

$AC$ $Code$
```cpp
#include<bits/stdc++.h>
using namespace std;
int a[2000000],n,m;
int main()
{
	cin>>n>>m;
	for(int i=0;i<m;i++)cin>>a[i];
	sort(a,a+m); //sort排序
	for(int i=0;i<m;i++)cout<<a[i]<<" ";
	return 0;
}
```
我们发现这还不够快，怎么办？

用桶排！

用$1000$的数组记录票出现的次数，最后根据票出现的次数输出即可

$AC$ $Code$
```cpp
#include<bits/stdc++.h>
using namespace std;
int a,n,m,b[1000];
int main()
{
	cin>>n>>m;
	for(int i=0;i<m;i++)cin>>a,++b[a]; //记录票出现的次数
	for(int i=0;i<1000;i++)while(b[i]--)cout<<i<<" "; //根据票出现的次数输出
	return 0;
}
```
