def calculate_grade(Practica01,Practica02, Practica03, Examen, Recuperacion, Actitud):
    '''La función recibirá las notas de todos los apartados evaluados de c/alumno(a)
    y devolverá una nota final y un valor Verdadero/Falso en función de si ha
    aprobado o suspendido.

    Como parámetros de entrada a la función tendremos seis float con las diferentes notas
    de c/alumno(a).

    La función deberá calcular la nota final mediante la siguiente fórmula,
    redondearla con dos decimales y evaluar si el/la alumno/a ha superado la asignatura 
    (NotaFinal >= 5):'''

    parte1 = ((Practica01 + Practica02 + Practica03)/3)* 0.3
    parte2 = max(Examen, Recuperacion)* 0.6
    parte3 = Actitud* 0.1

    NotaFinal = parte1 + parte2 + parte3
    verdadero_falso = NotaFinal >= 5

    if verdadero_falso:
        return f"Nota final: {float(NotaFinal):.2f}\t Supera: {verdadero_falso}"
    else:
        return f"Nota final: {float(NotaFinal):.2f}\t Supera: {verdadero_falso}"

print(calculate_grade(1.9,6.2,2.8,2.2,2.4,8.3))
print(calculate_grade(1.5, 5.7, 2.9, 9.1, 7.6, 2.6))