from functionsandclasses import*


set1 = [9.24,9.21,9.22,10.84,11.54]
set = [21,4]
set3 = [41,22]
set2 = [1241,21212]

#print('normal average:',av(set1))
#print('truncated average:',truncateave(set1))

##ans = av(set1)
#ans1 = truncateave(set1)
#print(ans)
#print(ans1)


##print('Totals are',av(set1),',',truncateave(set1),',','and',creation(set))

Gael = Mage('BattleMage','Abyssal','Destruction')
Alaster = Enemy('Sorcerer','Fire','Destruction')

Gael.magictraining()
Gael.rest()
Gael.magictraining()
Gael.rest()
Gael.physicaltraining()
Gael.magictraining()
print(Gael)


