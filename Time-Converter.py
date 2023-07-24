def timeconversion(time):

 zone=time[-2]
 hours=time[:2]

 if zone == "P":
     if int(hours) < 12:
        new_hours=12+int(hours)
        new_time=time.replace(hours,str(new_hours))
        new_time=new_time.replace("PM","")
        return str(new_time)
        #print(isinstance(new_time,str))

 if zone == "A":
     hours=time[:2]
     if int(hours) == 12:
       # new_hours=12-int(hours)
        new_time=time.replace(hours,"00")
        new_time=new_time.replace('AM','')
        return str(new_time)
        #print(isinstance(new_time,str))
     else:
        time=time.replace('AM','')
        return time
        

s="12:52:06Am"
result=timeconversion(s)
print(result + '\n')

