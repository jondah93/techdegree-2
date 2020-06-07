from constants import TEAMS, PLAYERS
import prints as p
import copy


def clean_data(players):
	for key in players:
		key['experience'] = (True if key['experience'] == 'YES' else False)
		key['height'] = int(key['height'][:2])
		key['guardians'] = key['guardians'].split(' and ')


def group_by_xp(players):
	'''Returns lists exp, inexp of all experienced, inexperienced players'''
	exp = [player for player in players if player['experience']]
	unexp = [player for player in players if not player['experience']]

	return exp, unexp


def balance_teams(players, teams):
	'''Populates the teams evenly with experienced and unexperienced players'''
	exp, inexp = group_by_xp(players)
	team_rosters = {team : [] for team in teams}

	i = 0
	for j in range(max(len(exp), len(inexp)) // len(TEAMS)):
		for team in team_rosters.keys():
			try:
				team_rosters[team].append(exp[i])
			except IndexError:
				pass
			try:
				team_rosters[team].append(inexp[i])
			except IndexError:
				pass
			i += 1

	return team_rosters


def get_average_height(teams, team):
	total = sum(player['height'] for player in teams[team])
	
	return str(round((total / len(teams[team])), 1)) + '"'


def get_guardians(teams, team):
	'''Returns the teams guardians as a comma separated string'''
	return ', '.join([', '.join(player['guardians']) for player in teams[team]])


def get_experience(teams, team):
	exp = sum(player['experience'] is True for player in teams[team])
	inexp = sum(player['experience'] is False for player in teams[team])
	
	return exp, inexp


def get_roster(teams, team):
	'''Returns a team roster in a comma separated string'''
	return ', '.join([player['name'] for player in teams[team]])


if __name__ == '__main__':
	players_mod = copy.deepcopy(PLAYERS)
	teams_mod = copy.deepcopy(TEAMS)
	clean_data(players_mod)
	balanced_teams = (balance_teams(players_mod, teams_mod))

	print('\nBASKETBALL TEAM STATS TOOL\n\n---- MENU ----')

	while True:
		if p.get_menu_input() == 1:
			team = p.get_team_input()
			print('\nTeam: %s\n\nStats:\n----------''' % team)
			print('Total players: %s' % len(balanced_teams[team]))
			print('''Total experienced: %s\nTotal inexperienced: %s''' % get_experience(balanced_teams, team))
			print('Average height: %s' % get_average_height(balanced_teams, team))
			print('\nPlayers on the team:\n%s' % get_roster(balanced_teams, team))
			print('\nGuardians:\n%s' % get_guardians(balanced_teams, team))
		else:
			# If the user selects Quit from the menu.
			break

		input('\nPress ENTER to continue...')
