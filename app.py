import copy
import os

from operator import itemgetter

from constants import PLAYERS, TEAMS


def clean_data(data):
    """Cleaning function for 'PLAYERS' data"""
    DATA_COPY = copy.deepcopy(data)
    for item in DATA_COPY:
        item['height'] = int(item['height'].split(" ")[0])
        if item['experience'] == 'YES':
            item['experience'] = True
        else:
            item['experience'] = False
        item['guardians'] = item['guardians'].split(" and ")
    return DATA_COPY


# Create a copy of TEAMS and PLAYERS data
TEAMS = copy.deepcopy(TEAMS)

PLAYERS = clean_data(PLAYERS)

# Create an object for each team
TEAMS = [{'team_name': team_name, 'players': []} for team_name in TEAMS]
# Sort the PLAYERS list by experience
PLAYERS.sort(key=itemgetter('experience'))


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


def main_menu():
    """Main menu logic"""
    while True:
        draw_main_menu()
        menu_selection = input("Enter an option: ").lower()
        if menu_selection == 'a':
            clear_screen()
            team_selection_menu()
        elif menu_selection == 'b':
            clear_screen()
            print("Thanks for using the Basketball Team Stats tool! Bye! \n")
            break
        else:
            clear_screen()
            print("That wasn't a valid selection. Please try again.")
            continue
    


def draw_team_menu():
    """Draw the team stats menu and return the user's menu selection"""
    print("Which team's stats would you like to view? \n")
    for count, team in enumerate(TEAMS):
        print(f"  {count+1}) {team['team_name']}")
    print("")



def team_selection_menu():
    """Team selection menu logic"""
    while True:
        draw_team_menu()
        menu_selection = input("Enter an option: ").lower()
        try:
            if int(menu_selection) in range(1, len(TEAMS)+1):
                display_team_stats(TEAMS[int(menu_selection)-1])
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
Average height: {average_team_height(team)}

Players on Team:
    {", ".join([player['name'] for player in team['players']])}

Guardians:
    {team_guardians(team)}
""")
    input("Press ENTER to continue...")
    clear_screen()


def balance_teams(players_list):
    """Evenly distribute the players to available teams"""
    while players_list:
        for team in TEAMS:
            team['players'].append(PLAYERS.pop())
    return True


if __name__ == '__main__':
    balance_teams(PLAYERS)
    clear_screen()
    main_menu()