import os
import fnmatch
from datetime import datetime
from os import path

def Home(): 
    print(user_name + """, press 1 to work with file
     press 2 to work with directory
                            """)

def FileHome():
    print("""
                            press 1 to delete file
                            press 2 to rename file
                            press 3 to add content to this file
                            press 4 to rewrite content of this file
                            press 5 to return to the parent directory
                            press 0 to go back""")

def DirHome(): 
        print("""
                            press 1 to rename directory
                            press 2 to print number of files in it
                            press 3 to print number of directories in it
                            press 4 to list content of the directory
                            press 5 to add file to this directory
                            press 6 to add new directory to this directory""")


print("What is your name?")
user_name = str(input())
while True:
    Home()
    location = int(input())
    curpath = os.getcwd()  
    print(curpath)
    
    if location == 1: 
        FileHome()
        n = int(input()) 
        if n == 0:
            continue

        if n == 1: 
            file_del = input('Enter the name of the file you want to delete: ')
            if os.path.exists(file_del + '.txt'):
                os.remove(curpath + '/' + file_del + '.txt')
                print("File removed!")
                continue
            else:
                print("The file does not exist in this directory")
                continue

        elif n == 2: 
            file_rename = input('Enter the name of file you want to rename: ')
            if os.path.exists(file_rename + '.txt'):
                print('How do you want to rename it?')
                new_name = input()
                os.rename(file_rename + '.txt', new_name + '.txt')
                print("File renamed")   
                continue
            else:
                print("The file does not exist in this directory.")
                continue

        elif n == 3: 
            file_addcon = input('Enter the name of file to add content: ')
            if os.path.exists(file_addcon + '.txt'):
                curFile = open(file_addcon + '.txt', 'a')
                new_content = str(input("What content do you want to add? "))
                curFile.write(new_content)
                curFile.close()
                print(" New content added")
                continue
            else:
                print("The file does not exist ")
                continue

        elif n == 4: 
            file_rewrite = input('Enter the name of file to rewrite content: ')
            if os.path.exists(file_rewrite + '.txt'):
                curFile = open(file_rewrite + '.txt', 'w')
                rewrite_content = input("What do you want to rewrite?")
                curFile.write(rewrite_content)
                curFile.close()
                print("Content rewritten.")
                continue
            else:
                print("The file does not exist in this directory.")
                continue

        elif n == 5:
            parentDir = os.path.dirname(os.getcwd())
            os.chdir(parentDir)
            print('Your parent directory is ' + parentDir)
            continue


    elif location == 2:  
        DirHome()
        curDir = os.getcwd()
        print('Yout current directory is ' + curDir)
        c = int(input())

        if c == 1: 
            dir_rename =  input('Which directory you want to rename? ')
            if os.path.exists(dir_rename):
                new_dir_name = input('Enter a new name for your directory: ')
                os.rename(dir_rename, new_dir_name)
                print('Directory renamed')
                continue
            else:
                print('Directory does not exist')
                continue

        elif c == 2: 
            dir_files = input('Enter the name of directory to print number of files: ')
            if os.path.exists(dir_files):
                dir_list = os.listdir(dir_files)
                num_files = len([1 for x in list(os.scandir(dir_files)) if x.is_file()])
                print('There are ' + str(num_files) + ' files')
                continue
            else:
                print('No such directory')
                continue
            
        elif c == 3: 
            dir_dir = input ('Enter the name of directory to print number of directories: ')
            if os.path.exists(dir_dir):
                num_dir = len([1 for x in list(os.scandir(dir_dir)) if x.is_dir()])
                print('There are ' + str(num_dir) + ' directories ')
                continue
            else:
                print('Directory does not exist')
                continue

        elif c == 4: 
            dir_content = input('Enter the name of directory to list content: ')
            if os.path.exists(dir_content):
                all_dir = os.listdir(dir_content)
                print(all_dir)
                continue
            else:
                print('Directory does not exist')
                continue

        elif c == 5: 
            file_name = input("Enter the new name: ")
            curFile = open(file_name + '.txt', 'w')
            print('File added')
            continue

        elif c == 6: 
            dir_name = input('Enter the new name of directory: ')
            os.mkdir(dir_name)
            print("Directory added")