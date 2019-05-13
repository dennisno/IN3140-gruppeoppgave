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
tidspunkter i filen det finnes en *beat*. Den publiserer dette til **/planner/delta_beat**,
og antallet meldinger den kommer til å sende til **/planner/controller_max_points**.
Videre publiserer den også til **/player/set_music** for å sette hva slags musikk som er planlagt.

Player
------
Player spiller musikk, og får info om hvilken musikk den skal spille fra **/player/set_music**,
og den subscriber også til **/player/start_music** for å vite når den skal starte musikken.

Point-to-point
------
*Denne brukes til å regne ut punkter som skal sendes til InverseKinematic, men erstattes av bypass_move. Se under for mer info.*
Point-to-point subscriber til **/planner/delta_beat** og får dermed &Delta; Time inn som den kalkulerer et punkt den vil til, før den publisher dette til **/mapper/point_delta** som lyttes til av en node som skal kalkulere hvilke vinkler leddene skal stå i.

InverseKinematic
------
*Dessverre er inverskinematikken ikke helt funksjonell. Eller, den kjører, men gir helt gale vinkler for hvert punkt den tar inn. Noden er er skrevet for en robot som har andre instillinger for 0-vinkler enn det som er default i gazebo-roboten. I utgangspunktet trenger vi den strengt tatt ikke uansett, og siden vi fikk litt dårlig tid, er den derfor ikke ferdigstillt.*  
InverseKinematic regner ut hvilke vinkler hvert ledd må ha for å komme til punktene vi setter til hver beat. Den subscriber til **/mapper/point_delta** hvor den får inn hvilke punkter vi vil nå, og publisher til **/inverse/joint_angles**.

Bypass_move
------
Denne noden erstatter inverskinematikken, ved at den bare regner ut de neste vinklene basert på enkel trigonometri. Den lytter til **/planner/delta_beat**, og setter sammen meldinger av typen *Delta_angles* som inneholder koordinater og tiden roboten har på å komme seg dit. Dette
publiserer den til **/inverse/joint_angles**.

Path_planner
------
Path_planner tar inn alle vinkeloppsett som blir sent gjennom **/inverse/joint_angles**, dette lagrer den inn i et trajectory som den videre utfører bevegelsen på robotarmen når den har fått hele meldingen. Den lytter til kanalen **/planner/controller_max_points** for å finne ut av hvor mange meldinger den kommer til å få. Det er også Path_planner som publiserer til **/player/start_music**, slik at robot-armen er synkronisert til musikken som spilles. 

Tick_queue
------
Tick_queue er en debugg klasse for å lage et printstatement hver gang det er en beat i sangen.
