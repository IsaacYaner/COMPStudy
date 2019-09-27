//Written by z5172587 CHANGYONG YANG, z5183946 YIYAN YANG
//  COMP2521 2019 T1
#include "Graph.h"
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct GraphRep {
   adjListNode **List_out;   // adjacency List matrix for outIncident
   adjListNode **List_in;    // adjaceny List matrix for inIncident
   int    noNodes;      // #vertices
} GraphRep;

//Helper function: add the found node to the end of the list
static AdjList add_end(AdjList new_list, AdjList find);

Graph newGraph(int noNodes) {
   assert(noNodes >= 0);

   Graph g = malloc(sizeof(GraphRep));
   assert(g != NULL);
   g->noNodes = noNodes;
   
   g->List_out = malloc(noNodes * sizeof(struct _adjListNode*));
   for (int i = 0; i < noNodes ; i++){g->List_out[i] = NULL;}
   assert(g->List_out != NULL);
   
   g->List_in = malloc(noNodes * sizeof(struct _adjListNode*));
   for (int i = 0; i < noNodes ; i++){g->List_in[i] = NULL;}
   assert(g->List_in != NULL);

   return g;
}

void  insertEdge(Graph g, Vertex src, Vertex dest, int weight){
    assert(g != NULL);
    //malloc new_out and update info
    AdjList new_out = malloc(sizeof (struct _adjListNode));
    new_out->w= dest;
    new_out->weight = weight;
    new_out->next = NULL;
    
    //malloc new_in and update info
    AdjList new_in = malloc(sizeof (struct _adjListNode));
    new_in->w= src;
    new_in->weight = weight;
    new_in->next = NULL;
    
    //add new_out and new_in to the end of corresponding list
    g->List_out[src] = add_end(g->List_out[src], new_out);
    g->List_in[dest] = add_end(g->List_in[dest], new_in);
    
}

void  removeEdge(Graph g, Vertex src, Vertex dest){
    assert(g != NULL);
    
    AdjList curr = g->List_out[src];
    if (curr->w == dest){
        //if the current node is to be removed
        g->List_out[src] = g->List_out[src]->next;
        free(curr);
    }else{
        //else go find the node in the miidle(or the end) of the list and remove
        while(curr->next != NULL && curr->next->w != dest){
            curr = curr->next;
        }
        if (curr->next->w == dest) {
            AdjList tmp = curr->next;
            curr->next = curr->next->next;
            free(tmp);
        }
    }
    
    curr = g->List_in[dest];
    if (curr->w == src){
        //if the current node is to be removed
        g->List_in[dest] = g->List_in[dest]->next;
        free(curr);
    }else{
        //else go find the node in the miidle(or the end) of the list and remove
        while(curr->next != NULL && curr->next->w != src){
            curr = curr->next;
        }
        if (curr->next->w == src) {
            AdjList tmp = curr->next;
            curr->next = curr->next->next;
            free(tmp);
        }
    }
}

bool adjacent(Graph g, Vertex src, Vertex dest){
    assert(g!=NULL);
    AdjList curr = g->List_out[src];
    
    bool flag = 0 ;
    while(curr != NULL && flag == 0){
        if (curr-> w == dest){
            flag = 1 ;
        }
        curr = curr->next;
    }   
    return flag;

}

int  numVerticies(Graph g){
    return g->noNodes;
}

AdjList outIncident(Graph g, Vertex v){
    assert(g != NULL);
    return g->List_out[v];
}

AdjList inIncident(Graph g, Vertex v){
    assert(g != NULL);
    return g->List_in[v];
}

//Helper function: add the found node to the end of the list
static AdjList add_end(AdjList list, AdjList find){
    AdjList curr = list;
    if (list == NULL){
        list = find;
    }else{
        while(curr->next != NULL){
            curr = curr->next;
        }
        curr->next = find;
    }
    return list;
}

void  freeGraph(Graph g){
    assert(g!=NULL);
    int i;
    AdjList curr;
    AdjList tmp;
    
    //free g->List_out
    for (i = 0; i < g->noNodes; i++){
        curr = g->List_out[i];
        while(curr!=NULL){
            tmp = curr;
            curr = curr->next;
            free(tmp);
        }
    }
    free(g->List_out);
    
    //free g->List_in
    for (i = 0; i < g->noNodes; i++){
        curr = g->List_in[i];
        while(curr!=NULL){
            tmp = curr;
            curr = curr->next;
            free(tmp);
        }
    }
    free(g->List_in);
    free(g);
}

void  showGraph(Graph g){
    assert(g!=NULL);
    
    printf("Number of vertices: %d\n", g->noNodes);
    
    int i = 0;
	int j = 0;
	for (i=0;i<g->noNodes;i++) {
		for (j=0; j<g->noNodes ;j++) {
			if (i == j) continue;
			printf("    %d -> %d : %d\n",i,j,adjacent(g,i,j));
		}
	}
}