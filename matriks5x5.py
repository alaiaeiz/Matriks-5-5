A = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 1, 1, 1, 1]]

B = [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]

result = []
for i in range (5):
    row = []
    for j in range (5):
        total = 0
        for k in range (5):
            total += A[i][k] * B[k][j]
        row.append (total)
    result.append (row)

print ("Hasil Perkalian dari Matriks A x B:")
for r in result:
    print(r)
