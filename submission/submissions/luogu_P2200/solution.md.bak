# P2200 题解

## 思路
本题涉及到的操作为”横向交换“与”纵向交换“。

实际上，”横向交换“即改变某张卡牌的列号，而”纵向交换“即改变某张卡牌的行号。

容易想到，既然连续进行同种交换不产生额外花费，我们应当试着先统一改变列号，再统一改变行号（或者反过来）。

可是，从第一个样例中我们就可以发现，这样的操作中可能会有冲突。例如，两张卡牌原先所处的行相同而目标列相同，这会使得按列归位时两张卡牌无法同时被移动到目标列。当两张卡牌原先所处的列相同而目标行相同时，也会产生类似的冲突。

通过手动模拟，可以发现，在出现冲突时，我们可以先正常地横向与纵向移动其它卡牌使其归位，再用一次额外的横向或纵向（注意，两种操作中有一种即可，另一种操作可以在之前提前进行）使冲突的卡牌归位。

还需要注意的是，我们需要尽可能减少冲突从而使花费尽可能小。这意味着当同种类型的卡牌有两张出现时，除非两张都会与某张卡牌产生冲突，否则我们就不将其视为冲突；另外，如果只有一个方向的冲突（如只有横向或纵向交换导致冲突），我们完全可以先进行另一个方向的交换，此时也不视为冲突。

最终的代码模拟上述过程即可。

## 代码
```c++
#include <bits/stdc++.h>
using namespace std;

#define CARDID 100003
#define N 303
int cxpos[CARDID],cypos[CARDID],cx2pos[CARDID],cy2pos[CARDID];	// 注意：x 纵向，y 横向。
int oxpos[CARDID],oypos[CARDID],ox2pos[CARDID],oy2pos[CARDID],targets[N][N];	// 卡牌的原先位置
int exist[CARDID] = {}, rexist[CARDID] = {};	// 有几张卡牌
bool counter[CARDID] = {};
bool failure = false;
bool cpx = false, cpy = false;		// 是否有冲突
int xmove = 0, ymove = 0;			// 是否需要进行该方向的交换

inline int mini(int x, int y) {
	return x<y?x:y;
}

inline bool judge(int x1, int y1, int x2, int y2) {
	int &type1 = targets[x1][y1], &type2 = targets[x2][y2];
	bool f1, f2;
	switch (rexist[type1]) {
		case 1:
			switch (rexist[type2]) {
				case 1:
					return (x1 == x2) ? (cypos[type1] == cypos[type2]) : (cxpos[type1] == cxpos[type2]);
					break;
				case 2:
					return (x1 == x2) ? (cypos[type1] == cypos[type2] && cypos[type1] == cy2pos[type2]
						&& oxpos[type1] == oxpos[type2] && oxpos[type1] == ox2pos[type2]) 
						: (cxpos[type1] == cxpos[type2] && cxpos[type1] == cx2pos[type2]
						&& oypos[type1] == oypos[type2] && oypos[type1] == oy2pos[type2]);
					break;
			}
			break;
		case 2:
			switch (rexist[type2]) {
				case 1:
					return (x1 == x2) ? (cypos[type1] == cypos[type2] && cy2pos[type1] == cypos[type2]
						&& oxpos[type1] == oxpos[type2] && ox2pos[type1] == oxpos[type2]) 
						: (cxpos[type1] == cxpos[type2] && cx2pos[type1] == cxpos[type2]
						&& oypos[type1] == oypos[type2] && oy2pos[type1] == oypos[type2]);
					break;
				case 2:
					f1 = (x1 == x2) ? (cypos[type1] == cypos[type2] && cy2pos[type1] == cypos[type2]
						&& oxpos[type1] == oxpos[type2] && ox2pos[type1] == oxpos[type2]) 
						: (cxpos[type1] == cxpos[type2] && cx2pos[type1] == cxpos[type2]
						&& oypos[type1] == oypos[type2] && oy2pos[type1] == oypos[type2]);
					f2 = (x1 == x2) ? (cypos[type1] == cypos[type2] && cypos[type1] == cy2pos[type2]
						&& oxpos[type1] == oxpos[type2] && oxpos[type1] == ox2pos[type2]) 
						: (cxpos[type1] == cxpos[type2] && cxpos[type1] == cx2pos[type2]
						&& oypos[type1] == oypos[type2] && oypos[type1] == oy2pos[type2]);
					return f1 && f2;
					break;
			}
			break;
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int n,a,b,tmp;
	cin>>n>>a>>b;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin>>tmp;
			targets[i][j] = tmp;
			if (!exist[tmp]) {
				oxpos[tmp] = i;
				oypos[tmp] = j;
			} else {
				ox2pos[tmp] = i;
				oy2pos[tmp] = j;
			}
			exist[tmp]++;
			rexist[tmp]++;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin>>tmp;
			if (!exist[tmp]) {
				failure = true;
			} else {
				exist[tmp]--;
				if (oxpos[tmp] != i && ox2pos[tmp] != i) {
					xmove = 1;
				}
				if (oypos[tmp] != j && oy2pos[tmp] != j) {
					ymove = 1;
				}
				if (counter[tmp]) {
					cx2pos[tmp] = i;
					cy2pos[tmp] = j;
				} else {
					cxpos[tmp] = i;
					cypos[tmp] = j;
				}
				counter[tmp] = true;
			}
		}
	}
	if (failure) {
		cout<<"Fail"<<endl;
		return 0;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < i; k++) {
				if (judge(i,j,k,j)) {
					cpx = true;
				}
			}
			for (int k = 0; k < j; k++) {
				if (judge(i,j,i,k)) {
					cpy = true;
				}
			}
		}
	}
	int result = xmove * b + ymove * a;
	if (cpx && cpy) {
		result += mini(a,b);
	}
	cout<<result<<endl;

	return 0;
}
```