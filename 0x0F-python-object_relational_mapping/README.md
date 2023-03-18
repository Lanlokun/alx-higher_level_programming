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

