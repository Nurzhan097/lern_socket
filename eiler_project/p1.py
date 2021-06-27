from functions import *


# Eiler project cods
def main():
	# 1
	sum1 = 0
	for i in range(0, 1001):
		# print(i)
		if i % 3 == 0 and i % 5 == 0:
			sum1 += i
	print("p1 t1:", sum1)

	# 2
	print("p1 t2:", fib_sum(4 * (10 ** 6)))

	# 3
	print("p1 t3:", find_max_prime_divider(600851475143))


if __name__ == "__main__":
	print(">>> Page #1 <<<")
	main()






























