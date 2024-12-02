import random
def roulerlesdes(face):
   valeur = random.randint(1,face)
   return valeur

question1 = str(input("Voulez-vous rouler les dès?"))

if question1 == "oui":
   question2 = int(input("Combien de face voulez-vous?"))
   de = roulerlesdes(question2)
   print(de)
   if de == question2:
      print("gagné")
   else: 
      print ("perdu")


if question1 == "non": 
   print ("vous ne voulez pas jouer")