#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2
import bleach # To clean inputs


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    query = "delete from matches;"
    c.execute(query)
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    query = "delete from players;"
    c.execute(query)
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    query = "select count(*) as total from players;"
    c.execute(query)
    total = c.fetchone()[0]
    db.close()
    return total

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    hurray
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    query = "insert into players(name) values ('%s');" % bleach.clean(name)
    c.execute(query)
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    query = "select * from player_standings;"
    c.execute(query)
    standings = c.fetchall()
    db.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    query = "insert into matches(winner, loser) values(%d,%d);" % (winner, loser)
    c.execute(query)
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db = connect()
    c = db.cursor()
    query1 = '''create temp table rankings as select id, name, wins, 
    row_number() over (order by wins desc) as rank 
    from player_standings;'''
    c.execute(query1)
    query2 = '''select a.id, a.name, b.id, b.name
    from rankings as a join rankings as b
    on a.rank = b.rank-1 and a.rank %2 = 1;'''
    c.execute(query2)
    pairings = c.fetchall()
    db.close()
    return pairings