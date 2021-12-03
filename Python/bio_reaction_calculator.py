yeast=1
glucoses=100
ethanol=0
hour=0

#First hour
hour= hour+1
glucoses=glucoses-yeast
ethanol=ethanol+(ethanol+1)
yeast=yeast+yeast
print("Hour",hour,":",glucoses,"moles of glucoses",yeast,"moles of yeast",ethanol,"moles of ethanol")
print("total biomass:",glucoses+yeast+ethanol,"mole")

#second hour starting
hour+=1
while(ethanol >0): 
    if(glucoses-yeast<0 and glucoses !=0):
        yeast=yeast+glucoses
        ethanol=ethanol+glucoses
        glucoses= glucoses - glucoses
    elif(glucoses==0):
        yeast=yeast+(ethanol/2)
        ethanol = ethanol- ethanol
    else: 
        glucoses=glucoses- yeast
        ethanol=ethanol+(ethanol+1)
        yeast=yeast+yeast
    print("Hour",hour,":",glucoses,"moles of glucoses",yeast,"moles of yeast",ethanol,"moles of ethanol")
    print("total biomass:",glucoses+yeast+ethanol,"mole")
    hour+=1

print("There is no carbon source left in the task")    
