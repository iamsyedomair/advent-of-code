def sim(actions, part):
    boss_hp, boss_dmg = 58, 9
    hp, mana, armor = 50, 500, 0
    turn_count = 0
    mana_spent = 0
    poison_left, shield_left, recharge_left = 0, 0, 0
    my_turn = True
    spell_cost = {'M': 53, 'D': 73, 'S': 113, 'P': 173, 'R': 229}

    while True:
        # Out of actions
        if turn_count >= len(actions):
            print("Out of moves")
            return 0

        # Apply active effects
        if poison_left > 0:
            boss_hp -= 3
            poison_left -= 1
        if shield_left > 0:
            armor = 7
            shield_left -= 1
        else:
            armor = 0
        if recharge_left > 0:
            mana += 101
            recharge_left -= 1

        # Check if boss is defeated
        if boss_hp <= 0:
            return mana_spent

        if my_turn:
            # Hard mode for Part 2: lose 1 HP on each of the player's turns
            if part == 2:
                hp -= 1
                if hp <= 0:
                    return 0

            # Select and execute the action
            action = actions[turn_count]
            mana -= spell_cost[action]
            mana_spent += spell_cost[action]

            # Ensure sufficient mana
            if mana < 0:
                return 0

            # Apply selected spell effects
            if action == 'M':
                boss_hp -= 4
            elif action == 'D':
                boss_hp -= 2
                hp += 2
            elif action == 'S':
                if shield_left > 0:
                    return 0  # Cannot reapply shield while active
                shield_left = 6
            elif action == 'P':
                if poison_left > 0:
                    return 0  # Cannot reapply poison while active
                poison_left = 6
            elif action == 'R':
                if recharge_left > 0:
                    return 0  # Cannot reapply recharge while active
                recharge_left = 5

            turn_count += 1
        else:
            # Boss's turn: calculate damage dealt to player
            hp -= max(boss_dmg - armor, 1)
            if hp <= 0:
                return 0

        # Toggle turns
        my_turn = not my_turn

def iterate_actions(pos):
    actions[pos] = 'DSPRM'['MDSPR'.index(actions[pos])]
    if actions[pos] == 'M':
        if pos + 1 < len(actions):
            iterate_actions(pos + 1)

for part in (1, 2):
    actions = ['M'] * 20
    min_spent = float('inf')
    for _ in range(1000000):
        result = sim(actions, part)
        if result:
            min_spent = min(result, min_spent)
        iterate_actions(0)
    print(min_spent)
