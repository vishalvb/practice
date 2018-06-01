#List slicing

my_list = [0,1,2,3,4,5,6,7,8,9]

print("list = ",my_list)
print("my_list[0:]",my_list[0:])
print("my_list[:]",my_list[:])
print("my_list[:-1]",my_list[:-1])
print("my_list[1:5]",my_list[1:5])

#list(start:end:step)
print("my_list[1::3]",my_list[1::3])
print("my_list[-1:1:-1]",my_list[-1:1:-1])

sample_url = 'https://mydomain.com'
print("sample_url =",sample_url)
print("reverse", sample_url[::-1])