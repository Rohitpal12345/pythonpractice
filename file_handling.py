# File handling in python means reading from and writing to files/folder stored on disk using python.
# your python code can open a file , pull data of it,put data into it and also close it properly.

#what is file
#files are store of data and information on the specific path of device.
# types of File
# Text file(.txt,.csv,.json)
# Binary file(image,videos,audio)

# type of path
# Absolute path:The complete path from the root of the file system.
# Relative Path:The path relative to where your current folder(current working directory)


#file mode:
# a: append,a+:append
# w: write,w+:write and read
# r: read, r+: read and write
# x: strictly create file

#Method
# open(file_name,mode):open File
# close():close file
# flush():memory cleanup
# read(): file read
#readLines(): read file line by line
#write(): write data in file only take string
# tail():cursor move
# seek():specific position set of cursor


# create a file in strict mode
# try:

#  file=open("strict.txt","x")
#  print("file craeted ")
# except Exception as e:
#  print("Error","file already exist")


# file=open("write.txt","w")
# file.write("This is completely python file handling")
# file.flush()
# file.close()
# print("file created..")

# context manager
# with open("manager.txt","w+")as file:
#     file.write("this is completely python file")
#     file.seek(0)
#     r=file.read()
#     print("file created and written")
#     print(f"file content:{r}")


# with open("demo.txt","r")as f:
#     r=f.read()
#     for i in r:
#         if i.isdigit():
#           print(i ,end=" ")

emp_list=["aman","shiavm","shubham","anshu","kamal"]
#emp name individual file create txt type

for i in emp_list:
    with open(f"{}.txt","w")as file:
    print(f"{i}.txt")
    print(i)
   

    


