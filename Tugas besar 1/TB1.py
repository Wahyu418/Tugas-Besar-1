import re

def decode_matrix():
    with open('matrix.txt', 'r') as file:
        dimensions = file.readline().strip().split()
        n, m = int(dimensions[0]), int(dimensions[1])
        
        matrix = [''] * n
        
        for i in range(n):
            matrix[i] = file.readline().strip()
            if len(matrix[i]) < m:
                matrix[i] = matrix[i].ljust(m, ' ')
    
    decoded = ''.join([''.join(row[i] for row in matrix) for i in range(m)])
    
    decoded_cleaned = re.sub(r'[^a-zA-Z0-9]+', ' ', decoded)
    
    print(decoded_cleaned)

decode_matrix()