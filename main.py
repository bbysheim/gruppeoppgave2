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
valg1 = ""
