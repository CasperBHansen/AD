def change(S, n):
	t = [[]]*(n+1)
	for i in range(1, n+1):
		for j in range(0, len(S)):
			if S[j] > i: continue
			elif t[i] == [] or len(t[i - S[j]]) + 1 < len(t[i]):
				if t[i - S[j]] != 0:
					t[i] = t[i - S[j]][:]
					t[i].append(S[j])
	return t[len(t)-1]

def main():
	S = [36,20,1]
	correct = [20,20]
	result = change(S, 40)
	print str(result) + " which is " + ("correct" if (result == correct) else "wrong")

if __name__ == "__main__":
	main()