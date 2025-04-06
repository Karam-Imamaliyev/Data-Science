import pandas as pd

# ------------------------------
# 🔷 STRATEGIE-MUSTER
# ------------------------------

class RisikoStrategie:
    def entscheidung(self, score):
        raise NotImplementedError()

class KatastrophenStrategie(RisikoStrategie):
    def entscheidung(self, score):
        return [
            "⚠️ KATASTROPHENALARM – GESETZLICHE MASSNAHMEN SOFORT!",
            "   BEFEHL: CO2-Ausstoß um 50% reduzieren, Waldfläche ausbauen."
        ]

class HohesRisikoStrategie(RisikoStrategie):
    def entscheidung(self, score):
        return [
            "⚠️ HOHES RISIKO – WENDEPUNKT ERREICHT.",
            "   BEFEHL: Sofortige Investitionen in erneuerbare Energie."
        ]

class InstabilStrategie(RisikoStrategie):
    def entscheidung(self, score):
        return [
            "⚠️ INSTABILE LAGE – VORSICHT!",
            "   BEFEHL: Notfallpläne und Klimagesetze aktivieren."
        ]

class StabilStrategie(RisikoStrategie):
    def entscheidung(self, score):
        return [
            "✅ STABIL – BEREITSCHAFT BEWAHREN.",
            "   BEFEHL: Bestehende Maßnahmen weiterführen und überwachen."
        ]

def strategie_auswaehlen(score):
    if score > 130:
        return KatastrophenStrategie()
    elif score > 100:
        return HohesRisikoStrategie()
    elif score > 80:
        return InstabilStrategie()
    else:
        return StabilStrategie()


# ------------------------------
# 🔷 LÄNDERANALYSE-KLASSE
# ------------------------------

class LandAnalyse:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.strategie = strategie_auswaehlen(score)

    def anzeigen(self):
        print(f"\n📍 {self.name.upper()} (Risiko-Score: {self.score:.2f})")
        entscheidungen = self.strategie.entscheidung(self.score)
        for line in entscheidungen:
            print(line)


# ------------------------------
# 🔷 DATENLADUNG & BERECHNUNG
# ------------------------------

def lade_risiken(pfad: str):
    df = pd.read_csv(pfad)

    # Strip und Quotes entfernen aus Country-Namen
    df['Country'] = df['Country'].str.strip().str.replace("'", "").str.replace('"', '')

    # Risiko-Score berechnen
    df['DER_KING_RISK_SCORE'] = (
        df['Extreme_Weather_Events'] * 2 +
        (100 - df['Forest_Area_pct']) * 1.5 +
        df['CO2_Emissions_tons_per_capita'] * 3
    )

    # Land: Score
    return df.groupby('Country')['DER_KING_RISK_SCORE'].mean().to_dict()


# ------------------------------
# 🔷 INTERAKTIVER MODUS
# ------------------------------

def interaktiv_starten(score_dict):
    print(f"\n ENTSCHEIDUNGSMASCHINE AKTIV – {len(score_dict)} Länder geladen.\n")

    while True:
        eingabe = input("Gib ein Land ein auf Englisch (oder 'exit' zum Beenden): ").strip()
        if eingabe.lower() == 'exit':
            print("Verabschiedet sich.")
            break

        land = eingabe.strip().replace("'", "").replace('"', '')
        if land in score_dict:
            analyse = LandAnalyse(land, score_dict[land])
            analyse.anzeigen()
        else:
            print("Land nicht gefunden.")
            auswahl = input("Willst du verfügbare Länder sehen? (Y/N): ").strip().lower()
            if auswahl == 'y':
                print("\n Verfügbare Länder:")
                for i, l in enumerate(sorted(score_dict.keys()), 1):
                    print(f"{i:>2}. {l}")



# ------------------------------
# 🔷 HAUPTPROGRAMM
# ------------------------------

if __name__ == "__main__":
    try:
        score_dict = lade_risiken("temperature.csv")
        interaktiv_starten(score_dict)
    except Exception as e:
        print("SYSTEMFEHLER:", str(e))
