# ZK Protocol Based on The Graph Isomorphism Problem

This is a very basic implementation of a zk protocol based on isomorphic graphs. The graph isomorphism problem is not known to be NP-complete for the general case and is currently an open problem.


## Basics

Every wallet is a graph with 70 nodes and some amount of edges less than a complete graph. There are approximately $10^{48}$ unique coloring where each coloring is a wallet.

Every object is a graph with 3 nodes and some amount of edges less than a complete graph. There are $4$ unique objects within this system.

Storing an object inside a wallet is a tensor product of two graphs, the wallet graph and the object graph.

To prove ownership is to show that two graphs are isomorphic.

# Wallets

A user is assigned a signing graph that can be uniquely colored using the coloring algorithm defined in coloring.py. The unique coloring of the signing graph is hashed and used as a mapping to define the verification graph. These two graphs are equalivent when looking at the hash of the colors list used in the coloring of each graph.

Let $G_{1}=(V_{1},𝐸_{1})$ be the signing graph and $F$ being some one-to-one mapping then $F: G_{1} \rightarrow G_{2}$ where $G_{2}=(V_{2},E_{2})$ is the verification graph. If $F$ is known then it is trival to obtain a signing graph from any verification graph but guessing $F$ is very challenging when the number of vertices is large.

The mapping $F$ is obtained by:

$$Base_{q}(Base_{10}(Hash(Col(G)))) \rightarrow F$$
The $Base_{i}$ function writes a number into base $i$. The $Hash$ function is the sha3_256 hashing algorithm and $Col$ is the coloring algorithm defined in coloring.py. The result is a list of integers than are used to map the vertices $V_{1}=\{1,..,n\}$ into $V_{2}$.

The state of a wallet is the hash of the verification graph's coloring solution.

# Objects

A user owns an object because the object graph becomes embedded into the verification graphs using a tensor product.

Let $O_{i} = (3, E)$ be an object being represented as a graph. A users verification graph will be advanced into a new state by the tensor product of the verification graph and the object graph.

$$G_{2}' = G_{2} \otimes O_{i}$$

The hash of new verification graph's coloring solution is the new state of the wallet.