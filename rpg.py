liste = ["MAIN MENU","1 .Create New Game","2 .Load Saved Game","3 .About","4 .Exit"]
user_name=input("Entrez votre prenom")
print(user_name , "bienvenu dans MEDELINE")
print(user_name , "choisissez dans la liste de menu un chiffre pour commencer a jouer")
print(liste[0])
print(liste[1])
print(liste[2])
print(liste[3])
print(liste[4])
user=int(input())
score = 0


#la commande Create New Game
if user==1:
  print("bienvenu dans ce jeu intitulé MEDELINE.")
  print("Le principe du jeu est le suivant: Immaginez vous que vous etes emprisonnez dans un chateau et qu'il faut battre plusieurs monstres en resolvant les enigmes auquelles vous serez confrontéés ")
  print("pour commencer le jeu tapez start")
  print("Au cour de votre partie si vous voulez relancer la partie tapez Y")
  gamer=input()
  if gamer== "start":
    print("ENIGME1: Je serai hier, j'étais demain.")
    gamer1=input()
    compteur=0
    while gamer1!="aujourd'hui" :
      print("mauvaise reponse, réesayez")
      gamer1=input()
      compteur=compteur+1
     
        
    if gamer1=="aujourd'hui":
      print("GAGNER!! vous venez de tuer le roi des gnome")
    
      print("monter au premier etage")
      score = score +10
      print("vous avez gagner",score,"xp")
      print("ENIGME2: Je détruit tout : os, chair et vie. Jamais je ne me repose car je suis infini. Ni l'acier des armes, ni la roche des montagnes ne me résistent.Dévoreur sans fin, mon appétit n'a pas de limite.Que suis-je ?")
      gamer1=input()
      compteur=0
      while gamer1!="le temps" :
           print("mauvaise reponse, réesayez")
           gamer1=input()
           compteur=compteur+1
      
               
      if gamer1=="le temps":
           print("GAGNER!! vous venez de tuer le roi du temps")
           
           print("monter au deuxième étage ")
           score = score +10
           print("vous avez gagner",score,"xp")
           print("ENIGMES3:Si de ton doigt tu veux me toucher, apprête toi alors à le retirer.Mais si tu sais le manipuler ta demeure en sera réchauffée et illuminée.")
           gamer1=input()
           compteur=0
           while gamer1!="le feu"  :
            print("mauvaise reponse, réesayez")
            gamer1=input()
            compteur=compteur+1
            
              
    if gamer1=="le feu":
        print("GAGNER!! vous venez de tuer le roi du feu")
        print("monter au troisième étage la demeure du roi de la mort(BOSS) ")
        score = score +20
        print("vous avez gagner",score,"xp")
        print("ENIGMES4 final: Vous ne pouvez que me deviner et ne pouvez qu'avancer vers moi.Quand vous arrivez, je ne suis plus là.Car à chaque pas avancé, je recule d'autant.")
        print("Le BOSS a 35 xp")
        gamer1=input()
        compteur=0
        while gamer1!="le future" :
            print("mauvaise reponse, réesayez")
            gamer1=input()
            compteur=compteur+1
            
              
    if gamer1== "le future":
           print("GAGNER!!!!!!!!!!!!!!! Vous venez de tuer le boss du jeux pour récupérer le tresor apui")
           
           score = score +100
           print("vous avez gagner",score,"xp")
    
           
    if gamer1=="oui" :
      print("ENIGME1: Je serai hier, j'étais demain.")
    gamer1=input()
    compteur=0
    while gamer1!="aujourd'hui" :
      print("mauvaise reponse, réesayez")
      gamer1=input()
      compteur=compteur+1
    
    if gamer1=="aujourd'hui":
      print("GAGNER!! vous venez de tuer le roi des gnome")
    
      print("monter au premier etage")
      score = score +10
      print("vous avez gagner",score,"xp")     


    


#la commande load saved Game

if user==2:
  print(user,"bienvenu dans les sauvegardes")
  print("rentrz le chiffre du niveau auquel vous etes dans la liste suivant")
  print("1 .Rez-de-chaussé")
  print("2 . Premier Etage")
  print("3 .Troisiemme Etage")
  print("4 .Big Boss")
  user_saved=input()

  if user_saved=="1":
    print("ENIGME1: Je serai hier, j'étais demain qui suis-je??")
    gamer1=input()
    compteur=0
    while gamer1!="aujourd'hui" :
      print("mauvaise reponse, réesayez")
      gamer1=input()
      compteur=compteur+1
      
        
    if gamer1=="aujourd'hui":
         print("GAGNER!! vous venez de tuer le roi des gnome")
         print("monter au premier etage")
         score = score +10
         print("vous avez gagner",score,"xp")
         print("ENIGME2: Je détruit tout : os, chair et vie. Jamais je ne me repose car je suis infini. Ni l'acier des armes, ni la roche des montagnes ne me résistent.Dévoreur sans fin, mon appétit n'a pas de limite.Que suis-je ?")
         gamer1=input()
         compteur=0
         while gamer1!="le temps" :
           
           gamer1=input()
           compteur=compteur+1
           
    if gamer1=="le temps":
           print("GAGNER!! vous venez de tuer le roi du temps")
           print("monter au deuxième étage ")
           score = score +10
           print("vous avez gagner",score,"xp")
           print("ENIGMES3:Si de ton doigt tu veux me toucher, apprête toi alors à le retirer.Mais si tu sais le manipuler ta demeure en sera réchauffée et illuminée.")
           gamer1=input()
           compteur=0
           while gamer1!="le feu" :
            print("mauvaise reponse, réesayez")
            gamer1=input()
            compteur=compteur+1
    if gamer1=="le feu":
           print("GAGNER!! vous venez de tuer le roi du feu")
           print("monter au troisième étage la demeure du roi de la mort(BOSS) ")
           score = score +20
           print("vous avez gagner",score,"xp")
           print("ENIGMES4 final: Vous ne pouvez que me deviner et ne pouvez qu'avancer vers moi.Quand vous arrivez, je ne suis plus là.Car à chaque pas avancé, je recule d'autant.")
           print("Le BOSS a 35 xp")
           gamer1=input()
           compteur=0
           while gamer1!="le feu" :
            print("mauvaise reponse, réesayez")
            gamer1=input()
            compteur=compteur+1
            
    if gamer1== "le future":
           print("GAGNER!!!!!!!!!!!!!!! Vous venez de tuer le boss du jeux pour récupérer le tresor apui")
  
    if user_saved=="2" :
      print("ENIGME2: Je détruit tout : os, chair et vie. Jamais je ne me repose car je suis infini. Ni l'acier des armes, ni la roche des montagnes ne me résistent.Dévoreur sans fin, mon appétit n'a pas de limite.Que suis-je ?")
      gamer=input()
      compteur=0
    while gamer1!="le temps" :
      print("mauvaise reponse, réesayez")
      gamer=input()
      compteur1=compteur+1
      

      if gamer1=="le temps":
        print("GAGNER!! vous venez de tuer le roi du temps")
        print("monter au deuxième étage ")
        score = score +10
        print("vous avez gagner",score,"xp")
        print("ENIGMES3:Si de ton doigt tu veux me toucher, apprête toi alors à le retirer.Mais si tu sais le manipuler ta demeure en sera réchauffée et illuminée.")
        gamer1=input()
        compteur=0
        while gamer1!="le feu" :
          print("mauvaise reponse, réesayez")
          gamer1=input()
          compteur=compteur+1
          
    if gamer1=="le feu":
           print("GAGNER!! vous venez de tuer le roi du feu")
           print("monter au troisième étage la demeure du roi de la mort(BOSS) ")
           score = score +20
           print("Le BOSS a 35 xp")
           print("vous avez gagner",score,"xp")
           print("ENIGMES4 final: Vous ne pouvez que me deviner et ne pouvez qu'avancer vers moi.Quand vous arrivez, je ne suis plus là.Car à chaque pas avancé, je recule d'autant.")
           gamer1=input()
           compteur=0
           while gamer1!="le feu":
            print("mauvaise reponse, réesayez")
            gamer1=input()
            compteur=compteur+1
    if gamer1== "le future":
           print("GAGNER!!!!!!!!!!!!!!! Vous venez de tuer le boss du jeux pour récupérer le tresor apui")


  if user_saved=="3":
    print("ENIGMES3:Si de ton doigt tu veux me toucher, apprête toi alors à le retirer.Mais si tu sais le manipuler ta demeure en sera réchauffée et illuminée.")
    gamer1=input()
    compteur=0
    while gamer1!="le feu":
      print("mauvaise reponse, réesayez")
      gamer1=input()
      compteur=compteur+1
      
    if gamer1=="le feu":
           print("GAGNER!! vous venez de tuer le roi du feu")
           print("monter au troisième étage la demeure du roi de la mort(BOSS) ")
           score = score +20
           print("vous avez gagner",score,"xp")
           print("ENIGMES4 final: Vous ne pouvez que me deviner et ne pouvez qu'avancer vers moi.Quand vous arrivez, je ne suis plus là.Car à chaque pas avancé, je recule d'autant.")
           print("Le BOSS a 35 xp")
           gamer1=input()
           compteur=0
           while gamer1!="le feu":
            print("mauvaise reponse, réesayez")
            gamer1=input()
            compteur=compteur+1
            
    if gamer1== "le future":
      print("GAGNER!!!!!!!!!!!!!!! Vous venez de tuer le boss du jeux pour récupérer le tresor apui")

      
    
  if user_saved=="4":
    print("ENIGMES4 final: Vous ne pouvez que me deviner et ne pouvez qu'avancer vers moi.Quand vous arrivez, je ne suis plus là.Car à chaque pas avancé, je recule d'autant.")
    print("Le BOSS a 35 xp")
    gamer1=input()
    compteur=0
    while gamer1!="le futur":
      print("mauvaise reponse, réesayez")
      gamer1=input()
      compteur=compteur+1
      
    if gamer1== "le futur":
      print("GAGNER!!!!!!!!!!!!!!! Vous venez de tuer le boss du jeux 🙌✨✨")
      
      score = score +10000
      print("vous avez gagner",score,"xp")
           
           


     
    
    






       



   
               