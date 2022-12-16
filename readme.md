# Mathekalender 2022

## Aufgabe 1
mit Blatt Papier gelöst

## Aufgabe 2
Brute force durchprobiert in python:
```
a=10, b=15, c=40, d=80
a=10, b=20, c=40, d=75
a=10, b=25, c=40, d=70
a=10, b=30, c=40, d=65
a=10, b=35, c=40, d=60
```
Es gibt 5 Möglichkeiten

## Aufgabe 3
Erste Teilaufgabe  
Wahrscheinlichkeiten:
```
1* 1/2 * 2/3 * ... * 11/12 = 1/12
```
Zweite Teilaufgabe  
Wahrscheinlichkeiten: 
```
1+1/2+...+1/12 =  3.1 ~ 3
```
## Aufgabe 4
[Beweis](4/beweis.md) 

## Aufgabe 5
Eine Lösung mit sieben Vergleichen ist: 
0-1,1-2,2-0, 3-4,4-5,5-3, 6-7 die Reihenfolge ist egal und wird durch den folgenden Graph ausgedrückt:

<img src="5/result.png" alt="drawing" width="400"/>

[Programm zum Berechnen der Strategie ](5/bf.py) und zum Nachweis, dass es keine Lösung mit 5 Vergleichen gibt.
[Beschreibung Algorithmus](5/description.md)
### Erklärung zur Lösung

In den Dreierklicken kann maximal eine rote Lampe vorhanden sein, in der zweierklicke ebenfalls. Bei 4 roten Lampen ist mindestens eine dieser Bedingungen verletzt.

## Aufgabe 6
[Programm](6/run.py)

## Aufgabe 7
<img src="7/cube.png" alt="drawing" width="400"/>

Man kann sich leicht überlegen, dass die Seiten des Würfels alle wie A und B oder Rotationen von A und B aussehen.

Folgende Überlegung zur Anzahl von Würfeln:
Ein grüner Würfel in einer Ecke muss auf genau drei Seitenflächen vorkommen, deshalb können wir auf jeder Seitenfläche für jedes Eckquadrat 1/3 zählen. In der Mitte einer Seitenfläche zählen wir 1/2 weil jeder Mittel-Rand-Würfel auf genau zwei Flächen vorkommen muss. Das Mittelquadrat zählt einfach.

Angenommen wir können eine Würfel bilden der auf allen Seitenflächen wie A aussieht dann haben wir 
6 * 2 2/3 = 16 grüne Päckchen. Weniger geht nicht.

Angenommen wir können einen Würfel bilden der nur
aus Seitenflächen B besteht und wir wählen den Würfel in der Mitte des Kubus, der nicht auf einer Seitenfläche sichtbar ist als grünen Würfel, dann haben wir 1 + 6*3 = 19 grüne Päckchen , mehr geht nicht.

Damit sind wir eigentlich schon fertig, es müssen auf jeden Fall 16 oder mehr und 19 oder wenige grüne Päckchen sein - alle anderen Lösungen machen keinen Sinn.

Man müsste jetzt eigentlich noch zeigen, dass es auch möglich ist eine reale Päckchenkombination mit den Flächen A und B zu erzeugen. Man sieht das leicht hier (und könnte natürlich auch hier einfach zählen und kommt auf dieselben Zahlen):

### Würfel mit nur Flächen von Typ A
<img src="7/a.png" alt="drawing" width="400"/>

### Würfel mit nur Flächen von Typ B
tbd

### Link auf Brute Force Programm
[Programm](7/wuerfel.py)
### Lösung
```
16 <= # gruene Päckchen <= 19
```
## Aufgabe 8
[Notizen](8/8.md)

# Aufgabe 9
Antowrt Nr. 7: [Programm](9/9.py)

# Aufgabe 10

# Aufgabe 11
Heisshunger: [Aufgabe](11/MK-2022-HS-Heisshunger-de.pdf)

Lösung: Nr. 4 [Rechnungen dazu](11/mathe-advent-wahrscheinlichkeiten.pdf)
# Aufgabe 12

# Aufgabe 13
Schokoladenspiel: [Aufgabe](13/MK-2022-PR-Schokoladenspiel-de-1.pdf)

Lösung: Nr 10. [Programm zur Simulation mit min-max](13/board.py)

Empirisch: Lösung Nr. 10

Strategie für quadratische Felder ist klar, für 2xn Felder auch

Allgemeine Strategie noch nicht beschreibbar - Simulation findet win Situation für Felder kleiner als 6x4 rechnerisch gerade noch möglich, danach dauert es zu lange
(evtl. noch Programm auf dynamische Programmierung umstellen)


# Aufgabe 14
Rentiere im Gehege: [Aufgabe](14/MK-2022-KH-ReindeerBreeding-de-1.pdf)

Lösung: Nr. 9

# Aufgabe 15
Verlorene Wunschzettel: [Aufgabe](15/MK-2022-Griesbach-Wunschzettel-de.pdf)

Lösung: Nr. 9, [Programm](15/15.py)

Ausgabe des Programms:
```
2535 ['0-1,t:10,c:250', '1-6,t:17,c:250', '6-5,t:25,c:1500', '1-2,t:37,c:2055', '0-4,t:47,c:2055', '4-3,t:48,c:2535']
```
D.h. mit dem angegebenen Weg haben wir im Durchschnitt 25.35 Stunden.

# Aufgabe 16
Weihnachtsbaum: [Aufgabe](16/MK-2022-BW-Weihnachtsbaum-de.pdf)

Lösung: Nr 3 = 8 Lichter müssen angemacht werden.

Rechnerische Lösung [Prog](16) von der Komplexität für 6,7 oder 8 Züge zu komplex (rechnerisch aufwändig)
Begründung: 
Folgendes Skizze zeigt eine Lösung:

<img src="16/loesung-mit-8.png" alt="drawing" width="400"/>

Beweisidee, dass nichts besseres möglich ist:

Angenommen die ausgefüllten Felder bedecken ein nxm Rechteck. Durch ein zusätzliches Licht kann entweder ein n+1 x m+1 Rechteck gefüllt werden oder man kann ein n x m+2 oder n+2 x m Rechteck füllen. Da man in beide Richtungen 8 Felder benötigt sind dann 8 Lichter nötig....