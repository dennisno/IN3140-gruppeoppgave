# IN3140 Gruppeoppgave
Gruppeoppgave for å lage en dansende robot-arm
av Eirik, Elias og Dennis

Dette programmet krever i tillegg til ROS følgende pakker:

Librosa:

*Install på linux med*
``` markdown
pip install librosa
```
*eller på conda med*
``` markdown
conda install -c conda-forge librosa
```

Pyglet:

*Install på linux med*
``` markdown
 pip install pyglet
 ```
*eller på conda med*
``` markdown
 conda install -c conda-forge pyglet
```
BeatPlanner
------
Denne filen tar inn en musikkfil som kjøres gjennom Librosa for å få ut hvilke
tidspunkter i filen det finnes en *beat*. Den publiserer dette til **Point-to-point**.
Videre publiserer den også til **Player** for å starte musikk.

Player
------
Player spiller musikk, og starter ikke å spille musikk før den får ok signal fra
**Point-to-point**, den subscriber også til **TimedMoveQueue** for å vite når den skal starte musikken.

Point-to-point
------
Point-to-point subscriber til **BeatPlanner** og får dermed &Delta; Time inn som den kalkulerer et punkt den vil til, før den publisher dette til **InverseKinematic** for å kalkulere hvilke vinkler leddene skal stå i.

InverseKinematic
------
InverseKinematic regner ut hvilke vinkler hvert ledd må ha for å komme til punktene vi setter til hver beat. Den subscriber til **Point-to-point** hvor den får inn hvilke punkter vi vil nå, og publisher til **Path_planner**.

Path_planner
------
Path_planner tar inn alle vinkeloppsett den mottar, dette lagrer den inn i et trajectory som den videre utfører bevegelsen på robotarmen når den har fått hele meldingen.

Bypass_move
------
bypass_move er en cache av **InverseKinematic** slik at vi ikke trenger å gå igjennom den, siden vi kun bruker noen få konfigurasjoner.

Tick_queue
------
Tick_queue er en debugg klasse for å lage et printstatement hver gang det er en beat i sangen.
