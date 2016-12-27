-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop database if exists tournament;
create database tournament;

\c tournament

create table players(
    id serial primary key,
    name text not null
);

create table matches(
   id serial primary key,
   winner int references players(id) on delete cascade,
   loser int references players(id) on delete cascade, check (loser != winner),
   unique (winner, loser)
);

create view winnings as
select players.id, count(matches.winner) as wins
from players left join matches on matches.winner = players.id
group by players.id order by wins desc;

create view matchcount as 
select players.id, count(matches.id) as matches
from players left join matches on matches.winner = players.id or
players.id = matches.loser
group by players.id order by matches desc;

create view player_standings as 
select players.id, players.name, winnings.wins, matchcount.matches                            
from players left join winnings on players.id = winnings.id
    left join matchcount on players.id = matchcount.id
order by winnings.wins desc;