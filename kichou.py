#!/usr/bin/env python3
import discord
import time
######################################### PARAMETRES A PERSONALISER ################
bot   = "KICHOU" # nom de votre bot
jouea = "Python ........" # activité du bot
guild = 693286944712556595 # id de votre serveur
from tokenkichou import token #token du bot il faut créer un fichier tokenkichou.py
# avec une ligne token ='le token de votre bot'
####################################################################################

class MyClient(discord.Client):

    jeux='off'
    cannaux =["général","test"]      # utilisable en restrictions ex : if message.channel     in MyClient.cannaux:
    utilisateurs = ["Olive","ipapy","kichou","margotte"] # utilisable en restrictions ex : if message.author.name in MyClient.utilisateurs:

    async def on_ready(self):
        await client.change_presence(status=discord.Status.online, activity=discord.Game('{}'.format(jouea)))
        print('BOT : {} actif joue à {} --- on ready ---> OK'.format(bot,jouea))

    # a travailler
    async def on_message_edit(self,before, after):
        print('edit:')
        print(before.content)
        print(after.content)


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

        print('roles: ',end='' )
        for toto in id.roles : # membres
            print('{},'.format(toto),end='')
        '''
        print('membres: ',end='' )
        for toto in id.members : # membres
            print('{},'.format(toto),end='')        
        print()

        if 1 == 1 :#tous les channels
        #if (str(message.channel)=='général') or (str(message.channel)=='test'): #seulement ces channels
            print('{} canal: {} de: {} message: {}'.format(bot,message.channel,message.author,message.content))
            print('ID message: {}'.format(message.id))
            print('')

            if (1==1):
                if str(message.content).lower().find('§') >= 0 :
                    await message.delete(delay=10)
                if str(message.content).lower().find('œ') >= 0 :
                    await message.delete(delay=120)                    
        if message.author == self.user:
            if str(message.content).lower().find('§') >= 0 :
                await message.delete(delay=10)
            return
        if message.author == self.user:
            if str(message.content).lower().find('œ') >= 0 :
                await message.delete(delay=120)
            return
        #COMMANDES simple en début de ligne #######################################################
        if message.content.startswith('>hello') or message.content.startswith('>Hello'):
            await message.channel.send('H e l l o, comment vas-tu {} ?'.format(message.author.name))

        if message.content.startswith('>aide') or message.content.startswith('>aide'):
            await message.channel.send('Liste des commandes : >hello, >miaou, 2')

        # VARIABLES globales et commande d'activation du jeux
        if message.content.startswith('jeux on'):
            MyClient.jeux = 'on'
            await message.channel.send('Activation du jeux, état = {}'.format(MyClient.jeux))
            return

        if message.content.startswith('jeux off'):
            MyClient.jeux = 'off'
            await message.channel.send('Désactivation du jeux, état = {}'.format(MyClient.jeux)) 
            return

        if message.content.startswith('jeux'):
            await message.channel.send('jeux = {}'.format(MyClient.jeux))            

        # JEUX ni oui ni nom ###################################
        if MyClient.jeux == 'on':       
            if str(message.content).lower().find('oui') > -1:
                await message.channel.send('Ta perdu {} Tu a dit OUI !'.format(message.author.name))
                await message.channel.send('https://tenor.com/view/picturstef-oui-yes-si-bien-s%C3%BBr-gif-17961526 §')
            if str(message.content).lower().find('non') > -1:
                await message.channel.send('Ta perdu {} Tu a dit NON !'.format(message.author.name))
                await message.channel.send('https://tenor.com/view/non-nan-the-cabbage-soup-gif-5034277 §')

        #COMMANDES CLEAR ####################################################################
        cmd='clear'
        if message.content.startswith(cmd) and message.author.name in MyClient.utilisateurs :
            nb = int(message.content[len(cmd):len(cmd)+10])+1
            print(nb)
            await message.channel.purge(limit=nb)
            await message.channel.send('{},{} messages supprimés !'.format(message.author.name,nb -1))

        #COMMANDES nbm compte les message dans un channel ###################################
        if message.content.startswith('nbm'):
            await message.channel.send('ta demande est en cours {}, ça peut être long !'.format(message.author.name))
            counter = 0
            async for message in message.channel.history(limit=50000):
                if 1 == 1:
                    counter += 1
            await message.channel.send('{} Messages  !'.format(counter))
            #print(counter)

        #COMMANDE AVEC EFFACE COMMANDE #######################################################
        if message.content.startswith('>miaou'):
            await message.channel.purge(limit=1)
            #await message.delete(delay=5)
            await message.channel.send('https://tenor.com/view/test-neko-test-neko-keyboard-test-neko-meow-meow-gif-14509709 §')

        #DETECION MOT mouse bonjour hello avion apero sieste level bière café givre café :coffee: pelle poubelle @kichou 
        if str(message.content).lower().find('mousse ') > -1:
            await message.channel.send('Qui Fait de la mousse ?')

        if str(message.content).lower().find('bonjour') >= 0 and str(message.content).find('@') == -1 :
            await message.channel.send('Bonjour, comment vas-tu {} ?'.format(message.author.name))
            print(str(message.content).find('@'))
            
        if str(message.content).lower().find('hello') >= 0 and str(message.content).find('@') == -1 :
            await message.channel.send('Hello, {} Comment ça va ?'.format(message.author.name))
            print(str(message.content).find('@'))

        if str(message.content).lower().find('avion') >= 0 :
            await message.channel.send('https://www.inc-conso.fr/sites/default/files/styles/picture_article/public/avion-2_252.png?itok=7v3a8NxD §')

        if str(message.content).lower().find('apero') >= 0 :
            await message.channel.send('https://tenor.com/view/baby-yoda-yoda-child-the-child-mandalorian-gif-16440753 §')

        if str(message.content).lower().find('apéro') >= 0 :
            await message.channel.send('https://tenor.com/view/baby-yoda-yoda-child-the-child-mandalorian-gif-16440753 §')         

        if str(message.content).lower().find('sieste') >= 0 :
            await message.channel.send('https://tenor.com/view/chillin-cat-nap-tom-sleeping-gif-14821084 §')

        if str(message.content).lower().find('level') >= 0 :
            await message.channel.send('https://tenor.com/view/play-hard-gamer-play-hard-level-gif-8993741 §')

        if str(message.content).lower().find('bière') >= 0 :
            await message.channel.send('https://tenor.com/view/scholleveld-sonneveld-gif-18747738 §')

        if str(message.content).lower().find('givre') > -1:
            await message.channel.send('Du givre ou ça dans quel coin ?')

        if str(message.content).lower().find('café') > -1:
            await message.channel.send('Moi aussi je veux bien un petit ☕ {} !'.format(message.author.name))

        if str(message.content).lower().find('☕') > -1:
            await message.channel.send('Moi aussi je veux bien un petit ☕ {} !'.format(message.author.name))

        if str(message.content).lower().find('pelle') > -1:
           await message.channel.send('https://tenor.com/view/coup-de-pelle-shovel-hit-shovel-whack-gif-12859565 §')

        if str(message.content).lower().find('👍') > -1:
           await message.channel.send('https://tenor.com/view/sponge-bob-thumbs-up-ok-smile-gif-12038157 §')

        if str(message.content).lower().find('🤣') > -1:
            await message.channel.send('https://tenor.com/view/rolling-on-the-floor-laughing-emoji-gif-9682311 §')
 
 
        if str(message.content).lower().find('poubelle') > -1:
           await message.channel.send('<:poubjaune:712187805643833424> §')

        if str(message.content).lower().find('<@!773136088582717441>') > -1: #@kichou
           await message.channel.send('Oui {} je suis la !'.format(message.author.name) )

        if str(message.content).lower().find('miaou') > -1:
           await message.channel.send('https://tenor.com/view/test-neko-test-neko-keyboard-test-neko-meow-meow-gif-14509709 §')

        if str(message.content).lower().find('mdr') > -1:
           await message.channel.send('https://tenor.com/view/hahaha-laugh-lol-tom-and-jerry-gif-8702712 §')

        if str(message.content).lower().find('temps') > -1:
           await message.channel.send('https://www.eurogif.com/files/uploads/2018/04/FxhH5Nh2c.gif §')

        if str(message.content).lower().find('compliqué') > -1:
           await message.channel.send('https://i.pinimg.com/originals/8b/a2/52/8ba252c309dca70fe6eae9d58bf47ade.gif §')  

        if str(message.content).lower().find('moche') > -1:
           await message.channel.send('https://www.gif-maniac.com/gifs/31/30867.gif §')  

        if str(message.content).lower().find('chut') > -1:
           await message.channel.send('https://img.over-blog-kiwi.com/0/98/03/83/20160528/ob_98283f_ir9cxgc8.gif §')         

client = MyClient()
client.run(token)
