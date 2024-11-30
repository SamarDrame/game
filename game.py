import random
def roulerlesdes(face):
   valeur = random.randint(1,face)
   return valeur

question1 = str(input("Voulez-vous rouler les dès?"))
question2 = int(input("Combien de face voulez-vous?"))


if question1 == "oui":
   patate = roulerlesdes(question2)
   print(patate)
   if patate == question2:
      print(gagné)
