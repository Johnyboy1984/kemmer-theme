# Kemmer Theme

[![Validate](https://github.com/Johnyboy1984/kemmer-theme/actions/workflows/validate.yaml/badge.svg)](https://github.com/Johnyboy1984/kemmer-theme/actions/workflows/validate.yaml)
[![Im Marketplace öffnen](https://my.home-assistant.io/badges/marketplace_repository.svg)](https://my.home-assistant.io/redirect/marketplace_repository/?owner=Johnyboy1984&repository=kemmer-theme&category=theme)

Eigenständiges Home-Assistant-Theme mit Petrol-Akzent, ruhigen Oberflächen und Hell-/Dunkelmodus. Version 0.1.0.

## Vorschau

Die folgenden Bilder zeigen die Theme-Farben mit fiktiven Beispieldaten. Es sind **schematische Vorschaubilder**, keine Screenshots einer HA-Installation; individuelle Karten können anders aussehen.

### Hell

![Kemmer Theme: heller Modus](docs/preview-light.svg)

### Dunkel

![Kemmer Theme: dunkler Modus](docs/preview-dark.svg)

## Gestaltung

- Heller Modus: kühles Grau, weiße Karten und dunkler Text.
- Dunkler Modus: blaugraue Flächen und heller Petrol-Akzent.
- 16-px-Kartenrundungen, feine Ränder, keine zusätzlichen Kartenschatten.
- Native Statusfarben der Geräte bleiben erhalten; Warnungen werden nicht pauschal durch die Akzentfarbe ersetzt.
- Keine externen Schriftarten, Bilder, JavaScript oder card-mod-Abhängigkeit.

## Installation

Kopiere `themes/kemmer_theme.yaml` in deinen HA-Konfigurationsordner, z. B. nach `themes/kemmer/kemmer_theme.yaml`.

Falls noch nicht eingerichtet:

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

Bestehende frontend-Einstellungen zusammenführen, keinen zweiten frontend-Block anlegen. Bei bereits aktiviertem Theme-Verzeichnis genügt die Aktion `frontend.reload_themes`. Anschließend im Benutzerprofil **Kemmer Theme** auswählen und Hell/Dunkel testen. Das bisherige Theme bleibt parallel verfügbar. Dashboard- oder Kartenangaben mit `theme: Google Theme` überschreiben die Profilauswahl und müssen für einen Vergleich gezielt angepasst werden.

## Marketplace / HACS

Die Struktur mit themes-Ordner und hacs.json ist vorbereitet. Installation als benutzerdefiniertes Theme-Repository ist vorgesehen; die Aufnahme in einen offiziellen Katalog ist damit nicht verbunden.

## Prüfung und Grenzen

YAML-Struktur und Textkontraste werden mit `python validate.py` geprüft (PyYAML erforderlich). Haupt- und Sekundärtext müssen mindestens 4,5:1 gegen die Kartenfläche erreichen. Noch keine visuelle Prüfung in einer laufenden HA-Installation. Benutzerdefinierte Karten können eigene Farben und Layouts verwenden. Einige Frontend-Variablen sind versionsabhängig. Zielversion: HA 2026.11.

## Herkunft und Lizenz

Eigenständig erstellte Theme-Definition; kein Fork und kein übernommener Quellcode des Google Themes von JuanMTech. Kein Google-Logo, keine Google-Schrift oder sonstigen fremden Medien enthalten. Keine Verbindung zu Google oder zum Home-Assistant-Projekt. MIT-Lizenz, siehe LICENSE.
