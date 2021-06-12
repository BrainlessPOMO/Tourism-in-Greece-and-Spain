from sys import winver
import time
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
print('Ξεκινάει η καταμέτρηση και θα αποθηκευτεί στο αρχείο time.txt')

start_time = time.time()

flag = 'oxidone'

while flag != 'done':
    flag = input('Όταν είναι να τελειώσει η καταμέτρηση, γράψε done \n')
    print('Έγραψες: ' + flag)

end_time = time.time()
time_elapsed = end_time - start_time

hours = (time_elapsed // 120)
mins = (time_elapsed // 60)

lines = [str(time_elapsed) + ' σε δευτερόλεπτα \n', str(mins) + ' σε λεπτά \n' , str(hours) + ' σε ώρες \n']

path = 'time.txt'
f = open(path, 'r')

with open('time.txt','r') as original_file:
    orig_data = original_file.read()
f.close()

path = 'time.txt'
f = open(path, 'w')
with open('time.txt', 'w') as f:
    f.write(orig_data)
    f.write('{\n')
    for line in lines:
        f.write('   Ο χρόνος που πέρασε μέχρι να κλείσει το pc, είναι: ' + line)
    f.write('} Η ημερομηνία που τελείωσε αυτό το session είναι: ' + str(d1) + '\n\n')
f.close()