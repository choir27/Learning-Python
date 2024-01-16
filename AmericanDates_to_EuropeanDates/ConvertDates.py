# 100 files with American style dates (MM-DD-YYYY)
# need to convert them to European style dates (DD-MM-YYY)

# first, let's automate the creation of these american files
# 100 files is a lot of space. lets compress it to be efficient

from pathlib import Path
import shutil, zipfile, os

# January - 31 days
# February - 28 days in a common year (we're ignoring leap year)
# March - 31 days
# April - 30 days
# May - 31 days
# June - 30 days
# July - 31 days
# August - 31 days
# September - 30 days
# October - 31 days
# November - 30 days
# December - 31 days

# def generateDates():
#     month = 1
#     day = 1
#     year = 2023

#     dates = []

#     for i in range(1, 101):

#         dates.append(f'{month}_{day}_{year}')

#         day += 1

#         if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
#             if day == 31:
#                 day = 1
#                 month += 1
#         if month == 4 or month == 6 or month == 9 or month == 11:
#             if day == 30:
#                 day = 1
#                 month += 1
#         if month == 2:
#             if day == 28:
#                 day = 1
#                 month +=1
#         if month == 12:
#             if day == 12:
#                 day = 1
#                 month = 1
#                 year +=1

#     return dates

# currP = Path.cwd()
# currDir = str(currP) + '/AmericanDates_to_EuropeanDates'

# ameDir = currDir + '/AmericanDates'

# for i in range(0,100):
#     dates = generateDates()
#     dateFile = open(Path(f"{ameDir}/{dates[i]}.txt"), 'w')
    # dateFile.write(str(dateFile))
    # dateFile.close()

    # newZip = zipfile.ZipFile('AmericanDates.zip', 'a')
    # newZip.write(f"{ameDir}/{dates[i]}.txt", compress_type= zipfile.ZIP_DEFLATED)
    # newZip.close()

currP = Path.cwd()
currDir = str(currP) + '/AmericanDates_to_EuropeanDates'

euroDir = currDir + '/EuropeanDates'

currZip = zipfile.ZipFile('AmericanDates.zip')

AmeDateFiles = currZip.namelist()

for files in AmeDateFiles:
    splitFiles = files.split('/')
    fileName = splitFiles[-1]

    tempSplit = fileName.split('.')
    tempSplit.pop()

    date = ''.join(tempSplit).split('_')

    # M - D - Y

    dateFile = open(Path(f"{euroDir}/{f'{date[1]}_{date[0]}_{date[-1]}'}.txt"), 'w')
    # need to convert them to European style dates (DD-MM-YYY)

    dateFile.write(str(dateFile))
    dateFile.close()

    newZip = zipfile.ZipFile('EuropeanDates.zip', 'a')
    newZip.write(f"{euroDir}/{f'{date[1]}_{date[0]}_{date[-1]}'}.txt", compress_type= zipfile.ZIP_DEFLATED)
    newZip.close()