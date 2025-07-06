# P11451 题解

~~好恶臭的题号哼哼哼啊啊啊啊啊~~（

前置：大佬的 [string 函数用法](https://blog.csdn.net/kumoue/article/details/123851809)。

本题有两种思路。



------------

#### 第一种：

一种是**对于每一个位置**，判断能否和后两个位置组成一种声音，和更改一个字符后组成的声音，然后统计所有声音出现的次数。

这种写法需要考虑的细节比较多。

```cpp
#include <bits/stdc++.h>
using namespace std;

map <string, int> mp;
map <string, bool> can; // 更改一个字符后可以组成的哞声 

vector <string> ans;

signed main() {
    //cin.tie(0); ios::sync_with_stdio(0);
    int n, f; cin >> n >> f;
    string s; cin >> s;
    for (int i = 0; i < n - 2; i++) {
    	string s1, s2, s3;
		s1 = s[i]; s2 = s[i + 1]; s3 = s[i + 2];
		
     	if (s[i] != s[i + 1] && s[i + 1] == s[i + 2]) {
			for (char j = 'a'; j <= 'z'; j++) {
				string v = string(1, j) + s2 + s3;
				if (v == s1 + s2 + s3) continue;
				string lst = string(1,s[i-2])+string(1,s[i-1])+string(1,s[i]);
				string lst2 = string(1,s[i-1])+string(1,s[i])+string(1,s[i+1]);
				if (j != s[i + 1] && v != lst && v != lst2) can[v] = 1, mp[v];
			}
     		mp[s1 + s2 + s3] ++;
		 }
		else if (s[i + 1] == s[i + 2]) 
			for (char j = 'a'; j <= 'z'; j++) {
				string v = string(1, j) + s2 + s3;
				string lst = string(1,s[i-2])+string(1,s[i-1])+string(1,s[i]);
				string lst2 = string(1,s[i-1])+string(1,s[i])+string(1,s[i+1]);
				if (j != s[i + 1] && v != lst && v != lst2) can[v] = 1, mp[v];
			}
		else { // s[i + 1] != s[i + 2]
			string nxt = string(s, i + 1, 3);
			string nxt2 = string(s, i + 2, 3);
			string now1 = s1 + s3 + s3;
			string now2 = s1 + s2 + s2;
			if (s[i] != s[i + 1] && nxt2 != now2) can[now2] = 1, mp[now1];
			if (s[i] != s[i + 2] && nxt != now1) can[now1] = 1, mp[now1];
		}
	}

	for (auto u : mp) 
		if (u.second + can[u.first] >= f) ans.push_back(u.first);
		
	cout << ans.size() << "\n";
	sort(ans.begin(), ans.end());
	for (auto u : ans) cout << u << "\n";
	return 0;
}
```


------------

#### 第二种：

第二种是**对于每一种声音**（将其命名为 $moo$ 吧），统计出现次数。

注意，如果 $\overline{s_{i+1}s_{i+2}s_{i+3}}$ 或者 $\overline{s_{i+2}s_{i+3}s_{i+4}}$ 能构成 $moo$，就不要更改 $\overline{s_{i}s_{i+1}s_{i+2}}$ 的值使得它为 $moo$，因为这样会浪费修改次数。

这种比较好写一些。

```cpp
#include <bits/stdc++.h>
using namespace std;

vector <string> ans;

int diff(string a, string b) {
	int n = a.size(), cnt = 0;
	for (int i = 0; i < n; i++) cnt += (a[i] != b[i]);
	return cnt;
}

signed main() {
    //cin.tie(0); ios::sync_with_stdio(0);
    int n, f; cin >> n >> f;
    char str[114514]; cin >> str;
    for (char a = 'a'; a <= 'z'; a++)
    	for (char b = 'a'; b <= 'z'; b++) {
    		if (a == b) continue;
    		string moo = string(1, a) + string(2, b), s(str);
    		int change = 1, cnt = 0;
    		
    		for (int i = 0; i < n - 2; i++) {
    			string v = string(s, i, 3);
    			if (v == moo) cnt ++, i += 2;
    			else if (diff(v, moo) <= 1 && change && string(s, i + 1, 3) != moo
					&& string(s, i + 2, 3) != moo) { // 仅相差一位 
    				cnt ++;
    				for (int j = 0; j < 3; j++)
    					if (s[i + j] != moo[j]) s[i + j] = moo[j];
    				change --;
				}
			}
			if (cnt >= f) ans.push_back(moo);
		}
	
	cout << ans.size() << "\n";
	sort(ans.begin(), ans.end());
	for (auto u : ans) cout << u << "\n";
	return 0;
}
```

感觉这么简单的题没什么好说的？还有什么问题或建议就发在评论区吧。

可以催我把代码注释补上。