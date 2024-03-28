rows = 9

star = "*"

for i in range(1, rows):
   
    if i <= 4:
     print(star)
     star += "*"
    
    else:
        print(star)
        star = star [:-1]

print("*")

# References
# https://stackoverflow.com/questions/77422605/program-for-an-upright-and-inverted-triangle-pattern-with-one-for-loop-and-if-el
# https://www.youtube.com/watch?v=fX64q6sYom0&t=20s