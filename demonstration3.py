def add(a, b): return a + b

tests = [(2, 3, 5), (0, 0, 0), (-1, 1, 0), (2, 2, 5)]

for i, (a, b, e) in enumerate(tests, 1):
    print(f"Test {i}: {'PASS' if add(a, b) == e else 'FAIL'}")
