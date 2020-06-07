def get_menu_input():
	while True:
		try:
			menu_input = int(input(('\nHere are your options:\n\n'
									'1) View team stats\n'
									'2) Quit\n\n'
									'> ')))
		except ValueError:
			print('\nInvalid input.')
			continue
		else:
			if menu_input not in range(1, 3):
				print('\nInvalid input.')
				continue
		break

	return menu_input


def get_team_input():
	while True:
		try:
			team_input = int(input(('\nSelect team:\n\n'
									'1) Bandits\n'
									'2) Panthers\n'
									'3) Warriors\n\n'
									'> ')))
		except ValueError:
			print('\nInvalid input.')
			continue
		else:
			if team_input not in range(1, 4):
				print('\nInvalid input')
				continue
		break

	if team_input == 1:
		team = 'Bandits'
	elif team_input == 2:
		team = 'Panthers'
	else:
		team = 'Warriors'
	
	return team
