calificación = 85
if calificación <= 100 and calificación >= 0:
    print("Es una calificación válida")
    if calificación <= 100 and calificación >= 90:
        print(calificación, " tiene un valor alfabético de A ")
    else:
        if calificación <= 89 and calificación >= 80:
            print(calificación, " tiene un valor alfabético de B ")
        else:         
            if calificación <= 79 and calificación >= 70:
                print(calificación, " tiene un valor alfabético de C ")
            else:
                if calificación <= 69 and calificación >= 60:
                    print(calificación, " tiene un valor alfabético de D ")
                else:
                    print(calificación, " tiene un valor alfabético de F ")
else:
    print("Esa no es una calificación válida")