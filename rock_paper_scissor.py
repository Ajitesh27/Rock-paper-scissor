import time
import getpass
global u
u=["q","n"]#q=quit,n=no quit
global h
h=["r","p","s"]#r =rock,p=paper,s=scissor
global p
p=["e","m","h"] #e-easy,m-medium,h-hard
global q
q=["1","2"] #1-single,2-double
global w
w=["y","n"] #y-yes,n-no
def score(l): #Function to print current score
     print("Current Score: ",end=" ")
     for i in l:
          print(i,end=" ")
     print()
def num(i): #Function to check if user input is valid 
     c=0
     f=0
     d=list(i)    
     for k in d:
          for j in range(49,58):
               if ord(k)==j:                    
                    c=c+1
     if c==len(d):
          f=1             
     return(f)
def graph(): # Function to print the name of the game
     print('''
 ===================================================================================================
|                                                                                                   |
|          =========     ==========     =========   ||         //                                        |
|         ||               ||   ||              ||   ||                 ||       //                                         |
|         ||               ||   ||              ||   ||                 ||    //                                          |
|         ||               ||   ||              ||   ||                 ||  //                                           |
|         ||======== ||    ||             ||   ||                  ||//                                            | 
|         || \\                ||             ||   ||                 ||\\                                             |
|         ||  \\               ||             ||   ||                 ||   \\                                            |
|         ||   \\              ||             ||   ||                 ||       \\                                           |
|         ||    \\\\           ==========     ========= ||        \\                                        |
|                                                                                                   |
|          =========     ==========     =========    =========    =======                           |
|         ||              ||   ||                ||   ||             ||  ||                  ||           ||                          |
|         ||              ||   ||                ||   ||             ||  ||                  ||           ||                          |
|         ||========    ||========    ||   ||========   ||                  ||            ||                          |
|         ||                 ||                 ||   ||                 ||=======      ||======                           |
|         ||                 ||                 ||   ||                 ||                  || \\                               |
|         ||                 ||                 ||   ||                 ||                  ||     \\                              |
|         ||                 ||                 ||   ||                 ||=========   ||         \\                          |
|                                                                                                   |
|         =========    ==========   ===========   =========   ==========    ========    =======     
          ||                  ||                          ||           ||                ||                    ||           ||  ||          ||   
          ||                   ||                          ||          ||                 ||                   ||          ||  ||          ||   
          ||                   ||                         ||           ||                 ||                   ||          ||  ||          ||   
            ======== ||    ||                        ||           ||========   ||========      ||          ||  ||=======    
                           ||   ||                         ||                        ||                ||      ||          ||  ||\\         
                           ||   ||                         ||                         ||               ||      ||          ||  ||   \\        
                           ||   ||                      ||                            ||               ||      ||          ||  ||     \\       
          =========     ==========   ===========   =========   =========     =======   ||        \\   
|                                                                                                   |
 ===================================================================================================
 ''')   
def paper(): #Function to print paper
     print('''
           =========     ==========     =========    =========    =======                           |
|         ||              ||   ||                ||   ||             ||  ||                  ||           ||                          |
|         ||              ||   ||                ||   ||             ||  ||                  ||           ||                          |
|         ||========    ||========    ||   ||========   ||                  ||            ||                          |
|         ||                 ||                 ||   ||                 ||=======      ||======                           |
|         ||                 ||                 ||   ||                 ||                  || \\                               |
|         ||                 ||                 ||   ||                 ||                  ||     \\                              |
|         ||                 ||                 ||   ||                 ||=========   ||         \\                          |
|                                                                                                   |
                                   ''')
def rock(): #Function to print rock
     print('''                                                                                       
              =========     ==========     =========   ||         //                                        |
|         ||               ||   ||              ||   ||                 ||       //                                         |
|         ||               ||   ||              ||   ||                 ||    //                                          |
|         ||               ||   ||              ||   ||                 ||  //                                           |
|         ||======== ||    ||             ||   ||                  ||//                                            | 
|         || \\                ||             ||   ||                 ||\\                                             |
|         ||  \\               ||             ||   ||                 ||   \\                                            |
|         ||   \\              ||             ||   ||                 ||       \\                                           |
|         ||    \\\\           ==========     ========= ||        \\                                        |
|                                                                                                   |

             ''')
def scissor(): #Function to print scissor
     print('''
          =========    ==========   ===========   =========   ==========    ========    =======     
          ||                  ||                          ||           ||                ||                    ||           ||  ||          ||   
          ||                   ||                          ||          ||                 ||                   ||          ||  ||          ||   
          ||                   ||                         ||           ||                 ||                   ||          ||  ||          ||   
            ======== ||    ||                        ||           ||========   ||========      ||          ||  ||=======    
                           ||   ||                         ||                        ||                ||      ||          ||  ||\\         
                           ||   ||                         ||                         ||               ||      ||          ||  ||   \\        
                           ||   ||                      ||                            ||               ||      ||          ||  ||     \\       
          =========     ==========   ===========   =========   =========     =======   ||        \\   
          ''')
def method(l,b,i):
     if b=="rock": #assigning value of d based on computer's random selection of b
         d=3
     if b=="paper":
         d=1
     if b=="scissor":
         d=2     
     a=getpass.getpass("Player enter any one out of rock,paper,scissor as r for rock,s for scissor and p for paper or q to quit: ").lower()     
     if a=="q": #Quit if user decides to quit
          quit()     
     while a not in h:
          print("SORRY WE CANNOT RESPOND TO WHAT YOU ENTERED,PLEASE RE-ENTER IN THE GIVEN FORMAT SPECIFIED ABOVE.")
          a=getpass.getpass("Player enter any one out of rock,paper,scissor as r for rock,s for scissor and p for paper or q to quit: ").lower()##
          if a=="q":
              quit()  
     if a in h:
          if a=="r":  #Assigning values to f based on user input
               f=3
          if a=="p":
               f=1
          if a=="s":
               f=2
          if d==1 and f==3: #Increment points of winner
              l[0]+=1
          elif d==3 and f==1:
              l[1]+=1
          else:
              if f>d:
               l[1]+=1
              if d>f:
               l[0]+=1
          score(l)
          print("Computer's move: ",end=" ")  #Print computer's move
          if b=="rock":
             rock()
          if b=="paper":
             paper()
          if b=="scissor":
             scissor()
          print(i,"'s move: ",end=" ") #Print user's move
          if a=="r":
             rock()
          if a=="p":
             paper()
          if a=="s":
             scissor()
     return(l)
def method1(l,i,j):    
     b=getpass.getpass("Player1 enter any one out of rock,paper,scissor as r for rock, p for paper and s for scissor or q to quit: ").lower()     
     if b=="q":
          quit()     
     a=getpass.getpass("Player2 enter any one out of rock,paper,scissor as r for rock, p for paper and s for scissor or q to quit: ").lower()
     if a=="q":
          quit()     
     while b not in h:
          print(i,"SORRY WE CANNOT RESPOND TO WHAT YOU ENTERED,PLEASE RE-ENTER IN THE GIVEN FORMAT SPECIFIED ABOVE.")
          b=getpass.getpass("Player1 enter any one out of rock,paper,scissor as r for rock, p for paper and s for scissor or q to quit: ").lower()
          if b=="q":
              quit()    
     while a not in h:
          print(j,"SORRY WE CANNOT RESPOND TO WHAT YOU ENTERED,PLEASE RE-ENTER IN THE GIVEN FORMAT SPECIFIED ABOVE.")
          a=getpass.getpass("Player2 enter any one out of rock,paper,scissor as r for rock, p for paper and s for scissor or q to quit: ").lower()
          if a=="q":
              quit()     
     if b in h:          
          if b=="r":  #Assigning values to d based on user input
            d=3
          if b=="p":
            d=1
          if b=="s":
            d=2
     if a in h:
          if a=="r":
            f=3
          if a=="p":
            f=1
          if a=="s":
            f=2
     if d==1 and f==3:
            l[0]+=1   #Increment winner's points
     elif d==3 and f==1:
            l[1]+=1    #Increment winner's points
     else:
            if f>d:
                l[1]+=1
            if d>f:
                l[0]+=1
     score(l)
     print(i,"'s move; ",end=" ")
     if b=="r":  #Printing user 1 move
            rock()
     if b=="p":
            paper()
     if b=="s":
            scissor()
     print(j,"'s move: ",end=" ")  
     if a=="r":  #Printing user 2 move
            rock()
     if a=="p":
            paper()
     if a=="s":
            scissor()          
     return(l)
def single(x):
     z=""
     import random
     l=["rock","paper","scissor"]   
     l1=[0,0]
     w=l1
     s1=input("please enter your name player: ")
     while s1=="":#To check whether input is enter or not
         print("SORRY WE CANNOT RESPOND TO WHAT YOU ENTERED,PLEASE RE-ENTER IN THE GIVEN FORMAT SPECIFIED ABOVE.")
         s1=input("please enter your name player: ")
     n1=input("Enter the level easy,medium,hard as e for easy, m for medium and h for hard: ").lower()     
     while n1 not in p:   #check if user input for level is valid 
         print(" PLEASE ENTER THE LEVEL IN THE GIVEN FORMAT ONLY")
         n1=input("Enter the level easy,medium,hard as e for easy, m for medium and h for hard: ").lower()         
     z=input("If you want to quit press q else enter n: ").lower()#Quit if user decides to quit
     if z=="q":
               quit()    
     while z not in u:                    
          z=input("If you want to quit press q else enter n: ").lower()#Quit if user decides to quit
          if z=="q":
               quit()              
     if n1=="e":  #If level selected is easy
        b=random.choice(l)   #b gets one random value from l 
        while x not in w:         
             w=method(w,b,s1)    #Invoke method function to play the game
        for i in range(0,len(w)):
             if w[i]==x:
                  if i==0:   #Deciding the winner 
                       print("Computer is the winner")
                  else:
                       print(s1,"is the winner")     
     if n1=="m":    #If user input for level is medium
        b=random.sample(l,2)    #b is assigned 2 random values from l
        while x not in w:
            c=random.choice(b)         
            w=method(w,c,s1)
        for i in range(0,len(w)):
             if w[i]==x:    #Declaring the winner
                  if i==0:
                       print("Computer is the winner")
                  else:
                       print(s1,"is the winner")     
     if n1=="h":
        while x not in w:
             b=random.choice(l)         
             w=method(w,b,s1)          
        for i in range(0,len(w)):
             if w[i]==x:
                  if i==0:   #Declaring the winner
                       print("Computer is the winner")
                  else:
                       print(s1,"is the winner")        
def double(y):
    z=""
    l1=[0,0]
    w=l1
    s1=input("Please enter your name player1: ")
    while s1=="":#To check whether input is enter or not
         print("SORRY WE CANNOT RESPOND TO WHAT YOU ENTERED,PLEASE RE-ENTER IN THE GIVEN FORMAT SPECIFIED ABOVE.")
         s1=input("please enter your name player1: ")
    s2=input("Please enter your name player2: ")
    while s2=="":#To check whether input is enter or not
         print("SORRY WE CANNOT RESPOND TO WHAT YOU ENTERED,PLEASE RE-ENTER IN THE GIVEN FORMAT SPECIFIED ABOVE.")
         s2=input("please enter your name player2: ")
    z=input("If you want to quit press q else enter n: ").lower()#Quit if user decides to quit    
    if z=="q":
        quit()  
    while z not in u:
        z=input("If you want to quit press q else enter n: ").lower() #Option to restart or quit        
        if z=="q":
            quit()         
    while y not in w:
        w=method1(w,s1,s2)    
    for i in range(0,len(w)):
             if w[i]==y:
                  if i==0:    #Declaring the winner
                       print(s1," is the winner")
                  else:
                       print(s2,"is the winner")   
def restart(f):    
    if f in w:
        if f=="y":
            main()
        if f=="n":
            print("Thanks")
        if f=="q":
             quit()
    else:
        print("SORRY WE CANNOT RESPOND TO WHAT YOU ENTERED,PLEASE RE-ENTER IN THE GIVEN FORMAT SPECIFIED ABOVE.")
        k=input("Enter y for yes if you want to restart or else enter n for no and q to quit ").lower()        
        restart(k)
def player(s,n):
     if s in q:
        if s=="1":
             single(n)    #Invoke single  function if user decides to play in single mode
        if s=="2":
             double(n)     #Invoke double function if user decides to play in double mode
     else:
         print("SORRY WE CANNOT RESPOND TO WHAT YOU ENTERED,PLEASE RE-ENTER IN THE GIVEN FORMAT SPECIFIED ABOVE.")
         g=input("Enter you want to play single player or double player, input single or double accordingly as 1 for single and 2 for double: ").lower()
         player(g,n)
def main():
    graph()    #Invoking graph function to print the name of the game
    n=input("Enter the maximum number of points: ")
    while n=="":#To check whether input is enter or not
         print("SORRY WE CANNOT RESPOND TO WHAT YOU ENTERED,PLEASE RE-ENTER IN THE GIVEN FORMAT SPECIFIED ABOVE.")
         n=input("Enter the maximum number of points: ")     
    y=num(n)   
    while y==0:#To check whether input is a numeric value only
        print("SORRY WE CANNOT RESPOND TO WHAT YOU ENTERED,PLEASE RE-ENTER IN THE GIVEN FORMAT SPECIFIED ABOVE.")
        n=input("Enter the maximum number of points: ")
        y=num(n)
    if y==1:
         n=int(n)
    while n<0:   # Checking if maximum number of points is positive
         print("SORRY WE CANNOT RESPOND TO WHAT YOU ENTERED,PLEASE RE-ENTER IN THE GIVEN FORMAT SPECIFIED ABOVE.")
         n=input("Enter the maximum number of points: ")
    s=input("Enter you want to play single player or double player, input single or double accordingly as 1 for single and 2 for double and q for quit: ").lower()    
    if s=="q":
         quit()    #Exit program if user desires to quit
    player(s,n)    
    f = input("Please enter y for yes if you want to replay else n for no if you don't and q to quit: ").lower()
    if f=="q":
         quit()
    restart(f)   #Invoking restart function to restart the game or to quit 
main()   #Program execution starts here
time.sleep(60)
