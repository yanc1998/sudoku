# sudoku
se brinda un conjunto de funciones para darle solcion a un Sudoku,\
--check_sudoku_sol, se encarga de revisar si el tablero es una distribucion valida\
--check_3x3_square, este se utiliza como parte del anterior metodo, para determinar si en un cuadrado se cumple que todos los numeros son distintos\
--create_sudoku_candidates, devuelve para cada posicion vacia del tablero los posibles candidatos\
--find_unico_oculto, devuelve todas las posiciones donde solo existe un unico posible valor para poner\
--valid, se utiliza para buscar los candidatis, devuelve para una posicion todos los posibles candidatos\
--find_fil, devuelve para una posicion todos los ocupados en la fila de esa posicion\
--find_column, devuelve para esa posicion todos los ocupados en la columna de esa posicion\
--solve, genera las posibles soluciones del sudoku
