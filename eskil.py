# Poengsummen starter på 0 og øker etter hvert valg
poeng = 0

print("Situasjon 1: Silje og Elias")
print("Uenighet om teknologivalg og design har utviklet seg fra en sakskonflikt til en personkonflikt.")
print(" - Silje mener løsningen Elias foreslår vil låse brukeropplevelsen og hindre innovasjon.")
print(" - Elias mener Siljes forslag er urealistisk, usikkert og for kostbart.")
print("Hvordan bør Erling håndtere konflikten mellom Silje og Elias?")
print("A: Felles møte - begge får forklare synspunktene sine.")
print("B: Individuelle samtaler - Erling snakker med dem hver for seg.")
print("C: Utsette konflikten - la dem jobbe videre og håpe det løser seg.")

#input() venter på at brukeren skriver noe.
# .strip() fjerner mellomrom, .upper() gjør "a" om til "A"
valg1 = input("Ditt valg (A/B/C): ").strip().upper()

# Spør på nytt helt til brukeren skriver et gyldig svar
while valg1 not in ["A", "B", "C"]:
    valg1 = input("Ugyldig valg. Skriv A, B eller C: ").strip().upper()

# if/elif/else bestemmer hva som skjer ut fra valget
if valg1 == "A":
    print("Silje og Elias får lagt fram sine syn. Det blir litt tøft, men det forstår hverandre bedre.")
    poeng = poeng + 2
elif valg1 == "B":
    print("Samtalene demper temperaturen, og begge føler seg hørt.")
    poeng = poeng + 2
else:
    print("konflikten ulmer videre, og stemnningen i teamet blir dårligere.")
    poeng = poeng + 1

print ("Situasjon 2: Den ulmende saken")
print ("Etter den første konflikten oppdager Erling uenighet mellom Hamdi og Hallgeir. Hva bør Erling gjøre?")
print ("De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter:")
print (" - Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform.")
print (" - Hallgeir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.")
print ("A: Felles møte - De diskuterer behovene sine og prøver å finne en løsning.")
print ("B: Samtaler og felles plan - Erling snakker med begge og lager en plan som tar hensyn til begge.")
print ("C: La dem prøve å finne en løsning på egen hånd.")

valg2 = input("Ditt valg (A/B/C): ").strip().upper()

while valg2 not in ["A", "B", "C"]:
    valg2 = input("Ugyldig valg. Skriv A, B eller C: ").strip().upper()

if valg2 == "A":
    print("Møtet gir dem en bedre forståelse av hverandre, og de finner en løsning som fungerer for begge.")
    poeng = poeng + 2
elif valg2 == "B":
    print("Erling hjelper dem med å lage en plan som tar hensyn til begge, og de føler seg hørt.")
    poeng = poeng + 2
else: 
    print("De prøver å finne en løsning, men ender opp med å misforstå hverandre og konflikten eskalerer.")
    poeng = poeng + 1

print("Situasjon 3")
print("Nå nærmer fristen seg, og teamet er fortsatt preget av konfliktene. Hva bør Erling prioritere?")
print("A: Fokus på samarbeid, tillit og sosiale aktiviteter.")
print("B: Arbeidsplan og oppfølging - Lage tydelig plan fordele ansvar og følge opp teamet.")
print("C: Fokus på leveransen - Prioritere fremdrift og utsette arbeidet med konfliktene.")

valg3 = input("Ditt valg (A/B/C): ").strip().upper()

while valg3 not in ["A", "B", "C"]:
    valg3 = input ("Ugyldig valg. Skriv A, B eller C: ").strip().upper()

if valg3 == "A":
    print("Teamet får bedre samarbeid og tillit, og de håndterer konfliktene bedre.")
    poeng = poeng + 2
elif valg3 == "B":
    print("Teamet får en tydelig plan og ansvar, og de jobber mer effektivt sammen.")
    poeng = poeng + 2
else:
    print("Teamet fokuserer på leveransen, men konfliktene fortsetter å påvirke samarbeidet negativt.")
    poeng = poeng + 1

print("=== Resultat ===")
print("Din poengsum:", poeng)

if poeng == 6:
    print("Slutt 1: Godt samarbeid! Teamet gjenoppretter tilliten og prosjektet går videre.")
elif poeng >= 4:
    print("Slutt 2: Delevis løsning Noen konflikter står igen, men prosjektet fortsetter.")
else:
    print("Slutt 3: Prosjektet er i fare. Konfliktene kan føre til forsinkelser.")