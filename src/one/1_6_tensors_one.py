# Tensors are closely-related to arrays. If you interchange tensor/array/matrix when it comes
# to machine learning, people probably won’t give you too hard of a time. But there are subtle
# differences

# simple list
l = [1, 5, 6, 2]

# list of lists
lol = [[1, 5, 6, 2], [3, 2, 1, 3]]

# list of lists of lists
lolol = [[[1, 5, 6, 2], [3, 2, 1, 3]], [[5, 2, 1, 2], [6, 4, 8, 4]], [[2, 8, 5, 3], [1, 1, 9, 4]]]

# list of lists cannot be an array because it is not homologous. A list of lists is
# homologous if each list along a dimension is identically long, and this must be true for each
# dimension.
another_list_of_lists = [[4, 2, 3], [5, 1]]


# A matrix is pretty simple. It’s a rectangular array. It has columns and rows. It is two dimensional.
# So a matrix can be an array (a 2D array). Can all arrays be matrices? No. An array can be far more
# than just columns and rows, as it could have four dimensions, twenty dimensions, and so on.
list_matrix_array = [[4, 2], [5, 1], [8, 2]]


a = [1, 2, 3]
b = [2, 3, 4]

dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print(dot_product)