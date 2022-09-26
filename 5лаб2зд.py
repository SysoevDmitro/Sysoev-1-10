Ax = int(input("Координаты А x"))
Ay = int(input("Координаты А y"))
Bx = int(input("Координаты B x"))
By = int(input("Координаты B y"))
Cx = int(input("Координаты C x"))
Cy = int(input("Координаты C y"))

As= Ax + Ay
Cs= Cx + Cy
Bs= Bx + By

if As > Bs and As > Cs:
    print("Найбільша сума відстаней до точки A")
elif Bs > As and Bs > Cs:
    print("Найбільша сума відстаней до точки B")
else:
    print("Найбільша сума відстаней до точки C")

    