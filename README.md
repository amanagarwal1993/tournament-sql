# Tournament Results Database
##### An SQL Learning Experiment

So, this project is actually an implementation of an assignment which is part of the [Full Stack Web Developer Nanodegree](www.udacity.com/nanodegree) program at Udacity. In this project, we create a database for a Swiss-style game tournament, used to store players and their match records. Then, we have some functions which give you extra data such as
* What are the player rankings (number of matches won etc) at any given point in time
* To give you match pairings for the next 'round', based on current player standings

This database structure can be used for any sport or game, but only supports one tournament at a time (so far).

### How to run this project
The project uses the Python DB API, and a Postgres database. So, you would likely need to have something like psql installed. I personally used a virtual machine which had the psql package etc already installed, so I can't really help you with this. Send me a message if you need help setting this up.
Assuming you have everything set up,

1. In PSQL, first import the **tournament.sql** file and run its commands. This will create the database, connect to it and also create the relevant tables.
2. Then, run python (I used Python 2.7 btw). You can then run `import tournament` and then use the functions defined in **tournament.py**.
3. You can also run the command `python tournament_test.py` which will directly test out all the functions in tournament.py and give you results. It's pretty sweet, thanks to Udacity!

### How the project is organized
As mentioned before, there are three files in this repository.

1. **Tournament.sql**: Contains sql commands. Upon running this in psql, you can set up the database and its tables etc.
2. **Tournament.py**: Contains python code. It's based on psycopg2, a library which allows us to implement the Python DB API. This file contains pre-defined functions like registerPlayer(), playerStandings(), countPlayers() etc that you can run in your python terminal to play with the database.
3. **Tournament_test.py**: This is a file provided by Udacity that runs automatic tests on your *Tournament.py* functions to see if they're working fine. No need to tinker with the functions there, but feel free to add your own if you feel 'hacky'. Like, in a hacking mood? Not sure if this word exists and/or is used in the way I just did...

### A poem about the tournament.py file
Okay not a poem, but a few words nonetheless for this beautiful creation. Well as I said it uses psycopg2. And I use the **bleach** library to clean my inputs so that people who have dirty minds *(compared with mine for reference)* don't screw up my database.

Here's how each function works:
1. It connects to the database
2. I declare a `query` string which will be run on the database. This is an SQL query.
3. I run the query using `c.execute()`. Sometimes in insert operations I also do a `db.commit` otherwise the query doesn't reflect in the database.
4. I return the results of the query operation and close the connection to the database.

Ta-daaa!!!!

### License
[GNU General Public License](http://choosealicense.com/licenses/gpl-3.0/#)

