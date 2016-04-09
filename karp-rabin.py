from rollinghashADT import rollinghash

print("String--Space--StringToBeSearched")
s1, s2 = input().split(' ')

def in_first(s1, s2):
	r1 = rollinghash()
	for i in s1[:len(s2)]: r1.append(i)

	r2 = rollinghash()
	for i in s2: r2.append(i)

	for i in range(len(s2), len(s1) + 1):
		if r1.hashval() == r2.hashval():
			if s2 == s1[i - len(s2) : i]:
				return i - len(s2)
		else:
			r1.append(s1[i])
			r1.pop_left(s1[i - len(s2)])
	return -1

print("The first occurence of s2 in s1:")
print(in_first(s1, s2))