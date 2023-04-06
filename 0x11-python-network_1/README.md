# 0x11. Python - Network #1


# 0. What's my status? #0

    Write a Python script that fetches https://alx-intranet.hbtn.io/status

<ul>

    ./0-hbtn_status.py | cat -e

</ul>



# 1. Response header value #0

    Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

<ul>

    ./1-hbtn_header.py https://alx-intranet.hbtn.io

</ul>

# 2. POST an email #0


    Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

<ul>

    ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com

</ul>


# 3. Error code #0


    Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

<ul>

    ./3-error_code.py http://0.0.0.0:5000
    ./3-error_code.py http://0.0.0.0:5000/status_401
    ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
    ./3-error_code.py http://0.0.0.0:5000/status_500

</ul>


# 4. What's my status? #1


    Write a Python script that fetches https://alx-intranet.hbtn.io/status


<ul>

    ./4-hbtn_status.py | cat -e
   
</ul>

# 5. Response header value #1


    Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header


<ul>
    chmod u+x 5-hbtn_header,py
    ./5-hbtn_header.py https://alx-intranet.hbtn.io  
   
</ul>

# 6. POST an email #1

    Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.



<ul>

    ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
   
</ul>

# 7. Error code #1


    Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.


<ul>

   ./7-error_code.py http://0.0.0.0:5000
   ./7-error_code.py http://0.0.0.0:5000/status_401
   
</ul>