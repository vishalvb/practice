import os

'''methods we have access using os module'''
#print(dir(os))

'''get working directory and also list the files and folders inside it'''
print(os.getcwd())
print(os.listdir(os.getcwd()))
#os.rename('new.txt','test.txt')
print(os.listdir(os.getcwd()))

'''to get current path, directories, files'''
print(os.walk(os.getcwd()))

'''to get environment variable'''
print(os.environ.get('APPDATA'))