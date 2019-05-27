import csv

with open('test.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)


    # next(csv_reader)
    # with open('new_test.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='\t')

        # with open('new_test.csv', 'w') as new_file:
        #     csv_writer = csv.writer(new_file, delimiter='-')



        # for line in csv_reader:
        #     csv_writer.writerow(line)

# with open('new_test.csv', 'r') as csv_file_2:
#     csv_reader_2 = csv.reader(csv_file_2, delimiter='\t')
#
#     for line_2 in csv_reader_2:
#         print(line_2)
