#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    list = []
    for i in range(list_length):
        try:
            result = 0
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("out of range type")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            list.append(result)
    return list
