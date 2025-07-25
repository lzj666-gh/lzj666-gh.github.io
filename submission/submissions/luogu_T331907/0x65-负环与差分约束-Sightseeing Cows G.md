# 0x65-负环与差分约束-Sightseeing Cows G

## 题目描述

Farmer John has decided to reward his cows for their hard work by taking them on a tour of the big city! The cows must decide how best to spend their free time.

Fortunately, they have a detailed city map showing the L (2 ≤ L ≤ 1000) major landmarks (conveniently numbered 1.. L) and the P (2 ≤ P ≤ 5000) unidirectional cow paths that join them. Farmer John will drive the cows to a starting landmark of their choice, from which they will walk along the cow paths to a series of other landmarks, ending back at their starting landmark where Farmer John will pick them up and take them back to the farm. Because space in the city is at a premium, the cow paths are very narrow and so travel along each cow path is only allowed in one fixed direction.

While the cows may spend as much time as they like in the city, they do tend to get bored easily. Visiting each new landmark is fun, but walking between them takes time. The cows know the exact fun values Fi (1 ≤ Fi ≤ 1000) for each landmark i.

The cows also know about the cowpaths. Cowpath i connects landmark L1i to L2i (in the direction L1i -> L2i ) and requires time Ti (1 ≤ Ti ≤ 1000) to traverse.

In order to have the best possible day off, the cows want to maximize the average fun value per unit time of their trip. Of course, the landmarks are only fun the first time they are visited; the cows may pass through the landmark more than once, but they do not perceive its fun value again. Furthermore, Farmer John is making the cows visit at least two landmarks, so that they get some exercise during their day off.

Help the cows find the maximum fun value per unit time that they can achieve.

作为对奶牛们辛勤工作的回报，$Farmer\ John$决定带她们去附近的大城市玩一天。旅行的前夜，奶牛们在兴奋地讨论如何最好地享受这难得的闲暇。  
很幸运地，奶牛们找到了一张详细的城市地图，上面标注了城市中所有$L(2\leqslant L\leqslant1000)$座标志性建筑物（建筑物按$1\dots L$顺次编号），以及连接这些建筑物的$P(2\leqslant P\leqslant5000)$条道路。按照计划，那天早上$Farmer\ John$会开车将奶牛们送到某个她们指定的建筑物旁边，等奶牛们完成她们的整个旅行并回到出发点后，将她们接回农场。由于大城市中总是寸土寸金，所有的道路都很窄，政府不得不把它们都设定为通行方向固定的单行道。  
尽管参观那些标志性建筑物的确很有意思，但如果你认为奶牛们同样享受穿行于大城市的车流中的话，你就大错特错了。与参观景点相反，奶牛们把走路定义为无趣且令她们厌烦的活动。对于编号为$i$的标志性建筑物，奶牛们清楚地知道参观它能给自己带来的乐趣值$F_i (1\leqslant F_i\leqslant1000)$。相对于奶牛们在走路上花的时间，她们参观建筑物的耗时可以忽略不计。  
奶牛们同样仔细地研究过城市中的道路。她们知道第i条道路两端的建筑物$L1_i$和$L2_i$（道路方向为$L1_i  \rightarrow L2_i$），以及她们从道路的一头走到另一头所需要的时间$T_i(1\leqslant T_i\leqslant1000)$。  
为了最好地享受她们的休息日，奶牛们希望她们在一整天中平均每单位时间内获得的乐趣值最大。当然咯，奶牛们不会愿意把同一个建筑物参观两遍，也就是说，虽然她们可以两次经过同一个建筑物，但她们的乐趣值只会增加一次。顺便说一句，为了让奶牛们得到一些锻炼，$Farmer\ John$要求奶牛们参观至少$2$个建筑物。  
请你写个程序，帮奶牛们计算一下她们能得到的最大平均乐趣值。

## 输入格式

\* Line 1: Two space-separated integers: L and P

\* Lines 2..L+1: Line i+1 contains a single one integer: Fi

\* Lines L+2..L+P+1: Line L+i+1 describes cow path i with three space-separated integers: L1i , L2i , and Ti


## 输出格式

\* Line 1: A single number given to two decimal places (do not perform explicit rounding), the maximum possible average fun per unit time, or 0 if the cows cannot plan any trip at all in accordance with the above rules.


## 时空限制

时间限制: 1000 ms
内存限制: 128 MB
