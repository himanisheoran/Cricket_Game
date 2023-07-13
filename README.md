# Cricket_Game
Advanced Cricket Tournament Simulation Program using Python

The goal of this assignment is to develop a Python program that simulates a cricket tournament involving various teams with an advanced level of detail. The application is designed to mimic real-world cricket matches and statistics.

Program Requirements: The program consist of the following key classes:

Player: This class contains information on player stats, such aas : name, bowling, batting, fielding, running, experience. These player stats are used when running the simulation and affects the probabilities of various events occurring like a boundary, getting out, etc.

Teams: A team consists of players. It have methods like selecting the captain, sending the next player to the field, choosing a bowler for an over, deciding batting order, etc.

Field: This class contains factors like field size, fan ratio, pitch conditions, home advantage, etc., which can impact the probabilities of the simulation.

Umpire: This class is responsible for chunking probabilities of all the players on the field and predicting the outcome of a ball. The Umpire class also keeps track of scores, wickets, and overs. It also makes decisions on LBWs, catches, no-balls, wide-balls, etc.

Commentator: This class provides commentary for each ball and over. It uses the match stats to give a description of the ongoing game events.

Match: This class simulates an individual cricket match. It uses objects of the Teams, Field, and Umpire classes and have methods to start the match, change innings, and end the match.


HERE IS THE VIDEO OF WORKING PROJECT:



https://github.com/himanisheoran/Cricket_Game/assets/88571812/07d83a84-8a65-4497-9292-ff84e46e4cdf




