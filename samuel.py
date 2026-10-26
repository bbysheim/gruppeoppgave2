# Individuell løsning: Erlings prosjektteam
# Poengsummen viser hvor mye valgene støtter tillit og samarbeid.

print("ERLING OG DEN DIGITALE MEDBORGERPORTALEN")
print("Seks uker inn i prosjektet opplever teamet flere uenigheter.")
print("Den første prototypen skal være klar om tre uker. Erling må ta tre beslutninger.\n")

score = 0

# Beslutning 1: Silje og Elias
print("BESLUTNING 1: Hvordan bør Erling håndtere konflikten mellom Silje og Elias?")
print("A. Arrangere et møte der begge kan forklare synspunktene sine. (+2 poeng)")
print("B. Snakke med dem hver for seg. (+2 poeng)")
print("C. Utsette konflikten og håpe at de løser den selv. (+1 poeng)")

choice1 = input("Velg A, B eller C: ").strip().lower()
while choice1 not in ("a", "b", "c"):
    choice1 = input("Ugyldig valg. Skriv A, B eller C: ").strip().lower()

if choice1 == "a":
    print("Begge forklarer perspektivene sine og kan få bedre forståelse for hverandre.")
    score += 2
elif choice1 == "b":
    print("Begge får snakke med Erling hver for seg. Et felles oppfølgingsmøte kan fortsatt være nødvendig.")
    score += 2
else:
    print("De fortsetter arbeidet, men den uløste konflikten kan påvirke neste diskusjon.")
    score += 1

# Beslutning 2: Hamdi og Hallgeir
print("\nBESLUTNING 2: Hvordan bør Erling håndtere uenigheten om digitale folkemøter?")
print("A. Arrangere et felles møte for å diskutere behovene deres. (+2 poeng)")
print("B. Snakke med begge og lage en felles plan som tar hensyn til begge perspektivene. (+2 poeng)")
print("C. La dem prøve å finne en løsning selv. (+1 poeng)")

choice2 = input("Velg A, B eller C: ").strip().lower()
while choice2 not in ("a", "b", "c"):
    choice2 = input("Ugyldig valg. Skriv A, B eller C: ").strip().lower()

if choice2 == "a":
    print("De diskuterer behovene sine og prøver å bli enige om en løsning.")
    score += 2
elif choice2 == "b":
    print("Erling hjelper dem med å lage en plan som balanserer struktur og åpen dialog.")
    score += 2
else:
    print("De får ansvar for å løse saken selv, men uenigheten kan fortsette.")
    score += 1

# Beslutning 3: Motivasjon og prototypfristen
print("\nBESLUTNING 3: Hva bør Erling prioritere når fristen nærmer seg?")
print("A. Styrke relasjonene gjennom samarbeid og sosiale aktiviteter. (+2 poeng)")
print("B. Lage en arbeidsplan, avklare ansvar og følge opp teamet. (+2 poeng)")
print("C. Fokusere på leveransene og utsette arbeidet med konfliktene. (+1 poeng)")

choice3 = input("Velg A, B eller C: ").strip().lower()
while choice3 not in ("a", "b", "c"):
    choice3 = input("Ugyldig valg. Skriv A, B eller C: ").strip().lower()

if choice3 == "a":
    print("Teamet får tid til å styrke tilliten og forbedre kommunikasjonen.")
    score += 2
elif choice3 == "b":
    print("Teamet får tydelige oppgaver, ansvarsområder og oppfølging.")
    score += 2
else:
    print("Teamet fokuserer på leveransene, men uløste konflikter kan svekke samarbeidet.")
    score += 1

# Total poengsum avgjør hvilken av de tre avslutningene spilleren får.
print("\nSLUTTRESULTAT")
print(f"Samarbeidspoeng: {score} av 6")

if score == 6:
    print("Slutt 1: Godt samarbeid. Teamet gjenoppretter tilliten og går videre sammen.")
elif score >= 4:
    print("Slutt 2: Konfliktene løses delvis. Noen utfordringer gjenstår, men prosjektet fortsetter.")
else:
    print("Slutt 3: Prosjektet er i fare. Konfliktene kan svekke teamet og føre til forsinkelser.")
