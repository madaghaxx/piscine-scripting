import sys

if len(sys.argv) != 2:
    print("Error: wrong number of arguments")
    sys.exit(1)

num_candidates = int(sys.argv[1])
candidates = []
for i in range(num_candidates):
    print("Add a new candidate:")
    name = input("name: ")
    age = int(input("age: "))
    candidate = {"name": name, "age": age}
    candidates.append(candidate)

for candidate in candidates:
    name = candidate["name"]
    age = candidate["age"]
    
    if age < 18:
        print(f"{name} is not eligible (underaged)")
    elif age > 60:
        print(f"{name} is not eligible (over the legal age)")
    else:
        print(f"{name} is eligible")