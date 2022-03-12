
DEF = 100
BD = 0
prevAttack4 = False
prevAttack5 = False
attack4Effect = False
BD_B4_set = False
BD_B4 = 0
attack5Effect = 0
BD_B5_set = False
BD_B5 = 0
attack6Effect = False


def attack1():
	ATK = 900
	a1d = damage(ATK)
	# print("a1: " + str(a1d))
	return a1d


def attack2():
	global DEF
	global BD
	ATK = 600
	BD += BD * 0.5
	if BD > DEF:
		BD = DEF
	a2d = damage(ATK)
	# print("a2: " + str(a2d))
	return a2d


def attack3():
	global prevAttack4
	global prevAttack5
	ATK = 700
	if prevAttack4 and prevAttack5:
		ATK = 1200
	return damage(ATK)


def attack4():
	global DEF
	global BD
	global attack4Effect
	global BD_B4_set
	global BD_B4
	global prevAttack4
	ATK = 400
	prevAttack4 = True
	result = damage(ATK)
	BD += 50
	if BD > DEF:
		BD_B4_set = True
		BD_B4 = BD
		BD = DEF
	attack4Effect = True
	return result


def attack5():
	global DEF
	global BD
	global attack5Effect
	global BD_B5_set
	global BD_B5
	global prevAttack5
	ATK = 400
	prevAttack5 = True
	BD += 30
	if BD > DEF:
		BD_B5_set = True
		BD_B5 = BD
		BD = DEF
	attack5Effect = 2
	a5d = damage(ATK)
	return a5d


def attack6():
	global DEF
	global BD
	global attack6Effect
	ATK = 1200
	a6d = damage(ATK)
	# print("a6: " + str(a6d))
	attack6Effect = True
	return a6d


def damage(ATK):
	global DEF
	global BD
	global attack4Effect
	global BD_B4_set
	global BD_B4
	global attack5Effect
	global BD_B5_set
	global BD_B5
	global attack6Effect
	if attack6Effect:
		DEF = 150
		BD = 0

	result = ATK * (100 / ((DEF - BD) + 100))
	if attack4Effect:
		attack4Effect = False
		if BD_B4_set:
			BD = BD_B4
		else:
			BD = 0  # -= 50
	if attack5Effect > 0:
		attack5Effect -= 1
		if attack5Effect == 0:
			if BD_B5_set:
				BD = BD_B5
			else:
				# BD -= 30
				BD = 0
	return result


def reset():
	global DEF
	global BD
	global attack4Effect
	global BD_B4_set
	global BD_B4
	global prevAttack4
	global attack5Effect
	global BD_B5_set
	global BD_B5
	global prevAttack5
	global attack6Effect
	DEF = 100
	BD = 0
	prevAttack4 = False
	prevAttack5 = False
	attack4Effect = False
	BD_B4_set = False
	BD_B4 = 0
	attack5Effect = 0
	BD_B5_set = False
	BD_B5 = 0
	attack6Effect = False


"""
total1 = attack1() + attack5() + attack2() + attack6()
fitness1 = round(total1, 2)
print("1,5,2,6: " + str(fitness1))

reset()
total2 = attack1() + attack2() + attack4() + attack3()
fitness2 = round(total2, 2)
print("1,2,4,3: " + str(fitness2))

reset()
total3 = attack4() + attack3() + attack6() + attack3()
fitness3 = round(total3, 2)
print("4,3,6,3: " + str(fitness3))

reset()
total4 = attack2() + attack4() + attack2() + attack4()
fitness4 = round(total4, 2)
print("2,4,2,4: " + str(fitness4))
"""

# Crossovers
total12 = attack1() + attack2() + attack2() + attack6()
fitness12 = round(total12, 2)
print("1,2,2,6: " + str(fitness12))

reset()
total21 = attack1() + attack5() + attack4() + attack3()
fitness21 = round(total21, 2)
print("1,5,4,3: " + str(fitness21))

reset()
total34 = attack2() + attack4() + attack6() + attack3()
fitness34 = round(total34, 2)
print("2,4,6,3: " + str(fitness34))

reset()
total43 = attack4() + attack3() + attack2() + attack4()
fitness43 = round(total43, 2)
print("4,3,2,4: " + str(fitness43))



































