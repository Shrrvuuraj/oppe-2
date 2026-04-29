age=int(input("age :"))

def eligible(age):
     if (age>=18):
          return "eligible"
     else:
          return "ineleigible"

eligible=eligible(age)
print(eligible)