# Gruppeoppgave 2 - IS-118. Høsten 2026
# Interaktiv historiefortelling om Erling sitt prosjektarbeid.
# 
# 
def hent_valg(alt_a, alt_b):
    """Viser to alternativer og spør til brukeren svarer A eller B."""
    print("  A) " + alt_a)
    print("  B) " + alt_b)
    while True:
        svar = input("Ditt valg (A/B): ").strip().upper()
        if svar == "A" or svar == "B":
            return svar
        # Ugyldig input: historien står stille til vi får et gyldig svar
        print("Ugyldig valg. Skriv A eller B.")


# variabler
valg1 = "" # silje & elias
valg2 = "" # hamdi & hallgeir
valg3 = "" # motivasjon i teamet
tillit = "" # tillit i teamet
fremdrift = "" # fremdrift i teamet

# ---------- Introduksjon ----------
print("=" * 60)
print("        ERLING OG MEDBORGERPORTALEN")
print("=" * 60)
print()
 
# litt kunst =)
print(r"    o     " * 6)
print(r"   /|\    " * 6)
print(r"   / \    " * 6)
print("  Silje   " + "  Elias   " + "  Hamdi   " + "Hallgeir  " + " Marcia   " + "   Noa    ")
print()
 
# 
# r foran teksten gjør at \ skrives ut som et vanlig tegn.
print(" " * 29 + "O")
print(" " * 28 + r"/|\ ")
print(" " * 27 + r"/ | \ ")
print(" " * 29 + "|")
print(" " * 28 + r"/ \ ")
print(" " * 27 + r"/   \ ")
print(" " * 26 + "ERLING")
print()
 
# Introduksjonstekst
print("Det har gått seks uker siden du, Erling, samlet prosjektteamet.")
print("Stemningen var god i starten, men nå krangler Silje og Elias")
print("om teknologi og design, og det ulmer mellom Hamdi og Hallgeir.")
print("Første prototype skal være klar om tre uker.\n")
 
# Pause slik at spilleren rekker å lese før første valg
input("Trykk Enter for å starte...\n")
 
# ---------- Beslutningspunkt 1: Silje og Elias ----------
print("--- Beslutning 1: Konflikten mellom Silje og Elias ---")
valg1 = hent_valg(
    "Ta individuelle samtaler med begge for å dempe temperaturen.",
    "Ta saken opp i plenum for å skape åpenhet.",
)
 
if valg1 == "A":
    print("\nSilje og Elias føler seg hørt, og tonen i teamet blir roligere.")
    print("Men det tar tid, og prototypen risikerer å bli forsinket.")
    tillit = tillit + 2
else:
    print("\nDiskusjonen i plenum blir hard, men alle får sagt sitt.")
    print("Teamet vet nå hvor uenigheten ligger, og arbeidet går raskere.")
    tillit = tillit + 1
    fremdrift = fremdrift + 1
 
# ---------- Beslutningspunkt 2: Hamdi og Hallgeir ----------
print("\n--- Beslutning 2: Uenigheten mellom Hamdi og Hallgeir ---")
valg2 = hent_valg(
    "Kall inn til et felles møte for å avklare uenighetene.",
    "Avvent og håp at de finner en løsning selv.",
)
 
if valg2 == "A":
    print("\nHamdi og Hallgeir finner et kompromiss: en kontrollert")
    print("plattform med en egen åpen kanal for spontane innspill.")
    tillit = tillit + 2
else:
    print("\nSaken blir liggende. Frustrasjonen vokser i det stille,")
    print("men du får brukt tiden på å følge opp prototypen.")
    fremdrift = fremdrift + 1
 
# ---------- Beslutningspunkt 3: Motivasjonen i teamet ----------
print("\n--- Beslutning 3: Motivasjonen i teamet ---")
valg3 = hent_valg(
    "Sett av tid til relasjonsbygging og sosiale aktiviteter.",
    "Prioriter fremdrift og leveranser for å holde fokus på resultatet.",
)
 
if valg3 == "A":
    print("\nEn felles middag gjør at teamet snakker sammen på nytt.")
    tillit = tillit + 2
else:
    print("\nTeamet leverer, men noen føler seg oversett og slitne.")
    fremdrift = fremdrift + 2
 
# ---------- Avslutning: tre mulige utfall ----------
print("\n" + "=" * 50)
print("UTFALL")
print("=" * 50)
 
if tillit >= 5:
    # Utfall 1: høy tillit
    print("Teamet gjenoppretter tillit og går videre til norming-fasen.")
    print("Prototypen blir godt mottatt av bystyret.")
elif tillit >= 3:
    # Utfall 2: middels tillit
    print("Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
    print("Prototypen leveres, men nye konflikter kan oppstå.")
else:
    # Utfall 3: lav tillit
    print("Prosjektet mister samhold og forsinkes.")
    if fremdrift >= 3:
        print("Prototypen blir levert, men teamet er utslitt og splittet.")
    else:
        print("Prototypen er ikke klar til fristen.")
 
# Oppsummering av valgene som ble lagret underveis
print("\nDine valg: " + valg1 + ", " + valg2 + ", " + valg3)
print("Tillit: " + str(tillit) + " | Fremdrift: " + str(fremdrift))