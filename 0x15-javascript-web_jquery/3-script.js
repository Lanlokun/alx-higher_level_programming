#!/usr/bin/node
// Script that adds the class red to the HTML tag HEADER when the user clicks on the tag DIV#red_header:
$('DIV#red_header').click(function () {
    $('header').addClass('red');
    }
);