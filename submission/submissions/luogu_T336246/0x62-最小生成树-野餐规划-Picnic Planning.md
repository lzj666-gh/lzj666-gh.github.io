# 0x62-最小生成树-野餐规划-Picnic Planning

## 题目描述

一群小丑演员，以其出色的柔术表演，可以无限量的钻进同一辆汽车中，而闻名世界。

现在他们想要去公园玩耍，但是他们的经费非常紧缺。

他们将乘车前往公园，为了减少花费，他们决定选择一种合理的乘车方式，可以使得他们去往公园需要的所有汽车行驶的总公里数最少。

为此，他们愿意通过很多人挤在同一辆车的方式，来减少汽车行驶的总花销。

由此，他们可以很多人驾车到某一个兄弟的家里，然后所有人都钻进一辆车里，再继续前进。

公园的停车场能停放的车的数量有限，而且因为公园有入场费，所以一旦一辆车子进入到公园内，就必须停在那里，不能再去接其他人。

现在请你想出一种方法，可以使得他们全都到达公园的情况下，所有汽车行驶的总路程最少。

## 输入格式

第一行包含整数 n，表示人和人之间或人和公园之间的道路的总数量。

接下来 n 行，每行包含两个字符串 A、B 和一个整数 L，用以描述人 A 和人 B 之前存在道路，路长为 L，或者描述某人和公园之间存在道路，路长为 L。

道路都是双向的，并且人数不超过 20，表示人的名字的字符串长度不超过 10，公园用 Park 表示。

再接下来一行，包含整数 s，表示公园的最大停车数量。

你可以假设每个人的家都有一条通往公园的道路。

## 输出格式

输出 Total miles driven: xxx，其中 xxx 表示所有汽车行驶的总路程。

## 时空限制

时间限制: 1000 ms
内存限制: 128 MB
