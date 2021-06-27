def fib_sum(max_fib):
	sum2 = 0
	fib_previous = 0
	fib_now = 1
	while fib_now <= max_fib:
		# print(fib_now, fib_previous)
		fib_now, fib_previous = fib_previous + fib_now, fib_now
		if fib_now % 2 == 0:
			sum2 += fib_now
	return sum2


# divider
def is_divider(val, divider):
	if val % divider == 0:
		return True
	else:
		return False


# is prime number
def is_prime_number(val):
	divider = val

	while divider > 1:
		divider -= 1
		if is_divider(val, divider) and divider > 1:
			return False

	return True


# max prime number divider
def find_max_prime_divider(val):
	divider = val
	while divider != 1:
		divider -= 1
		if is_divider(val, divider):
			if is_prime_number(divider):
				return divider


# simple dividers
def simple_dividers(n):
	answer = []
	d = 2

	while d * d <= n:
		if n % d == 0:
			answer.append(d)
			n //= d
		else:
			d += 1

	if n > 1:
		answer.append(n)
	return answer


if __name__ == "__main__":
	print(">>> functions <<<")

