# P10994 题解

# A. Seats 官方题解

本题考察的主要知识点：

- 【2】string 类与相关函数
- 【2】分支语句、循环语句

### 做法（普通）

首先判断座位够不够坐。如果 $a+b>n$，那么座位一定不够坐，否则一定够坐。

然后用一重 `for` 循环统计一下老师和学生的座位分别有几个。

- 假设学生座位有 $c_s$ 个，不够坐，那么学生需要更改 $c_s-a$ 个座位。
- 假设教师座位有 $c_t$ 个，不够坐，教师就会要求更改 $c_t-a$ 个座位。
- 如果老师和学生都够坐，就输出 $0$。

接下来判断一下老师和学生是否分别够坐。显然不可能学生和老师都不够坐（因为刚才 $-1$ 已经判掉了），按照对应情况输出即可。

```cpp
#include<bits/stdc++.h>
using namespace std;
int a,b;
string s;
int main(){
	cin>>a>>b>>s;
	if(a+b>s.size())
		cout<<-1;
	else{
		int cs=0,ct=0;
		for(int i=0;i<s.size();i++)
			if(s[i]=='S')cs++;
			else ct++;
		int ans=0;
		ans=max(ans,a-cs);
		ans=max(ans,b-ct);
		cout<<ans;
	}
	return 0;
}
```

### 做法（快速）

使用 STL 中的 `count` 函数可以辅助统计字符串当中 `S` 或 `T` 的数量。

注意到 $c_s-a,c_t-a$ 中如果有正数则输出这个正数，否则输出 $0$，相当于输出 $c_s-a,c_t-a,0$ 的最大值，可以使用 `max` 函数计算。

```cpp
#include<bits/stdc++.h>
using namespace std;
int a,b;
string s;
int main(){
	cin>>a>>b>>s;
	int cS=count(s.begin(),s.end(),'S'),cT=s.size()-cS;
	if(a+b>s.size())
		cout<<-1<<endl;
	else
		cout<<max({a-cS,b-cT,0});
	return 0;
}
```