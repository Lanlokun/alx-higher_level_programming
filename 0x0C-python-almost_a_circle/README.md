# alx-higher_level_programming
Everything Python


# 0x0C. Python - Almost a circle


# 0. If it's not tested it doesn't work

<ul>
        python3 -m unittest discover tests
</ul>

# 1. Base class

        Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new value to the public instance attribute id
This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)


<ul>

        chmod u+x 0-main.py
        ./0-main.py
</ul>

# 2. First Rectangle

        Write the class Rectangle that inherits from Base:

        In the file models/rectangle.py
        Class Rectangle inherits from Base
        Private instance attributes, each with its own public getter and setter:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
        Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
        Call the super class with id - this super call with use the logic of the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute
        Why private attributes with getter/setter? Why not directly public attribute?

        Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.


<ul>

        chmod u+x 1-main.py
        ./1-main.py

</ul>


# 3. Validate attributes


        Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

        If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer
        If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example: width must be > 0
        If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0

 <ul>

        chmod u+x 2-main.py
        ./2-main.py

</ul>


# 4. Area first

        Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

<ul>

        chmod u+x 3-main.py
        ./3-main.py

</ul>

# 5. Display #0


        Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.


<ul>

        chmod u+x 4-main.py
        ./4-main.py

</ul>


# 6. __str__


        Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

<ul>

        chmod u+x 5-main.py
        ./5-main.py

</ul>

# 7. Display #1

        Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

<ul>

        chmod u+x 6-main.py
        ./6-main.py

</ul>

# 8. Update #0

        Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:

        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        This type of argument is called a “no-keyword argument” - Argument order is super important.

<ul>

        chmod u+x 7-main.py
        ./7-main.py

</ul>

# 9. Update #1


        Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:

        **kwargs can be thought of as a double pointer to a dictionary: key/value
        As Python doesn’t have pointers, **kwargs is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
        **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance
        This type of argument is called a “key-worded argument”. Argument order is not important.

<ul>

        chmod u+x 8-main.py
        ./8-main.py

</ul>

# 10. And now, the Square!

        Write the class Square that inherits from Rectangle:


<ul>

        chmod u+x 9-main.py
        ./9-main.py

</ul>

# 11. Square size


        Update the class Square by adding the public getter and setter size

<ul>

        chmod u+x 10-main.py
        ./10-main.py

</ul>

# 12. Square update

        Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:

<ul>

        chmod u+x 11-main.py
        ./11-main.py

</ul>

# 13. Rectangle instance to dictionary representation


        Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:


<ul>

        chmod u+x 12-main.py
        ./12-main.py

</ul>

# 14. Square instance to dictionary representation


        Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:

<ul>

        chmod u+x 13-main.py
        ./13-main.py

</ul>

# 15. Dictionary to JSON string


        JSON is one of the standard formats for sharing data representation.

        Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries:

<ul>

        chmod u+x 14-main.py
        ./14-main.py

</ul>

# 16. JSON string to file

        Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:

<ul>

        chmod u+x 15-main.py
        ./15-main.py

</ul>

# 17. JSON string to dictionary


        Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:

<ul>

        chmod u+x 16-main.py
        ./16-main.py

</ul>

# 18. Dictionary to Instance

        Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:

<ul>

        chmod u+x 17-main.py
        ./17-main.py

</ul>

# 19. File to instances

    Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:

<ul>

        chmod u+x 18-main.py
        ./18-main.py

</ul>

# 20. JSON ok, but CSV?


        Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV:

<ul>

        chmod u+x 100-main.py
        ./100-main.py

</ul>

# 21. Let's draw it

        Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:


<ul>

        chmod u+x 101-main.py
        ./101-main.py

</ul>