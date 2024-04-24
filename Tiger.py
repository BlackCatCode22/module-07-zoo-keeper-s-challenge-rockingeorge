# Import the Animal class from the Animal module
from Animal import Animal

class Tiger(Animal):
    # create a static class variable to keep track of the number of tiger created
    numOfTigers = 0

    # Create the tiger sound
    tiger_sound = " mrow...mrow "

    # Create a list of tiger names.
    list_of_tiger_names = []

    file_path = r'animalNames.txt' # I tried localizing this file path and looked up a different code to implement to try and pull the file path and it STILL DIDNT WORK LOL!!!!
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Iterate through the lines in the file
        line_num = 1
        for line in lines:
             # Tigers are on #15
            if line_num == 15:
                list_of_tiger_names.extend(line.strip().split(', '))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id", birth_date="2099-01-01", color="a_color", sex="a_sex",
                 weight="a_weight", originating_zoo="a_zoo", date_arrival="2099-01-01"):
        # Increment the static variable numOfTigers when a new Tiger object is created
        Tiger.numOfTigers += 1

        # Generate a unique ID for the Tigers
        self.gen_unique_id()

        # Call the constructor of the parent class (Animal) with 'Tiger' as the species
        super().__init__("tiger", name, animal_id, birth_date, color, sex, weight, originating_zoo, date_arrival)

    def make_sound(self):
        return self.tiger_sound

    # the tiger object will call this method to get an unused tiger name. pop() will remove the first element from
    #   the list_of_tiger_names[]
    def get_tiger_name(self):
        return self.list_of_tiger_names.pop(0)

    # generate ID abrev 'Ti' + number with padding from 0 hopefully 2 dig. long ideally
    def gen_unique_id(self):
        self.animal_id = "Ti" + str(Tiger.numOfTigers).zfill(2)