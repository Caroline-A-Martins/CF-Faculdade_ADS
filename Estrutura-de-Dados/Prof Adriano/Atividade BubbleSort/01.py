def bubble_sort(v):
    fim = len(v)

    while fim > 0:
        i = 0

        while i < fim - 1:
            if v[i] > v[i+1]:
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
                print(v)
            i += 1
        fim -= 1

vetor1 = [40,16,8,4,12]
vetor2 = [20,50,5,4,2,90]
vetor3 = [21,10,11,5,30,50,54]
vetor4 = [12,15,3,4,47,61,33,20]
vetor5 = [9,6,16,23,14,31,29,11,50]

print('1° vetor: ')
bubble_sort(vetor1)

# print(f'2° vetor:')
# bubble_sort(vetor2)

# print(f'3° vetor:')
# bubble_sort(vetor3)

# print(f'4° vetor:')
# bubble_sort(vetor4)

# print(f'5° vetor:')
# bubble_sort(vetor5)
