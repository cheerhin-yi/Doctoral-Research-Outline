# 扩展：图搜索与 A\*

层：扩展。当前阶段不读。路径或任务顺序再打开。

参考：Hart, Nilsson, Raphael. A Formal Basis for the Heuristic Determination of Minimum Cost Paths. *IEEE Trans. Systems Science and Cybernetics*, 1968. https://doi.org/10.1109/TSSC.1968.300136

## 必学

图 \(G=(V,E)\)。\(V\) 是节点，\(E\) 是边。边代价 \(c(u,v)\ge 0\)。\(g(n)\) 是从起点到 \(n\) 的已付代价。启发式 \(h(n)\) 是从 \(n\) 到目标的估计，不能高估才保证最优。

\[
f(n)=g(n)+h(n)
\]

A\* 每次扩展 \(f\) 最小的节点。Dijkstra 是 \(h(n)=0\) 的特例，只按已付代价扩。

## 查阅

RRT：连续空间随机树，不是网格 A\*。匈牙利法：二分图最小代价匹配，用于分配而不是寻路。
