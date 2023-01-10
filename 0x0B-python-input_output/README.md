# alx-higher_level_programming
Everything Python


# 0. Read file

        Write a function that reads a text file (UTF8) and prints it to stdout:

<ul>

        chmod u+x 0-main.py
        ./0-main.py

</ul>

# 1. Write to a file

        Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

<ul>

        chmod u+x 1-main.py
        ./1-main.py

</ul>

# 2. Append to a file

        Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:


<ul>

        chmod u+x 2-main.py
        ./2-main.py

</ul>

# 3. To JSON string

        Write a function that returns the JSON representation of an object (string):

<ul>

        chmod u+x 3-main.py
        ./3-main.py

</ul>

# 4. From JSON string to Object


        Write a function that returns an object (Python data structure) represented by a JSON string:

<ul>

        chmod u+x 4-main.py
        ./4-main.py

</ul>

# 5. Save Object to a file

        Write a function that writes an Object to a text file, using a JSON representation:

<ul>

        chmod u+x 5-main.py
        ./5-main.py

</ul>

# 6. Create object from a JSON file

        Write a function that creates an Object from a “JSON file”:

<ul>

        chmod u+x 6-main.py
        ./6-main.py

</ul>

# 7. Load, add, save

        Write a script that adds all arguments to a Python list, and then save them to a file:


<ul>

        chmod u+x 7-add_item.py
        ./7-add_item.py
        cat add_item.json

</ul>

# 8. Class to JSON


        Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

<ul>

        chmod u+x 8-main.py
        chmod u+x 8-main_2.py
        ./8-main.py
        ./8-main_2.py

</ul>



# 9. Student to JSON


        Write a class Student that defines a student by:

            Public instance attributes:
                first_name
                last_name
                age

<ul>

        chmod u+x 9-main.py
        ./9-main.py

</ul>

# 10. Student to JSON with filter


        Write a class Student that defines a student by: (based on 9-student.py)

            Public instance attributes:
                first_name
                last_name
                age

<ul>

        chmod u+x 9-main.py
        ./9-main.py

</ul>

# 11. Student to disk and reload


Write a class Student that defines a student by: (based on 10-student.py)

        Public instance attributes:
                first_name
                last_name
                age

<ul>

        chmod u+x 11-main.py
        ./11-main.py student.json

</ul>

# 12. Pascal's Triangle


        Technical interview preparation:

<ul>

        chmod u+x 12-main.py
        ./12-main.py

</ul>


# 13. Search and update

        Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

<ul>

        chmod u+x 100-main.py
        ./100-main.py

</ul>


# 14. Log parsing


        Write a script that reads stdin line by line and computes metrics:

            Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
                Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
                Total file size: File size: <total size>
                where is the sum of all previous (see input format above)
                Number of lines by status code:
                possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
                if a status code doesn’t appear, don’t print anything for this status code
                format: <status code>: <number>
                status codes should be printed in ascending order

    <ul>

        chmod u+x 100-main.py
        ./100-main.py

</ul>