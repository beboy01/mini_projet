liste=[]
print("1:Ajouter")
print("2:Ajouter")
print("3:Afficher")
print("4:vider")
print("5:quiter")
choix=int(input("votre choix :  "))
while (choix>=0 and choix <=5): 
     choix= int(input("entrez votre choix :"))    
     if choix==1:
          element= input("Donnez l'element à ajouter :")
          liste.append(element)
          print("L'element à bien été ajouter à la liste")
          print(liste)
     elif (choix==2):
          element=input("donner le nom de l'element ")
          if element in liste:
               liste.remove(element)
               print("l'élément bien ajouter à la liste!")
     elif (choix==3):
          print(liste)
     elif (choix==4):
          liste.clear()
     elif (choix==5):
          exit()

