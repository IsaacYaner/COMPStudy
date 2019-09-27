// PQ ADT interface for Ass2 (COMP2521)
//Written by z5172587 CHANGYONG YANG, z5183946 YIYAN YANG
//  COMP2521 2019 T1
#include "PQ.h"
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

typedef struct Item{
    ItemPQ *data;
    struct Item *next;
}Item;

struct PQRep {
    Item *head;
    Item *tail;
    int length;
};

//Helper function: use the key to find the pointer to the item
static Item *find_key(PQ p, int key);

PQ newPQ() {
    PQ q = malloc(sizeof(struct PQRep));
    q->head = NULL;
    q->tail = NULL;
    q->length = 0;
	return q;
}

int PQEmpty(PQ p) {
    return (p->length == 0);
}

void addPQ(PQ pq, ItemPQ element) {
    Item *find = find_key(pq, element.key);
    if (find == NULL){
        //if there is not element which has the key of the element
        //then create a new item with relevant info
        Item *new = malloc(sizeof(struct Item));
        new->next = NULL;
        new->data = malloc(sizeof (struct ItemPQ));
        new->data->key = element.key;
        new->data->value = element.value;
        
        //add the new item to the queue
        if (pq->tail != NULL){
            pq->tail->next = new;
            pq->tail = new;
        }else{
            pq->head = new;
            pq->tail = new;
        }
        pq->length++;
    }else{
        find->data->value = element.value; 
    }
}

ItemPQ dequeuePQ(PQ pq) {
	ItemPQ throwAway;
	assert(pq->length != 0);
	
	Item *throw = pq->head;
	Item *pre_throw; //used to store the pointer pointing to the previous item
	Item *curr;
	//if there is only one item, throwaway is the head
	if (pq->length == 1){
	    throwAway.key = pq->head->data->key;
	    throwAway.value = pq->head->data->value;
	    free(pq->head->data);
	    free(pq->head);
	    pq->head = NULL;
	    pq->tail = NULL;
	    pq->length--;
	    return throwAway;
	}else{
	//else start traversing the queue to find the throwaway with smallest value
	    curr = pq->head;
	    while(curr->next != NULL ){
	        if (curr->next->data->value < throw->data->value){
	            throw = curr->next;
	            pre_throw = curr;
	        }
	        curr = curr->next;
	    }
	    throwAway.key = throw->data->key;
	    throwAway.value = throw->data->value;
	 
	    //if head is to be thrown, update pq->head
	    if (throw == pq->head){
	        pq->head = pq->head->next;
	    } else {
	     //if tail is to be thrown, update pq->tail
	        if(throw == pq->tail){
	            pq->tail = pre_throw;
	            pq->tail->next = NULL;
	        }
	        pre_throw->next = throw->next;
	    }
	    pq->length--;
	    free(throw->data);
	    free(throw);
	}
	return throwAway;
}

void updatePQ(PQ pq, ItemPQ element) {
    Item *find = find_key(pq, element.key);
    if (find == NULL){return;} //If item with 'key' does not exist, do nothing.
    else{
        find->data->value = element.value;
        //now we need to move the updated value to the end of the queue
        //to make sure FIFO for the next time
        
        if (find == pq->head && pq->length >1){
            pq->head = pq->head->next;
            find->next = NULL;
            pq->tail->next = find;
            pq->tail = find;
        }else if (find == pq->tail){
            return ;
        }else {
        //if uodated item is in the middle of the queue, move it to the end
            Item *curr = pq->head;
            while(curr->next != find){
                curr = curr->next;
            }
            curr->next = find->next;
            find->next = NULL;
            pq->tail->next = find;
            pq->tail = find;
        } 
    }
    return ;
}

void  showPQ(PQ pq) {
	assert (pq != NULL);
    int count = 0;
	for (Item *curr = pq->head; curr != NULL; curr = curr->next) {
	    count++;
		printf("key: %d, value = %d, count = %d \n", curr->data->key, 
		curr->data->value, count);
		if (curr->next != NULL)
			printf (">");
	}
	printf ("\n");
}

void  freePQ(PQ pq) {
    assert (pq != NULL);
	for (Item *curr = pq->head, *next; curr != NULL; curr = next) {
		next = curr->next;
		//free ItemPQ
		free(curr->data);
		//free the whole item
		free(curr);
	}
	free (pq);
}

//Helper function: use the key to find the pointer to the item
static Item *find_key(PQ p, int key){
    Item *curr = p->head;
    if (p->head == NULL){
        return NULL;
    
    }else{
        while(curr != NULL){
            if (curr->data->key == key){
                return curr;
            }
            curr = curr->next;
        }
        //if not found, then return NULL
        return NULL;
    }
}
