# Tutorial

## Keywords

+ direct acyclic graph (**DAG**)
+ Strongly connected directed graph
  + Any node can go to and come from any node 
  + v can reach each node in $G$ and $G^T$

## Topological sorting

+ 父节点永远在子节点之前。
+ Possible **iff** the graph is DAG
+ multiple order may exist

### Implementation

+ pushing to stack after marking black and reverse in the end
  + 如果是黑色，说明所有子节点已经被访问。

## Minimal Spanning Tree

+ Include every vertex and have $n-1$ edges
+ Adding one edge produce a cycle

### Implementation

+ Greedy
+ Add the shorted edge encountered
