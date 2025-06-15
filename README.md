# KN-Python
Team-A6 | Hotelreservierungssystem

## Autoren

Kendric Scoles



## Ressourcen

https://deepnote.com/workspace/Fachhochschule-Nordwestschweiz-Bachelor-Business-AI-8a7f9eed-981d-4902-9a28-e7a9a4e7820c/project/AnwendungsentwicklungmitPythonScolesLardinois-Duplicate-87d0d38b-da6f-4a15-8815-f6371a6d7983/notebook/Notebook-1-08f61a8664af47b4b24dfbb243c4cea2



# User Stories

## Minimale User Stories

Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit ich dasjenige auswählen kann, welches meinen Wünschen entspricht. Wünsche sind: 1.1. Ich möchte alle Hotels in einer Stadt durchsuchen, damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann. 1.2. Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen. 1.3. Ich möchte alle Hotels in einer Stadt durchsuchen, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung). 1.4. Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date) und "bis" (check_out_date)) Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe. 1.5. Ich möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne. 1.6. Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.
Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen, einschliesslich der maximalen Anzahl von Gästen für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine fundierte Entscheidung zu treffen. 2.1. Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis. 2.2. Ich möchte nur die verfügbaren Zimmer sehen, sofern ich meinen Aufenthalt (von – bis) spezifiziert habe.
Als Admin des Buchungssystems möchte ich die Möglichkeit haben, Hotelinformationen zu pflegen, um aktuelle Informationen im System zu haben. 3.1. Ich möchte neue Hotels zum System hinzufügen 3.2. Ich möchte Hotels aus dem System entfernen 3.3. Ich möchte die Informationen bestimmter Hotels aktualisieren, z. B. den Namen, die Sterne usw.
Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.
Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.
Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice.
Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann. Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.
Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.
Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.
Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat. Hint: Stammdaten sind alle Daten, die nicht von anderen Daten abhängen.
User Stories mit DB-Schemaänderung

## Mindestens zwei der folgenden User Stories auswählen:

Als Admin möchte ich alle Buchungen bearbeiten können, um fehlende Informationen zu ergänzen (z.B. Telefonnummer).
Als Gast möchte ich auf meine Buchungshistorie zuzugreifen ("lesen"), damit ich meine kommenden Reservierungen verwalten kann. 2.1. Die Anwendungsfälle für meine Buchungen sind "neu/erstellen", "ändern/aktualisieren", "stornieren/löschen".
Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.
Als Gast möchte ich vor der Buchung Hotelbewertungen lesen, damit ich das beste Hotel auswählen kann.
Als Gast möchte ich für jeden Aufenthalt Treuepunkte sammeln, die ich dann für Ermässigungen einlösen kann. Hint: Nur häufige Gäste sollten Treuepunkte erhalten. Definieren Sie eine Regel, um häufige Gäste zu identifizieren.
Als Gast möchte ich meine Buchung mit der von mir bevorzugten Zahlungsmethode bezahlen, damit ich meine Reservierung abschliessen kann.
User Stories mit Datenvisualisierung

## Eine der folgenden User Stories auswählen:

Als Admin möchte ich die Belegungsraten für jeden Zimmertyp in meinem Hotel sehen, damit ich weiss, welche Zimmer am beliebtesten sind und ich meine Buchungsstrategien optimieren kann. Hint: Wählt ein geeignetes Diagramm, um die Auslastung nach Zimmertyp darzustellen (z. B. wie oft jeder Zimmertyp gebucht wird).
Als Admin möchte ich eine Aufschlüsselung der demografischen Merkmale meiner Gäste sehen, damit ich gezieltes Marketing planen kann. Hint: Wählt ein geeignetes Diagramm, um die Verteilung der Gäste nach verschiedenen Merkmalen darzustellen (z. B. Altersspanne, Nationalität, wiederkehrende Gäste). Möglicherweise müssen Sie der Tabelle „Gäste“ einige Spalten hinzufügen.
Optionale User Stories

Als Admin möchte ich die Gesamteinnahmen meines Hotels sehen, damit ich die finanzielle Leistung des Hotels analysieren kann. 1.1. Zeigt die Gesamteinnahmen (Revenue) an, die sich aus allen Buchungen für einen bestimmten Zeitraum ergeben. 1.2. Eine zeitliche Aufschlüsselung (z. B. Umsatz nach Monat, Quartal, Jahr) bereitstellen. Hint: Füge eine Trendlinie ein, um zu veranschaulichen, wie sich die Einnahmen im Laufe der Zeit verändern.
Als Gastnutzer möchte ich die Details meiner Reservierung in einer lesbaren Form erhalten (z.B. die Reservierung in einer dauerhaften Datei speichern), damit ich meine Buchung später überprüfen kann. Hint: Erzeugt eine «booking.txt»-Datei oder verwendet die Python-Bibliothek «fpdf» oder eine ähnliche Library, um eine PDF-Version zu erzeugen.
Als Gastnutzer möchte ich eine Karte mit Zoom- und Filterfunktion sehen können, welche Sehenswürdigkeiten oder Restaurants in der Nähe meines gebuchten Hotels liegen, um meine Aufenthaltsplanung zu erleichtern. Hint: Verwende die Python-Bibliothek «geopandas» oder eine ähnliche.
Als Gastnutzer möchte ich ein Zimmer buchen und eine Buchungsbestätigung mit allen Details per E-Mail erhalten, um einen verbindlichen Nachweis meiner Reservierung zu haben. Hint: Verwende die Python-Bibliothek «smtplib» oder eine ähnliche.
