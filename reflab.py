# importing libraries 
import subprocess 
import os 

def runcmd(cmd):
    print(cmd)
    os.system(cmd)

def build(args,type,flag,port):
    os.chdir('./'+args)
    buildstr = ''
    contport = 80
    if(type == 'java'):
        buildstr = 'mvn clean install'
        contport = 8080
    if(type == 'ng'):
        buildstr = 'ng build --prod'
        contport = 80
    runcmd(buildstr)
    builddocker(args+'img')
    if(flag == 'y'):
        rundocker(args+'img',contport,port)

def builddocker(args):
    runcmd('docker image rm '+args)
    runcmd('docker build -t '+ args +' .')

def rundocker(args,contport, sysport):
    temp = 'docker ps -a | awk \'{ print $1,$2 }\' | grep '+args+' | awk \'{print $1 }\' | xargs -I {}  docker rm -f {}'
    runcmd(temp)
    runcmd('docker run -d --rm -p '+sysport+':'+str(contport)+' '+args)

def clean(args):
    temp = 'docker ps -a | awk \'{ print $1,$2 }\' | grep '+args+' | awk \'{print $1 }\' | xargs -I {}  docker rm -f {}'
    runcmd(temp)
    runcmd('docker image rm '+args)


if __name__ == '__main__':     
    projs = {"sbservice":"java","sbservice2":"java","ngui":"ng"}
    currentDirectory = os.getcwd()
    cmd = input("What do you want to do \n 1. Cleanup docker \n 2. Build and Deploy\n::")
    if cmd == '1':
        print("Cleaning")
        for proj in projs:
            clean(proj+'img')
    elif cmd == '2':
        inp = input("Do you want to start docker instances? (y/n): ")
        for proj in projs:
            dep = input("Do you want to deploy "+proj+"(y/n):")
            if dep =='y':
                os.chdir(currentDirectory)
                por = 0
                if inp == 'y':
                    por = input("Please enter the port for "+proj+": ")
                build(proj,projs[proj],inp,por)
