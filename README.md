# ProgettoIA
## Componenti del gruppo
- **Masri Omar** (879237)
- **Piazza Lorenzo** (886010)
## Domande
- Calcolare la dimensione dello spazio degli stati in funzione di n e M.
  - Siccome la matrice è una matrice $n\times n$ e abbiamo $M$ veicoli (dove $M \leq n$) e questi devono tutti trovarsi in caselle differenti in ogni possibile stato allora la dimensione dello spazio degli stati risulta la M-permutazione su $n\times n$ ovvero $P^{n \times n}_M$ 
 $$\frac{(n \times n)!}{(n \times n - M)!}$$
- Calcolare il fattore di ramificazione in funzione di n e M
	- Essendo il fattore di ramificazione una stima superiore dei nodi figlio per ogni nodo dell'albero, e siccome ad ogni passo temporale, ognuno degli M veicoli può muoversi di una casella con una delle seguenti 5 azioni $a$:
		1. In Alto		($\uparrow$)
		2. In Basso		($\downarrow$)
		3. A Sinistra	($\leftarrow$)
		4. A Destra		($\rightarrow$)
		5. Rimanere Fermi	($\circ$)

		quindi questo risulta: $$5^M$$
- Definire un’euristica ammissibile focalizzata sul singolo obiettivo
   - Definizione del problema sul singolo obiettivo: Definiamo come problema sul singolo obiettivo il problema in cui la matrice $n \times n$ contiene un singolo veicolo
   - Definizione di **ammissibile**: Un'euristica $h$ **ammissibile** è un'euristica che non sovrastima mai il costo atteso, ed è quindi ottimista. 
	
	- Se definiamo la funzione costo $c$ come:  
```math
 c(k, a, k')= \begin{cases} 1 & \ (\circ) \\ 1 & \  (( \uparrow ) \lor  (\downarrow) \lor (\leftarrow) \lor (\rightarrow)) \ senza\ salti \\ 1 & \  (( \uparrow ) \lor  (\downarrow) \lor (\leftarrow) \lor (\rightarrow)) \ effettuando\ un \ salto \end{cases} 
 ```
E un'euristica $h$ come la **distanza di Manhattan** tra la posizione attuale di del veicolo e la sua destinazione finale, questa risulta ammissibile.
- **PROOF** dell'ammissibilità: restringendo il problema al singolo obbiettivo, nella matrice $n \times n$ abbiamo un solo veicolo. Quindi la distanza di Manhattan risulta ammissibile in quanto il veicolo non può eseguire salti, e inoltre seguirà solamente i "passi" di Manhattan o rimarrà fermo, di conseguenza questa non andrà mai a sovrastimare il path cost.
	- Quindi dato $k=(x_1, y_1)$ e dato il goal $g'= (x_2, y_2)$ relativo al singolo obiettivo nello stato goal $g$ l'euristica $h$ risulta: $$h(k) = \lvert x_1 - x_2 \lvert +\lvert y_1-y_2 \lvert $$

- Costruire un euristica complessiva combinando quelle dei singoli veicoli
	- Per definire un'euristica complessiva $H$ basta sommare le euristiche focalizzate sui singoli veicoli: 
	$H:S \longrightarrow \mathbb{N}$ $$H(s) = \sum_{i =1}^{M}{h(s_i)}\ \ t.c.\ s_i\ posizione\ del\ veicolo\ i$$
	- Un'euristica $h$ è **consistente** se vale la seguente disuguaglianza triangolare: per ogni nodo $k$ e ogni suo successore $k'$ generato dall'azione $a$ abbiamo: $$h(k) \leq c(k, a, k') + h(k')$$ quindi ogni euristica **consistente** è **ammissibile** (ma non viceversa).
Se un'euristica è **consistente** allora trova la soluzione ottimale per A*.
- **PROOF** della consistenza: Essendo il problema non più focalizzato sul singolo obiettivo nella matrice $n \times n$ possiamo avere più di un veicolo, di conseguenza è possibile che vengano anche eseguiti dei salti. 
Abbiamo quindi due casi:
	- Non vengono eseguiti salti: Nel caso in cui non vengano eseguiti salti è possibile ricondursi al caso focalizzato sul singolo veicolo $k$ per ogni veicolo nella matrice infatti:
		- nel caso facessimo una mossa in una qualsiasi direzione, avremmo che $h(k) \leq 1 + h(k')$ dove $c(k, a, k')=1$ per come è definita la funzione di costo (una qualsiasi mossa ha costo 1) e $h(k') = h(k) - 1$ in quanto $h(k')$ diminuirà dato che il veicolo ci si avvicinerà al goal e la distanza di Manhattan, quindi la funzione euristica $h$ diminuirà di conseguenza.
		- nel caso rimanesse fermo, avremmo che $h(k) \leq 1 + h(k)$
	- Vengono eseguiti salti: Nel caso venga eseguito un salto consideriamo due veicoli adiacenti $a$ e $b$, per far si che $a$ possa saltare $b$ necessariamente $b$ deve rimanere fermo e nessun altro veicolo può saltare $b$ se non $a$ per definizione del problema. Sia $a'$ è lo stato risultante dopo che $a$ ha eseguito il salto otteniamo che $h(a) + h(b) \leq h(a') + h(b) + 2$ dato che $h(a') = h(a) - 2$, e essendo $b$ rimasto fermo la sua euristica non varierà ma verra aggiunto il costo dell'azione ($\circ$) cioè 1. Quindi sostituendo risulta: $$h(a) + h(b) \leq h(a) - 2 + h(b) + 2$$ cioè $$h(a) + h(b) \leq h(a) + h(b)$$
## Definizione del problema
- Spazio degli stati $S$
	- Matrice $n \times n$ dove $M$ delle celle devono essere occupate dagli $M$ veicoli, dove una cella può contenere al massimo un solo veicolo
- Stato iniziale $s' \in S$
	- $M$ veicoli occupano caselle da $(1,1)$ a $(n,1)$
- Azioni $A:S \longrightarrow \Omega$
	- ognuno degli M veicoli può muoversi di una casella con una delle seguenti 5 azioni $\Omega$:
		1. In Alto		($\uparrow$)
		2. In Basso		($\downarrow$)
		3. A Sinistra	($\leftarrow$)
		4. A Destra		($\rightarrow$)
		5. Rimanere Fermi	($\circ$)

		Se ci troviamo in una cella "di bordo" le uniche azioni consentite sono quelle che non portano il veicolo out of bound
		
- Modello di transizione $R: S \times \Omega \longrightarrow S$
	- Se usiamo ($\uparrow$) un veicolo si muove in alto di una cella
	- Se usiamo ($\downarrow$) un veicolo si muove in basso di una cella
	- Se usiamo ($\leftarrow$) un veicolo si muove a sinistra di una cella
	- Se usiamo ($\rightarrow$) un veicolo si muove a destra di una cella
	- Se usiamo ($\circ$) un veicolo non si muove e rimane fermo nella stessa cella

		Se un veicolo rimane fermo, un altro veicolo adiacente (ma non più di uno) può saltarci sopra e fare uno spostamento maggiore
- Goal $g \in S$
	- I veicoli devono essere spostati nella fila superiore ma in ordine inverso; quindi il veicolo i che inizia in (i,1) deve finire in (n−i+1,n)
- Costo Azioni $C : S \times \Omega \times S \longrightarrow \mathbb{N}$
	- definiamo la funzione costo $C$ come: 
```math
 C(s, a, s')= \sum_{i=1}^{M}{c(k_i, a, k_i')} \ t.c. \ k_i \in s \ \wedge \ k_i' \in s'
 ```

## Algoritmi
Dati $b$ il branching factor, $d$ il la profondità massima e $\beta$ la beam width
| |A*|IDA*|Beam Search|
|:---:|:---:|:---:|:---:|
| Spazio | $O(b^d)$|$O(d)$|$O(\beta)$|
| Tempo | $O(b^d)$|$O(b^d)$|$O(\beta^d)$|
| Ottimale | $\checkmark$|$\checkmark$|✘|
| Completo | $\checkmark$ |$\checkmark$|✘|

Definiamo un algoritmo:
- **Ottimale** quando trova sempre la soluzione ottimale
- **Completo** quando trova sempre una soluzione (se esiste)

### A*
L'algoritmo A* è un algoritmo di ricerca informata utilizzato per la ricerca su grafi al fine di individuare un percorso ottimale da un nodo iniziale a un nodo obiettivo. Basandosi su una tecnica chiamata "stima euristica", valuta e classifica ogni nodo in base a una stima della migliore strada che passa attraverso quel nodo. L'algoritmo A* segue questa stima euristica per determinare l'ordine di visita dei nodi durante la ricerca. È considerato un esempio di ricerca best-first.
A* utilizza come funzione di valutazione $f(n)=g(n) + h(s)$ dove:
- $g(n)$ è il path cost dallo stato iniziale fino allo stato n (stato attuale) 
- $h(s)$ è una funzione euristica che da una stima utile a capire dove si trova il goal.

### IDA*
Iterative deepening A* (nota anche con l'acronimo IDA*) è un algoritmo euristico introdotto da Richard Korf nel 1985. Il suo scopo è quello di trovare il percorso minimo da un nodo iniziale a ciascuno dei nodi soluzione in un grafo pesato.

Questo algoritmo rappresenta una variante dell'iterative deepening depth-first search (ricerca in profondità con incremento iterativo) utilizzata per ottimizzare le prestazioni di A*. Il principale vantaggio di IDA* risiede nell'uso di memoria lineare, a differenza di A*, che può richiedere uno spazio esponenziale nel peggiore dei casi. Tuttavia, va notato che IDA* utilizza una quantità limitata di memoria, che potrebbe essere sfruttata per migliorare le prestazioni in termini di tempo.

### Beam search
L'algoritmo beam search adotta una strategia di ricerca in ampiezza per costruire il suo albero di ricerca. Ad ogni livello di profondità dell'albero, l'algoritmo genera tutti i successori dei nodi correnti, organizzandoli in modo tale che i valori della funzione euristica siano disposti in ordine crescente. Tuttavia, a differenza della best-first search, beam search salva solo un numero predefinito, indicato come "beam width", di stati "migliori" per ogni livello. Maggiore è l'ampiezza predefinita, minore sarà il numero di stati esclusi dalla ricerca. In teoria, impostando l'ampiezza a infinito nessuno stato verrebbe escluso e il comportamento dell'algoritmo sarebbe identico a quello di una best-first search. Limitare l'ampiezza massima predefinita aiuta a controllare i requisiti di memoria per l'esecuzione di questa ricerca. Tuttavia, l'algoritmo non offre garanzie di completezza o ottimalità della soluzione.

L'ampiezza può anche essere resa variabile. Un approccio possibile consiste nel far partire l'algoritmo con ampiezza impostata al valore minimo e, in caso di mancata individuazione di una soluzione, aumentare gradualmente il valore ad ogni nuova esecuzione.

ROBE IN PIù
Sistema definizione di C
Sistemare tab
