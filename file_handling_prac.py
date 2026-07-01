import os 
#print(os.listdir()) all file folder in directory
# print("current folder:",os.getcwd()) current working director


emp_list=["aman","shiavm","shubham","anshu","kamal"]
for i in emp_list:
 os.remove(f"{i}.txt")
print(i,"removed..")

os.path.join() # to add file in another folder 