import copy
import os

from operator import itemgetter

from constants import PLAYERS, TEAMS


def clean_data(data):
    """Cleaning function for 'PLAYERS' data"""
    for item in data:
        item['height'] = int(item['height'].split(" ")[0])
        if item['experience'] == 'YES':
            item['experience'] = True
        else:
            item['experience'] = False
        item['guardians'] = item['guardians'].split(" and ")
    return data


def clear_screen():
    """Clear the screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')


def average_team_height(team):
    """Calculate and return the average height of the team"""
    heights = []
    for player in team['players']:
        heights.append(player['height'])
    return sum(heights) / len(heights)


def team_guardians(team):
    """Return a string of the names of the guardians of the team players"""
    guardians = []
    for player in team['players']:
        for guardian in player['guardians']:
            guardians.append(guardian)
    return ", ".join(guardians)


def draw_main_menu():
    """Draw the main menu and return the user's menu selection"""
    print("""
BASKETBALL TEAM STATS TOOL

---- MENU ----

  Please make a selection:
          
    A) Display Team Stats
    B) Quit

""")


def main_menu(teams):
    """Main menu logic"""
    while True:
        draw_main_menu()
        menu_selection = input("Enter an option: ").lower()
        if menu_selection == 'a':
            clear_screen()
            team_selection_menu(teams)
        elif menu_selection == 'b':
            clear_screen()
            print("Thanks for using the Basketball Team Stats tool! Bye! \n")
            break
        else:
            clear_screen()
            print("That wasn't a valid selection. Please try again.")
            continue
    


def draw_team_menu(teams):
    """Draw the team stats menu and return the user's menu selection"""
    print("Which team's stats would you like to view? \n")
    for count, team in enumerate(teams):
        print(f"  {count+1}) {team['team_name']}")
    print("")



def team_selection_menu(teams):
    """Team selection menu logic"""
    while True:
        draw_team_menu(teams)
        menu_selection = input("Enter an option: ").lower()
        try:
            if int(menu_selection) in range(1, len(teams)+1):
                display_team_stats(teams[int(menu_selection)-1])
                break
            else:
                clear_screen()
            print("That wasn't a valid selection. Please try again.")
            continue
        except ValueError:
            clear_screen()
            print("That wasn't a valid selection. Please try again.")
            continue



def display_team_stats(team):
    """Display the stats for a team and return to the main menu when done"""
    clear_screen()
    print(f"""
Team: {team['team_name']} Stats
--------------------------
Total players: {len(team['players'])}
Total of experienced players: {len([exp_player for exp_player in team['players'] if exp_player['experience']])}
Total of inexperienced players: {len([exp_player for exp_player in team['players'] if not exp_player['experience']])}
Average height: {round(average_team_height(team), 2)}

Players on Team:
    {", ".join([player['name'] for player in team['players']])}

Guardians:
    {team_guardians(team)}
""")
    input("Press ENTER to continue...")
    clear_screen()


def balance_teams(teams, players):
    """Evenly distribute the players to available teams"""
    while players:
        for team in teams:
            team['players'].append(players.pop())
    return True


if __name__ == '__main__':
    # Create a copy of TEAMS and PLAYERS data
    TEAMS = TEAMS
    PLAYERS = PLAYERS

    teams_copy = copy.deepcopy(TEAMS)
    players_copy = copy.deepcopy(PLAYERS)

    # Clean players data
    clean_data(players_copy)
    # Create an object for each team
    teams_objects = [{'team_name': team_name, 'players': []} for team_name in teams_copy]
    # Sort the players list by experience
    players_copy.sort(key=itemgetter('experience'))

    balance_teams(teams_objects, players_copy)
    clear_screen()
    main_menu(teams_objects)