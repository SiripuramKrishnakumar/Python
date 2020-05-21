f = open('My Personal Details', 'r')

print(f)

# print(f.read()) # print entire content

# print(f.readline()) # print 1st line
# print(f.readline()) # print 2nd line it has inbuild next function

# print(f.readline(3)) # print mentioned line number

# print(f.readable()) # it returns boolean which file is readable or not

'''TO WRITE DATA'''

f1 = open('Emptyfile','w') # if file not exist it will create file with mentioned name

print(f1)
f1.write('Hello World')
print(f1.writable())
f1.write('hkfvgfghligdsf')
f1 = open('abc','a')
print(f1)
# a = append
f1.write('Hello') # it delete previous data nd wirte this content

# copying f data in f1

for data in f:
    f1.write(data)
# we can do with images etc also