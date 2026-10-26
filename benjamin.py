# Gruppeoppgave 2 - IS-118. Høsten 2026
# Interaktiv historiefortelling om Erlings prosjektarbeid.
#
# Spillet har tre beslutningspunkter med to valg hver. Valgene lagres i
# variabler, og poengene for tillit og fremdrift avgjør hvilket utfall
# spilleren får til slutt.


# ---------- Hjelpefunksjoner ----------

def hent_valg(alt_a, alt_b):
    """Viser to alternativer og spør til brukeren svarer A eller B."""
    print("  A) " + alt_a)
    print("  B) " + alt_b)

    while True:
        svar = input("Ditt valg (A/B): ").strip().upper()

        if svar in ("A", "B"):
            return svar

        # Ugyldig input: spør på nytt til vi får A eller B
        print("Ugyldig valg. Skriv A eller B.")


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
    "Tillit og fremdrift er poengene som følger deg gjennom historien.",
    "Tillit gjør at teamet tåler motgang. Fremdrift gjør at prototypen",
    "blir levert i tide. Hvert valg gir tillit, fremdrift eller begge.",
    "Før du velger, får du vite hva slags konsekvenser alternativene",
    "kan ha. Velg med omhu.",
]
for linje in intro:
    print(linje)
print()

input("Trykk Enter for å starte...\n")


# ---------- Variabler som lagrer valg og poeng underveis ----------
valg1 = ""       # Silje og Elias
valg2 = ""       # Hamdi og Hallgeir
valg3 = ""       # Motivasjon i teamet

tillit = 0       # Tillit i teamet
fremdrift = 0    # Fremdrift i prosjektet


# ---------- Beslutningspunkt 1: Silje og Elias ----------
vis_beslutning(
    "BESLUTNING 1: Konflikten mellom Silje og Elias",
    ["Silje", "Elias"],
    [
        "Silje og Elias krangler om design og teknologi. Diskusjonen",
        "har blitt personlig, og begge henter støtte hos sine nærmeste.",
        "",
        "Mulige konsekvenser:",
        "  - Individuelle samtaler kan dempe konflikten og bygge tillit,",
        "    men prototypen kan bli forsinket.",
        "  - Plenum gir åpenhet og fremdrift, men konflikten kan bli",
        "    hardere før den blir bedre.",
        "",
        "Hva gjør du?",
    ],
)

valg1 = hent_valg(
    "Ta individuelle samtaler med begge for å dempe temperaturen.",
    "Ta saken opp i plenum for å skape åpenhet.",
)

if valg1 == "A":
    print("\nSilje og Elias føler seg hørt, og tonen i teamet blir roligere.")
    print("Men det tar tid, og prototypen risikerer å bli forsinket.")
    tillit += 2
else:
    print("\nDiskusjonen i plenum blir hard, men alle får sagt sitt.")
    print("Teamet vet nå hvor uenigheten ligger, og arbeidet går raskere.")
    tillit += 1
    fremdrift += 1


# ---------- Beslutningspunkt 2: Hamdi og Hallgeir ----------
vis_beslutning(
    "BESLUTNING 2: Uenigheten mellom Hamdi og Hallgeir",
    ["Hamdi", "Hallgeir"],
    [
        "Hamdi vil ha en kontrollert løsning på kommunens plattform.",
        "Hallgeir vil ha et åpent system for spontane innspill.",
        "Spenningen mellom dem øker.",
        "",
        "Mulige konsekvenser:",
        "  - Et felles møte kan avklare uenighetene og gi tillit,",
        "    men det tar tid og kan bli ubehagelig.",
        "  - Å vente gir fremdrift nå, men frustrasjonen kan vokse.",
        "",
        "Hva gjør du?",
    ],
)

valg2 = hent_valg(
    "Kall inn til et felles møte for å avklare uenighetene.",
    "Avvent og håp at de finner en løsning selv.",
)

if valg2 == "A":
    print("\nHamdi og Hallgeir finner et kompromiss: en kontrollert")
    print("plattform med en egen åpen kanal for spontane innspill.")
    tillit += 2
else:
    print("\nSaken blir liggende. Frustrasjonen vokser i det stille,")
    print("men du får brukt tiden på å følge opp prototypen.")
    fremdrift += 1


# ---------- Beslutningspunkt 3: Motivasjonen i teamet ----------
vis_beslutning(
    "BESLUTNING 3: Motivasjonen i teamet",
    ["Silje", "Elias", "Hamdi", "Hallgeir", "Marcia", "Noa"],
    [
        "Stemningen er spent i hele teamet. Prototypen nærmer seg,",
        "og flere føler seg slitne.",
        "",
        "Mulige konsekvenser:",
        "  - Tid til relasjonsbygging og sosiale aktiviteter gir tillit,",
        "    men tar tid fra arbeidet med prototypen.",
        "  - Fokus på leveranser gir fremdrift, men noen kan føle seg",
        "    oversett og utslitt.",
        "",
        "Hva gjør du?",
    ],
)

valg3 = hent_valg(
    "Sett av tid til relasjonsbygging og sosiale aktiviteter.",
    "Prioriter fremdrift og leveranser for å holde fokus på resultatet.",
)

if valg3 == "A":
    print("\nEn felles middag gjør at teamet snakker sammen på nytt.")
    tillit += 2
else:
    print("\nTeamet leverer, men noen føler seg oversett og slitne.")
    fremdrift += 2


# ---------- Avslutning: Tre mulige utfall ----------
print("\n" + "=" * 60)
print("UTFALL")
print("=" * 60)

if tillit >= 5:
    # Utfall 1: Høy tillit
    print("Teamet gjenoppretter tillit og går videre til norming-fasen.")
    print("Prototypen blir godt mottatt av bystyret.")

elif tillit >= 3:
    # Utfall 2: Middels tillit
    print("Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
    print("Prototypen leveres, men nye konflikter kan oppstå.")

else:
    # Utfall 3: Lav tillit. Fremdrift avgjør om prototypen rekker fristen.
    print("Prosjektet mister samhold og forsinkes.")

    if fremdrift >= 4:
        print("Prototypen blir levert, men teamet er utslitt og splittet.")
    else:
        print("Prototypen er ikke klar til fristen.")


# Oppsummering 
print("\nDine valg: " + valg1 + ", " + valg2 + ", " + valg3)
print(f"Tillit: {tillit} | Fremdrift: {fremdrift}")