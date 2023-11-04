def shift_list(arr, k, direction):
    n=len(arr)
    if k<n:
        k=k%n 
   
    
    if direction == 'left':
        return arr[k:] + arr[:k]
    elif direction == 'right':
        return arr[-k:] + arr[:-k]
    else:

        return arr

# Example usage:
original_list = list(range(10))
k = int(input('enter the number :'))
direction =input('enter the direction:')
shifted_list = shift_list(original_list, k, direction)
print(f'{shifted_list}')