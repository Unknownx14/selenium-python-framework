import csv

def getCSVData(fileName):
    # create an empty list to store the rows from csv file
    listForRows = []

    # open the CSV file
    dataFile = open(fileName, "r")

    # create a CSV reader from the CSV file
    reader = csv.reader(dataFile)

    # skip the headers
    next(reader)

    # add rows from reader to the list
    for row in reader:
        listForRows.append(row)
    return  listForRows