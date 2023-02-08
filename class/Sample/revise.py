import csv,os
try:
   os.rename("data", "datass")
   with open('data/countriess.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print('Header:')
            print(line)  # header
            print('Data:')
        else:
            print(line)  # data
except :
    print("Khong tim thay file")