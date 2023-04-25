#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

request(process.argv[2], function (err, response, body)
{
    if (err)
    {
        console.log(err);
    }
    else
    {
        let count = 0;
        const data = JSON.parse(body).results;
        for (let i = 0; i < data.length; i++)
        {
            const characters = data[i].characters;
            for (let j = 0; j < characters.length; j++)
            {
                if (characters[j].includes('18/'))
                {
                    count++;
                }
            }
        }
        console.log(count);
    }
}
);