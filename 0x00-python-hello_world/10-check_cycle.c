#include "lists.h"

/**
 * check_cycle - checks if list is cyclical
 * @list: pointer to list
 * Return: 1 o 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = list->next;
		fast = list->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
