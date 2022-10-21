# Tomas Gael Estrera IV
# Made for fun as i was bored during quarantine
# the more grandmages you defeat, more bosses to appear
# the more grandmages you defeat, you can upgrade skills and grandmages upgrade damage
from tkinter import*
from tkinter.scrolledtext import*
from PIL import Image, ImageTk
import random
import time
#sign of commit!

#strings
fireball = 'Fireball'
lightning = 'Lightning Strike'
water = 'Water Surge'
strike = 'Abyssal Strike'
lifesteal = 'Abyssal Lifesteal'
blast = 'Abyssal Blast'

garden = 'a = Garden of Mystrus'
castle = 'b = Castle of Garmadan'
mansion = 'c = Mansion of Decoretum'

words = 'a = Expository speeches'
words1 = 'b = Dream Scaping'

f = 'Fireball = -4 Energy, 6 HP damage'
l = 'Water Surge = -5 Energy, 8 HP damage'
w = 'Lightning Strike = -10 Energy, 10 HP damage, 7 Energy damage'
s = 'Abyssal Lifesteal = -6 Energy, 4 HP damage, +10 HP'
p = 'Abyssal Strike = +8 Energy, 4 HP damage'
a = 'Abyssal Blast = -3 Energy, 3 HP damage, +1 Abyssal Charge'
u = 'Ultimatum = 10 Energy, 20 MP HP damage, 8 Charge cost'

b1 = 'Chaos Meteors'
b2 = 'Chaos Fire'
b3 = 'Cyclones of Destruction'
b4 = 'Arcane Lifesteal'
b5 = 'Arcane Strike'


completechoices = f+'\n'+'\n'+l+'\n'+'\n'+w+'\n'+'\n'+s+'\n'+'\n'+p+'\n'+'\n'+a+'\n'+'\n'+u
energychoices = words+'\n'+words1
listchoices = f+'\n'+l+'\n'+w
spellchoices = fireball+'\n'+lightning+'\n'+water+'\n'+strike+'\n'+lifesteal
spellchoices1 = fireball+'\n'+lightning+'\n'+water+'\n'+blast
harvestchoices = garden +'\n'+castle+'\n'+mansion
bossmoves = b1 + '\n' + b2 + '\n' + b3 + '\n' + b4 + '\n' + b5

class Decoretum():
    def __init__(self):
        self.energy = 20
        self.essence = 0
        self.answer = 0
        self.counter = 0
        self.mages = 0
        self.grandmages = 0 #counter for bosses, should update
        self.ultimate = 0
        self.life = 100
        self.bosslife = 100
        self.bossenergy = 20
        self.bossalive = ''
        self.bossname = ''
        self.condition = ''
        self.alive = ''
        self.turn = ''
        self.mainanswer = ''
        self.status = ''
        self.answerlist=[]
        self.repeat = 0
        self.darkness = 0
        self.light = 0
        self.chaos = 0
        self.nature = 0
        self.elemental = 0
    
    
        
    def killstreak(self):
        abyssalentry.delete('1.0',END)
        abyssalentry.insert(INSERT,'Mages defeated: {mages}'.format(mages=self.mages))
        abyssalentry.insert(INSERT,'\n')
        abyssalentry.insert(INSERT,'Darkness Mage: {mages}'.format(mages=self.darkness))
        abyssalentry.insert(INSERT,'\n')
        abyssalentry.insert(INSERT,'Light Mage: {mages}'.format(mages=self.light))
        abyssalentry.insert(INSERT,'\n')
        abyssalentry.insert(INSERT,'Chaos Mage: {mages}'.format(mages=self.chaos))
        abyssalentry.insert(INSERT,'\n')
        abyssalentry.insert(INSERT,'Nature Mage: {mages}'.format(mages=self.nature))
        abyssalentry.insert(INSERT,'\n')
        abyssalentry.insert(INSERT,'Elemental Mage: {mages}'.format(mages=self.elemental))
        abyssalentry.insert(INSERT,'\n')
        abyssalentry.insert(INSERT,'\n')
        abyssalentry.insert(INSERT,'Grand Mages defeated: {grandmages}'.format(grandmages=self.grandmages))
    
# BOSS
    
    def bossstart(self):
        self.bossalive = ''
        self.bossenergy = 20
        bossname = random.randint(1,5)
        if bossname == 1:
            self.bossname = 'Darkness Grand Mage'
        elif bossname ==2:
            self.bossname = 'Light Grand Mage'
        elif bossname ==3:
            self.bossname = 'Chaos Grand Mage'
        elif bossname ==4:
            self.bossname = 'Nature Grand Mage'
        elif bossname ==5:
            self.bossname = 'Elemental Grand Mage'
        self.boss()
        
    
    def boss(self):
        self.condition = 'boss'
        if self.bosslife <= 0 and self.bossalive != 'dead' and self.condition == 'boss':
            self.bossdeath()
        else:
            self.turn = 'stuck'
            content.delete('1.0',END)
            content.insert(INSERT,'A {grandmage} has appeared in front of you!'.format(grandmage=self.bossname))
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}: We have finally met, Abyssal Mage. This will be worthy battle'.format(grandmage=self.bossname))
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}: I have travelled across Bladespire to find a worthy opponent'.format(grandmage=self.bossname))
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}: I seek to conquer the arcane arts, and I will eliminate every obstacle I encounter!'.format(grandmage=self.bossname))
            content.insert(INSERT,'\n')
            content.insert(INSERT,'Let the battle commence!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,bossmoves)    
            bossrandom = random.randint(1,5)       
            if self.bossenergy == 0:
                self.bossattack5()          
            elif bossrandom == 1:
                self.bossattack1()
            elif bossrandom == 2:
                self.bossattack2()
            elif bossrandom == 3:
                self.bossattack3()
            elif bossrandom == 4:
                self.bossattack4()
            elif bossrandom == 5:
                self.bossattack5()
                
        
        
    def defeat(self):
        self.turn=''
        self.alive='dead'
        self.energy = 0
        energynum.configure(text=''+str(self.energy))
        content.delete('1.0',END)
        content.insert(INSERT,'You have lost the battle and your life')
        content.insert(INSERT,'\n')
        content.insert(INSERT,'May you wander into the endless abyss')
        content.insert(INSERT,'\n')
        content.insert(INSERT,'\n')
        wisdom.delete('1.0',END)
        wisdom.insert(INSERT,'Abyssal Archmage, you have failed')
        wisdom.insert(INSERT,'\n')
        wisdom.insert(INSERT,'You must use your spells more wisely,')
        wisdom.insert(INSERT,'\n')
        wisdom.insert(INSERT,'for power without intellectual depth is meaningless')
        
    
    def bossdeath(self):
        self.bossalive = 'dead'
        self.energy += 20
        energynum.configure(text=''+str(self.energy))
        self.life = 100
        lifenum.configure(text=''+str(self.life))
        self.grandmages += 1
        self.condition = ''
        self.killstreak()
        self.turn = ''
        content.delete('1.0',END)
        content.insert(INSERT,'The {grandmage} has fallen'.format(grandmage=self.bossname))
        content.insert(INSERT,'\n')
        content.insert(INSERT,'You absorb 20 energy of the {grandmage}, and you feel empowered'.format(grandmage=self.bossname))
        content.insert(INSERT,'\n')
        content.insert(INSERT,'You strike fear into the hearts of your enemies')
        content.insert(INSERT,'\n')

        
        
        
        
    def bossattack1(self):
        Praxis = False
        if self.bossenergy < 4:
            self.boss()
        else:
            Praxis = True
        if Praxis == True and self.turn == 'stuck':
            self.bossenergy -= 4
            self.life -= 6
            lifenum.configure(text=''+ str(self.life))
            content.delete('12.0',END)
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}\'s HP:'.format(grandmage=self.bossname))
            content.insert(INSERT,self.bosslife)
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}\'s Energy:'.format(grandmage=self.bossname))
            content.insert(INSERT,self.bossenergy)
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The {grandmage} summons two chaos meteors and collided them to your body'.format(grandmage=self.bossname))
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You lose 6 HP')
            

            if self.life <= 0 and self.bossalive != 'dead' and self.bosslife > 0:
                self.life = 0
                lifenum.configure(text=''+ str(self.life))
                self.defeat()
                
        
    def bossattack2(self):
        Praxis = False
        if self.bossenergy < 5:
            self.boss()
        else:
            Praxis = True
        if Praxis == True and self.turn == 'stuck':
            self.bossenergy -= 5
            self.life -= 8
            lifenum.configure(text=''+ str(self.life))
            content.delete('12.0',END)
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}\'s HP:'.format(grandmage=self.bossname))
            content.insert(INSERT,self.bosslife)
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}\'s Energy:'.format(grandmage=self.bossname))
            content.insert(INSERT,self.bossenergy)

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The {grandmage} summons a volley of chaos fire!'.format(grandmage=self.bossname))
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You lose 8 HP')
            
            if self.life <= 0 and self.bossalive != 'dead' and self.bosslife > 0:
                self.life = 0
                lifenum.configure(text=''+ str(self.life))
                self.defeat()
        
    def bossattack3(self):
        Praxis = False
        if self.bossenergy < 10:
            self.boss()
        else:
            Praxis = True
        if Praxis == True and self.turn == 'stuck':
            self.bossenergy -= 10
            self.life -= 10
            lifenum.configure(text=''+ str(self.life))
            self.energy -= 7
            energynum.configure(text=''+str(self.energy))
            content.delete('12.0',END)
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}\'s HP:'.format(grandmage=self.bossname))
            content.insert(INSERT,self.bosslife)
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}\'s Energy:'.format(grandmage=self.bossname))
            content.insert(INSERT,self.bossenergy)

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The {grandmage} releases cyclones of destructive wind towards you!'.format(grandmage=self.bossname))
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The destructive cyclones drain your abyssal energy at the same time!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You lose 10 HP')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You lose 7 energy')
        
            if self.life <= 0 and self.bossalive != 'dead' and self.bosslife > 0:
                self.life = 0
                lifenum.configure(text=''+ str(self.life))
                self.defeat()

            elif self.energy < 0:
                self.energy = 0
                energynum.configure(text=''+str(self.energy))
            
            
        
    def bossattack4(self):
        Praxis = False
        if self.bossenergy < 6:
            self.boss()
        else:
            Praxis = True
        if Praxis == True and self.turn == 'stuck':
            self.life -= 4
            lifenum.configure(text=''+ str(self.life))
            self.bosslife += 10
            self.bossenergy -= 6
            content.delete('12.0',END)
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}\'s HP:'.format(grandmage=self.bossname))
            content.insert(INSERT,self.bosslife)
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}\'s Energy:'.format(grandmage=self.bossname))
            content.insert(INSERT,self.bossenergy)

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT, 'The {grandmage} strikes you with an arcane lifesteal spell!'.format(grandmage=self.bossname))
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You lose 4 HP')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The {grandmage} gains 10 HP'.format(grandmage=self.bossname))
        
            if self.life <= 0 and self.bossalive != 'dead' and self.bosslife > 0:
                self.life = 0
                lifenum.configure(text=''+ str(self.life))
                self.defeat()
    
    def bossattack5(self):
        if self.turn == 'stuck':
            if self.bossenergy <= 0:
                self.bossenergy = 0
            self.bossenergy += 8
            self.life-= 4
            lifenum.configure(text=''+ str(self.life))
            content.delete('12.0',END)
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}\'s HP:'.format(grandmage=self.bossname))
            content.insert(INSERT,self.bosslife)
            content.insert(INSERT,'\n')
            content.insert(INSERT,'{grandmage}\'s Energy:'.format(grandmage=self.bossname))
            content.insert(INSERT,self.bossenergy)

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT, 'The {grandmage} uses its raw arcane power to generate energy with its'.format(grandmage=self.bossname))
            content.insert(INSERT,'\n')
            content.insert(INSERT,'arcane strike!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You lose 4 HP')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The {grandmage} gains 8 energy'.format(grandmage=self.bossname))

            if self.life <= 0 and self.bossalive != 'dead' and self.bosslife > 0:
                self.life = 0
                lifenum.configure(text=''+ str(self.life))
                self.defeat()

        
        
    def battle(self):
        wisdom.delete('1.0',END)
        self.counter = 0     
        if self.turn == 'stuck':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You cannot escape from this battle, Abyssal')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'ArchMage!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You can only proceed with the button after you\'ve dealt with your enemy')
        else:
            say = random.randint(1,2)
            monsters = random.randint(1,5)      
            if self.turn == '' and self.condition != 'boss' and self.alive != 'dead': 
                if say == 1 and monsters == 1 and self.energy >= 3:
                    self.bossalive = ''
                    self.turn = 'stuck'
                    content.delete('1.0',END)
                    self.condition = 'darkness'
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'Shadows emerged from the ground, unable to be penetrated by light!')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'The shadows formed a figure of a battlemage surrounded with the aura of Darkness')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'The battlemage engaged in combat position, ready to deliver devastating arcane spells')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'Choose your spell, or perish by the power of Darkness!')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,spellchoices1)

                elif say == 1 and monsters == 2 and self.energy >= 3:
                    self.bossalive = ''
                    self.turn = 'stuck'
                    content.delete('1.0',END)
                    self.condition = 'light'
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'A ray of light from the sky of Bladespire struck the ground with ferocity')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'From the light emerged a battlemage reciting chants of a language you do not understand')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'The battlemage of Light speaks to you, but its language is foreign to you')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'The battlemage\'s tone becomes aggressive, and it conjures spheres of light magic!')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'The time is now! Choose your spell to defeat this mage!')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,spellchoices1)

                elif say == 1 and monsters == 3 and self.energy >= 3:
                    self.bossalive = ''
                    self.turn = 'stuck'
                    content.delete('1.0',END)
                    self.condition = 'chaos'
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'You hear screams of agony and suffering from a distance')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'In front of you, the enemies you\'ve slain in the past has appeared')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'Amidst the figures of your past enemies, you see a battlemage cloaked with what seems to be blur')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'The Chaos battlemage attempts to destroy your thoughts, memories, and experiences with its spells,')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'However, you destroy all of the battlemage\'s illusions using your Abyssal magic')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'Now is the time to retaliate!')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,spellchoices1)

                elif say == 1 and monsters == 4 and self.energy >= 3:
                    self.bossalive = ''
                    self.turn = 'stuck'
                    content.delete('1.0',END)
                    self.condition = 'elemental'
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'From the distance, you see a cyclone of destructive wind heading your direction')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'On your left, you see a blaze of fiery flames burn the ground')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'On your right, you see a gigantic tidal wave raised, and it ceases to fall on the ground')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'On top of the tidal wave, a battlemage is hovering with both of its hands raised')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'The battlemage controls three of the destructive magical spells in unison')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'The battlemage intends to destroy you with its elemental mastery')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'Now is the time to retaliate!')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,spellchoices1)

                elif say == 1 and monsters == 5 and self.energy >= 3:
                    self.bossalive = ''
                    self.turn = 'stuck'
                    content.delete('1.0',END)
                    self.condition = 'nature'
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'As you are walking, you notice that the ground below you is shaking')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'A large sprout of vines emerges in front of you')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'Several large sprout of vines emerges from all directions within your vicinity')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'Trees and flowers emerge, making the vicinity a forest')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'A battlemage appears on top of a tree, mocking you for falling into its domain')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'The battlemage has you in its domain of expertise, and it intends to eradicate you')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,spellchoices1)
                
                elif self.energy <= 2 and self.condition != 'boss':
                    self.bosslife = 100
                    self.bossstart()

                elif say == 2:
                    self.bosslife = 100
                    self.bossstart()  
                
            if self.alive == 'dead' and self.bossalive != 'dead' and self.repeat < 1:
                    self.repeat += 1
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'\n')
                    content.delete('4.0',END)
                    content.insert(INSERT,'You are already dead, how can you battle further?')
                    content.insert(INSERT,'\n')
                    content.insert(INSERT,'Restart the code and play again. Choose your spells more wisely')

            elif self.repeat >= 1 and self.alive == 'dead' and self.bossalive != 'dead':
                    content.insert(INSERT,'')
            
                
    
    def insight(self):
        getting = abyssalentry.get('1.0',END)
        if getting == '':
            abyssalentry.insert(INSERT,'You cannot input blank')
            
        else:
            self.energy += 1
            energynum.configure(text=''+ str(self.energy))
            
    def abyssalblast(self):
        praxis = False
        if self.energy < 3:
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You do not have enough energy for this spell')
        else:
            praxis = True
            
        if self.condition == 'darkness' and praxis == True and self.counter < 1:
            self.energy -= 3
            energynum.configure(text=''+str(self.energy))
            self.energy += 1
            energynum.configure(text=''+str(self.energy))
            self.bosslife -= 3
            self.ultimate += 1
            chargesnum.configure(text=''+str(self.ultimate))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You unleash a blast made of pure Abyssal energy!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You empower yourself by gaining an Abyssal charge')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 1 Abyssal charge')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 1 energy')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You decimate the Darkness mage with the power of the abyss!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'However, the magnitude of your spell is not enough to absorb')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'most of the Darkness mage\'s energy')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You absorb 1 energy from the Darkness Mage')
            self.counter += 1
            self.darkness += 1
            self.mages += 1
            self.killstreak()
            self.turn=''
                        
        elif self.condition == 'light' and praxis == True and self.counter < 1:
            self.energy -= 3
            energynum.configure(text=''+str(self.energy))
            self.energy += 2
            energynum.configure(text=''+str(self.energy))
            self.bosslife -= 3
            self.ultimate += 1
            chargesnum.configure(text=''+str(self.ultimate))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You unleash a blast made of pure Abyssal energy!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You empower yourself by gaining an Abyssal charge')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 1 Abyssal charge')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 2 energy')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You decimate the Light mage with the power of the abyss!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'However, the magnitude of your spell is not enough to absorb')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'most of the Light mage\'s energy')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You absorb 2 energy from the Light Mage')
            self.counter += 1
            self.light += 1
            self.mages += 1
            self.killstreak()
            self.turn=''
                           
        elif self.condition == 'chaos' and praxis == True and self.counter < 1:
            self.energy -= 3
            energynum.configure(text=''+str(self.energy))
            self.bosslife -= 3
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You unleash a blast made of pure Abyssal energy!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'However, the Chaos mage used its blur spell evasion to dodge your blast')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You do not gain Abyssal charge and energy from the Chaos mage')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Chaos mage evaded your blast with its blur spell evasion!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You do not gain any Abyssal charges and energy from the chaos mage') 
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            self.counter += 1
            self.turn=''
            
                           
        elif self.condition == 'nature' and praxis == True and self.counter < 1:
            self.energy -= 3
            energynum.configure(text=''+str(self.energy))
            self.bosslife -= 3
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You unleash a blast made of pure Abyssal energy!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'However, the Nature mage easily blocked the attack')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You do not gain an Abyssal charge and energy from the Nature mage')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Nature mage blocks your blast by raising a vine from the ground to absorb the impact!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You do not gain any Abyssal charges and energy from the Nature mage') 
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            self.counter += 1
            self.killstreak()
            self.turn=''
            
                           
        elif self.condition == 'elemental' and praxis == True and self.counter < 1:
            self.energy -= 3
            energynum.configure(text=''+str(self.energy))
            self.energy += 4
            energynum.configure(text=''+str(self.energy))
            self.bosslife -= 3
            self.ultimate += 1
            chargesnum.configure(text=''+str(self.ultimate))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You unleash a blast made of pure Abyssal energy!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'The Elemental mage succumbed to the Abyssal blast')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 1 Abyssal charge')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 4 energy ')
                           

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Elemental mage\'s elemental mastery does not have any counter for the Abyssal blast!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You gain 1 Abyssal charge from the Elemental mage') 
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You gain 4 energy from the Elemental mage')
            self.counter += 1
            self.elemental += 1
            self.mages += 1
            self.killstreak()
            self.turn=''
        
            
        elif self.condition == 'boss' and praxis == True and self.bossalive != 'dead':
            self.bosslife -= 3
            self.energy -= 3
            energynum.configure(text=''+str(self.energy))
            self.ultimate += 1
            chargesnum.configure(text=''+str(self.ultimate))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You unleash a blast made of pure Abyssal energy!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You empower yourself by gaining an Abyssal charge')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You deal 3 life damage to the {grandmage}'.format(grandmage=self.bossname))
            self.boss()
            
        
        if self.alive == 'dead' and self.bossalive != 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You have already been defeated, Abyssal Archmage')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'There is no point of using your Abyssal blast anymore')
                           
        elif self.bossalive == 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'The {grandmage} has already been defeated'.format(grandmage=self.bossname))
    
    def abyssalstrike(self):
        praxis = True
        if self.condition == 'boss' and praxis == True and self.bossalive != 'dead' and self.alive != 'dead':
            self.energy += 8
            energynum.configure(text=''+ str(self.energy))
            self.bosslife -= 4
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You strike your opponent with the power of the')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'Abyss!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You feel empowered with the Abyss with that strike')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 8 energy')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You deal 4 life damage to the {grandmage}'.format(grandmage=self.bossname))
            self.boss()
        
        if self.bossalive == 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'The {grandmage} has already been defeated'.format(grandmage=self.bossname))
            
        elif self.alive == 'dead' and self.bossalive != 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You have already been defeated, Abyssal Archmage')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'There is no point of leeching energy anymore')
        
    
            
    
    def lifesteal(self):
        praxis = False
        if self.energy < 6:
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You do not have enough energy for this spell')
        else:
            praxis = True
            
        if self.condition == 'boss' and praxis == True and self.bossalive != 'dead' and self.alive != 'dead':
            self.life += 10
            lifenum.configure(text=''+ str(self.life))
            self.energy -= 6
            energynum.configure(text=''+ str(self.energy))
            self.bosslife -= 4
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You use the Abyssal energies to leech the')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'lifeforce from your opponent!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 10 HP')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You deal 4 life damage to the {grandmage}'.format(grandmage=self.bossname))
            self.boss()
            
        if self.bossalive == 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'The {grandmage} has already been defeated'.format(grandmage=self.bossname))
        elif self.alive == 'dead' and self.bossalive != 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You have already been defeated, Abyssal Archmage')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'There is no point of using your lifesteal anymore')
        
    def ultimatum(self):
        praxis = False
        if self.energy < 10 and self.ultimate < 8 and self.condition=='boss':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You do not have enough energy and Abyssal charges for this spell')
            
        elif self.energy < 10 and self.condition =='boss':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You do not have enough energy for this spell')
        elif self.ultimate < 8 and self.condition =='boss':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You do not have enough Abyssal charges for this spell')
        else:
            praxis = True
            
        if praxis == True and self.condition == 'boss' and self.alive != 'dead' and self.bossalive != 'dead':
                self.energy -= 10
                energynum.configure(text=''+str(self.energy))
                self.ultimate -= 8
                chargesnum.configure(text=''+str(self.ultimate))
                self.bosslife -= 20
                self.bossenergy -= 20
                wisdom.delete('1.0',END)
                wisdom.insert(INSERT,'You gather your might, wisdom, and rage into one devastating blast!')
                wisdom.insert(INSERT,'\n')
                wisdom.insert(INSERT,'\n')
                wisdom.insert(INSERT,'You release the violent sphere and direct it towards the {grandmage}'.format(grandmage=self.bossname))
                wisdom.insert(INSERT,'\n')
                wisdom.insert(INSERT,'\n')
                wisdom.insert(INSERT,'You deal 20 HP damage to the {grandmage}'.format(grandmage=self.bossname))
                wisdom.insert(INSERT,'\n')
                wisdom.insert(INSERT,'\n')
                wisdom.insert(INSERT,'You deal 20 energy damage to the {grandmage}'.format(grandmage=self.bossname))
                if self.bossenergy < 0:
                    self.bossenergy = 0
                self.boss()
        
        if self.bossalive == 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'The {grandmage} has already been defeated'.format(grandmage=self.bossname))
        
                      
        elif self.alive == 'dead' and self.bossalive != 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You have already been defeated, Abyssal Archmage')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'There is no point of using your Abyssal Ultimatum anymore')
                                      
                
                
    def fireball(self):
        praxis = False
        if self.energy < 4:
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You do not have enough energy for this spell')
        else:
            praxis = True
                    
        if self.condition == 'darkness' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 4
            energynum.configure(text=''+ str(self.energy))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'Your rage manifested into fiery flames!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You direct the flames towards your enemy')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 3 energy from the battle')
            self.energy += 3
            energynum.configure(text=''+ str(self.energy))

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You burn the Darkness Mage with the power of the Fireball!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You absorb 3 energy from the Darkness Mage')
            self.darkness += 1
            self.mages += 1
            self.killstreak()
            self.turn=''
            


        elif self.condition == 'light' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 4
            energynum.configure(text=''+ str(self.energy))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You release a fireball with fiery flames towards your enemy!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You do not gain energy from the battle')           
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The light mage passed through the fireball! Your efforts were in vain!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You did not absorb energy from the Darkness Mage')
            self.turn=''
        
        elif self.condition == 'chaos' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 4
            energynum.configure(text=''+ str(self.energy))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'Your rage manifested into fiery flames!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You direct the flames towards your enemy')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 3 energy from the battle')
            self.energy += 3
            energynum.configure(text=''+ str(self.energy))

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Chaos mage is overwhelmed by the raw power of your flames!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You absorb 3 energy from the Chaos mage')
            self.elemental += 1
            self.mages += 1
            self.killstreak()
            self.turn=''
            
        
        elif self.condition == 'elemental' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 4
            energynum.configure(text=''+ str(self.energy))
            self.life -= 5
            lifenum.configure(text=''+str(self.life))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'Your rage manifested into fiery flames!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You direct the flames towards your enemy')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'However, the Elemental mage uses its elemental mastery to absorb your flames!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'The Elemental mage unleashes a combined elemental blast towards you!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You lose 5 HP')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Elemental mage absorbs your water surge and unleashes a powerful elemental blast towards you!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You did not absorb any energy from the Chaos mage')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You lost 5 HP')
            self.turn=''
            
        elif self.condition == 'nature' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 4
            energynum.configure(text=''+ str(self.energy))
            self.energy += 3
            energynum.configure(text=''+str(self.energy))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'Your rage manifested into fiery flames!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You direct the flames towards your enemy')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 3 energy from the battle')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Nature mage is overwhelmed by the raw power of your flames!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Nature mage\'s nature magic cannot contest the power of your unforgiving flames!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You absorb 3 energy from the Chaos mage')
            self.mages += 1
            self.nature += 1
            self.killstreak()
            self.turn=''
            
        
            
        elif self.condition == 'boss' and praxis == True and self.bossalive != 'dead' and self.alive != 'dead':
            self.energy -= 4
            self.bosslife -= 6
            energynum.configure(text=''+ str(self.energy))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'Your Abyssal power manifests into fiery flames!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You direct the fiery flames towards the')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'{grandmage}'.format(grandmage=self.bossname))
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'The {grandmage} is caught in flames'.format(grandmage=self.bossname))
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You deal 6 life damage to the {grandmage}'.format(grandmage=self.bossname))
            self.boss()  
            
        if self.bossalive == 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'The {grandmage} has already been defeated'.format(grandmage=self.bossname))
            
            
        elif self.alive == 'dead' and self.bossalive != 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You have already been defeated, Abyssal Archmage')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'There is no point of using your fireball anymore')
            
       
    
        
    def water(self):
        praxis = False
        if self.energy < 5:
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You do not have enough energy for this spell')
        else:
            praxis = True
            
        if self.condition == 'darkness' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 5
            energynum.configure(text=''+ str(self.energy))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You release a torrent of water from the aqautic')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'depths!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 4 energy from the battle')
            self.energy += 4
            energynum.configure(text=''+ str(self.energy))
            
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The darkness mage was swallowed by the torrent from the aquatic depths!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You absorb 4 energy from the Darkness mage')
            self.darkness += 1
            self.mages += 1
            self.killstreak()
            self.turn=''
            
            
            
        elif self.condition == 'light' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 5
            energynum.configure(text=''+ str(self.energy))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You release a torrent of water from the aqautic') 
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'depths!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 4 energy from the battle')
            self.energy += 4
            energynum.configure(text='' + str(self.energy))
            
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The light mage\'s light could not escape the raging wave of water!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You absorb 4 energy from the Darkness mage')
            self.light += 1
            self.mages += 1
            self.killstreak()
            self.turn=''
            
        
        elif self.condition == 'chaos' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 5
            energynum.configure(text=''+ str(self.energy))
            self.life -= 5 
            lifenum.configure(text=''+str(self.life))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'Your release a torrent of water from the aquatic depths!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'However, the Chaos mage easily evaded your water surge')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You did not gain energy from this battle')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You lost 5 HP')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Chaos mage utilizes its blur evasion spell to evade your water surge!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Chaos mage releases a powerful arcane blast towards you')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'which turns your thoughts against you!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Chaos mage deals 5 life damage to you')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You did not gain energy from the Chaos mage')
            self.turn=''
    
        
        elif self.condition == 'elemental' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 5
            energynum.configure(text=''+ str(self.energy))
            self.life -= 5
            lifenum.configure(text=''+str(self.life))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'Your release a torrent of wave towards your enemy!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'However, the Elemental mage absorbs your water surge!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'The Elemental mage unleased a combined elemental blast towards you!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You lose 5 HP')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Elemental mage absorbs your water surge!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The energy from the water surge fueled the Elemental mage\'s')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'channeling of the elemental blast which blasts you from afar!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You did not absorb any energy from the Elemental mage')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You lose 5 HP')
            self.turn=''
            
            
        elif self.condition == 'nature' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 5
            energynum.configure(text=''+ str(self.energy))
            self.life -= 5
            lifenum.configure(text=''+str(self.life))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'Your unlease a torrent of wave towards your enemy!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'However, the Nature mage absorbed it and damaged')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'you with nature magic!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You lost 5 HP')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You did not gain energy from the battle')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Nature mage absorbed your water surge and uses your spell\'s')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'energy to channel a powerful ground spike spell!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Nature mage dealt 5 life damage to you')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You did not gain energy from this battle')
            self.turn=''
            
                           
        elif self.counter > 1 and self.condition == 'monster':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'The battle is already concluded. No other spells are needed')
            
            
        elif self.condition == 'boss' and praxis == True and self.bossalive != 'dead' and self.alive != 'dead':
            self.energy -= 5
            self.bosslife -= 8
            energynum.configure(text=''+ str(self.energy))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'Your Abyssal power manifests into a torrent of')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'aquatic water!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You shape the torrent to form a violent sphere of destruction')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'The {grandmage} is overwhelmed by the'.format(grandmage=self.bossname))
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'torrent')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You deal 8 life damage to the {grandmage}'.format(grandmage=self.bossname))
            self.boss()
                
        if self.bossalive == 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'The {grandmage} has already been defeated'.format(grandmage=self.bossname))
       
        elif self.alive == 'dead' and self.bossalive != 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You have already been defeated, Abyssal Archmage')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'There is no point of using your water surge anymore')
            
        
        
        
        
    def lightning(self):
        praxis = False
        if self.energy < 10:
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You do not have enough energy for this spell')
        else:
            praxis = True
            
        if praxis == True and self.condition == 'darkness' and self.counter < 1:
            self.energy -= 10
            energynum.configure(text=''+ str(self.energy))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You bring forth raw lightning to erase your enemy from existence!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 7 energy from the battle')
            self.energy += 7
            energynum.configure(text='' + str(self.energy))  
      
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You strike the Darkness Mage with Lightning, and the Darkness Mage cannot contest the power of lightning!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The darkness mage is now erased from existence')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You absorb 7 energy from the Darkness Mage')
            self.counter += 1
            self.mages += 1
            self.darkness += 1
            self.killstreak()
            self.turn=''
            
            
                
        elif praxis == True and self.condition == 'light' and self.counter < 1:
            self.energy -= 10
            energynum.configure(text=''+ str(self.energy))
            self.life -= 5
            lifenum.configure(text=''+str(self.life))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You bring forth raw lightning to erase your enemy from existence!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You lost 5 HP')  
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You did not gain energy from the battle')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Light mage hastily harnessed the power of the lightning!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Light mage absorbed the energy and retreated to the light')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Light mage brought forth the the divine light')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'beams of Bladespire to strike you down!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Light mage dealt 5 life damage to you!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You did not gain energy from the Light mage')
            self.counter += 1
            self.turn=''
            
        
        elif self.condition == 'chaos' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 10
            energynum.configure(text=''+ str(self.energy))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You channel the power of the sky through your mortal hands')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'Your knuckles is filled with the rage of the sky')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You bring forth lightning from the sky of Bladespire')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'to strike down the battlemage')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 7 energy from the battle')
            self.energy += 7
            energynum.configure(text=''+ str(self.energy))

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Chaos mage is struck by the powerful lightning that was willed by your command!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You absorb 7 energy from the Chaos mage')
            self.counter += 1
            self.chaos += 1
            self.mages += 1
            self.killstreak()
            self.turn=''
            
            
        
        elif self.condition == 'elemental' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 10
            energynum.configure(text=''+ str(self.energy))
            self.energy -= 5
            energynum.configure(text=''+ str(self.energy))
            self.life -= 10
            lifenum.configure(text=''+str(self.life))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You channel the power of the sky through your mortal hands')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'Your knuckles is filled with the rage of the sky')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You strike the Elemental battlemage down')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'However, the Elemental battlemage absorbed the rage of the sky')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'The Elemental battlemage strikes you down with the') 
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'energy from the lightning!')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You did not gain energy from this battle')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You lost 10 HP')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You lost 5 energy')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Elemental mage absorbs your water surge and unleashes a powerful elemental blast towards you!')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You did not absorb any energy from the Chaos mage')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You lost 10 HP')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'You lost 5 energy')
            self.counter += 1
            self.turn=''
           
            
            
        elif self.condition == 'nature' and praxis == True and self.counter < 1:
            self.counter += 1
            self.energy -= 10
            energynum.configure(text=''+ str(self.energy))
            self.energy += 7
            energynum.configure(text=''+str(self.energy))
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You channel the power of the sky through your mortal hands')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'Your knuckles is filled with the rage of the sky')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You bring forth lightning from the sky of Bladespire')
            wisdom.insert(INSERT,'to strike down the battlemage')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You gain 7 energy from the battle')

            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Nature mage attempts to block the lightning by raising trees and vines from the ground')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'However, the lightning strike\'s raw nature penetrated through the nature magic')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'\n')
            content.insert(INSERT,'The Nature battlemage qucikly disappeared from existence, leaving only traces of arcane energy')
            self.nature += 1
            self.mages += 1
            self.counter += 1
            self.killstreak()
            self.turn=''
            
            
        
        elif self.counter > 1 and self.condition == 'monster':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'The battle is already concluded. No other spells are needed')
           
            
        elif self.condition == 'boss' and praxis == True and self.bossalive != 'dead' and self.alive != 'dead':
            self.energy -= 10
            energynum.configure(text=''+ str(self.energy))
            self.bosslife -= 10
            self.bossenergy -= 7
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You raise your hand towards the sky')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You shape your Abyssal power into the rage of the sky itself')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'The {grandmage}\'s lifeforce and energy is greatly diminished'.format(grandmage=self.bossname))
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'The {grandmage} is electrified and'.format(grandmage=self.bossname))
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'weakened')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You deal 10 life damage to the {grandmage}'.format(grandmage=self.bossname))
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'You deal 7 energy damage to the {grandmage}'.format(grandmage=self.bossname))
            if self.bossenergy < 0:
                self.bossenergy = 0
            self.boss()
        
        if self.bossalive == 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'The {grandmage} has already been defeated'.format(grandmage=self.bossname))
        elif self.alive == 'dead' and self.bossalive != 'dead':
            wisdom.delete('1.0',END)
            wisdom.insert(INSERT,'You have already been defeated, Abyssal Archmage')
            wisdom.insert(INSERT,'\n')
            wisdom.insert(INSERT,'There is no point of using your lightning strike anymore')


gael = Decoretum()

game = Tk()
game.title('Abyssal Advance')
game.geometry('2000x2000')


background = PhotoImage(file='backgroundpic.png')
icon = PhotoImage(file='player.png')
game.iconphoto(False,icon)

b = Label(image=background)
b.place(x=0, y=0, relwidth=1, relheight=1)

powerlabel = Label(game, text = 'Abyssal Archmage\'s Power Status ') #self.name
powerlabel.grid(row = 0, column=0)


fireball = Button(game,text='Fireball',bg='#FF4040',fg='#030303',command=gael.fireball) #Fireball skills and effects
fireball.grid(row=0,column=3)

water = Button(game,text='Water Surge',bg='#00FFFF',fg='#030303',command=gael.water) #Water skills and effects
water.grid(row=1,column=3)

lightning = Button(game,text='Lightning Strike',bg='#FFB90F',fg='#030303',command=gael.lightning) #Lightning strike skills and effects
lightning.grid(row=2,column=3)

lifesteal = Button(game,text='Abyssal Lifesteal',bg='#FF1493',fg='#030303',command=gael.lifesteal) #leech life
lifesteal.grid(row=3,column=3)

abyssalstrike = Button(game,text='Abyssal Strike',bg='#EE1289',fg='#030303',command=gael.abyssalstrike) #Abyssal strike
abyssalstrike.grid(row=4,column=3)

abyssalblast = Button(game,text='Abyssal Blast',bg='#CD1076',fg='#030303',command=gael.abyssalblast) #Abyssal blast
abyssalblast.grid(row=5,column=3)

ultimatum = Button(game,text='Abyssal Ultimatum',bg='#8B0A50',fg='#F4F4F4',command=gael.ultimatum) #Ultimate
ultimatum.grid(row=7,column=3)

lifelabel = Label(game,text= 'HP',fg='#FF4040')
lifelabel.grid(row=1,column=0,sticky=N)

lifenum = Label(game,text=gael.life)
lifenum.grid(row=1,column=1,sticky=N)  

energylabel = Label(game,text = 'Energy:',fg='#0000EE')
energylabel.grid(row = 2, column=0,sticky=N) 

energynum = Label(game,text = gael.energy)
energynum.configure(state='normal')
energynum.grid(row = 2, column=1,sticky=N) 

essencelabel = Label(game,text='Essence:',fg='#006400')
essencelabel.grid(row=3, column=0,sticky=N) 

essencenum = Label(game,text = gael.essence)
essencenum.grid(row = 3, column=1,sticky=N) 

charges = Label(game,text='Abyssal Charges',fg='#BF3EFF')
charges.grid(row=4,column=0,sticky=N)

chargesnum = Label(game,text=gael.ultimate)
chargesnum.grid(row=4,column=1,sticky=N)

imgmain = (Image.open('Main.png'))
resizedmain = imgmain.resize((200,200),Image.ANTIALIAS)
main = ImageTk.PhotoImage(resizedmain)
hero = Label(image=main,height=135,width=125,bg='#C1FFC1')
hero.grid(row=5,column=0,rowspan=10,sticky=N)

wisdom = ScrolledText(game,width=50,height=15,bg='#F0E68C',fg='#000000') #General dialogue and events
wisdom.configure(state='normal')
wisdom.grid(row=1,column=2,rowspan=12,sticky=N)

abyssalguide = Label(game,text='Abyssal Guide:')
abyssalguide.grid(row=0,column=6)

abyssalentry = ScrolledText(game,width=30,height=15,bg='#BDFCC9',fg='#8B0000')
abyssalentry.delete('1.0',END)
abyssalentry.insert(INSERT,'Mages defeated: {mages}'.format(mages=gael.mages))
abyssalentry.insert(INSERT,'\n')
abyssalentry.insert(INSERT,'Darkness Mage: {mages}'.format(mages=gael.darkness))
abyssalentry.insert(INSERT,'\n')
abyssalentry.insert(INSERT,'Light Mage: {mages}'.format(mages=gael.light))
abyssalentry.insert(INSERT,'\n')
abyssalentry.insert(INSERT,'Chaos Mage: {mages}'.format(mages=gael.chaos))
abyssalentry.insert(INSERT,'\n')
abyssalentry.insert(INSERT,'Nature Mage: {mages}'.format(mages=gael.nature))
abyssalentry.insert(INSERT,'\n')
abyssalentry.insert(INSERT,'Elemental Mage: {mages}'.format(mages=gael.elemental))
abyssalentry.insert(INSERT,'\n')
abyssalentry.insert(INSERT,'\n')
abyssalentry.insert(INSERT,'Grand Mages defeated: {grandmages}'.format(grandmages=gael.grandmages))
abyssalentry.configure(state='normal')
abyssalentry.grid(row=1,column=6,rowspan=8)


img = (Image.open('arcaneboy.png'))
resized = img.resize((75,60), Image.ANTIALIAS)
arcaneboy = ImageTk.PhotoImage(resized)
spacemaker = Label(image=arcaneboy,height=50,width=50)
spacemaker.grid(row=9,column=6)

lists = Label(game,text=completechoices,bg='#EEDFCC')
lists.grid(row=0,column=7,rowspan=5,sticky=W)

content = ScrolledText(game,width=80,height=20,bg='#CAFF70',fg='#000000') #All the events happening
content.insert(INSERT,'This is a text-based game in development')
content.insert(INSERT,'\n')
content.insert(INSERT,'\n')
content.insert(INSERT,'The game will initialize once you press the button below')
content.insert(INSERT,'\n')
content.insert(INSERT,'\n')
content.insert(INSERT,'Enemies will range from normal mages to "Grand Mages"')
content.insert(INSERT,'\n')
content.insert(INSERT,'\n')
content.insert(INSERT,'After you conclude your battles, press the button below to move on')
content.insert(INSERT,'\n')
content.insert(INSERT,'\n')
content.insert(INSERT,'Enemy actions are identical to that of the player\'s. Hence, the enemy would act similarly to the player')
content.insert(INSERT,'\n')
content.insert(INSERT,'\n')
content.insert(INSERT,'Grand Mages will have HP and Energy similar to the player\'s stats')
content.insert(INSERT,'\n')
content.insert(INSERT,'\n')
content.insert(INSERT,'This game was created by Gael Estrera for fun during his quarantine')
content.insert(INSERT,'\n')
content.insert(INSERT,'\n')
content.insert(INSERT,'Pixel Arts created by Gael as well')
content.configure(state='normal')
content.grid(row=13,column=0,columnspan=5,rowspan=10,sticky=W)

battle = Button(game,text = 'Battle through the land of Bladespire', command=gael.battle)
battle.grid(row = 23,column=0)

game.mainloop()