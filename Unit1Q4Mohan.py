# Name: Mohan Dixit
# Date: Feb 23rd
# Purpose: Given the radius of a sphere, we need to find the volume and surface area of the sphere

# Get the radius from the user

radius = float(input("Enter the radius: "))


# Calculate the volume and surface area
volume_of_the_sphere = (4/3)*3.14*(radius**3)
surface_area_of_the_sphere = 4*3.14*(radius**2)


# Print out the non-rounded volume and surface area
# Answer to 4a

print(f"The volume of the sphere is approximately {volume_of_the_sphere} cm cubed. " +
      f"The surface area of the sphere is approximately {surface_area_of_the_sphere} cm squared.")


# Print out the rounded volume and surface area(to one decimal place)
# Answer to 4b

print(f"The volume of the sphere is approximately {format(volume_of_the_sphere,'.1f')} cm cubed. " +
      f"The surface area of the sphere is approximately {format(surface_area_of_the_sphere,'.1f')} cm squared.")
