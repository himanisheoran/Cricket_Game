import random 

class Player:
    def __init__(self, p_name, bowling, batting, t_fielding, running, experience):
        """Represents a player in a cricket team."""
        self.p_name = p_name 
        self.bowling = bowling 
        self.batting = batting 
        self.t_fielding = t_fielding 
        self.running = running 
        self.experience = experience

class Team:

    def __init__(self, p_name, players):
        """Initialize a Team object with the provided attributes."""
        self.p_name = p_name 
        self.players = players 
        self.team_captain = None 
        self.batting_order = players.copy()
        self.bowlers = []

    def captain_selection(self, team_captain):
        """Select the team_captain for the team."""
        self.team_captain = team_captain

    def sending_next_player(self):
        """Send the next player from the batting order."""
        if len(self.batting_order)>0:
            return self.batting_order.pop(0)
        return None 
    
    def bowler_selection(self):
        """Choose a bowler randomly from the team's bowlers."""
        return random.choice(self.bowlers)
    

class field_conditions:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        """Initialize a field_conditions object with the provided attributes."""
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage


class Umpire:
    def __init__(self, field_conditions):
        """Initialize an Umpire object with the provided attributes. """
        self.field_conditions = field_conditions
        self.total_scores = 0
        self.total_wickets = 0
        self.total_overs = 0

    def update_score(self, runs):
        """Update the score based on the runs scored."""
        self.total_scores += runs

    def update_wickets(self):
        """Update the total_wickets count."""
        self.total_wickets += 1

    def update_overs(self):
        """Update the total_overs count."""
        self.total_overs += 1

    def predict_outcome(self, batsman, bowler):
        """Predict the outcome of a ball based on batsman and bowler stats."""
        batting_probability = batsman.batting * self.field_conditions.pitch_conditions * random.random()
        bowling_probability = bowler.bowling * self.field_conditions.pitch_conditions * random.random()
        if batting_probability > bowling_probability:
            return "OUT"
        return "NOT OUT"

class Commentator:
    def __init__(self, umpire):
        """Initialize a Commentator object with the provided attributes."""
        self.umpire = umpire

    def ball_details(self, batsman, bowler):
        """Generate a description of the ball played by the batsman."""
        outcome = self.umpire.predict_outcome(batsman, bowler)
        print("Outcome : ", outcome)
        if outcome == "OUT":
            description = f"{batsman.p_name} is OUT!"
        else:
            description = f"{batsman.p_name} plays the shot."

        return description

    def game_details(self, captain1, captain2, Country_1, Country_2, over):
        """Provide a description of the cricket match."""
        print("\n********      Game Description     ********\n")
        print(f"{Country_1} Vs {Country_2}")
        print(f"\nTeam 1 Captain : {captain1}\nTeam 2 Captain : {captain2}")
        print(f"\nCurrent Over : {over}")

    def match_start(self, team):
        """Provide a description of the start of an innings."""
        print("\n*******    INNINGS STARTED   ********\n")
        print(f"\nTeam {team} is playing: ")
    
    def match_end(self):
        """Provide a description of the end of an innings."""
        print(f"\n\nFinal Runs: {self.umpire.total_scores} \nTotal Wickets: {self.umpire.total_wickets} \nTotal Overs: {self.umpire.total_overs}")

    
    def innings_status(self, ball_count):
        """
        Provide the current match information."""
        print(f"\nBalls played: {ball_count} \nOver Played: {self.umpire.total_overs} \nTotal Runs: {self.umpire.total_scores} \nWicket dropped: {self.umpire.total_wickets}")

    def innings_final_result(self, p_name, total_scores):
        """Provide a description of the final result of the match."""
        print("******       Winner       ******")
        print(f"\nTEAM : {p_name} WON BY SCORE: {total_scores}")
        print("\n____________________________________\n")

class Match:
    def __init__(self, team1, team2, field_conditions, total_overs):
        """Represents a cricket match between two teams."""
        self.team1 = team1
        self.team2 = team2
        self.field_conditions = field_conditions
        self.umpire = Umpire(field_conditions)
        self.commentator = Commentator(self.umpire)
        self.total_overs = total_overs

    def start_match(self):
        """Starts the cricket match."""
        self.team1.captain_selection(random.choice(self.team1.players))
        self.team2.captain_selection(random.choice(self.team2.players))
        self.team1.batting_order = self.team1.players.copy()
        self.team2.batting_order = self.team2.players.copy()
        self.team1.bowlers = self.team1.players.copy()
        self.team2.bowlers = self.team2.players.copy()

        self.commentator.game_details(self.team1.team_captain.p_name, self.team2.team_captain.p_name, self.team1.p_name, self.team2.p_name, over=self.total_overs)

        # Team 1 playing    
        self.commentator.match_start(self.team1.p_name)
        self.play_innings(self.team1, self.team2)
        self.commentator.match_end()
        lastScores = self.commentator.umpire.total_scores


        # Team 2 playing    
        self.commentator.umpire.total_scores = 0
        self.commentator.umpire.total_wickets = 0
        self.commentator.umpire.total_overs = 0
        self.commentator.match_start(self.team2.p_name)
        self.play_innings(self.team2, self.team1)
        self.commentator.match_end()
        newScores = self.commentator.umpire.total_scores

        # Final outcome
        if lastScores > newScores:
            self.commentator.innings_final_result(team1.p_name, lastScores)
        else:
            self.commentator.innings_final_result(team2.p_name, newScores)


    def play_innings(self, batting_team, bowling_team):
        """Simulates the innings of a team."""
        ball_count = 1
        over = 0
        bowler = bowling_team.bowler_selection() 
        batsman = batting_team.sending_next_player()
        
        while over < self.total_overs:
            print("\n")
            self.commentator.innings_status(ball_count)
            ball_description = self.commentator.ball_details(batsman, bowler)
            
            print(ball_description)
            if ball_description.endswith("OUT!"):
                batsman = batting_team.sending_next_player()
                if batsman is None:
                    break
                self.umpire.update_wickets()
                print(f"\n\nTotal Wickets Dropped: {self.umpire.total_wickets} , \nTotal Overs Played: {self.umpire.total_overs}")
                print(f"{batsman.p_name} Has Started Playing")
            else:
                runs = random.randint(0, 6)
                self.umpire.update_score(runs)

            if ball_count > 5:
                over += 1
                print(f"New Over {over} Starting")
                self.umpire.update_overs()
                bowler = bowling_team.bowler_selection()
                ball_count = 0

            self.commentator.innings_status(ball_count)
            ball_count += 1

player1 = []
for i in range(10):
    player1.append(Player("Team 1 Player Number "+str(i+1), round(random.random(),1), round(random.random(),1),round(random.random(),1), round(random.random(),1), round(random.random(),1)))

player2 = []
for i in range(10):
    player2.append(Player("Team 2 Player Number "+str(i+1), round(random.random(),1), round(random.random(),1),round(random.random(),1), round(random.random(),1), round(random.random(),1)))

team1 = Team("Country 1", player1)
team2 = Team("Country 2", player2)

field_conditions = field_conditions("Large", 0.5, 0.6, 0.9)

total_overs = 5
match = Match(team1, team2, field_conditions, total_overs)
match.start_match()