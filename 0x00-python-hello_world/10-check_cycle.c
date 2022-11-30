#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *current;
    listint_t *temp;

    current = list;
    temp = list;
    while (current != NULL && temp != NULL && temp->next != NULL)
    {
        current = current->next;
        temp = temp->next->next;
        if (current == temp)
            return (1);
    }
    return (0);
}