from director import director

inputt= input("Nach welcher Person suchst du?: ")

rldirector1=director("Einar Schleef", 32, 2013, "HfmT Hamburg", "contemporary", True)

if inputt == rldirector1.name : 
    print(f"Die Regie Person {inputt} ist {rldirector1.age} Jahre alt")
else:
    print("uns ist keine Regieperson mit diesem namen bekannt")