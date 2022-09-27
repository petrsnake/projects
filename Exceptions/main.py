test = [1, 2, 3, 4]
while True:
    try:
        a = int(input("zadej číslo 0 - 3: "))
        print (test[a])
    except IndexError as exc:
        print("Zadávejte čísla pouze 0 - 3")
    finally:
        if a == 1:
            break
# Demonstrace chycení výjimky