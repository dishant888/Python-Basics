#Print array without Loop

from array import *

list = array('i',[1,3,44,12,1,35,23,12,45,3]);

def listPrint(list,i):
    if(i == len(list)):
        return 1;
    else:
        print(list[i]);
        i +=1;
        listPrint(list,i);

def revPrint(list,i):
    if(i == 0):
        return 1;
    else:
        print(list[i]);
        i -=1;
        revPrint(list,i);

listPrint(list,0);
print('Reverse: ');
revPrint(list,len(list)-1);