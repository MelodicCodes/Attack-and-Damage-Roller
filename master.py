#*******************************START OF NEW SCRIPT*****************************
import random
atkrolls=[]

#-------------------------------------------------------------------------------
#--ATTACK ROLL SECTION--
#-------------------------------------------------------------------------------
def SingleRoll(mod):
    crit = 0
    roll = int(random.randint(1,20))
    if roll==20:
        crit = 1
    if crit==0:
        return str(roll+int(mod))
    else:
        return '--'+str(roll+int(mod))+'--'

def RollAttacks(atkmod,fullatk,flurryofblows,frenzy,rage):
    atkrolls=[]
    sub=0
    if fullatk==0 and flurryofblows==0 and frenzy==0 and rage==0:
        list.append(atkrolls,SingleRoll(atkmod-sub))
    elif fullatk==1:
        if rage==1: #If raging
            sub = sub - 3 #Add 3 to the attack modifier(+6 str)
        if flurryofblows==1: #If using flurry of blows
            sub = sub + 2 #minus 2 to the attack modifier
            list.append(atkrolls,SingleRoll(atkmod-sub)) #Extra attack from Flurry of Blows
        if frenzy==1: #If frenzying
            sub = sub - 5 #Add 5 to the attack modifier(+5 str)
            list.append(atkrolls,SingleRoll(atkmod-sub)) #Extra attack from Frenzy

        for i in range(5): #25 bab
            for i in range(4): #attack 4 times with each limb
                list.append(atkrolls,SingleRoll(atkmod-sub)) #Attack
            sub=sub+5 #Increase the subtraction to the attack roll
    list.sort(atkrolls)
    list.reverse(atkrolls)
    print (atkrolls)

#-------------------------------------------------------------------------------
#--DAMAGE ROLL SECTION--
#-------------------------------------------------------------------------------
def DamageCalc(numdice,dicenum,strmod,numhits,numcrits):
    totaldmg=0
    subtotaldmg=0
    for i in range(numcrits):
        numhits = numhits - 1
        subtotaldmg=strmod
        for i in range(numdice):
            subtotaldmg=subtotaldmg+random.randint(1,dicenum) #Roll the damage die
        subtotaldmg = subtotaldmg * 2
        totaldmg = totaldmg + subtotaldmg
    for i in range(numhits):
        subtotaldmg=strmod
        for i in range(numdice):
            subtotaldmg=subtotaldmg+random.randint(1,dicenum) #Roll the damage die
        totaldmg = totaldmg + subtotaldmg
    print ("Damage = "+str(totaldmg))
#-------------------------------------------------------------------------------
#--USAGE--
#-------------------------------------------------------------------------------
#RollAttacks(Attack modifier,Full Attack?,Flurry of Blows?,Frenzy?,Rage?)
#DamageCalc(Number of damage dice rolled, Number on the dice(d6, d20 etc),Strength Modifier,how many hits?,how many crits?)

RollAttacks(43,1,0,0,0)
#DamageCalc(6,6,18,20,0)