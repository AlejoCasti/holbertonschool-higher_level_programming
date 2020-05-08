#include <Python.h>
/**
 * print_python_list - print info of python list
 * @p: object
 */
void print_python_list(PyObject *p)
{
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zu\n", PyList_Size(p));
	printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
/**
 * print_python_bytes - print info of python list
 * @p: object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *s;
	unsigned int i;

	printf("[.] bytes object info\n");
	s = (PyBytesObject *)p;
	if (s && PyBytes_Check(s))
	{
		printf("  size: %ld\n", s->ob_base.ob_size);
		printf("  trying string: %s\n", s->ob_sval);
		printf("  address of the data: %p\n", (void *)(s->ob_sval));
		printf("  bytes:");
		for (i = 0; i < s->ob_base.ob_size + 1 && i < 10; i++)
		{
			printf(" %02x", s->ob_sval[i] & 0xff);
		}
		printf("\n");
	}
	else
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
	}
}
