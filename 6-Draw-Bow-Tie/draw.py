width = int(input('Enter the width of one side of the bow tie : '))

# Pattern problem....It prints the bowtie of specified width of one side.

tot_length = 2*width
for i in range(tot_length-1):
    if i < width:
        for j in range(tot_length):
            if j <= i or j >= tot_length-i-1:
                print('* ', end='')
            else:
                print('  ', end='')
    else:
        temp = i - width + 1
        index = width - temp - 1
        for j in range(tot_length):
            if j <= index or j >= tot_length-index-1:
                print('* ', end='')
            else:
                print('  ', end='')
    print('\n', end='')
