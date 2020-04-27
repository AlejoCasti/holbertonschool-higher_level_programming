#include "lists.h"
/**
 * check_cycle - find loop
 * @head: pointer to the list
 * Return: node that start loop
 */
int check_cycle(listint_t *head)
{
	listint_t *tmp, *tmp_t;

	if (!head || !head->next)
		return (0);
	tmp = head->next;
	tmp_t = head->next->next;
	while (tmp && tmp_t && tmp_t->next)
	{
		if (tmp == tmp_t)
			return (1);
		tmp = tmp->next;
		tmp_t = tmp_t->next->next;
	}
	return (0);
}
