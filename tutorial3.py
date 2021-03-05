
print("das ist ein Potenziomat.")

base_num= int(input("Gib die Zahl ein die du potenzieren willst: "))
expo_num= int(input("Gib die Potenz ein um die du deine Zahl potenzieren willst: "))

def raise_to_power(base_num, expo_num):
    result = 1
    for index in range(expo_num):
        result= base_num * result
    return result

print("Das Ergebnis ist: ", raise_to_power(base_num,expo_num))
