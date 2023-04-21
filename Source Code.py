
print('Welcome To BRAIN GAMES:')
print()
print()
print()
print()
import mysql.connector as sql
my=sql.connect(host='localhost',user='root',passwd='scott',database='project')
print('1. New User')
print('2. Existing User')
yn=int(input('Enter Your choice (1/2)'))
cursor=my.cursor()
con=0
if yn==1:
    print('PLAYER ID CREATION')
    name=input('Enter Your Name')
    password=input('Enter your password.. keep it 8 character long')
    cursor.execute("insert into user(username,password) values('{}','{}')".format(name,password))
    print('You are logged in.User ID created.')
    my.commit()
    con=1
if yn==2:
    print('Login here')
    name=input('Enter Your Name')
    cursor.execute("Select * from user where username='{}'".format(name))
    data=cursor.fetchall()
    pd=data[0][1]
    password=input('Enter your password')
    if password==pd:
        con=1
        print('You are logged in.')
    else:
        con=0
        print('Wrong password. You are not the authorised player.Not allowed to play.')
if con==1:
    print()
    print()        
    print()
    while True:
        print(' Available Options : - 1. Information ')
        print('                       2. Games')
        print('                       3. Exit')
        kl=int(input('Enter Your Choice(1/2/3)'))
        if kl==1:
            while True:
                    print('Available Informations:- 1. ABOUT US')
                    print('                         2. USER MANUAL')
                    print('                         3. RULES FOR SYNANTO')
                    print('                         4. RULES FOR MASTERMIND')
                    print('                         5. RULES FOR SHORTFORMS')
                    print('                         6. Exit from information')
                    kl1=int(input('Enter Your Choice :'))
                    if kl1==1:
                        myfile=open('about us.txt')
                        content=myfile.read()
                        print(content)
                        myfile.close()
                    elif kl1==2:
                        myfile=open('usermanual.txt')
                        content=myfile.read()
                        print(content)
                        myfile.close()
                    elif kl1==3:
                        myfile=open('SYNANTO.txt')
                        content=myfile.read()
                        print(content)
                        myfile.close()
                    elif kl1==4:
                        myfile=open('rulesmastermind.txt')
                        content=myfile.read()
                        print(content)
                        myfile.close() 
                    elif kl1==5:
                        myfile=open('ABBREVATION.txt')
                        content=myfile.read()
                        print(content)
                        myfile.close()
                    elif kl1==6:
                        break
        if kl==2:
            while True:
                print('Available Games:- 1. SYNANTO')
                print('                  2. MASTERMIND')
                print('                  3. ABBREVATIONS')
                print('                  4. Exit')
                kl2=int(input('Enter Your Choice :'))
                if kl2==1:
                    def hint(word):
                        print('Hint for the word, Word looks like ',end='')
                        lenword=len(word)
                        for m in range(0,lenword):
                            if m%2==0:
                                print(word[m],end='')
                            else:
                                print('_',end='')
                    def synonym():
                        for x in synread:
                            num=str(number)
                            if x[0]==num:
                                print('Write synonyms of this word:  ',end='')
                                print(x[1])
                                hint(x[2])
                                print()
                                syn1=input(('Your answer: '))
                
                                if syn1.capitalize()==x[2]:
                                    global count
                                    count+=1
                                    print('Good! Your answer is right')
                                else:
                                    print('Nope! Your answer is wrong')
                                    print('The correct answer is ', x[2])
                                print()
                                print('Next question')
                                global n
                                n+=20
                        filesyn.seek(0,0)
                    def antonym():
                        for x in antoread:
                            num=str(number)
                            if x[0]==num:
                                print('Write antonym of this word:  ',end='')
                                print(x[1])
                                hint(x[2])
                                print()
                                syn1=input(('Your answer: '))
                                
                                if syn1.capitalize()==x[2]:
                                    global count
                                    count+=1
                                    print('Good! Your answer is right')
                                else:
                                    print('Nope! Your answer is wrong')
                                    print('The correct answer is ', x[2])
                                print()
                                if number<=80:
                                    print('Next question')
                                global n
                                n+=20
                        fileanto.seek(0,0)
                    import csv
                    import random
                    filesyn=open(r'C:\Users\DELL\Desktop\EL Project\Synonyms.csv','r')
                    fileanto=open(r'C:\Users\DELL\Desktop\EL Project\Antonyms.csv','r')
                    synread=csv.reader(filesyn)
                    antoread=csv.reader(fileanto)
                    n=1
                    count=0
                    while n<=100:
                        number=(random.randint(n,n+19))
                        if number<=40 and number>20:
                            antonym()
                        elif number<=20:
                            synonym()
                        elif number<=60 and number>40:
                            antonym()
                        elif number<=80 and number>60:
                            synonym()
                        elif number>80:
                            antonym()
                    print()
                    print()
                    print()
                    print('YOUR POINTS')
                    print(count,'/5')
                    print()
                    print()
                    
            
            
                if kl2==2:
                    import random
                    print('Game Name :- Mastermind')
                    print('Rules of Game are as follows:')
                    print('1. You have to Guess the 4-digit number in at max 12 chances')
                    print('2. The system will give the hint by giving the count of :')
                    print('     i) Exist:- Correct Number at incorrect position')
                    print('     ii) Position:- Correct Number at correct positon')
                    print('NOTE:- If you enter a number multiple times it will be count as different number everytime')
                    x=random.randint(1000,9999)
                    uo=x
                    l=[]        
                    w=0
                    for z in range(4):
                        l.append(x%10)
                        x=x//10
                    for zz in range(1,13):
                        if zz==7:
                            print('One hint can be provided')
                            yan=input('Press Y for YES or any other key for NO')
                            if yan=='y' or yan=='Y':
                                print('First Or Last number can be known,Which Number You want to know')
                                q=int(input('Press (1) for first and (4) for last'))
                                if q==1:
                                    print('First Number is :',uo//1000)
                                elif q==4:
                                    print('Last number is :',uo%10)
                        p=0
                        e=0
                        y=uo
                        n=input('Enter A four digit Number')    
                        if n.isdigit():
                            nn=int(n)
                            nnn=int(n)  
                            if nn>999 and nn<10000:
                                if nn==uo:
                                    print('You gussed correct')
                                    print('Congratulations you have won the game')
                                    print('You Took',zz,'guess')
                                    w=1
                                    break
                                else:
                                    a=0
                                    for qwew in range(4):
                                        if y%10==nnn%10:
                                            e=e+1
                                        y=y//10
                                        nnn=nnn//10
                                    for xyz in range(4):
                                        if nn%10 in l:
                                            p+=1
                                        nn=nn//10
                                print('Exist:',p,'Position:',e)
                            else:
                                print('Invalid Input: Value out of range 1000-9999')
                        elif n.isalpha():
                            print('Invalid Input: String value not allowed')
                        elif n.isalnum():
                            print('Invalid Input: Enter only Intergral Value')
                        else:
                            print('Invalid Input: Special Character or Symbols Not allowed')
                    if w!=1:
                        print('END OF GAME!!!')
                        print('You have ran out of turns')
                        print('Correct guess is',uo)

            
                if kl2==3:
                    import mysql.connector as myconn
                    import random
                    score=0
                    def question(n):
                        if n==1:
                            num=random.randint(1,7)
                        if n==2:
                            num=random.randint(8,14)
                        if n==3:
                            num=random.randint(15,21)
                        conn=myconn.connect(host='localhost',user='root',password='scott',database='project')
                        sor=conn.cursor()
                        sor.execute('select * from abbreviation where sno={}'.format(num))
                        data=sor.fetchone()
                        print('WRITE THE FULL FORM OF :  ',data[1])
                        print()
                        print('NOTE: KEEP SINGLE SPACE BETWEEN THE WORDS IN ANSWER')
                        fullform=input('YOUR ANSWER:')
                        X=data[2]
                        if fullform.lower()==X:
                            print('your answer is right')
                            global score
                            score=score+1
                        else:
                            print('WRONG ANSWER')
                            print('CORRECT ANSWER WILL BE:',X)
                    print('QUESTION 1')
                    print()
                    question(1)
                    print()
                    print()
                    print('QUESTION 2')
                    print()
                    print()
                    question(2)
                    print()
                    print()
                    print('QUESTION 3')
                    question(3)
                    print()
                    print()
                    print('You got ',score,' right answers')
                    print('So your score is',score,'/3')
                if kl2==4:
                    break
        if kl==3:
            print('Thank You!!')
            break

