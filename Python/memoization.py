def fibbonacci(n):
    f = {}
    if ( n in f.keys() ):
        return f[n]
    f[n] = f[n-1] + f[n-2]
    return f[n]

def fibbonacci(s1, s2, n):
	f = [s1, s2, 0]
	for x in range(min(s1, s2), n):
		f[2] = f[0] + f[1]
		f[0] = f[1]
		f[1] = f[2]
	return f[2]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    f = {}
    if ( n in f.keys() ):
        return f[n]
    f[n] = n*factorial(n-1)
    return f[n]
