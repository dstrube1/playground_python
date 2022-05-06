import math

# https://gatech.instructure.com/courses/225196/pages/33-decision-tree-quiz-2-answer?module_item_id=2197174

def get_entropy(q):
	if q == 1:
		return 0
	return -(
		(q * math.log2(q)) + 
		((1 - q) * math.log2(1-q))
		)

q = 9/14
total_entropy = get_entropy(q)
print(round(total_entropy, 3))

# TODO: loop
pk_plus_nk_over_p_plus_n = 5/14
q = 2/5
entropy = get_entropy(q)
outlook_sunny_remainder = pk_plus_nk_over_p_plus_n * entropy

pk_plus_nk_over_p_plus_n = 4/14
q = 4/4
entropy = get_entropy(q)
outlook_overcast_remainder = pk_plus_nk_over_p_plus_n * entropy

pk_plus_nk_over_p_plus_n = 5/14
q = 3/5
entropy = get_entropy(q)
outlook_rain_remainder = pk_plus_nk_over_p_plus_n * entropy

remainder = outlook_sunny_remainder + outlook_overcast_remainder + outlook_rain_remainder

gain = total_entropy - remainder
print(round(gain, 3))
