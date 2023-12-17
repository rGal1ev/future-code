first_module_test = [
    {
        "id": 1,
        "answer": """a=int(input())
b=int(input())
S=a+b
print(S)"""
    },

    {
        "id": 2,
        "answer": """a=int(input())
b=int(input())
c=int(input())
S = 2 * (a * b + b * c + a * c)
print(S)"""
    },
    {
        "id": 3,
        "answer": """a=int(input())
b=int(input())
c=int(input())
V = a * b * c
print(V)"""
    },
    {
        "id": 4,
        "answer": """a=int(input())
b=int(input())
S = (a + b) / 2
print(S)"""
    },
    {
        "id": 5,
        "answer": """a=int(input())
b=int(input())
S = (a + b) * 2
print(S)"""
    },
    {
        "id": 6,
        "answer": """a=int(input())
b=int(input())
S = 0
if a != b:
	if a > b:
		S = a - b
	else:
		S = b - a
print(S)"""
    },
    {
        "id": 7,
        "answer": """n = int(input())
for i in range(n):
	print(i)
"""
    },
]
