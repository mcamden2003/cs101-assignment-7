import csv

vehicles = []

min_mpg = -1
while min_mpg < 0 or min_mpg > 100:
    try:
        min_mpg = int(input('Enter the minimum mpg ==> '))
    except ValueError:
        print('You must enter a number for the fuel economy')
    else:
        if min_mpg <= 0:
            print('Fuel economy must be greater than 0')
        elif min_mpg > 100:
            print('Fuel economy must be less than 100')
        else:
            break

while True:
    try:
        file_inp_name = input('Enter the name of the input vehicle file ==> ')
        file_inp = open(file_inp_name, 'r')
    except FileNotFoundError:
        print('Could not open file', file_inp_name)
    else:
        break

while True:
    try:
        file_out_name = input('Enter the name of the output vehicle file ==> ')
        file_out = open(file_out_name, 'w')
    except IOError:
        print('IO Error while opening', file_out_name)
    else:
        break

vehicle_reader = csv.reader(file_inp, delimiter='\t')
header = True
for row in vehicle_reader:
    if header == True:
        header = False
        continue
    try:
        if int(row[7]) >= min_mpg:
            file_out.write('{:<40} {:>10.3f}\n'.format(row[0] + ' ' + row[1] + ' ' + row[2], float(row[7])))
    except ValueError:
            print('Could not convert value', row[7], 'for vehicle', row[0], row[1], row[2])

file_inp.close()
file_out.close()
