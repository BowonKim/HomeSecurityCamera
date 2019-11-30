from math import floor

def binary_search(l, num):
    l.sort()
    start = 0
    end = len(l) - 1
    mid = floor((start + end) / 2)
    print(l)
    while start <= end:
        if l[mid] < num:
            start = mid + 1
            mid = floor((start + end) / 2)
        elif l[mid] > num:
            end = mid - 1
            mid = floor((start + end) / 2)
        else:
            return mid
    return False

myfile = open("storedVideo.txt", "r")   #open text file
myfile_int = [] #make list to convert text file from str to int
for lines in myfile.read().split(): #read the line and append to myfile_int
    myfile_int.append(int(lines))
myfile.close()
#print(myfile_int)

date = int(input("Enter the date when do you want to find the saved video"))
index = binary_search(myfile_int, date)

if index is not False:
    print(date)
else:
    print("Search term not found")