#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */


int is_palindrome(listint_t **head)
{
    if (*head == NULL)
        return (1);
    else 
    {
        listint_t *current = *head;
        int i = 0;
        int j = 0;
        int arr[1000];
        while (current != NULL)
        {
            arr[i] = current->n;
            current = current->next;
            i++;
        }
        i--;
        while (i > j)
        {
            if (arr[i] != arr[j])
                return (0);
            i--;
            j++;
        }
        return (1);
    }

}