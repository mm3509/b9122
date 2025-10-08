a_list = ["a", ["b", "c"]]  # A list can contain other lists
b_list = a_list.copy()
b_list[0] = "z"
b_list[1][0] = 0

# If b_list is a copy o a_list, why does a_list change when changing
# b_list? Use id() to find the reason.
print(a_list)


# .copy() performs a shallow copy of the values. If the value is a
# memory address, .copy() copies that, not the value inside that
# address.
print("Same memory address of the first element:", id(a_list[0]) == id(b_list[0]))
print("Same memory address of the second element:", id(a_list[1]) == id(b_list[1]))

import copy
a_list = ["a", ["b", "c"]]
c_list = copy.deepcopy(a_list)
c_list[1][0] = 0
print(a_list)
