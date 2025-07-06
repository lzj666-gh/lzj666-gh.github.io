# P2161 题解

### 一个非常简单的STL做法（非常好想，代码很短）

题意已经暗示的很明确要你使用平衡树了，但本蒟蒻太懒，不想打平衡树，于是便考虑偷懒用STL~~（还不是是因为太弱）~~

我们可以用一个有两个元素的结构体来保存一个预约，如下：
```cpp
struct Plan{
	int l,r; //l,r分别表示预约开始,结束的时间
};
```

首先考虑A操作，由于STL的set有**相同元素只保留一个**的特性，因此我们不难想到令有冲突的预约相等，这样我们就可以很方便的用.find()这个函数来完成A操作了。

#### 怎么令它们相等呢？

其实也很简单，由于使用自定义数据类型的set要重载运算符，因此我们可以这样：
```cpp
struct Plan{
	int l,r;
	bool operator <(const Plan &rhs)const{
		return r<rhs.l;
	}
};
```
这样对于两个Plan类型的结构体a,b来说，a<b就代表a完全在b的左边，a>b就代表a完全在b的右边，a==b就代表a与b有冲突(有重叠部分)

对于B操作，直接输出set里元素的个数就好了

~~于是我们就可以快乐的A掉这道题了~~

有了上面的思路，代码也不难写出:
```cpp
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<set>
using namespace std;
struct Plan{
	int l,r;
	bool operator <(const Plan &rhs)const{
		return r<rhs.l;
	}
};
int T;
set<Plan> s;
int main(){
	cin>>T;
	while(T--){
		char c; scanf(" %c",&c); //空格可以防止读入无效字符
		if(c=='A'){
			int l,r,cnt=0; scanf("%d %d",&l,&r);
			Plan tmp=(Plan){l,r};
            //删掉与该预约冲突的预约，并统计个数
			set<Plan>::iterator it=s.find(tmp);
			while(it!=s.end()){
				++cnt; s.erase(it);
				it=s.find(tmp);
			}
			s.insert(tmp);
			printf("%d\n",cnt);
		}
		else{
			printf("%d\n",s.size());
		}
	}
	return 0;
}
```
AC记录：[R14872282 评测详情](https://www.luogu.org/recordnew/show/14872282)