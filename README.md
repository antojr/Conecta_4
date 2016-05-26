# Conecta_4

Asignatura: Fundamentos de los Sistemas Inteligentes. 2015/2016 Alumnos del Grupo: - Diego Martín Hernández - Airán Villacorta Betancor

Para el desarrollo de la práctica Conecta 4, hemos modificado los ficheros run.py y games.py, así como la creación
de un nuevo fichero llamado hey.py que contiene la heurística.

El fichero run.py se ha modificado con el fin de preguntar al usuario en que nivel desea jugar y si desea empezar
el mismo usuario o la máquina. Para ello hemos hecho uso de prompts.

El fichero games.py se ha modificado el método alphabeta_search(), le hemos añadido dos parámetros más el jugador y la
dificultad seleccionada por el usuario.

El fichero heu.py alberga la heurística que funciona de la siguiente manera, hacemos una comprobación de cada movimiento que podamos hacer, esto genera un valor de utilidad el cual informa sobre la cercanía a un posible estado objetivo.

En caso de no estar cercano a un estado objetivo hacemos una comprobación del tablero en el cual miramos a ambos jugadores, cuando encontramos fichas aliadas consecutivas sumamos 200 y si no hay nada sumamos 10, en caso de ser una
pieza del adversario cesamos la suma. Cuando encontramos 4 o más huecos y piezas aliadas devolvemos el valor heuristico, en caso contrario devolvemos 0. El cálculo final de la heurística es la diferencia entre el jugador y el adversario.