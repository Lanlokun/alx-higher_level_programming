# 0x10. Python - Network #0

# 0. cURL body size

    Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

<ul>
    ./0-body_size.sh {paste_your_url_here}
</ul>

# 1. cURL to the end


    Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response


<ul>

    ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""

</ul>

# 2. cURL Method


    Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

<ul>

    ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""

</ul>

# 3. cURL only methods


    Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

<ul>
    
    ./3-methods.sh 0.0.0.0:5000/route_4

</ul>

# 4. cURL headers


    Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response


<ul>

    /4-header.sh 0.0.0.0:5000/route_5 ; echo ""
</ul>

# 5. cURL POST parameters

    Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response


<ul>

    ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""

<ul>

# 6. Find a peak


    Write a function that finds a peak in a list of unsorted integers.

<ul>

    ./6-main.py

</ul>

# 7. Only status code


    Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.


<ul>

    ./100-status_code.sh 0.0.0.0:5000 ; echo ""

</ul>

# 8. cURL a JSON file


    Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

<ul>

    ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""

</ul>

# 9. Catch me if you can!


    Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.


<ul>

    ./102-catch_me.sh ; echo ""

</ul>



