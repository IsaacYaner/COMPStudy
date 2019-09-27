// Dijkstra ADT interface for Ass2 (COMP2521)
//Written by z5172587 CHANGYONG YANG, z5183946 YIYAN YANG
//  COMP2521 2019 T1
#include "Dijkstra.h"
#include "PQ.h"
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include <limits.h>

//Helper function:add the new predecessor Vertex to the end of pred list
static void add_preEnd(ShortestPaths paths, Vertex i, Vertex new_pre);

//Helper function:free pred-list because new predecessor with smaller dist is 
//found
static void free_pred(ShortestPaths paths, Vertex i);

ShortestPaths dijkstra(Graph g, Vertex v) {
	ShortestPaths paths;
	paths.noNodes = numVerticies(g);
	paths.src = v;
	paths.dist = malloc(numVerticies(g) * sizeof(int));
	//first set all the value in dist array to infinity
	for (int i = 0; i < paths.noNodes; i++){paths.dist[i] = INT_MAX;}
	paths.dist[v] = 0;
	
	paths.pred = malloc(numVerticies(g) * sizeof(struct PredNode *));
	for(int i = 0; i < paths.noNodes; i++){paths.pred[i] = NULL;}
	
	//initialise new PQ and add all the vertices to it
	ItemPQ new_item;
	PQ pq = newPQ();
	for (int i = 0; i < paths.noNodes;i++ ){
	    new_item.key = i, 
	    new_item.value = paths.dist[i];
	    addPQ(pq,new_item);
	}
	
	ItemPQ minidist;
	ItemPQ new;
	AdjList neighbour;
	AdjList curr;
	while(PQEmpty(pq) == 0 ){
	//in every iteration, dequeue will give the vertex with smallest distance
	    minidist = dequeuePQ(pq);
        
        neighbour = outIncident(g, minidist.key);
        curr = neighbour;
        while(curr != NULL){
        //if the weight of the edge + distance of minidist equals the distance
        //to the current Vertex, that means we have found another predecessor
            if(paths.dist[minidist.key] != INT_MAX 
            && curr->weight + paths.dist[minidist.key] 
            == paths.dist[curr->w]) {
	            
                add_preEnd(paths, curr->w, minidist.key);
	    
	    //if the weight of the edge + distance of minidist is less than the 
	    //distacne to the current Vertex, then we need remove all the previous
	    //predecessors and add this new one to it
            }else if (paths.dist[minidist.key] != INT_MAX 
            && curr->weight + paths.dist[minidist.key] 
            < paths.dist[curr->w]){
	            //update the value in dist array since we find a smaller path
                paths.dist[curr->w] = curr->weight + paths.dist[minidist.key]; 
                //remove all the previous predesscesor
                free_pred(paths, curr->w);
                //add this new predecessor to curr->w's pred list
                add_preEnd(paths, curr->w, minidist.key);    
                new.key = curr->w;
                new.value = paths.dist[curr->w];
                //update the value in the queue, which is the distance 
                updatePQ(pq, new);
            }
            curr = curr->next;
        }
	    
    }
    //finally set all the INT_MAX value in dist array to be 0
    for (int i = 0; i < paths.noNodes; i++){
        if (paths.dist[i] == INT_MAX){
            paths.dist[i] = 0;
        }
    }
	return paths;
}

void showShortestPaths(ShortestPaths paths) {
    int i = 0;
	printf("Node %d\n",paths.src);
	printf("  Distance\n");
	for (i = 0; i < paths.noNodes; i++) {
        if(i == paths.src){
	        printf("    %d : X\n",i);
	    }
	    else{
	        printf("    %d : %d",i,paths.dist[i]);
		    PredNode* curr = paths.pred[i];
			printf(" ");
			while(curr!=NULL) {
			    printf("[%d]->",curr->v);
			    curr = curr->next;
		    }
		    printf("NULL\n");
		}
	}
}

void  freeShortestPaths(ShortestPaths paths) {
    free(paths.dist);
    int i = 0;
    while(i < paths.noNodes){
        free_pred(paths, i);
        i++;
    }  
}

//Helper function:add the new predecessor Vertex to the end of pred list
static void add_preEnd(ShortestPaths paths, Vertex i, Vertex new_pre){
    PredNode *curr = paths.pred[i];
    PredNode *new = malloc(sizeof (struct PredNode));
    new->v = new_pre;
    new->next = NULL;
    if (paths.pred[i] == NULL){
        paths.pred[i] = new;
    }else{
        while(curr->next != NULL){
            curr = curr->next;
        }
        curr->next = new;
    }
}

///Helper function:free pred-list because new predecessor with smaller dist is 
//found
static void free_pred(ShortestPaths paths, Vertex i){
    PredNode *curr = paths.pred[i];
    PredNode *next;
    if (curr == NULL) return;
    while(curr != NULL){
        next = curr->next;
        free(curr);
        curr = next;
    }
    paths.pred[i] = NULL;
}

