# -*- coding: utf-8 -*-
"""
IS-118: Gruppeinnlevering 2 - Høst 2026
Gruppeoppgave: Interaktiv storyline for prosjektleder Erling
Filnavn: master.py
"""

def vis_introduksjon():
    print("=" * 70)
    print("         VELKOMMEN TIL DEN INTERAKTIVE HISTORIEN OM IS-118")
    print("=" * 70)
    print("Det har gått seks uker siden Erling samlet sitt tverrfaglige prosjektteam")
    print("for å utvikle kommunens nye digitale medborgerportal.")
    print("Energien var høy i starten, men nå har teamet truffet 'storming-fasen'.")
    print("Faglige uenigheter har personifisert seg, og tidsfristen nærmer seg!")
    print("-" * 70)
    print("Du spiller som prosjektleder Erling. Dine valg vil avgjøre om teamet")
    print("kollapser i stormen, eller navigerer trygt videre mot 'norming'.")
    print("=" * 70)
    input("\nTrykk ENTER for å starte spillet...")


def hent_bruker_valg():
    """Henter og validerer input fra brukeren for å sikre en flytende historie."""
    while True:
        valg = input("Ditt valg (A, B eller C): ").strip().upper()
        if valg in ['A', 'B', 'C']:
            return valg
        print("Ugyldig valg! Vennligst tast inn enten A, B eller C.")


def spill_historie():
    total_poeng = 0
    
    # --- BESLUTNINGSPUNKT 1 ---
    print("\n\n=== SITUASJON 1: KONFLIKTEN MELLOM SILJE OG ELIAS ===")
    print("Silje (UX) og Elias (IT) krangler intenst om teknologi og design.")
    print("Diskusjonene har blitt emosjonelle og splitter teamet i to leire.")
    print("\nHva gjør du som prosjektleder?")
    print("A) Kaller inn til et felles møte i plenum for å skape full åpenhet.")
    print("B) Tar individuelle samtaler med hver av dem for å dempe temperaturen.")
    print("C) Utsetter konflikten, ber dem fokusere på oppgavene og la det gå seg til.")
    print("-" * 50)
    
    valg1 = hent_bruker_valg()
    
    if valg1 == 'A':
        print("\n-> Konsekvens: Møtet blir opphetet, men fasiliteringen din gjør")
        print("   at de endelig lytter til hverandres faglige argumenter.")
        total_poeng += 2
    elif valg1 == 'B':
        print("\n-> Konsekvens: Gjennom separate samtaler roer gemyttene seg.")
        print("   Både Silje og Elias føler seg hørt av deg, og tilliten bygges opp.")
        total_poeng += 2
    else: # C
        print("\n-> Konsekvens: Stillheten sprer seg, men konflikten ulmer videre.")
        print("   Klikkdannelsen forsterkes i korridorene bak din rygg.")
        total_poeng += 1

    input("\nTrykk ENTER for å gå til neste situasjon...")

    # --- BESLUTNINGSPUNKT 2 ---
    print("\n\n=== SITUASJON 2: DEN ULMENDE SAKEN MELLOM HAMDI OG HALLGEIR ===")
    print("Du oppdager en voksende, lavmælt frustrasjon angående digitale folkemøter.")
    print("Hamdi ønsker en strengt kontrollert kommunal løsning.")
    print("Hallgeir krever et helt åpent, dialogbasert system for innbyggerne.")
    print("\nHva gjør du?")
    print("A) Arrangerer et felles møte for å drøfte de ulike behovene åpent.")
    print("B) Tar samtaler med begge og utarbeider en felles plan som kombinerer begge deler.")
    print("C) Lar dem løse det selv på egen hånd, siden uenigheten foreløpig er lavmælt.")
    print("-" * 50)
    
    valg2 = hent_bruker_valg()
    
    if valg2 == 'A':
        print("\n-> Konsekvens: Dere får kartlagt rammene tidlig, noe som hindrer")
        print("   at uenigheten eskalerer til en unødvendig personkonflikt.")
        total_poeng += 2
    elif valg2 == 'B':
        print("\n-> Konsekvens: Du finner et godt kompromiss. Teamet opplever")
        print("   at tverrfaglighet faktisk fører til bedre og mer robuste løsninger.")
        total_poeng += 2
    else: # C
        print("\n-> Konsekvens: Frustrasjonen vokser i det skjulte. Samarbeidsklimaet")
        print("   blir enda mer anspent ettersom ingen skjærer igjennom.")
        total_poeng += 1

    input("\nTrykk ENTER for å gå til siste situasjon...")

    # --- BESLUTNINGSPUNKT 3 ---
    print("\n\n=== SITUASJON 3: MILEPÆLEN NÆRMER SEG ===")
    print("Det er nå bare uker igjen til første fungerende prototype skal presenteres.")
    print("Teamet bærer tydelig preg av de siste ukers gnisninger og turbulente klima.")
    print("\nHva velger du å prioritere i innspurten?")
    print("A) Relasjonsbygging. Vi setter av tid til sosiale aktiviteter for å gjenreise tillit.")
    print("B) Arbeidsplan og oppfølging. Lage knallhårde strukturer, roller og tette tidsfrister.")
    print("C) Fokus på leveransen. Vi presser på fremover og ignorerer alt av interne gnisninger.")
    print("-" * 50)
    
    valg3 = hent_bruker_valg()
    
    if valg3 == 'A':
        print("\n-> Konsekvens: Teamet finner tilbake til smilet og motivasjonen.")
        print("   Dette gir fornyet energi inn i det faglige arbeidet.")
        total_poeng += 2
    elif valg3 == 'B':
        print("\n-> Konsekvens: Tydelig retning gir trygghet i oppgavene.")
        print("   Alle vet nøyaktig hva de skal gjøre de neste kritiske ukene.")
        total_poeng += 2
    else: # C
        print("\n-> Konsekvens: Teamet jobber under høyt press. Stresset øker,")
        print("   og det faglige resultatet preges av hastverksarbeid.")
        total_poeng += 1

    input("\nSpillet er over! Trykk ENTER for å se resultatene og lagret poengsum...")

    # --- AVSLUTNING / EVALUERING BASERT PÅ POENGSUM ---
    print("\n" + "=" * 70)
    print(f"                     SLUTTRESULTAT (Total poengsum: {total_poeng}/6)")
    print("=" * 70)
    
    if total_poeng == 6:
        print("SLUTT 1: GODT SAMARBEID")
        print("Gratulerer! Du har håndtert lederutfordringene på en glimrende måte.")
        print("Teamet har lagt stormingen bak seg og beveget seg inn i 'norming-fasen'.")
        print("Tilliten er fullt gjenopprettet, og dere leverer en fantastisk prototype i tide!")
    elif 4 <= total_poeng <= 5:
        print("SLUTT 2: DELVIS LØSNING")
        print("Prosjektet berges i havn, og en brukbar prototype blir levert.")
        print("Men håndteringen din har etterlatt noen uavklarte spenninger i teamet.")
        print("Relasjonene er fortsatt sårbare, og du må bruke mye tid på mekling fremover.")
    else: # 3 poeng
        print("SLUTT 3: PROSJEKTET ER I FARE")
        print("Strategien med å unngå problemene slo feil ut.")
        print("Konfliktene har eskalert totalt, klikkene motarbeider hverandre, og samholdet er brutt.")
        print("Prosjektet opplever en kritisk forsinkelse, og styringsgruppen må kalles inn.")
    
    print("=" * 70)
    print("Takk for at du spilte!")

if __name__ == "__main__":
    vis_introduksjon()
    spill_historie()