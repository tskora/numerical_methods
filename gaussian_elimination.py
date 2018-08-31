
def find_row_with_max_value(matrix, column):
    maximal = max(matrix[column:,column])
    for i, value in enumerate(matrix[column:,column]):
        if value == maximal: return i+column
    else: return column

def swap_equations(index1, index2, matrix, vector):
    if index1 != index2:
        n = len(vector)
        for j in range(n):
            matrix[index1,j], matrix[index2,j] = matrix[index2,j], matrix[index1,j]
        vector[index1], vector[index2] = vector[index2], vector[index1]

def gauss_eliminate(matrix, vector):
    n = len(vector)
    for k in range(n-1):
        l = find_row_with_max_value(matrix,k)
        swap_equations(k,l,matrix,vector)
        for i in range(k+1,n):
            multiplier = matrix[i,k]/matrix[k,k]
            matrix[i,k] = 0.0
            vector[i] -= multiplier*vector[k]
            for j in range(k+1,n):
                matrix[i,j] -= multiplier*matrix[k,j];

def back_substitute(matrix, vector, answer):
    n = len(vector)
    for i in reversed(range(0,n)):
        resolved_sum = 0
        for j in range(i+1,n):
            resolved_sum += matrix[i,j]*answer[j]
        answer[i] = (vector[i] - resolved_sum)/matrix[i,i]
    return answer

def gaussian_elimination_solve(system_matrix, right_hand_sides):
    solution = np.zeros(len(right_hand_sides))
    gauss_eliminate(system_matrix, right_hand_sides)
    return system_matrix,back_substitute(system_matrix, right_hand_sides, solution)