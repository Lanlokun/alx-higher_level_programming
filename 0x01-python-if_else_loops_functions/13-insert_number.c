#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer to head of list
 * @number: number to insert
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current;

    if (head == NULL)
        return (NULL);

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        current = malloc(sizeof(listint_t) * 2);
        if (current == NULL)
            return (NULL);

        current = *head;
        while (current->next != NULL)
        {
            if (current->n <= number && current->next->n >= number)
            {
                new->next = current->next;
                current->next = new;
                return (new);
            }
            current = current->next;
        }
        current->next = new;
    }
    return (new);
}