P1 = [16, 12, 24, 20, 12]
P2 = [20, 12, 16, 12, 24]
J1 = []
J2 = []
i = 0
lam = 0.75
for p in P1:
	j = (lam * p) + ((1 - lam) * P2[i])
	if j not in P1:
		temp_P1 = P1.copy()
		temp_P1.sort(reverse=True)
		for t in temp_P1:
			if t < j:
				j = t
				break
	J1.append(j)
	i += 1
i = 0
for p in P2:
	j = ((1 - lam) * P1[i]) + (lam * p)
	if j not in P2:
		temp_P2 = P2.copy()
		temp_P2.sort()
		for t in temp_P2:
			if t > j:
				j = t
				break
	J2.append(j)
