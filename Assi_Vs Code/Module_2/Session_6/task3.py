team=['rcb','csk','kkr','rrr']
points=[10,20,30,40]

dict=dict(zip(team,points))

for key,value in dict.items():
    if value>10:
        print(key,":",value)