import math

#fCost = 1.1 * L * D^1.5
LDs = {
	7 : 24,
	9 : 12,
	10 : 20,
	17 : 16,
	13 : 16
}

fCostS = 0 #1.1 * (7 * 12^1.5 + 9 * 20^1.5 + 10 * 16^1.5 + 17 * 24^1.5 + 13 * 12^1.5)
yS = 0
for L, D in LDs.items():
	fCostS += L * pow(D, 1.5)
	yS += pow(L, 0.5) / pow(D, 2.5)
fCostS *= 1.1
yS *= 10000

CS = fCostS + yS
fitness = 1/CS
print("fCostS: " + str(round(fCostS, 6)))
print("CS: " + str(round(CS, 6)))
print("fitness: " + str(round(fitness, 6)))