                                                #task 1
class Vehicle:

    # Define the valid set of colors and door numbers for validation purposes
    _valid_colors = {"red", "purple", "violet", "black", "white"}
    _valid_doors = {2, 4, 5}

    def __init__(self, color, number_of_doors, gas_powered):
        # Initialize the vehicle with the provided attributes
        self.color = color
        self.number_of_doors = number_of_doors
        self.gas_powered = gas_powered

    # Property for color with getter and setter
    @property
    def color(self):
        return self._color  # Return the color

    @color.setter
    def color(self, value):
        # colour should be from given values
        if isinstance(value, str) and value.lower() in Vehicle._valid_colors:
            self._color = value.lower()  # Set the color after converting to lowercase
        else:
            raise ValueError(f"Invalid color: {value}. Choose from {Vehicle._valid_colors}.")  # Raise error if invalid

    #number of doors with getter and setter
    @property
    def number_of_doors(self):
        return self._number_of_doors  # Return the number of doors

    @number_of_doors.setter
    def number_of_doors(self, value):
        # number of doors should be within the allocated values
        if value in Vehicle._valid_doors:
            self._number_of_doors = value  # Set the number of doors
        else:
            raise ValueError(f"Invalid number of doors: {value}. Choose from {Vehicle._valid_doors}.")  # Raise error if invalid

    # getter and setters for the gas powered
    @property
    def gas_powered(self):
        return self._gas_powered

    @gas_powered.setter
    def gas_powered(self, value):
        #  gas-powered attribute is a boolean value
        if isinstance(value, bool):
            self._gas_powered = value
        else:
            raise ValueError("Invalid value for gas powered. Must be a Boolean.")  # Raise error if invalid

    # String representation of the vehicle
    def __str__(self):
        gas_type = "Gas Powered" if self.gas_powered else "Electric"
        return (f"Vehicle Details:\n"
                f"Color: {self.color}\n"
                f"Number of doors: {self.number_of_doors}\n"
                f"Type: {gas_type}")

    #to determine if the vehicle is eco-friendly
    def is_eco_friendly(self):
        return self.number_of_doors == 2 and not self.gas_powered






                                           #Task 2:


class Truck(Vehicle):
    def __init__(self, color, number_of_doors, gas_powered, seats, trunk_space):
        super().__init__(color, number_of_doors, gas_powered)
        self.seats = seats
        self.trunk_space = trunk_space

    # seats with getter and setter
    @property
    def seats(self):
        return self._seats  # private attribute

    @seats.setter
    def seats(self, value):
        # Ensure the number of seats is an integer greater than zero
        if isinstance(value, int) and value > 0:
            self._seats = value  # Set the number of seats
        else:
            raise ValueError("Seats must be a whole number greater than zero.")  # Raise an error for invalid input

    # trunk space with getter and setter
    @property
    def trunk_space(self):
        return self._trunk_space  # private attribute

    @trunk_space.setter
    def trunk_space(self, value):
        # Ensure the trunk space is a positive integer
        if isinstance(value, int) and value > 0:
            self._trunk_space = value  # Set the trunk space
        else:
            raise ValueError("Trunk space must be a whole number greater than zero.")  # Raise an error for invalid input

    # string representation of the Truck
    def __str__(self):
        vehicle_summary = super().__str__()
        return (f"{vehicle_summary}\n"
                f"Seats: {self.seats}\n"
                f"Trunk space: {self.trunk_space} cubic feet")

    # method to determine the truck is eco friendly
    def is_eco_friendly(self):
        return super().is_eco_friendly() and self.seats <= 2 and self.trunk_space == 0
