#! /usr/bin/env python3
#SHEBANG

def dikupatuples():
    #tuples
    modules = ('netmiko','scapy','socket','smtp')
    extramodules = ('paramiko','loguru')

    print("Printing tuple");
    print(modules)

    try:
        print("Printing append tuple");
        modules.append('pytube')
        modules.sort()
        modules.reverse()
        modules.insert(0,'beautifulsoap')
        print(modules)
    except:
        print("Tuples not have append, reverse,sort,insert,pop,remove,extend")

    print("Printing single value from tuple");
    print(modules[0])

    print("Printing specific range values from tuple");
    print(modules[1:3])

    print("Printing specific values from last on tuple");
    print(modules[-2])

    print("Checking value available in tuple or not");
    print('pytube' in modules)

    print("Checking position of value in tuple");
    print(modules.index('socket'))

    numeric = (1,2,3)

    print("Printing sum of tuple");
    print(sum(numeric))

    print("Printing max of tuple");
    print(max(numeric))

    print("Printing min of tuple");
    print(min(numeric))
    

def main():
    try:
        
        dikupatuples()
            
    except KeyboardInterrupt:
        
        print("Exiting because of program interpreted by user"); print("Thanks for using my application");
       


if __name__=='__main__':
       main() 
