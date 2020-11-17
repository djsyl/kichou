#!/usr/bin/env python3
# coding: utf-8
_______________________________________________ MAIN________________________________
import discord
import time

######################################### PARAMETRES A PERSONALISER ################
bot   = "kichou" # nom de votre bot
jouea = bot+" fait du Python" # activité du bot
guild = 693286944712556595 # id de votre serveur
from tokenkichou import token #token du bot il faut créer un fichier tokenkichou.py
# avec une ligne token ='le token de votre bot'
####################################################################################

from dickichou import dickichou # dictionaire des mots reconnus par le boot

class MyClient(discord.Client):
    global dickichou # dictionaire

    timer1 = 10  #timing §
    timer2 = 120 #timing œ
    jeux='off'
    cannaux =["général","test"]      # utilisable en restrictions ex : if message.channel     in self.cannaux:
    utilisateurs = ["Olive","iPapy",bot,"margotte"] # utilisable en restrictions ex : if message.author.name in self.utilisateurs:

    async def on_ready(self):
        await client.change_presence(status=discord.Status.online, activity=discord.Game('{}'.format(jouea)))
        print('BOT : {} actif joue à {} --- on ready ---> OK'.format(bot,jouea))

    # a travailler <------------------------------------------------------------------
    async def on_message_edit(self,before, after):
        print('edit:')
        print(before.content)
        print(after.content)

    # receptinn d'un message _________________________________________________________
    async def on_message(self, message):
        id = client.get_guild(guild) # <

        print("id membercount     {}".format(id.member_count)) #nombre d'utilisateur
        print("id server name     {}".format(id.name)) #nom du serveur

        ''' OK quel ques commandes en options
        for toto in id.channels: # tous les channels
            print(toto)

        for toto in id.text_channels: # les channels text seulement
            print('channels texte : {},'.format(toto),end='')
            print()
        
        print('channels categorie : ',end='' )
        for toto in id.categories : # les categories
            print('{},'.format(toto),end='')
        '''
        print('roles: ',end='' )
        for toto in id.roles : # membres
            print('{},'.format(toto),end='')
        print('')

        print('membres: ',end='' )
        for toto in id.members : # membres
            print('{},'.format(toto),end='')        
        print()
        
        print('membres 2: ',end='' )
        for toto in client.users : # membres
            print('{},'.format(toto),end='')        
        print()

        print('membres 3: ',end='' )
        for toto in client.get_all_members() : # membres
            print('{},'.format(toto),end='')        
        print()        


        if 1 == 1 :#tous les channels
        #if (str(message.channel)=='général') or (str(message.channel)=='test'): #seulement ces channels
            print('{} canal: {} de: {} message: {}'.format(bot,message.channel,message.author,message.content))
            print('ID message: {}'.format(message.id))
            print('')
        if str(message.content).lower().find('"') >= 0 :
            print('pas de réaction')
            return
        if message.author != self.user: #si c'est le bot qui a envoyer
            if (1==1):
                if str(message.content).lower().find('§') >= 0 :
                    print('debug: {}'.format('A'))
                    await message.delete(delay=self.timer1)
                if str(message.content).lower().find('œ') >= 0 :
                    print('debug: {}'.format('B'))
                    await message.delete(delay=self.timer2)
        if message.author == self.user:
            if str(message.content).lower().find('§') >= 0 :
                print('debug: {}'.format('C'))
                await message.delete(delay=self.timer1)
            return
        if message.author == self.user:
            if str(message.content).lower().find('œ') >= 0 :
                print('debug: {}'.format('D'))
                await message.delete(delay=self.timer2)
            return

        #COMMANDES simple en début de ligne #######################################################
        if message.content.startswith('>hello') or message.content.startswith('>Hello'):
            await message.channel.send('H e l l o, comment vas-tu {} ?'.format(message.author.name))
        #_________________ A revoir avec l'histoire du dictionaire __________________________________
        if message.content.startswith('>aide') or message.content.startswith('>aide'):
            await message.channel.send('```md\n#Liste des commandes :\n>aide >hello, >miaou, jeux on, jeux off, jeux\
 \n\n#mots déclancheur :\navion, mdr, pelle, miaou, mousse, bonjour, hello, apero, apéro,\
 sieste, level, givre, café, ☕, 👍, 🤣, poubelle , temps, compliqué, moche, chut,\
 columbo, combo, salut, bravo, 👏\n\n#caractères spéciaux :\n\
 " anti mot déclancheur \n Œ efface aprés 120 secondes\n § efface aprés 15 secondes```')

        # VARIABLES globales et commande d'activation du jeux
        if message.content.startswith('jeux on'):
            self.jeux = 'on'
            await message.channel.send('Activation du jeux, état = {}'.format(self.jeux))
            return

        if message.content.startswith('jeux off'):
            self.jeux = 'off'
            await message.channel.send('Désactivation du jeux, état = {}'.format(self.jeux)) 
            return

        if message.content.startswith('jeux'): #donne l'etat du jeux
            await message.channel.send('jeux = {}'.format(self.jeux))            

        # JEUX ni oui ni nom ###################################
        if self.jeux == 'on':       
            if str(message.content).lower().find('oui') > -1:
                await message.channel.send('Ta perdu {} Tu a dit OUI !'.format(message.author.name))
                await message.channel.send('https://tenor.com/view/picturstef-oui-yes-si-bien-s%C3%BBr-gif-17961526 §')
            if str(message.content).lower().find('non') > -1:
                await message.channel.send('Ta perdu {} Tu a dit NON !'.format(message.author.name))
                await message.channel.send('https://tenor.com/view/non-nan-the-cabbage-soup-gif-5034277 §')

        #COMMANDES kichou sauvegarde le dictionaire ###################################################
        cmd= bot + ' sauvegarde le dictionaire'
        if message.content.startswith(cmd) and message.author.name in self.utilisateurs :
            with open('dickichou.py', 'w') as f:
                f.write('dickichou={}\n')
                for k,v in dickichou.items():
                    f.write('dickichou["{}"]="{}"\n'.format(k,v))
                f.close
            await message.channel.send('Dictionaire sauvegardé')
            return
            
        #COMMANDES kichou ajoute clef:value ### et opérations sur dictionaire dickichou
        cmd= bot + ' ajoute '
        if message.content.startswith(cmd) and message.author.name in self.utilisateurs :
            rep = message.content[len(cmd):len(message.content)]
            sep = rep.find(':') 
            clef = rep[0:sep]
            value = rep[sep+1:] 

            dickichou[clef] = value 

            await message.channel.send('Dictionaire '+bot+', ajout de la Clef={} Valeur={}'.format(clef,value))
            return

        cmd= bot+' retire '
        if message.content.startswith(cmd) and message.author.name in self.utilisateurs :
            rep = message.content[len(cmd):len(message.content)]
            if dickichou.get(rep) != None:
                del dickichou[rep]
                await message.channel.send('Dictionaire '+bot+', Clef={} Supprimée !'.format(rep))
                return
            else :
                await message.channel.send("Dictionaire "+bot+", La Clef={} n'existe pas !".format(rep))
                return

        
        cmd= bot+' dictionaire' ################ A REVOIR
        if message.content.startswith(cmd) and message.author.name in self.utilisateurs :
            for k,v in dickichou.items():
                print('{} : {}"'.format(k,v))
            return
        
        
        
        #DETECTION MOT DIC KICHOU ##############################################################     
        for k,v in dickichou.items() :
            if k.lower() in str(message.content).lower() :
                await message.channel.send('{}'.format(v))       
        
        #COMMANDES TIMER ####################################################################
        cmd='timer1'
        if message.content.startswith(cmd) and message.author.name in self.utilisateurs :
            nb = int(message.content[len(cmd):len(cmd)+10])
            mem = self.timer1
            self.timer1 = nb
            await message.channel.send('TIMER 1 timer1 = {} -> {}\ntimer2 = {}'.format(mem,nb,self.timer2))
            return

        cmd='timer2'
        if message.content.startswith(cmd) and message.author.name in self.utilisateurs :
            nb = int(message.content[len(cmd):len(cmd)+10])
            mem = self.timer2
            self.timer2 = nb
            await message.channel.send('TIMER 1 timer1 = {} \ntimer2 = {}-> {}'.format(self.timer1,mem,self.timer2))
            return

        cmd='timer'
        if message.content.startswith(cmd) and message.author.name in self.utilisateurs :
            #await message.channel.send(message.author.name)
            await message.channel.send('timer1 = {}\ntimer2 = {}'.format(self.timer1,self.timer2))
            return

        if message.content.startswith('timer'):
            await message.channel.send('commande staff seulement {}'.format(message.author.name))

        #COMMANDES CLEAR ####################################################################
        cmd='xclear'
        if message.content.startswith(cmd) and message.author.name in self.utilisateurs :
            nb = int(message.content[len(cmd):len(cmd)+10])+1
            print('{} messages à supprimer'.format(nb -1))
            await message.channel.purge(limit=nb)
            await message.channel.send('{},{} messages supprimés !'.format(message.author.name,nb -1))
            while True : #______________ATTENTION REPETITION AUTOMATIQUE DE LA COMMANDE
                time.sleep(2)
                await message.channel.purge(limit=nb-1)
                await message.channel.send('{},{} messages supprimés !'.format(message.author.name,nb -1))

        cmd='clear'
        if message.content.startswith(cmd) and message.author.name in self.utilisateurs :
            nb = int(message.content[len(cmd):len(cmd)+10])+1
            print('{} messages à supprimer'.format(nb -1))
            await message.channel.purge(limit=nb)
            await message.channel.send('{},{} messages supprimés !'.format(message.author.name,nb -1))

        #COMMANDES nbm compte les message dans un channel ###################################
        if message.content.startswith('nbm'):
            await message.channel.send('ta demande est en cours {}, ça peut être long !'.format(message.author.name))
            counter = 0
            async for message in message.channel.history(limit=500000):
                if 1 == 1:
                    counter += 1
            await message.channel.send('{} Messages  !'.format(counter))
            #print(counter)

        #COMMANDE AVEC EFFACE COMMANDE #######################################################
        if message.content.startswith('>miaou'):
            await message.channel.purge(limit=1)
            #await message.delete(delay=5)
            await message.channel.send('https://tenor.com/view/test-neko-test-neko-keyboard-test-neko-meow-meow-gif-14509709 §')

        #DETECION MOT hors dictionaire traitement particulier #######################################

        if str(message.content).lower().find('bonjour') >= 0 and str(message.content).find('@') == -1 :
            await message.channel.send('Bonjour, comment vas-tu {} ?'.format(message.author.name))
            
        if str(message.content).lower().find('hello') >= 0 and str(message.content).find('@') == -1 :
            await message.channel.send('Hello, {} Comment ça va ?'.format(message.author.name))
            print(str(message.content).find('@'))

        #if str(message.content).lower().find('café') > -1:
        #    await message.channel.send('Moi aussi je veux bien un petit ☕ {} !'.format(message.author.name))

        #if str(message.content).lower().find('☕') > -1:
        #    await message.channel.send('Moi aussi je veux bien un petit ☕ {} !'.format(message.author.name))


        #if str(message.content).lower().find('poubelle') > -1:
        #   await message.channel.send('<:poubjaune:712187805643833424> §')

        if str(message.content).lower().find('<@!773136088582717441>') > -1: #@kichou
           await message.channel.send('Oui {} je suis la !'.format(message.author.name) )


client = MyClient()
client.run(token)
