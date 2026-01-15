import json

def merge_two(dicta):
    dicti = {}
    while True:
        print("Add a new entry:")
        key = input("key: ")
        if key in dicti:
            break
        if key == "exit":
            break
        val = input("value: ")
        try:
            value = int(val)
        except ValueError:
            break
        dicti[key] = value
    dicto = dicta.copy()
    dicto.update(dicti)

    return json.dumps(dicto)