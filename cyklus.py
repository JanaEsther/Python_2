marks = [1, 3, 2, 1, 1, 2, 5, 4, 3]
# variable source
for mark in marks: # znamka = znamky[0]
    if mark == 1:
        print("Excellent")
    elif mark == 2:
        print("Very good")
    elif mark == 3:
        print("Good")
    elif mark == 4:
        print("Satisfactory")
    else:
        print("Failed")

print("This is the end.")