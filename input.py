import json 

data=open('tatortrechts.json')
json.load(data)

ort=input("Bitte gebe hier den Ort ein (z.b. Dortmund, Dorstfeld): ")

datum=input("Bitte gebe hier das Datum ein (TT.MM.JJJ): ")

titel=input("Beschreib in ein paar Worten, was passiert ist. Z. B. 'Hakenkreuz an Schulwand gesprüht': ")

beschreibung=input("Erzähl in ein paar Sätzen, worum es geht. Z. B. 'In der XY Schule ist eine unbekannte Person dabei beobachtet worden, wie sie ...: ")




tatort_rechts_dict = {
     "Vorfall": {
         "ort": ort,
         "datum": datum,
         "Titel": titel,
         "Beschreibung": beschreibung
         }
}



data=json.dumps(tatort_rechts_dict,  indent=4 )


