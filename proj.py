def calculateRect(length, width):
    if length > 0 and width > 0:
            return length*width
    else:
          return("кощунство")
print('Площадь:', calculateRect(5, 10))
def calculateCircle(radius):
    if radius>0:
            return 3.14*radius^2
    else:
          return("кощунство")
print('Площадь:', calculateCircle(10))