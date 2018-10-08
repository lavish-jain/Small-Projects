n_bottles = 99
bottle = 'bottles'

while(n_bottles > 0):
    if n_bottles == 1:
        bottle = 'bottle'
    line_one = str(n_bottles) + ' ' + bottle + ' of beer on the wall, ' + str(n_bottles) + ' ' + bottle + ' of beer.'
    n_bottles -= 1
    if n_bottles == 1:
        bottle = 'bottle'
    if n_bottles == 0:
        line_two = 'Take one down and pass it around, no more bottles of beer on the wall.'
    else:
        line_two = 'Take one down and pass it around, ' + str(n_bottles) + ' ' + bottle + ' of beer on the wall'
    print(line_one)
    print(line_two)
    print()

print('No more bottles of beer on the wall, no more bottles of beer.')
print('Go to the store and buy some more, 99 bottles of beer on the wall.')
