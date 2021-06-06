# mini_projet
projet mini sur les liste
```python
liste=[]
choix=1
cont=0
for choix in range(1,5):

     while (choix>=0 and choix <=5): 
          try:
               print("-------------------------------------------------\nChoissez parmie ces 5 options suivantes :\n1:Ajouter un element à la liste\n2:Retirer un element de la liste\n3:Afficher la liste\n4:vider la liste\n5:quiter le programme")
               choix=int(input("   votre choix :"))
          except:
               print("vous devez entrez u nombre") 
          if choix==1:
               element= input("Donnez l'element à ajouter :")
               liste.append(element)
               print("L'element à bien été ajouter à la liste")
          elif (choix==2):
               element=input("donner le nom de l'element ")
               if element in liste:
                    liste.remove(element)
                    cont-=1
                    print("l'élément a  bien été retirer de la liste!")
          elif (choix==3):
               print("voici les informations que vous avez renseignez")
               for i in liste:
                    cont+=1
                    print(f"{cont}.  {i}")
               if not (i in liste):
                    print("votre liste ne contient aucun element")
                    cont=0
          elif (choix==4):
               liste.clear()
               print("vous avez vider la liste")
          elif (choix==5):
               print("vous avez quitez le programme mercie")
               exit()
               


```
