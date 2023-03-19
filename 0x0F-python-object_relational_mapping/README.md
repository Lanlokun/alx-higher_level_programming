# 0x0F. Python - Object-relational mapping

# 0. Get all states


    Write a script that lists all states from the database hbtn_0e_0_usa:

<ul>

    cat 0-select_states.sql | mysql -uroot -p
    ./0-select_states.py root root hbtn_0e_0_usa

</ul>

# 1. Filter states

    Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

<ul>

    cat 0-select_states.sql | mysql -uroot -p
    ./1-filter_states.py root root hbtn_0e_0_usa

</ul>

# 2. Filter states by user input


    Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

<ul>

    cat 0-select_states.sql | mysql -uroot -p
    ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'

</ul>

# 3. SQL Injection...


    Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?


<ul>

    cat 0-select_states.sql | mysql -uroot -p
    ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'

</ul>

# 4. Cities by states


    Write a script that lists all cities from the database hbtn_0e_4_usa


<ul>

    cat 0-select_states.sql | mysql -uroot -p
    ./4-cities_by_state.py root root hbtn_0e_4_usa

</ul>

# 5. All cities by state


    Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

<ul>

    cat 0-select_states.sql | mysql -uroot -p
    ./5-filter_cities.py root root hbtn_0e_4_usa Texas
</ul>

# 6. First state model


    Write a python file that contains the class definition of a State and an instance Base = declarative_base():

<ul>

    cat 0-select_states.sql | mysql -uroot -p
    ./6-model_state.py root root hbtn_0e_6_usa

</ul>

# 7. All states via SQLAlchemy


    Write a script that lists all State objects from the database hbtn_0e_6_usa


<ul>

    cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
    ./7-model_state_fetch_all.py root root hbtn_0e_6_usa

</ul>

# 8. First state


    Write a script that prints the first State object from the database hbtn_0e_6_usa

<ul>

   ./8-model_state_fetch_first.py root root hbtn_0e_6_usa

</ul>


# 9. Contains `a`

    Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa


<ul>

   ./9-model_state_filter_a.py root root hbtn_0e_6_usa

</ul>

# 10. Get a state


    Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa


<ul>

   ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas

</ul>

# 11. Add a new state


    Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

<ul>

    ./11-model_state_insert.py root root hbtn_0e_6_usa 

</ul>

# 12. Update a state


    Write a script that changes the name of a State object from the database hbtn_0e_6_usa


<ul>

    ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
    /7-model_state_fetch_all.py root root hbtn_0e_6_usa 

</ul>


# 13. Delete states

    Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa

<ul>

    ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
    /7-model_state_fetch_all.py root root hbtn_0e_6_usa 

</ul>

# 14. Cities in state


    Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.



<ul>

    ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
    
</ul>

# 15. City relationship

    Improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py:

    City class:
    No change
    State class:
    In addition to previous requirements, the class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked 
<ul>

    ./100-relationship_states_cities.py root root hbtn_0e_100_usa

</ul>

# 16. List relationship


    Write a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa


<ul>

    cat 101-relationship_states_cities_list.sql | mysql -uroot -p
    chmod u+x 101-relationship_states_cities_list.py
    ./101-relationship_states_cities_list.py root root hbtn_0e_101_usa

</ul>


# 17. From city


    Write a script that lists all City objects from the database hbtn_0e_101_usa



<ul>
    chmod u+x 102-relationship_cities_states_list.py
   ./102-relationship_cities_states_list.py root root hbtn_0e_101_usa

</ul>