def convert_cylindrical_power(spherical, cylindrical, axis):
   """
   Convert between positive and negative cylindrical power.
   
   Parameters:
   - spherical (float): The spherical power of the lens.
   - cylindrical (float): The cylindrical power of the lens.
   - axis (int): The axis of the cylindrical power in degrees (0-180).
   
   Returns:
   - tuple: Converted (spherical, cylindrical, axis)
   """
   spherical += cylindrical  # Adjust spherical power
   cylindrical = -cylindrical  # Flip cylindrical power sign
   axis = (axis + 90) % 180  # Adjust axis
   
   if spherical == -0:
    spherical = 0
   if cylindrical == -0:
    cylindrical =0

   
   return spherical, cylindrical, axis

while True:
   try:
       # Ask the user for input
       spherical_power = float(input("Enter the spherical power: "))
       cylindrical_power = float(input("Enter the cylindrical power: "))
       axis = int(input("Enter the axis (0-180): "))

       # Ensure the axis is in the valid range
       if not (0 <= axis < 180):
           raise ValueError("Axis must be between 0 and 180 degrees.")

       # Convert the prescription
       converted_spherical, converted_cylindrical, converted_axis = convert_cylindrical_power(spherical_power, cylindrical_power, axis)
       
       # Display the converted valuesIn 
       print(f"\nConverted Prescription:\nSpherical: {converted_spherical}\nCylindrical: {converted_cylindrical}\nAxis: {converted_axis}")

   except ValueError as e:
       print(f"Invalid input: {e}")
   
   # Prompt to continue or exit
   proceed = input("\nPress enter to calculate another value ")
   if proceed.strip():  # Exit if anything other than space is pressed
       print("Exiting the program.")
       break