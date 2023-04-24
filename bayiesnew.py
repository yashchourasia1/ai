probability ={
    "Burglary_True":0.002,
    "Burglary_False":0.998,
    "Earthquake_True":0.001,
    "Earthquake_False":0.999,
    "AlarmBurglaryEarthquake_True":0.94,
    "AlarmBurglaryEarthquake_False":0.06,
    "AlarmBurglary_True":0.95,
    "AlarmBurglary_False":0.05,
    "AlarmEarthquake_True":0.31,
    "AlarmEarthquake_False":0.69,
    "Alarm_True":0.001,
    "Alarm_False":0.999,
    "JohnAlarm_True":0.91,
    "JohnAlarm_False":0.09,
    "John_True":0.05,
    "John_False":0.95,
    "MarryAlarm_True":0.75,
    "MarryAlarm_False":0.25,
    "Marry_True":0.02,
    "Marry_False":0.98
    }

def E_prob(E):
    if(E==1):
        return probability["Earthquake_True"]
    else :
        return probability["Earthquake_False"]

def B_prob(B):
    if(B==1):
        return probability["Burglary_True"]
    else :
        return probability["Burglary_False"]

def D_prob(D,A):
    if(A==1 and D==1):
        return probability["JohnAlarm_True"]
    elif(A==1 and D==0):
        return probability["JohnAlarm_False"]
    elif(A==0 and D==1):
        return probability["John_True"]
    else:
        return probability["John_False"]


def S_prob(S,A):
    if(A==1 and S==1):
        return probability["MarryAlarm_True"]
    elif(A==1 and S==0):
        return probability["MarryAlarm_False"]
    elif(A==0 and S==1):
        return probability["Marry_True"]
    else:
        return probability["Marry_False"]

def A_prob(E,B,A):
    if(E==1 and B==1 and A==1):
        return probability["AlarmBurglaryEarthquake_True"]
    elif(E==1 and B==1 and A==0):
        return probability["AlarmBurglaryEarthquake_False"]
    elif(E==1 and B==0 and A==1):
        return probability["AlarmEarthquake_True"]
    elif(E==1 and B==0 and A==0):
        return probability["AlarmEarthquake_False"]
    elif(E==0 and B==1 and A==1):
        return probability["AlarmBurglary_True"]
    elif(E==0 and B==1 and A==0):
        return probability["AlarmBurglary_False"]
    elif(E==0 and B==0 and A==1):
        return probability["Alarm_True"]
    else:
        return probability["Alarm_False"]

burglary = (int(input("Burglary Happened ? (1=True,0=False) : ")))
check = 0
while check != 1:
    if burglary == 1 :
        check = 1
    elif burglary == 0:
        check = 1
    else:
        burglary = (int(input("Wrong input, Burglary Happened ?(1=True,0=False) : ")))

earthquake = (int(input("Earthquake Happened ? (1=True,0=False) : ")))
check = 0
while check != 1:
    if earthquake == 1 :
        check = 1
    elif earthquake == 0:
        check = 1
    else:
        earthquake = (int(input("Wrong input, Earthquake Happened ? (1=True,0=False) : ")))

alarm = (int(input("Alarm Rang ? (1=True,0=False) : ")))
check = 0
while check != 1:
    if alarm == 1 :
        check = 1
    elif alarm == 0:
        check = 1
    else:
        alarm = (int(input("Wrong input, Alarm Rang ? (1=True,0=False) : ")))

Johncall = (int(input("John Called ? (1=True,0=False) : ")))
check = 0
while check != 1:
    if Johncall == 1 :
        check = 1
    elif Johncall == 0:
        check = 1
    else:
        Johncall = (int(input("Wrong input, John Called ? (1=True,0=False) : ")))

Marrycall = (int(input("Marry Called ? (1=True,0=False) : ")))
check = 0
while check != 1:
    if Marrycall == 1 :
        check = 1
    elif Marrycall == 0:
        check = 1
    else:
        Marrycall = (int(input("Wrong input, Marry Called ? (1=True,0=False) : ")))

PE=E_prob(earthquake)
PB=B_prob(burglary)
PA=A_prob(earthquake,burglary,alarm)
PD=D_prob(Johncall,alarm)
PS=S_prob(Marrycall,alarm)
P=(PE*PA*PB*PD*PS) 
print("Probability is {:.10f}".format(P))
