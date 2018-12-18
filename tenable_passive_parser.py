import csv
output = open('host_passive_tenable.txt','w+')
 with open('report_0.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
     line_count=0
     for row in csv_reader:
         try:
             output.write(row[4]+'\n')
         except:
             continue
