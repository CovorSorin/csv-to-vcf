import csv
import sys

contacts = []

with open(sys.argv[1], 'r') as in_file:
    next(in_file)
    for line in in_file:
        line = line.rstrip().split(',')
        contact = []
        for col in line:
            if col != '""':
                contact.append(col.replace('"', ''))
        contacts.append(contact)

out_file = open(sys.argv[2], 'w')

for contact in contacts:
    tel = contact[-1]
    contact.pop()
    fn = ' '.join(contact)
    if len(contact) < 5:
        for i in range(0, 5 - len(contact)):
            contact.append('')
    n = ';'.join(contact)

    out_file.write('BEGIN:VCARD\n')
    out_file.write('VERSION:2.1\n')
    out_file.write('N:' + n+'\n')
    out_file.write('FN:' + fn + '\n')
    out_file.write('TEL;CELL:' + tel + '\n')
    out_file.write('END:VCARD\n')

out_file.close()
