# ProgettoIA
## Componenti del gruppo
- **Masri Omar** (879237)
- **Piazza Lorenzo** (886010)
## Domande
- Calcolare la dimensione dello spazio degli stati in funzione di n e M.
  - Siccome la matrice è una matrice $n\times n$ e abbiamo $M$ veicoli (dove $M \leq n$) e questi devono tutti trovarsi in caselle differenti in ogni possibile stato allora la dimensione dello spazio degli stati risulta la M-combinazione su $n\times n$ ovvero $C^{n \times n}_M$ 
 $$\binom{n \times n}{M} = \frac{(n \times n)!}{M!(n \times n - M)!}$$
- Calcolare il fattore di ramificazione in funzione di n e M
	- Essendo il fattore di ramificazione una stima superiore dei nodi figlio per ogni nodo dell'albero, e siccome ad ogni passo temporale, ognuno degli M veicoli può muoversi di una casella con una delle seguenti 5 azioni $a$:
		1. In Alto		($\uparrow$)
		2. In Basso		($\downarrow$)
		3. A Sinistra	($\leftarrow$)
		4. A Destra		($\rightarrow$)
		5. Rimanere Fermi	($\circ$)
		6. In Alto		($\uparrow \uparrow$)
		7. In Basso		($\downarrow \downarrow$)
		8. A Sinistra	($\leftarrow \leftarrow$)
		9. A Destra		($\rightarrow \rightarrow$)

		quindi questo risulta: $$5^M$$
- Definire un’euristica ammissibile focalizzata sul singolo obiettivo
	- Un'euristica $h$ **ammissibile** è un'euristica che non sovrastima mai il costo atteso, ed è quindi ottimista. 
	- Un'euristica $h$ è **consistente** se vale la seguente disuguaglianza triangolare: per ogni nodo $k$ e ogni suo successore $k'$ generato dall'azione $a$ abbiamo: $$h(k) \leq c(k, a, k') + h(k')$$ quindi ogni euristica **consistente** è **ammissibile** (ma non viceversa).
Se un'euristica è **consistente** allora trova la soluzione ottimale.
	- Se definiamo la funzione costo $c$ come:  
```math
 c(k, a, k')= \begin{cases} 0 & \ (\circ) \\ 1 & \  (( \uparrow ) \lor  (\downarrow) \lor (\leftarrow) \lor (\rightarrow)) \ senza\ salti \\ 2 & \  (( \uparrow ) \lor  (\downarrow) \lor (\leftarrow) \lor (\rightarrow)) \ effettuando\ un \ salto \end{cases} 
 ```
E un'euristica come la **distanza di Manhattan** tra la posizione attuale di del veicolo e la sua destinazione finale. Ciò fornisce una stima del costo minimo per spostare ogni veicolo alla sua posizione finale. Otteniamo così un'euristica **consistente** per il problema dato e quindi **ammissibile**. Quindi dato $k=(x_1, y_1)$ e dato il goal $g'= (x_2, y_2)$ relativo al singolo obiettivo nello stato goal $g$ $$h(k) = \lvert x_1 - x_2 \lvert +\lvert y_1-y_2 \lvert $$

- Costruire un euristica complessiva combinando quelle dei singoli veicoli
	- Per definire un'euristica complessiva $H$ basta sommare le euristiche focalizzate sui singoli veicoli: $H:S \longrightarrow \mathbb{N}$ $$H(s) = \sum_{i =1}^{M}{h(s_i)}\ \ t.c.\ s_i\ posizione\ del\ veicolo\ i$$
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

### IDA*

### Beam search

ROBE IN PIù
Sistema definizione di C
Sistemare tab
Trovare un modo per fare il sistema sopra nel costo
Spiegare distanza di manhattan
