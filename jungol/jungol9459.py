def check_info(g, a):
    if g == 'M' or g =="m":
        if a > 20:
            return "MAN"
        else:
            return "BOY"
    else:
        if a >= 20:
            return "WOMAN"
        else:
            return "GIRL"

gender, age = map(int, input().split())
print(check_info(gender, int(age)))    



def check_info(g, a):
    if g.upper() == "M":
        if a >= 20:
            res =  "MAN"
    else:
        return "GIRL"



print(check_info(gender, int(age)))      


