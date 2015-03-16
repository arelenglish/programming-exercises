// A simple double linked list implemented in C. 

#include <stdio.h>
#include <stdlib.h>

typedef char bool;
#define true 1
#define false 0

struct list_element 
{
  struct list_element * next;
  struct list_element * previous;
};

typedef struct list_element list_element;

typedef struct
{
  list_element * first;
  list_element * last;
} list;

void list_init(list * container)
{
  container->first = 0;
  container->last = 0;
}

bool list_empty(list * container)
{
  return 0 == container->first;
}

list_element * list_begin(list * container)
{
  return container->first;
}

list_element * list_next(list_element * element)
{
  return element->next;
}

list_element * list_previous(list_element * element)
{
  return element->previous;
}

void list_push_back(list * container, list_element * element)
{
  if(list_empty(container))
  {
    container->first = element;
    container->first->previous = 0;
    container->last = element;
  } 
  else
  {
    container->last->next = element;
    element->previous = container->last;
    container->last = element;
  }
  element->next = 0;
}

list_element * list_pop_front(list * container)
{
  list_element * element = container->first;
  container->first = container->first->next;
  if(container->first)
  {
    container->first->previous = 0;
  }
  return element;
}


// Add data to the program to see how it works
typedef struct
{
  list_element header;
  int value;
} item;

int main()

{
  list items;
  item * a = (item *) malloc(sizeof(item));
  item * b = (item *) malloc(sizeof(item));
  item * c = (item *) malloc(sizeof(item));

  printf("What is the value of the first node?\n");
  scanf("%i", &a->value);
  printf("What is the value of the second node?\n");
  scanf("%i", &b->value);
  printf("What is the value of the third node?\n");
  scanf("%i", &c->value);

  list_init(&items);
  list_push_back(&items, &a->header);
  list_push_back(&items, &b->header);
  list_push_back(&items, &c->header);

  for(a = (item *) list_begin(&items); a; a = (item *) list_next(&a->header))
  {
    printf("Loop Started\n");
    
    if(list_previous(&a->header))
    {
      b = (item *) list_previous(&a->header);
      printf("Previous element:%d\n", b->value);
    }

    printf("Current element:%d\n",a->value);

    if(list_next(&a->header))
    {
      c = (item *) list_next(&a->header);
      printf("Next element:%d\n",c->value);
    }
    
    printf("Loop Ended\n\n");
  }

  while(!list_empty(&items))
  {
    a = (item *) list_pop_front(&items);
    free(a);
  }

  return 0;
}
