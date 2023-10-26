
class Tournament :
    def __init__(self):
        self.stock_number_team = 0
        self.stock_team_name = []
        self.stock_number_of_game = 0
        self.stock_team_score = {}

    def input_number_of_teams(self) : 
        while 1 : 
            number_of_team = input("Enter the number of teams in the tournament: ")
            if number_of_team.isdigit() and int(number_of_team)>=2 :
                self.stock_number_team = int(number_of_team) 
                break
            else : 
                print("The minimum number of teams is 2, try again.")
        return self.stock_number_team

    def input_team_name(self) :
        for team_num in range(1,self.stock_number_team+1) : 
            while 1 :
                team_name = input(f"Enter the name of the team #{team_num}: ")
                if isinstance(team_name,str) and len(team_name)<2:
                    print("Team names must have at least 2 characters, try again.")
                elif isinstance(team_name,str) and len(team_name.split(" "))>=2 : 
                    print("Team names may have at most 2 words, try again")
                else : 
                    self.stock_team_name.append(team_name)  
                    break     
        return self.stock_team_name

    def number_of_game(self) : 
        while 1 : 
            number_of_game = input("Enter the number of games played by each team: ")
            if number_of_game.isdigit() and int(number_of_game)>=self.stock_number_team-1 :
                self.stock_number_of_game = int(number_of_game)
                break
            else :
                print("Invalid number of games.Each team plays each other at least once in the regular season, try again.")         
        return self.stock_number_of_game


    def input_team_score(self) :
        for team in self.stock_team_name :
            while 1 :
                score = input(f"Enter te number of wins Team {team} had: ")
                if score.isdigit() and int(score)<0 :
                    print("The minimum number of wins is 0, try again.")
                elif score.isdigit() and int(score)>self.stock_number_of_game :
                    print(f"The maximum number of wins is {self.stock_number_of_game}, try again")
                else :
                    self.stock_team_score[team] = int(score)
                    break
        return self.stock_team_score




    def versus(self) :
        print("Generating the games to be played in the first round of the tournament...")
        while len(self.stock_team_score) !=0 :
            home = ""
            away = ""
            home_score = 0
            for team,score in self.stock_team_score.items() :
                if score > home_score : 
                    home_score = score
                    home = team
            away_score = home_score
            for team,score in self.stock_team_score.items() :
                if score < away_score : 
                    away_score = score
                    away = team
            print(f"HOME: {away} VS AWAY: {home}") 
            del self.stock_team_score[home]
            del self.stock_team_score[away]


if __name__ == "__main__" :
    tournament = Tournament()
    tournament.input_number_of_teams()
    tournament.input_team_name()
    tournament.number_of_game()
    tournament.input_team_score()
    tournament.versus()