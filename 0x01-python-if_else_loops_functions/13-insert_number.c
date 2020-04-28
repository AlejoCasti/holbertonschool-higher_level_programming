#include "lists.h"
/**
 * insert_node - add new nodo in a sorted linked list
 * @head: pointer to list
 * @number: index to add a new nodo
 * Return: struct added
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *ptr = malloc(sizeof(listint_t));
	unsigned int i;

	if (!ptr)
		return (NULL);
	ptr->n = number;
	if (!head)
		return (ptr->next = NULL, *head = ptr, ptr);
	for (i = 0; tmp; i++)
	{
		if (tmp->n > number && i == 0)
			return (ptr->next = *head, *head = ptr, ptr);
		if (tmp->n < number && (tmp->next == NULL || tmp->next->n > number))
			return (ptr->next = tmp->next, tmp->next = ptr, ptr);
		tmp = tmp->next;
	}
	return (NULL);
}
