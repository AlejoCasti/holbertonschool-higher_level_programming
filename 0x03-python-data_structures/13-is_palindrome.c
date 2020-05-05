#include "lists.h"
/**
 * get_result - verify if is palindrome word
 * @head: first node of linked list
 * @a: module of list length
 * @middle: middle of linked
 * Return: 1 is palindrome 0 is not
 */
int get_result(listint_t **head, int a, int middle)
{
	listint_t *ptr = *head;
	int i, sum = 0;

	for (i = 0; ptr; i++)
	{
		if (a == 1 && i == middle)
		{
			ptr = ptr->next;
			continue;
		}
		if (i < middle)
			sum += ptr->n;
		else if (i >= middle)
			sum -= ptr->n;
		if (!ptr->next)
			break;
		ptr = ptr->next;
	}
	if (sum != 0 || (*head)->n != ptr->n)
		return (0);
	else
		return (1);
}
/**
 * is_palindrome - verify if is palindrome word
 * @head: first node of linked list
 * Return: 1 is palindrome 0 is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	int counter = 0;

	while (ptr)
		ptr = ptr->next, counter++;
	if (counter == 1)
		return (1);
	return (get_result(head, counter % 2, counter / 2));

}
