# # igraph_community_fastgreedy — Finding community structure by greedy optimization of modularity.

# int igraph_community_fastgreedy(const igraph_t *graph,
#                                 const igraph_vector_t *weights,
#                                 igraph_matrix_t *merges,
#                                 igraph_vector_t *modularity,
#                                 igraph_vector_t *membership);

# This function implements the fast greedy modularity optimization algorithm for finding community structure, see A Clauset, MEJ Newman, C Moore: Finding community structure in very large networks, http://www.arxiv.org/abs/cond-mat/0408187 for the details.

# Some improvements proposed in K Wakita, T Tsurumi: Finding community structure in mega-scale social networks, http://www.arxiv.org/abs/cs.CY/0702048v1 have also been implemented.

# Arguments: 

# graph:
	

# The input graph. It must be a graph without multiple edges. This is checked and an error message is given for graphs with multiple edges.

# weights:
	

# Potentially a numeric vector containing edge weights. Supply a null pointer here for unweighted graphs. The weights are expected to be non-negative.

# merges:
	

# Pointer to an initialized matrix or NULL, the result of the computation is stored here. The matrix has two columns and each merge corresponds to one merge, the ids of the two merged components are stored. The component ids are numbered from zero and the first n components are the individual vertices, n is the number of vertices in the graph. Component n is created in the first merge, component n+1 in the second merge, etc. The matrix will be resized as needed. If this argument is NULL then it is ignored completely.

# modularity:
	

# Pointer to an initialized vector or NULL pointer, in the former case the modularity scores along the stages of the computation are recorded here. The vector will be resized as needed.

# membership:
	

# Pointer to a vector. If not a null pointer, then the membership vector corresponding to the best split (in terms of modularity) is stored here.

# Returns: 

	

# Error code.

# See also: 

	

# igraph_community_walktrap(), igraph_community_edge_betweenness() for other community detection algorithms, igraph_community_to_membership() to convert the dendrogram to a membership vector.

# Time complexity: O(|E||V|log|V|) in the worst case, O(|E|+|V|log^2|V|) typically, |V| is the number of vertices, |E| is the number of edges. 

from igraph import *
import igraph

# creat a graph from a edge list
g = Graph.Read_Edgelist("facebook_combined.txt", directed=False)


# algo : initiallt every vertex belongs to a separate community 
# and communities are merged one by one. in every step , the two communities bieng merged are the ones 
# which result in the maximal increase in modularity

dendrogram_var = g.community_fastgreedy()


clusters = dendrogram_var.as_clustering()
print(clusters)

# how many color 
pallet = igraph.drawing.colors.ClusterColoringPalette(len(clusters))

g.vs["color"] = pallet.get_many(clusters.membership)

igraph.plot(g)


