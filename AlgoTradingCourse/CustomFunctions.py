# method of checking if int value is inputted, and will continue looping until correct value type
def get_int(prompt="Enter portfolio size ($): "):
    while True:
        try:
            return int(input(prompt))
        # ValueError is raised when the input is not an integer
        except ValueError:
            print("Invalid input. Please try again.")