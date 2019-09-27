// Graph ADT interface for Ass2 (COMP2521)
//Written by z5172587 CHANGYONG YANG, z5183946 YIYAN YANG
//  COMP2521 2019 T1
#include "CentralityMeasures.h"
#include "Dijkstra.h"
#include "PQ.h"
#include <stdlib.h>
#include <stdio.h>

//Helper function: Recursive function to find the number of paths which is through
//the Vertex key from Vertex src
static double find_thru(ShortestPaths paths, PredNode *curr, int key, int src);

//Helper function: Recursive functon to find the number of paths which has the 
//source Vertex src
static double find_count(ShortestPaths paths, PredNode *curr, int src);

NodeValues outDegreeCentrality(Graph g){
	NodeValues throwAway;
	throwAway.noNodes = numVerticies(g);
	throwAway.values = malloc(throwAway.noNodes * sizeof(double));
	
	//Traverse through outIncident linked-list to count the outdegree
	double outNode_count;
	for (int i = 0; i < throwAway.noNodes; i++){
	    outNode_count = 0;
	    AdjList curr = outIncident(g, i);
	    while(curr != NULL){
	        outNode_count ++;
	        curr = curr->next;
	    }
	    throwAway.values[i] = outNode_count;
	}

	return throwAway;
}
NodeValues inDegreeCentrality(Graph g){
	NodeValues throwAway;
	throwAway.noNodes = numVerticies(g);
	throwAway.values = malloc(throwAway.noNodes * sizeof(double));
	
	//Traverse through inIncident linked-list to count the Indegree
	double inNode_count;
	for (int i = 0; i < throwAway.noNodes; i++){
	    inNode_count = 0;
	    AdjList curr = inIncident(g, i);
	    while(curr != NULL){
	        inNode_count ++;
	        curr = curr->next;
	    }
	    throwAway.values[i] = inNode_count;
	}

	return throwAway;
}
NodeValues degreeCentrality(Graph g) {
	NodeValues throwAway;
	throwAway.noNodes = numVerticies(g);
	throwAway.values = malloc(throwAway.noNodes * sizeof(double));
	
	//Simply add both values of outdegree and indegree together
	double outNode_count, inNode_count;
	for (int i = 0; i < throwAway.noNodes; i++){
	    outNode_count = 0;
	    AdjList curr = outIncident(g, i);
	    while(curr != NULL){
	        outNode_count ++;
	        curr = curr->next;
	    }
	    
	    inNode_count = 0;
	    curr = inIncident(g, i);
	    while(curr != NULL){
	        inNode_count ++;
	        curr = curr->next;
	    }
	    
	    throwAway.values[i] = outNode_count + inNode_count;
	}
	return throwAway;
}

NodeValues closenessCentrality(Graph g){
	NodeValues throwAway;
	throwAway.noNodes = numVerticies(g);
	throwAway.values = malloc(throwAway.noNodes * sizeof(double));
	
	ShortestPaths paths;
	double reachable_count;
	double paths_sum;
	for (int i = 0; i < throwAway.noNodes; i++){
	    //for each node, first find the shortest paths to evrey other node
	    paths = dijkstra(g, i);
	    //set reachable_count to 1 since a node can reach to iteself
	    reachable_count = 1;
	    paths_sum = 0;
	    //goes into every value in path.dist array and add its value 
	    //to paths_sum
	    for (int j = 0;j < throwAway.noNodes; j++){
	        if (j != i && paths.dist[j] != 0){
	            reachable_count++;
	            paths_sum += paths.dist[j];
	        }
	    }
        //if paths_sum == 0 ,then it means there is no shortest path to 
        //other nodes
	    if (paths_sum == 0){
	        throwAway.values[i] = 0;
	    }else{
	    //normalise the values using the Wasserman and Faust formula
	        throwAway.values[i] = (reachable_count - 1) / (throwAway.noNodes - 1)
	         * (reachable_count - 1)/ paths_sum;
	    }   
	    freeShortestPaths(paths);
	}
	return throwAway;
}

NodeValues betweennessCentrality(Graph g){
	NodeValues throwAway;
	throwAway.noNodes = numVerticies(g);
	throwAway.values = malloc(throwAway.noNodes * sizeof(double));
	for (int i = 0; i < throwAway.noNodes; i++){throwAway.values[i] = 0;}
	
	ShortestPaths paths;
	double paths_count;
	double paths_thru;
	for (int i = 0; i < throwAway.noNodes; i++){
	    for (int j = 0; j < throwAway.noNodes; j++){
	        if (j != i){
	            paths = dijkstra(g, j);
	            for (int k = 0; k < throwAway.noNodes; k++){
	                if (k != j && k != i){
                        paths_thru = 0;
                        paths_count = 0;
                        //find the number of paths which is through
                        //the Vertex i from source Vertex j
                        paths_thru = find_thru(paths, paths.pred[k], i, j);
                        //if paths_thru is not zero, continue calculating,
                        //otherwise continue to the next loop
                        if (paths_thru != 0){
                            //find the numbers of all paths from source Vertex j
                            paths_count = find_count(paths, paths.pred[k], j);
                            throwAway.values[i] += (paths_thru / paths_count);
                        }
                    }
	            }
	            freeShortestPaths(paths);
	        }
	    }
	}
	return throwAway;
}

NodeValues betweennessCentralityNormalised(Graph g){
    NodeValues throwAway;
	throwAway.noNodes = numVerticies(g);
	throwAway.values = malloc(throwAway.noNodes * sizeof(double));
	for (int i = 0; i < throwAway.noNodes; i++){throwAway.values[i] = 0;}
	
	ShortestPaths paths;
	double paths_count;
	double paths_thru;
	for (int i = 0; i < throwAway.noNodes; i++){
	    for (int j = 0; j < throwAway.noNodes; j++){
	        if (j != i){
	            paths = dijkstra(g, j);
	            for (int k = 0; k < throwAway.noNodes; k++){
	                if (k != j && k != i){
                        paths_thru = 0;
                        paths_count = 0;
                        //find the number of paths which is through
                        //the Vertex i from source Vertex j
                        paths_thru = find_thru(paths, paths.pred[k], i, j);
                        //normalise the value by dividing (n-1)*(n-2)
                        if (paths_thru != 0){
                            //find the numbers of all paths from source Vertex j
                            paths_count = find_count(paths, paths.pred[k], j);
                            throwAway.values[i] += (paths_thru / paths_count) / 
                           ( (throwAway.noNodes - 1) * (throwAway.noNodes - 2));
                            
                        }
                    }
	            }
	            freeShortestPaths(paths);
	        }
	    }
	}
	return throwAway;
}

//Helper function: Recursive function to find the number of paths which is through
//the Vertex key from Vertex src
static double find_thru(ShortestPaths paths, PredNode *start, int key, int src){
    PredNode *curr = start;
    double paths_thru = 0;
    if (curr == NULL){
        return 0;
    }
    while (curr != NULL){
        if (curr->v == key){
        //if current->v is key, then use find_count to find the paths from source
        //to curr->v
            paths_thru += find_count(paths, paths.pred[key], src);
        } else {
            paths_thru += find_thru(paths, paths.pred[curr->v], key, src);
        }
        curr = curr->next;
    }
    return paths_thru;
} 

//Helper function: Recursive functon to find the number of paths which has the 
//source Vertex src
static double find_count(ShortestPaths paths, PredNode *start, int src){
    double paths_count = 0;
    PredNode *curr = start;
    if (curr == NULL){
        return 0;
    }
    while(curr != NULL){
        if (curr ->v == src){
            paths_count++;
        }else {
            paths_count += find_count(paths, paths.pred[curr->v], src);
        }
        curr = curr->next;
    }
    return paths_count;
}
    

void showNodeValues(NodeValues values){
    int i = 0;
    while(i < values.noNodes){
        printf("%d: %f", i, values.values[i]);
        printf("\n");
        i++;
    }
}

void freeNodeValues(NodeValues values){
    free(values.values);
}