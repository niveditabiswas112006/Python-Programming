# file_object=open("file path","mode")     
# file_odject.closer()
# r - opens a file reading only
# rb - opens a file fpr reading only in binary format
# r+ - opens a file for both reading and writing
# rb+ - opens a file for both reading an dwriting in binary format
# w - opens a file for writing only
# wb - opens a file for writing only in binary fromat
# w+ - opens a file for both writing and reading
# wb+ - opens a file for both writing and reading in binary formate
# a - opens a file for appending
# ab - opens a file for appending in binary format
# a+ - opens a file for both appending and reading
# ab+ - opens a file for both appending and reading in binary formate 

# ..........................................................................................................................................

# f=open("/Users/niveditabiswas/Documents/python-programmings/myfile.txt","w")
# f=open("./myfile.txt","w")
# data="ITM Kharghar"
 
# f.write(data)

# f.close()

# ..........................................................................................................................................

# f=open("./myfile.txt","r")

# data=f.read()
# print("File contents:",data)
# f.close()

# ............................................................................................................................................

# f=open("./myfile.txt","w")
# data="BTECH CS"
# f.write(data)
# f.close()

# .............................................................................................................................................

# f=open("./myfile.txt","a")
# data="BTECH CS"
# f.write(data)
# f.close()

# .............................................................................................................................................


# f=open("./myfile.txt","r")

# data=f.readlines()
# print("File contents:",data)

# f.close()

# .............................................................................................................................................

# f=open("./myfile.txt","r")

# data=f.readlines()
# print("File contents:",data)
# c=1
# for line in data:
    # print(c,line)
    # c=c+1
# f.close()

# .............................................................................................................................................

# f=open("./myfile.txt","w")
# data=['BTECH CS\n', 'ITM Kharghar']
# f.writelines(data)

# f.close()

# ............................................................................................................................................

f=open("./myfile.txt","w")
f.write("Hello! Learn Python.")
f.close()

lines=["Hello world.\n","Welcome"]
























"""f=open("./myfile.txt","r")
s = f.read(10)        #read the next 10 charater only
print (s)
f.close()
"""
# 