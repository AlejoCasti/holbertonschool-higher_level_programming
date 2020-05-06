#include <Python.h>
/**
 * print_python_list_info - print info of python list
 * @p: object
 */
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %zu\n", PyList_Size(p));
	printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);

}
