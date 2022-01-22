import csv

with open("/Users/snehaprakash/PycharmProjects/pythonBackendAutomation/utilities/Application.csv") as csvfile:
    csvReader = csv.reader(csvfile,delimiter=',')
    #print(list(csvReader))
    namelist = []
    statslist = []
    for item in csvReader:
        namelist.append(item[0])
        statslist.append(item[1])
    print(namelist)
    print(statslist)

Index = namelist.index("Sam")
loanStatus = statslist [Index]
print('Sam loan status is '+ loanStatus)

with open("/Users/snehaprakash/PycharmProjects/pythonBackendAutomation/utilities/Application.csv",'a') as csvwritefile:
    csvWriter = csv.writer(csvwritefile,delimiter=',')
    csvWriter.writerow(["bob","rejected"])