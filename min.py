liste=[]

print("-------------------------------------------------\nChoissez parmie ces 5 options suivantes :\n1:Ajouter un element à la liste\n2:Retirer un element de la liste\n3:Afficher la liste\n4:vider la liste\n5:quiter le programme")
choix=input("   votre choix :")

ranger= ["1","2","3","4","5"]
try:
     choix =int(choix)
except errmsg("Vous devez entrer un nombre compris entre 1 et 5"):
     print(errmsg())
                
for choix in ranger:
     suivant = input("Voulez-vous ajouter autre element (oui/non)?: ")
     while suivant=="oui":
          print("-------------------------------------------------\nChoissez parmie ces 5 options suivantes :\n1:Ajouter un element à la liste\n2:Retirer un element de la liste\n3:Afficher la liste\n4:vider la liste\n5:quiter le programme")
          choix=input("   votre choix :") 
          
          try:
               choix =int(choix)
          except :
               errmsg = "Erreur de saisie ! Vous devez entrer un nombre compris entre 1 et 5."
               print(errmsg)
                
          if choix==1:
               element= input("Donnez l'element à ajouter :")
               liste.append(element)
               print(f"{element}L'element à bien été ajouter à la liste")
          elif (choix==2):
               element=input("donner le nom de l'element à retirer de la liste ")
               
               if element in liste:
                    liste.remove(element)
                    
                    print(f"{element} a  bien été retirer de la liste!")
               if not (element  in liste):
                    print(f"{element} l'est pas dans la liste !")
                    
          elif (choix==3):
               print(" \nVoici vos informations dans le pannier :")
               
               for i ,element in enumerate(liste):
                   
                    print(f"{i}.  {element}")
               if not (element  in liste):
                    print("votre liste ne contient aucun element")
                    
          elif (choix==4):
               liste.clear()
               print("vous avez vider la liste")
          elif (choix==5):
               print("vous avez quitez le programme mercie")
               exit()
     if suivant=="non":
          print("mercie au revoir !")
          exit()
