import sys
import os
from github import Github
import getpass

def create():
    path = "E:/projects/"
    username = input('Enter your github username: ')
    password = getpass.getpass('Enter your github password: ')

    while True:
        private = input('Make the repo private?(y/n): ')
        if private not in ['y', 'Y', 'n', 'N']:
            print('Please enter y or n')
        else:
            if private in ['y', 'Y']:
                private = True
            else:
                private = False
            break

    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    try:
        user = Github(username, password).get_user()
        repo = user.create_repo(folderName, private=private)
        print(f"Succesfully created repository {folderName}")

        os.chdir(path + str(folderName))
        os.system('echo # ' + str(folderName) + ' >> README.md')
        os.system('git init')
        os.system('git add README.md')
        os.system('git commit -m "added README"')
        os.system(str("git remote add origin https://github.com/" + username + "/" + str(folderName) + ".git"))
        os.system('git push -u origin master')
    except:
        print('An error was encountered')

if __name__ == "__main__":
    create()
