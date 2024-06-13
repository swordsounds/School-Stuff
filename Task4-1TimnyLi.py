import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr3 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

if __name__ == '__main__':
    print('Orignal')
    print(f'Array 1:{arr1}\nArray 2:{arr2}\n')

    print('Modifiled')
    print(f'Element wise addition:{arr1 + arr2}')
    print(f'Element wise multiplication:{arr1 * arr2}\n')

    print('Different-shaped Arrays')
    print(f'Original: \n{arr3}')
    print(f'Transposed: \n{arr3.transpose()}')