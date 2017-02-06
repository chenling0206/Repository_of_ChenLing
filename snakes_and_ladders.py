# -*- coding: utf-8 -*-
"""
I want to program an old game, snakes and ladders, which is a game we all love to play when we were children.
But I am a rookie of python, so I can't finish this script any more, and I think the changes of this game are so much
that I can't finish it! 
Can you help me? Thank you very much!
"""

import random
from sys import exit

def start():
    print "Please hit the Space and Enter bar to start the game!" 
    space1 = raw_input("> ")

    if space1 == " ":
        space2()
    else:
        exit(0)

random1 = random.randint(1,6)

def space2():
    print "Please hit the Space and the Enter to generate numbers randomly." 
    space2 = raw_input("> ") 
    
    if space2 == " ":
        print random1
        step1()
    else:
        exit(0)

def step1():
    print "What number you've got, how much steps you go forward."
    print "Please hit the number you've got and hit the Enter."
    number1 = raw_input("> ")

    if number1 == str(random1):
        step1_1()
    else:
        exit(0)

def step1_1():
    print "If number1 equal to 4, you can go up to the 14 step through the ladder1."
    print "If number1 is not the 4, you just go to the number1 steps."

    if random1 == 4:
        ladder1 = random1 + 10
        print ladder1
        space3()
    else:
        print random1
        random1_steps()

random2 = random.randint(1,6)

def space3():
    print "Please hit the Space and the Enter to generate numbers randomly."
    space3 = raw_input("> ") 
    
    if space3 == " ":
        print random2
        step2()
    else:
        exit(0)

def random1_steps():
    print "Please hit the Space and the Enter to generate numbers randomly."
    space3 = raw_input("> ") 
    
    if space3 == " ":
        print random2
        step2()
    else:
        exit(0)

def step2():
    print "What number you've got, how much steps you go forward."
    print "Please hit the number you've got and hit the Enter."
    number2 = raw_input("> ")

    if number2 == str(random2):
        step3()
    else:
        exit(0)

def step3():
    print "If you are in 14 step, and number2 equal to 6, you can go up to the 42 step through the ladder2."
    print "If number1 add number2 equal to 4, you can go up to the 14 step through the ladder1."
    print "if number1 not equal to 4, you just go up to 'number1+number2' steps."
    if random1 == 4:
        step3_1()
    else:
        step3_2()

def step3_1():
    if random2 == 6:
        print 42
        space4()
    else:
        print 14+random2
        space4()

def step3_2():
    if random1+random2 == 4:
        print 14
        space4()
    else:
        print random1+random2
        space4()

random3 = random.randint(1,6)

def space4():
    print "Please hit the Space and the Enter to generate numbers randomly."
    space4 = raw_input("> ") 
    
    if space4 == " ":
        print random3
        step4()
    else:
        exit(0)
        
def step4():
    print "What number you've got, how much steps you go forward!"
    print "Please hit the number you've got and hit the Enter."
    number3 = raw_input("> ")

    if number3 == str(random3):
        step4_1()
    else:
        exit(0)

def step4_1():
    print "If you are in 42 step, you just go forward number3 steps more."
    print "If you are in 14 step, and number3 equal to 6, you can go up to the 42 step through the ladder2"
    print "If numbers1 add numbers2 add numbers3 equal to 4, you can go up to the 14 step through the ladder1."
    print "or, you just go up number3 steps more." 

    if random1 == 4:
        step4_1()
    else:
        step4_2()

def step4_1():
    if random2 == 6:
        step4_1_1()
    else:
        step4_1_2()

def step4_1_1():
    print 42+random3
    win1() 

def win1():
    if 42 + random3 == 48:
        print "Congratulations! you complete the game, and you win $100!"
    else:
        space5()

def step4_1_2():
    print 14+random3
    space5()

def step4_2():
    if random1+random2 == 4:
        step4_2_1()
    else:
        step4_2_2()

def step4_2_1():
    if random3 == 6:
        print 42
        space5()
    else:
        print 14+random3

def step4_2_2():
    print random1+random2+random3
    space5()

random4 = random.randint(1,6)

def space5():
    print "Just do follow the hints, or keep hitting the Space and Enter bar"
    space5 = raw_input("> ") 
    
    if space5 == " ":
        print random4
        step5()
    else:
        exit(0)
        
def step5():
    print "Please hit the number you've got and hit the Enter."
    number4 = raw_input("> ")

    if number4 == str(random4):
        step5_1()
    else:
        exit(0)

def step5_1():
    print "If you are between 42 step and 48 step, you just go forward followed the hints."
    print "If you are in 42 step, you just go forward number4 steps more."
    print "If you are in 14 step, and number4 equal to 6, you can go up to the 42 step through the ladder2"
    print "If you are between 14 and 20, and numbers1 add numbers2 add numbers3 add number4 equal to 20, you can go up to the 42 step through the ladder2."
    print "If you are between 4 and 14,  you just go forward number4 steps more."
    print "If numbers1 add numbers2 add numbers3 add number4 equal to 4, you can go up to the 14 step through the ladder1."
    print "or, you just go up number4 steps more." 

    if random1 ==4 and random2==6 and random3 + random4 ==6:
        win2()
    elif random1 ==4 and random2==6 and random3 + random4 !=6:
        print 42+random3 + random4
        space6()
    else:
        step5_1_0()

def step5_1_0():
    if random1 ==4 and random2+random3==6 and random4 ==6:
        win2()
    elif random1 ==4 and random2+random3==6 and random4 !=6:
        print 42+random4
        space6()
    else:
        step5_1_00()

def step5_1_00():
    if random1==4 and random2+random3+random4==6:
        print 42
        space6()
    else:
        step5_1_1()

def step5_1_1():
    if random1 +random2+random3 ==3:
       step5_1_1()
    else:
       step5_1_2()

def step5_1_1():
    if random1 +random2+random3+random4==4:
        print 14
        space6()
    else:
        print 3+random4
        space6()

def step5_1_2():
    if random1+random2+random3 ==4 and random4==6:
        print 42
        space6()
    elif random1+random2+random3 ==4 and random4 != 6:
        print 14+random4
        space6()
    else:
        step5_1_3()

def step5_1_3():
    if random1+random2==4 and random3==6:
        print 42+random4
        space6()
    elif random1+random2==4 and random3+random4==6:
        print 42
        space5()
    else:
        step5_1_4()

def step5_1_4():
    if random1 +random2+random3==14 and random4==6:
        print 42
        space6()
    elif random1+random2+random3 ==14 and random4 != 6:
        print 14+random4
        space6()
    else:
        step5_1_5()

def step5_1_5():
    if random1 +random2+random3+random4==20:
        print 42
        space6()
    else:
        print random1 +random2+random3+random4
        space6()

def space6():
    print "Game over!"
    exit(0)



start()
