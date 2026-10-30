# Gruppeoppgave 2 - IS-118. Høsten 2026
# Interaktiv historiefortelling om Erlings prosjektarbeid.
#
# Programmet følger storylinen fra del 1:
#   - 3 situasjoner, hver med 3 valg (A, B, C)
#   - Hvert valg gir poeng (A og B gir 2 poeng, C gir 1 poeng)
#   - Totalsummen (3-6 poeng) avgjør hvilken av de 3 slutten du får


# ---------- Hjelpefunksjoner ----------

def hent_valg(alt_a, alt_b, alt_c):
    """Viser tre alternativer og spør til brukeren svarer A, B eller C."""
    print("  A) " + alt_a)
    print("  B) " + alt_b)
    print("  C) " + alt_c)

    while True:
        svar = input("Ditt valg (A/B/C): ").strip().upper()

        if svar in ("A", "B", "C"):
            return svar

        # Ugyldig input: spør på nytt til vi får A, B eller C
        print("Ugyldig valg. Skriv A, B eller C.")


def tegn_figurer(navn):
    """Tegner stickman-figurer med navn under, én figur per navn."""
    bredde = 10  # Plass til hver figur
    print("".join("o".center(bredde) for _ in navn))
    print("".join("/|\\".center(bredde) for _ in navn))
    print("".join("/ \\".center(bredde) for _ in navn))
    print("".join(n.center(bredde) for n in navn))


def tegn_erling(bredde_totalt):
    """Tegner Erling foran de andre, sentrert under figurene."""
    midt = bredde_totalt // 2
    print(" " * midt + "O")
    print(" " * (midt - 1) + "/|\\")
    print(" " * (midt - 1) + "/ \\")
    print(" " * (midt - 3) + "ERLING")
    print()


def vis_beslutning(tittel, navn, tekst):
    """Viser overskrift, figurer og forklaring før et valg."""
    print("\n" + "-" * 60)
    print(tittel)
    print("-" * 60)
    tegn_figurer(navn)
    print()
    tegn_erling(10 * len(navn))
    for linje in tekst:
        print(linje)
    print()


# ---------- Åpning: Erling før jobb ----------
print("=" * 60)
print("")
print("        STORMING ERLING")
print("")
print("=" * 60)
print()

print("En tirsdag morgen sitter Erling på kjøkkenet med en kaffe")
print("han har glemt å drikke. Telefonen summer. Gruppechatten har")
print("vært stille i helgen, men nå står det:")
print()
print('  Silje: "Kan vi snakke om designen i dag?"')
print('  Elias: "Vi må nok snakke om kostnadene først."')
print()
print(r"          ( (")
print(r"           ) )")
print(r"        ........")
print(r"        |      |]")
print(r"        \      /")
print(r"         `----'")
print()
print("Erling sukker, setter fra seg koppen og tar på seg jakken.")
print("Kontoret venter, og prosjektet venter også.")
print()

input("Trykk Enter for å gå på jobb...\n")


# ---------- Introduksjon: problemet Erling står i ----------
tegn_figurer(["Silje", "Elias", "Hamdi", "Hallgeir", "Marcia", "Noa"])
print()
tegn_erling(60)

intro = [
    "Seks uker er gått siden du, Erling, samlet prosjektteamet for",
    "kommunens nye digitale medborgerportal. Portalen skal gjøre det",
    "lettere for innbyggerne å delta i lokaldemokratiet, og vise at",
    "kommunen er åpen og transparent.",
    "",
    "Oppstarten var full av energi, men nå har arbeidet begynt å",
    "sprike. Silje og Elias krangler om teknologi og design, og det",
    "har blitt personlig. Hamdi og Hallgeir er uenige om hvordan",
    "innbyggerne skal kunne delta i digitale folkemøter. Om tre uker",
    "skal første prototype være klar, og bystyret vil se den.",
    "",
    "Du møter tre situasjoner, og i hver av dem velger du hvordan",
    "Erling skal håndtere teamet. Valgene dine gir poeng, og summen",
    "av poengene avgjør hvordan historien ender. Før du velger, får",
    "du vite hva slags konsekvenser alternativene kan ha.",
    "Velg med omhu.",
]
for linje in intro:
    print(linje)
print()

input("Trykk Enter for å starte...\n")


# ---------- Variabler som lagrer valg og poeng underveis ----------
valg1 = ""    # Valg i situasjon 1: Silje og Elias
valg2 = ""    # Valg i situasjon 2: Hamdi og Hallgeir
valg3 = ""    # Valg i situasjon 3: fristen nærmer seg

poeng = 0     # Samlet poengsum som avgjør slutten (3-6 poeng)


# ---------- Situasjon 1: Silje og Elias ----------
vis_beslutning(
    "SITUASJON 1: Konflikten mellom Silje og Elias",
    ["Silje", "Elias"],
    [
        "Silje og Elias krangler om design og teknologi. Diskusjonen",
        "har blitt personlig, og begge henter støtte hos sine nærmeste.",
        "Hvordan bør Erling håndtere konflikten?",
        "",
        "Mulige konsekvenser:",
        "  - Et felles møte lar begge forklare synspunktene sine, men",
        "    kan bli ubehagelig der og da.",
        "  - Individuelle samtaler gir ro og trygghet, men tar tid.",
        "  - Å utsette gir mer tid til arbeid, men konflikten kan vokse.",
        "",
        "Hva gjør du?",
    ],
)

valg1 = hent_valg(
    "Kall inn til et felles møte der begge får forklare synspunktene sine.",
    "Ta individuelle samtaler med Silje og Elias hver for seg.",
    "Utsett konflikten, la dem fortsette å jobbe og håp det løser seg.",
)

if valg1 == "A":
    print("\nSilje og Elias legger frem synspunktene sine, og begge får")
    print("snakke ut. De oppdager at de egentlig vil det samme: en")
    print("portal innbyggerne har lyst til å bruke.")
    poeng += 2
elif valg1 == "B":
    print("\nErling tar en kaffe med hver av dem. Uten publikum tør både")
    print("Silje og Elias å si hva de egentlig mener, og tonen i teamet")
    print("blir roligere.")
    poeng += 2
else:
    print("\nErling lar dem jobbe videre. Det blir stille noen dager, men")
    print("irritasjonen ligger der fortsatt under overflaten.")
    poeng += 1


# ---------- Situasjon 2: Hamdi og Hallgeir ----------
vis_beslutning(
    "SITUASJON 2: Uenigheten mellom Hamdi og Hallgeir",
    ["Hamdi", "Hallgeir"],
    [
        "Etter den første konflikten oppdager Erling uenighet mellom",
        "Hamdi og Hallgeir. Hamdi vil ha en kontrollert løsning på",
        "kommunens plattform. Hallgeir vil ha et åpent system for",
        "spontane innspill. Spenningen mellom dem øker.",
        "",
        "Mulige konsekvenser:",
        "  - Et felles møte kan gi en løsning begge kan leve med,",
        "    men kan bli ubehagelig.",
        "  - Samtaler og en felles plan tar hensyn til begge, men krever",
        "    at Erling bruker tid på hver av dem.",
        "  - Å la dem løse det selv sparer tid, men de kan bli stående",
        "    fast.",
        "",
        "Hva gjør du?",
    ],
)

valg2 = hent_valg(
    "Kall inn til et felles møte der de diskuterer behovene sine.",
    "Snakk med begge og lag en felles plan som tar hensyn til begge.",
    "La dem prøve å finne en løsning på egen hånd.",
)

if valg2 == "A":
    print("\nHamdi og Hallgeir diskuterer behovene sine. Det blir litt")
    print("ubehagelig, men de finner et kompromiss: en kontrollert")
    print("plattform med en egen åpen kanal for spontane innspill.")
    poeng += 2
elif valg2 == "B":
    print("\nErling snakker med begge og lager en plan: Hamdi får")
    print("moderering på plattformen, og Hallgeir får sin åpne kanal.")
    print("Ingen får alt, men begge kan leve med løsningen.")
    poeng += 2
else:
    print("\nHamdi og Hallgeir prøver å finne en løsning selv, men blir")
    print("ikke enige. Frustrasjonen vokser i det stille, og Erling får")
    print("to halvferdige løsninger som ikke passer sammen.")
    poeng += 1


# ---------- Situasjon 3: Fristen nærmer seg ----------
vis_beslutning(
    "SITUASJON 3: Fristen nærmer seg",
    ["Silje", "Elias", "Hamdi", "Hallgeir", "Marcia", "Noa"],
    [
        "Nå nærmer fristen seg, og teamet er fortsatt preget av",
        "konfliktene. Stemningen er spent, og flere føler seg slitne.",
        "Hva bør Erling prioritere?",
        "",
        "Mulige konsekvenser:",
        "  - Relasjonsbygging gir samarbeid og tillit, men tar tid",
        "    fra arbeidet med prototypen.",
        "  - En tydelig arbeidsplan gir struktur og ansvar, men det",
        "    krever tett oppfølging.",
        "  - Fokus på leveransen gir fremdrift, men konfliktene kan",
        "    blusse opp igjen.",
        "",
        "Hva gjør du?",
    ],
)

valg3 = hent_valg(
    "Relasjonsbygging: fokus på samarbeid, tillit og sosiale aktiviteter.",
    "Arbeidsplan og oppfølging: tydelig plan, fordelt ansvar og tett oppfølging.",
    "Fokus på leveransen: prioriter fremdrift og utsett arbeidet med konfliktene.",
)

if valg3 == "A":
    print("\nEn felles middag gjør at teamet snakker sammen på nytt.")
    print("Folk ler, deler frustrasjoner og går hjem med ny energi.")
    poeng += 2
elif valg3 == "B":
    print("\nErling lager en tydelig plan, fordeler ansvaret og følger")
    print("opp hver enkelt. Alle vet hva de skal gjøre, og arbeidet")
    print("blir mer oversiktlig.")
    poeng += 2
else:
    print("\nTeamet jobber hardt mot fristen, men konfliktene er ikke")
    print("løst. Noen føler seg oversett og slitne.")
    poeng += 1


# ---------- Avslutning: Tre mulige utfall ----------
print("\n" + "=" * 60)
print("UTFALL")
print("=" * 60)

if poeng == 6:
    # Slutt 1: Godt samarbeid (6 poeng)
    print("SLUTT 1: Godt samarbeid")
    print()
    print("Teamet gjenoppretter tilliten og prosjektet går videre.")
    print("Prototypen blir godt mottatt av bystyret, og Erling kan")
    print("endelig drikke kaffen mens den fortsatt er varm.")

elif poeng >= 4:
    # Slutt 2: Delvis løsning (4-5 poeng)
    print("SLUTT 2: Delvis løsning")
    print()
    print("Noen konflikter står igjen, men prosjektet fortsetter.")
    print("Prototypen leveres, men relasjonene i teamet er fortsatt")
    print("sårbare, og nye konflikter kan oppstå.")

else:
    # Slutt 3: Prosjektet er i fare (3 poeng)
    print("SLUTT 3: Prosjektet er i fare")
    print()
    print("Konfliktene har ikke blitt løst, og teamet mister samhold.")
    print("Prototypen risikerer å bli forsinket, og bystyret må vente.")


# ---------- Oppsummering ----------
print("\nDine valg: " + valg1 + ", " + valg2 + ", " + valg3)
print(f"Poengsum: {poeng} av 6")