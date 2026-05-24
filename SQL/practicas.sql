SELECT ciudad, avg(seguidores) as seguidores_avg
from modelos 
GROUP by ciudad
HAVING seguidores > 0
LIMIT 3
order by seguidores DESC;


#con los join juntamos tablas por  columnas.
SELECT nombre, monto
FROM modelos as m 
JOIN pagos as p
    on m.id=p.id_modelo




# la union une filas segun condiciones como podemos ver en 
# este ejemplo 
SELECT nombre, ciudad, 'vive muy lejos' as descartados 
from modelos 
WHERE ciudad != 'vargas'
UNION
SELECT nombre, seguidores, 'no produce' as descartados 
from modelos 
WHERE seguidores < 1
order by nombre;

#-- en sql tambien tenemos funciones tipo texto,
# como length() para calcular la longitud de algun texto
SELECT nombre, length(nombre) as longi
from modelos
ORDER by longi;

#tambien tiene las funciones upper() y lower() para convertir
# texto a mayusculas o minusculas, podemos convertir una 
# columna por ejemplo

SELECT upper(nombre) as longi
from modelos
ORDER by longi ;

# la funcion de texto TRiM()
#elimina los espacios en blanco iniciales y finales.



#la funcion LEFT() y RIGHT() llevan un texto y al lado una coma 
# esas funciones buscan textos en las tablas que selecciones 
# en cuanto a los caracteres que pusite despues de la coma
#tambien esta la sub cadena que son los dos en uno,
#substring(texto,2,2) acepta 3 parametros y los enteros 
#el primero es la posicion donde arancamos y el otro es el 
#numero de caracteres que vamos hagarrar

SELECT nombre, Substring(nombre,2,2)
from modelos 

#la funcion remplace()acepta 3 parametros, la culumna o el texto
# a reemplazar la letra o el texto que queremos reamplazar,
#y el otro parametro seria con lo que vamos a remmplazar

SELECT nombre , REPLACE(nombre, 'a', 'b')


#la funcion locate() nos pide 2 parametros el string que vamos
# a buscar y en que palabra lo vamos a buscar y eso nos devolvera la 
#posicion
SELECT nombre, locate('a', nombre)
from modelos 


#la funcion concat() concatena varias columnas en una 
#añadimos un espacio entre las tablas para separar

SELECT nombre, seguidores
concat(nombre, ' ',seguidores) as nombre_+_segudores
from modelos 

# sentencia case son como if else en python

SELECT nombre, monto, 
CASE
    WHEN monto > 80  THEN 'poco'
    else 'promesa'
end as proyeccion
from modelos, pagos


# sub consultas, basicamente son una consulta dentro e otra
# es un SELECT dentro de otro SELECT.


#la funcion PARTITION by es cuando queremos evaluar 
# por ejemplo dos generos esa funcion va de dividir
#masculino y femenino y va hacer calculos separados
#genero masculo si calculo y fenenino su calculo




#ejercicio:
SELECT ciudad, SUM(monto) AS total_por_ciudad
FROM pagos as p
JOIN modelos as m
    on p.id_pago=m.id
WHERE monto>=100 
GROUP BY ciudad 
HAVING total_por_ciudad > 1500
ORDER by SUM(monto) DESC;

# ejercicio 2:
SELECT nombre, round(avg(monto),2) as promedio_pago
FROM modelos as m
JOIN pagos as p on m.id = p.id_modelo
where ciudad= 'vargas'
GROUP by nombre
HAVING avg(monto)<=400
ORDER by avg(monto) DESC
; 


#CTEs son expresiones de tablas conmunes, permite 
#definir un bloque de subconsulta al que podremos
#acceder despues dentro de la consulta principal
#la palabra clave para definirla es WITH nombre AS
#es literamente como una funcion en python
#creamos un bloque de codigo que mas adenlante 
#podemos llamar y usarla como FROM de otro SELECT
#para no enredarnos y crear bloques de codigos 
#que cumplan una funcion especifica y asi 
#poder filtrar varias veces sin usar muchos WHERE
# que despues confunden,
#se pueedde usar solo una vez exactamente debajo
#del bloque de codigo
#se pueden crear dos, tres... CTEs temporales dentro 
# la misma funcion y unirlos despues,
#eso lp hariamos para que filtre dos veces 
# solo separamos las cuncultas con comas y listo
#ejemplo:
WITH promedios_por_modelo as (
SELECT nombre, round(avg(monto),2) as promedio
from modelos as m 
JOIN pagos as p 
    on m.id=p.id_modelo
GROUP by nombre
)

SELECT * , 'premium'
FROM promedios_por_modelo
where promedio>500;

#ejercicio 2:
WITH metricas_por_ciudad as (
SELECT ciudad, sum(monto) as total, round(avg(monto),2) as promedio
from pagos as p
JOIN modelos as m
    on p.id_modelo=m.id
GROUP by ciudad 
)
SELECT *
FROM metricas_por_ciudad 
WHERE promedio > 20
order by total DESC;


#tablas temporales es casi lo mismo que los CTEs
#lo unico que cambia es como se declara  CREATE TEMPORARY TABLE nombre AS
# y que adiferencia de los CTEs si las puedes usar varias veces en el codigo
# solo desaparecen cuando cierres la base de datos o cierre el vs code
#o lo que usen como editor de codigo
# basicamente es una nueva tabla que creamos para analizar
# y se eliminan cuando te sales 
#tambien podemos unir tamblas temporales 
ejercicio 1:
CREATE TEMPORARY table localidad as 
SELECT ciudad, nombre 
from modelos
;
SELECT *
FROM localidad
WHERE ciudad = 'vargas';

SELECT *
FROM localidad
WHERE ciudad = 'caracas';

#Procedimientos almacenados: esto literamente si es una funcion 
#como en python
# acepta parametros literalmente es una funcion de python
DELIMITER //

CREATE PROCEDURE buscar_modelos_por_presupuesto(IN limite_monto INT)
BEGIN
    SELECT nombre, SUM(monto) AS total_generado
    FROM modelos AS m 
    JOIN pagos AS p 
        ON m.id = p.id_modelo 
    GROUP BY nombre 
    HAVING SUM(monto) <= limite_monto; 
END //

DELIMITER ;

CALL buscar_modelos_por_presupuesto(1500);



#la clausula OVER() permite ralizar calculos sobre conjunts 
# de filas relacionadas sin reducir el nemero de resultados finales

