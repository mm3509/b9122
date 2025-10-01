a_list = ["a", ["b", "c"]]  # A list can contain other lists
b_list = a_list.copy()
b_list[0] = "z"
b_list[1][0] = 0

# If b_list is a copy o a_list, why does a_list change when changing
# b_list? Use id() to find the reason.
print(a_list)
