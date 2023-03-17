

import nest_asyncio
nest_asyncio.apply()

import discord 



intents = discord.Intents.all()
client = discord.Client(intents=intents)
score = 0
Q1 = "J'apporte de la lumière et de la chaleur qui suis-je??"
Q2 = "je suis une période de l histoire de l'Europe s'étendant de la fin du 5 eme siècle à la fin du 15 eme siecle qui suis-je?"
Q3 = "je suis un champ chromatique regroupant l orange et le pourpre qui suis-je?"
Q4 = "je suis le successeur du roi.comment m'apppelle t_on"
Q5 = "je suis le roi soleil.qui suis_je?"
Q6 = "je suis une représentation mythologique d'un reptile qui suis-je "
Q7 = "je suis une construction médiévale qui cumule plusieurs fonctions "

R1 = "le feu"
R2 = "le moyen âge"
R3 = "rouge"
R4 = "dauphin"
R5 = "louis14"
R6 = "un dragon"
R7 = "un château"

indice1 ="Je suis l'effet visible du processus de combustion."
indice2 ="Je suis entre l'Antiquité et la Renaissance"
indice3 ="je suis la couleur de l'hémoglobine."
indice4 ="je suis la seconde au concours de beauté"
indice5 ="je me lève à l'est et me couche à l'ouest"
indice6 ="je crache du feu"
indice7 ="je suis un lieu fortifié "



@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_typing(channel, user, when):
     await channel.send(user.name+" is typing")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(1044972166564827186) 
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name)

@client.event
async def on_message(message):







  
  if message.author == client.user:
    return
  message.content = message.content.lower()
  global score
  if message.content.startswith("bonjour"):
  
    score = 0
    await message.channel.send("bonjour")
    await message.channel.send("bienvenue dans la grande chasse au trésor .Vous serez soumis à de grandes énigmes vous devrez braver tous les dangers et parvenir jusqu' au sommet de la tour  ou vous découvrirez la salle au trésor mais attention au plus redoutable le plus dangereux de tous les dragons. l'aventurier sera alors confronter à un dragon qui lui posera 7 questions  il aura ensuite accès à des indices pour l'aider mais attention chaque indice lui coutera -0.5 et a chaque bonne réponse il gagnera un point pour demander un indice il faudra marqué (indice1) 2,3,4....Et pour relancer le jeu depuis le debut vous avez qu'a taper 'relancer'")
    await message.channel.send("Pour commencer taper start")
    await message.channel.send("https://www.gif-maniac.com/gifs/41/41450.gif")
 
  if message.content.startswith("start"):
      
    await message.channel.send("vous seul pouvez retrouver le trésor perdu en vous aventurant là où d’autres ont peur de s’aventurer. Décodez ces énigmes et entrez dans la quête.")
    await message.channel.send("premiere question:")
    await message.channel.send(Q1)

  if message.content.startswith("indice1"):
    await message.channel.send(indice1)
    score = score -0.5
    print(score)

    

  if R1 in message.content:
    await message.channel.send("vous avez gagné !")
    await message.channel.send("vous pouvez monter au premier étage")
    await message.channel.send("https://www.gif-maniac.com/gifs/41/41446.gif")
    score = score+1
    print(score)
    await message.channel.send(f'ton score: {score}') 
    await message.channel.send("deuxième question ")                                                                              
    await message.channel.send(Q2)

  if message.content.startswith("indice2"):
    await message.channel.send(indice2)
    score = score -0.5
    print(score)

  if R2 in message.content:
    await message.channel.send("vous avez gagné !")
    await message.channel.send("vous pouvez monter au deuxième étage")
    await message.channel.send("https://media0.giphy.com/media/J2gAk7RIHjlDJDWyvI/giphy.gif?cid=ecf05e47zuuf21837hw02350rt5jy1qfspqd3hxre3fk73d4&rid=giphy.gif&ct=g")
    score = score+1
    print(score)
    await message.channel.send(f'ton score: {score}') 
    await message.channel.send("troisième  question ")                                                                              
    await message.channel.send(Q3)

  if message.content.startswith("indice3"):
    await message.channel.send(indice3)
    score = score -0.5
    print(score)

  if R3 in message.content:
    await message.channel.send("vous avez gagné !")
    await message.channel.send("vous pouvez monter au troisième étage")
    await message.channel.send("https://media0.giphy.com/media/J2gAk7RIHjlDJDWyvI/giphy.gif?cid=ecf05e47zuuf21837hw02350rt5jy1qfspqd3hxre3fk73d4&rid=giphy.gif&ct=g")
    score = score+1
    print(score)
    await message.channel.send(f'ton score: {score}') 
    await message.channel.send("quatrième question ")                                                                              
    await message.channel.send(Q4)

  if message.content.startswith("indice4"):
    await message.channel.send(indice4)
    score = score -0.5
    print(score)

  if R4 in message.content:
    await message.channel.send("vous avez gagné !")
    await message.channel.send("vous pouvez monter au quatrième étage")
    await message.channel.send("https://media0.giphy.com/media/J2gAk7RIHjlDJDWyvI/giphy.gif?cid=ecf05e47zuuf21837hw02350rt5jy1qfspqd3hxre3fk73d4&rid=giphy.gif&ct=g")
    score = score+1
    print(score)
    await message.channel.send(f'ton score: {score}') 
    await message.channel.send("cinquième question ")                                                                              
    await message.channel.send(Q5)

  if message.content.startswith("indice5"):
    await message.channel.send(indice5)
    score = score -0.5
    print(score)

  if R5 in message.content:
    await message.channel.send("vous avez gagné !")
    await message.channel.send("vous pouvez monter au cinquième étage")
    await message.channel.send("https://media0.giphy.com/media/J2gAk7RIHjlDJDWyvI/giphy.gif?cid=ecf05e47zuuf21837hw02350rt5jy1qfspqd3hxre3fk73d4&rid=giphy.gif&ct=g")
    score = score+1
    print(score)
    await message.channel.send(f'ton score: {score}') 
    await message.channel.send("sixième question ")                                                                              
    await message.channel.send(Q6)

  if message.content.startswith("indice6"):
    await message.channel.send(indice6)
    score = score -0.5
    print(score)

  if R6 in message.content:
    await message.channel.send("vous avez gagné !")
    await message.channel.send("vous pouvez monter au sixième étage")
    await message.channel.send("https://media0.giphy.com/media/J2gAk7RIHjlDJDWyvI/giphy.gif?cid=ecf05e47zuuf21837hw02350rt5jy1qfspqd3hxre3fk73d4&rid=giphy.gif&ct=g")
    await message.channel.send("la porte du dragon")
    await message.channel.send("https://previews.123rf.com/images/grafvision/grafvision1605/grafvision160500032/56626807-détail-d-une-porte-de-l-église-ou-d-un-château-vieux.jpg")
    await message.channel.send("https://media.tenor.com/M7jo4nJF-7AAAAAM/drogon-dracarys.gif")
    score = score+1
    print(score)
    await message.channel.send(f'ton score: {score}') 
    await message.channel.send("Question final ")                                                                              
    await message.channel.send(Q7)
  
  if message.content.startswith("indice7"):
    await message.channel.send(indice7)
    score = score -0.5
    print(score)

  if R7 in message.content:
    await message.channel.send("✨✨félicitations vous avez tué le dragon et gagné le trésord✨✨!!!!")
    await message.channel.send("https://media.tenor.com/gVPTCa8k4xgAAAAM/sleeping-beauty-prince-phillip.gif")
    await message.channel.send("https://www.photofunky.net/output/image/9/e/9/7/9e9727/photofunky.gif")
    score = score+1
    print(score)
  if message.content.startswith("relancer"):
    await message.channel.send("bienvenue dans la grande chasse au trésor .Vous serez soumis à de grandes énigmes vous devrez braver tous les dangers et parvenir jusqu' au sommet de la tour  ou vous découvrirez la salle au trésor mais attention au plus redoutable le plus dangereux de tous les dragons. l'aventurier sera alors confronter à un dragon qui lui posera 7 questions  il aura ensuite accès à des indices pour l'aider mais attention chaque indice lui coutera -0.5 et a chaque bonne réponse il gagnera un point pour demander un indice il faudra marqué (indice1) 2,3,4....Et pour relancer le jeu depuis le debut vous avez qu'a taper 'relancer'")
    await message.channel.send("Pour commencer taper start")
    await message.channel.send("https://www.gif-maniac.com/gifs/41/41450.gif")
 

  
  
  

  

   

client.run("MTA0NDk2ODU4MTg0ODM4NzYyNg.GvLBdQ.YWgdNd3Utt4DwaeBWO0iUvP5pzftROdxc6KDs8")