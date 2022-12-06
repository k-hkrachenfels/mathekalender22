# Beweis

Anmerkung: der Beweis vereinfacht sich, wenn man immer das am weitesten links stehende Pakete verschickt. Man muss dann nur noch die Fälle
```
      P (P u)
      P (P u)
      P (D g)
      P (D g)
```
betrachten (siehe unten).


Für jede Anfangsreihe von Geschenken mit einer ungeraden Anzahl von ordentlich verpackten Geschenken ist es möglich alle zu verschicken.

Die Behauptung gilt für alle Reihen mit Länge 1:
```
P -> -
```

Als Notation verwenden wir die Buchstaben g für Ketten mit gerader Anzahl von Ps oder mit 0 Ps.
Wir verwenden u für alle Ketten mit ungerader Anzahl an Ps.

# Beweis über vollständige Induktion

Angenommen die Annahme gilt für Ketten der Länge n.

Dann gilt sie auch für Ketten der Länge n+1.

## Beweis

Ketten der Länge n+1 können wie folgt aufgeschrieben werden:
```
g P g
```
schreiben, wobei die Ketten g eine Länge zwischen 0 und n-1 haben können.

Es gibt folgende Unterfälle:
```
(u P) P (P u)
(g D) P (P u)
(u P) P (D g)
(g D) P (D g)
(u P) P 
(g D) P 
(u P) P 
(g D) P 
      P (P u)
      P (P u)
      P (D g)
      P (D g)
#todo
(g P) P (P g)
(u D) P (D u)
```
die sich wie folgt weiterentwickeln lassen:
```
(u P) P (P u) -> (u D) - (D u)
(g D) P (P u) -> (g P) - (D u)
(u P) P (D g) -> (u D) - (P g)
(g D) P (D g) -> (g P) - (P g)
(u P) P       -> (u D) - 
(g D) P       -> (g P) - 
(u P) P       -> (u D) - 
(g D) P       -> (g P) - 
      P (P u) ->       - (D u)
      P (P u) ->       - (D u)
      P (D g) ->       - (P g)
      P (D g) ->       - (P g)
```
zu zeigen ist also, dass Ketten der Länge <= n
der Formen `u D`, `D u`, `P g`, `g P` auflösbar/reduzierbar sind. (Damit ist gemeint dass sie sich in Ketten die nur aus - bestehen auflösen lassen)

## Beweis für `u D`
Falls es für u (mit Länge <=n) eine Reduktion gibt,
dann muss diese den Schritt `x1 P -> x2 -` enthalten.
Für die um D erweiterte Kette hat man statt dessen die Produktionen `x1 P D -> x2 - P`, was dann auf der 
rechten Seite in `x2 - - ` weiterentwickelt werden kann. Die Linke seite lässt sich dann weil unser u ja eine Länge kleiner n hatte mit der Induktionsannahme reduzieren, d.h. x2 ist reduzierbar.

## Beweis für `D u`
hier nicht aufgeführt aber analog zu `u D`

## Beweis für `g P`:
Für g gibt es zwei Fälle: 
```
a.) g = u P
b.) g = g D
```
Wir können deshalb `g P` schreiben als
```
a.) u P P
b.) g D P
```
### Betrachtung für Fall a.
Wir können wie folgt reduzieren
```
u P P -> u D - 
```
und `u D` können wir wie oben bewiesen reduzieren.
### Betrachtung für Fall b.
Wir können wie folgt reduzieren
```
g D P -> g P - 
```
`g P` ist eine Kette mit ungerader Anzahl an Ps und Länge <=n dann nach Induktionsannahme reduzierbar.

## Beweis für `P g` analog zu `g P`

#Damit sind alle Ketten mit Länge n+1 reduzierbar, qed

# Beispiele für Längen 2 und 3
und Ketten mit Länge 2:
```
P D -> - P -> - -
D P -> P - -> - -
```
und Ketten mit Länge 3:
```
P D D -> - P D -> - - P -> - - -
D P D -> P - P -> - - -
D D P -> D P - -> P - - -> - - -
P P P -> - D P -> - P - -> - - -
```





