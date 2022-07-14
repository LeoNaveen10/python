

print('''
      welcome to car game
      start - start the engine
      stop - stop the engine
      quit - exit the game''');
startFlag=0;
stopFlag = 0;
while(1):
    temp=input('>');
    
    
    if(temp.lower()=='start'):
        if startFlag!=1:
            print('engine started ....');
            startFlag =1;
        else:
            print('engine already started');
            stopFlag=0;           
    elif(temp.lower()=='help'):
        print('''
start - start the engine
stop - stop the engine
quit - exit the game
      ''');
    elif(temp.lower()=='stop'):
        if(stopFlag!=1):
            print('engine stopped');
            stopFlag=1;
        else:
            print('engine already stopped');
            startFlag=0;
    elif(temp.lower()=='quit'):
        break;
    else:
        print('cannot understand the command');
