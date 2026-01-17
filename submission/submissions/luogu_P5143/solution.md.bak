# P5143 题解

	=w=冷门题，人群当中冒出一个游六：我来！
	23333没错又是我
    这题其实就是普通的排序+数学计算题，结构体快排操作一下就好。
    仔细审题，必须从低到高爬，那么我们最简单的方法就是计算每两个
   **高度相邻**
 	
    坐标之间的直线距离，然后把算出来的所有距离相加即可。
    那么首先我们需要用sort排序一下，具体使用方法请见
   [百度！](www.baidu.com)
   	
    接着就可以for计算了。
    
	```cpp
	#include<bits/stdc++.h>
	using namespace std;
	const int N = 100000;
	int read(){
      char ch = getchar();
      int x = 0, f = 1;
      while(ch < '0' || ch > '9'){
          if(ch == '-') f = -1;
          ch = getchar();
      }
      while('0' <= ch && ch <= '9'){
          x = x * 10 + ch - '0';
          ch = getchar();
      }
      return x * f;
  	}
	struct shan{
   	int x,y,z;
   	bool operator<(const shan &other)const{
		return z<other.z;//我偷到了啊啊啊！！！
		}
	}s[N];
	int main(){
    	int n = read();
    	double ans = 0;
    	for(int i = 0; i < n; ++i)
        	s[i].x = read(), s[i].y = read(), s[i].z = read();
    	sort( s, s + n);
    	for(int i = 1, j = 0; i < n; ++j, ++i)
        	ans += sqrt(pow(s[i].x - s[j].x,2) + pow(s[i].y - s[j].y,2) + pow(s[i].z-s[j].z,2));
    	printf("%0.3lf",ans);
    	return 0;
	} 
```

    
    反正就很好聊，坐等大牛牛牛的优化。