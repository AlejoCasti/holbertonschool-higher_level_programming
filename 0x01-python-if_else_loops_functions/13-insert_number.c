#include "lists.h"
/**
 * insert_node - add new nodo in a sorted linked list
 * @head: pointer to list
 * @number: index to add a new nodo
 * Return: struct added
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *ptr;

	ptr = malloc(sizeof(listint_t));
	if (!ptr)
		return (NULL);
	ptr->n = number;
	if (!head || tmp->n > number)
		return (ptr->next = *head, *head = ptr, ptr);
	while (tmp->next)
	{
		if (tmp->n <= number && tmp->next->n > number)
			return (ptr->next = tmp->next, tmp->next = ptr, ptr);
		tmp = tmp->next;
	}
	ptr->next = NULL;
	tmp->next = ptr;
	return (ptr);
}
