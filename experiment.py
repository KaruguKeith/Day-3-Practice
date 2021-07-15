def calculateVolumeOfCylinder (radius ,height):

    from math import pi

    volumeOfCylinder = (pi) * (radius*radius) * (height)

    return volumeOfCylinder

def inputOfMeasurements ():
        
    radius = float(input("What is the radius of the cylinder ? "))

    height =float(input("What is the height of the cylinder ?"))

    return calculateVolumeOfCylinder(radius, height)

print (("The cylider is") , (inputOfMeasurements()), ("Centimetres squared"))