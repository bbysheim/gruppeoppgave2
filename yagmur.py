#Konflikt 1

tid = 100
kvalitet = 0

print("\nProsjektelederen Erling er ansvalrig for utviklingen av kommunens nye digtal medborgerportal")


print("\nTeamet består av"
      

    "\n1.Erling = Prosjektleder"
    "\n2.Sivert og Elias = It rådgiver"
    "\n3.Silje = UI/UX designer"
    "\n4.Hamdi = Representant for kulturavdeling, ansvarlig for inngyggerdialog & kommunikasjon"
    "\n5.Marcia = Politisk rådgiver"
    "\n6.Noa og Marcia = Sikkerhetekseprt og ansavrlig for databeskytelse & personvern"
    "\n7.Hallgeir og Jabir = Brukerepresentant")



print("\nI starten var stemingen god. Teamet opplevde høy motivasjon og felleskap i målet om å lage en medborgerportal for komunen, men nå etter seks uker har prosjektet gått dårlig og ulike preferanser kommer frem")

print("uenigheten om teknologivalg og design har utviklet seg til en personkonflikt (storming fasen")
print()

print("Konflikt 1")
print("silje mener løsningen Elias foreslår vil låse brukeeropplevelsen og hindre innovasjon")
print("Elias mener siljes forslag er urelaistisk, usikker og for kostbart")
print()

valgmulighet_1 = "Erling snakker med Silje og Elias i plenum for å skape åpenhet i Teamet"
valgmulighet_2 = "Erling tar individuelle samtaler, for å dempe temperaturen"
valgmulighet_3 = "Erling tar seg en profosjonel og skalig tilnærming og derfor kontkater han HR teamet for å sikre en nøytral håndtering"
valgmulighet_4 = "Erling mener at Silje og Elias bortkaster tid og ødelegger for resten av teamet og derfor gir han Elias og Silje sparken"
print("\nHva skal Erling gjøre her?")

print(f"1.{valgmulighet_1}")
print(f"2.{valgmulighet_2}")
print(f"3.{valgmulighet_3}")
print(f"4.{valgmulighet_4}")

while True:
    valgkonflikt_1 = int(input("\nHvilket valg tar du, skriv et tall mellom 1-4: "))


    if valgkonflikt_1 < 1 or valgkonflikt_1 > 4:
        print("Ugyldig nummer. Skriv et tall mellom 1 & 4 ")
    else:
        break

if valgkonflikt_1 == 1:
    print(f"\nDu bestemte for at {valgmulighet_1}")
    kvalitet += 10
    tid -= 10
    print("kvalitet +10, tid -10")


elif valgkonflikt_1 == 2:
    print(f"\ndu bestemte for at {valgmulighet_2}")
    kvalitet += 7
    tid -= 7
    print(" kvalitet +7, tid -7")

elif valgkonflikt_1 == 3:
    print(f"\nDu bestemte for at {valgmulighet_3}")
    kvalitet += 5
    tid -= 5
    print("kvalitet +5, tid -5")


elif valgkonflikt_1 == 4:
    print(f"\nDu bestemte for at {valgmulighet_4}")
    kvalitet -= 15
    tid -= 25
    print("kvalitet -15, tid-25")


#konflikt 2
print("\nkonflikt 2")
print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksiterende platform")
print("Hallgeir ønsker et mer åpent, dialogbasert system med rom for spontante inspill")


print("\nuenigheten i teamet er ikke intenst til nå, men prosjketlederen erling merker at uenigheten i teamet vokser. Prosjktet bwggyner å nørme seg")
print("Første prototype nærmer seg!!!!!!")


valg_1 = "Erling tar intiativ til et felles møte for å avklare uenigheter"
valg_2 = "Erling avventer og håper at partene finner en løsning selv"
valg_3 = "Erling sjekker datoen, det er 19 november. GTA 6 HAR KOMMET UT!!!!!, han kjøper PS5 og GTA 6 til kontoret og alle spiller GTA 6 sammen"


print(f"1.{valg_1}")
print(f"2.{valg_2}")
print(f"3.{valg_3}")

while True:
    valgkonflikt_2 = int(input("Skriv et tall mellom 1-3 "))

    if valgkonflikt_2 < 1 or valgkonflikt_2 > 3:
        print("Ugyldig tall. Skriv et tall mellom 1 & 3!!!!!! ")
    else:
        break

if valgkonflikt_2 == 1:
    print(f"\nDu bestemte for at {valg_1}")
    kvalitet += 10
    tid -= 10
    print("Kvalitet +10, tid -10")

elif valgkonflikt_2 == 2:
    print(f"\nDu bestemte for at {valg_2}")
    kvalitet -=5
    tid += 10
    print("Kvalitet -5, tid +10")

elif valgkonflikt_2 == 3:
    print(f"\nDu bestemte for at {valg_3}")
    kvalitet -= 15
    tid -= 25
    print("Kvalitet -15, tid -25")




#Beslutningspunkt 3: motivasjon


print("\nBeslutningspunkt 3: Motivasjon")
print("Erling må bestmme om hvordan han skal bevare motivasjoen i teamet som helhet")


valgmotivasjon_1 = "Erling setter tid til Relasjonsbygging og sosiale aktiviteter for å gjenoprette tillit"
valgmotivasjon_2 = "Erling pririterer fremdrift og leveranse for å holde fokus på resultatet?"


print(f"\n1.{valgmotivasjon_1}")
print(f"2.{valgmotivasjon_2}")

while True:
    valgmotivasjon = int(input("Hvilket valg skal han ta (Velg et tall mellom 1-2 "))

    if valgmotivasjon < 1 or valgmotivasjon > 2:
        print("Ugyldig nummer. Skriv et tall mellom 1-2")
    else:
        break


if valgmotivasjon == 1:
    print(f"Du bestemte for at {valgmotivasjon_1}")
    kvalitet += 5
    tid -= 5
    print("Kvalitet +10, tid -10")

elif valgmotivasjon == 2:
    print(f"Du bestemte for at {valgmotivasjon_2}")
    kvalitet -= 5
    tid += 5
    print("kvalitet -5, tid +10")



#Sluttresultat
print(f"\nSluttresultat: Tid = {tid}, kvalitet = {kvalitet}")

if kvalitet >= 20 and tid <= 90:
    print("\n ENDEPUNKT 1")
    print("For å håndtere konflikten mellom Elias og Silje velger prosjektlederen Erling å ta det opp i plenum, med håp om å skape åpenhet i teamet, danne fellesskap i gruppa og unngå at folk i teamet holder tilbake informasjon.")
    print("Når det gjelder konflikten mellom Hamdi og Hallgeir, bestemmer Erling å ta initiativ slik at konflikten ikke utvikler seg, og hindrer at spenningen mellom dem blir til en åpen konflikt.")
    print("For å bevare motivasjonen i teamet som helhet setter Erling av tid til relasjonsbygging og sosiale aktiviteter, slik at folk blir trygge med hverandre og bygger tillit.")
    print("Som et resultat av disse valgene går teamet fra storming-fasen til norming-fasen. Nå får teamet muligheten til å bygge tillit, forbedre kommunikasjonen og styrke samarbeidet, men det ble brukt mindre tid på selve prosjektet, og prosjektet har blitt forsinket.")



elif kvalitet >= -4:
    print("\nENDEPUNKT 2")
    print("I den første konflikten velger prosjektlederen Erling å ta individuelle samtaler med partene i konflikten mellom Silje og Elias. Han inviterer begge til et møte der partene tar en og en samtale med prosjektlederen.")
    print("Dette sørger for at prosjektlederen får muligheten til å høre ulike perspektiver, men risikerer at han ikke får høre sannheten, dersom den ene kan lyve om den andre.")
    print("Når det gjelder konflikten mellom Hamdi og Hallgeir velger Erling å avvente og satse på at begge finner en løsning selv. Her risikerer Erling at konflikten ikke blir løst mellom dem, noe som kan påvirke teamet negativt.")
    print("I dette endepunktet prioriterer Erling fremdrift og leveranser for å holde fokus på resultatet. Det fører til at teamet får tydelig fokus på oppgaven som må fullføres innen fristen, men konflikten mellom Silje og Elias er bare delvis løst, mens konflikten mellom Hamdi og Hallgeir fortsatt ikke er løst.")


else:
    print("\nENDEPUNKT 3")
    print(
        "For å løse konflikten mellom Silje og Elias forsøker prosjektlederen å ta en profesjonell tilnærming, og viderekobler dermed begge partene til HR-avdelingen for å sikre en nøytral håndtering.")
    print("Når det gjelder konflikten mellom Hamdi og Hallgeir, bestemmer Erling seg for å vente på at partene finner en løsning selv. Erling håper at alle i teamet er fokusert på hovedoppgaven, og at det ikke oppstår tidsforsinkelser.")
    print("Erling prioriterer fremdrift og leveranser for å holde fokus på sluttproduktet, og prøver å unngå å ta ansvar for å opprettholde relasjonene i teamet.")
    print("I dette endepunktet blir prototypen ferdig utviklet i tide, men konflikten mellom de ulike partene er ikke løst, og selve kvaliteten i medborgerportalen er ikke så veldig bra.")