# dict = {"cat": "white", "dog": "black"}
# print(len(dict))
# print(dict["cat"])
# print(dict.get("dog"))
# dict["dog"]= "brown"
#
# dict["parrot"]= "red-blue"
#
# print(dict)

# alph = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# print(alph.keys())
# print(alph.values())
#
# for key in alph:
#     print(f"key - {key}, val - {alph[key]}")
#
# # returns tuple
# for key, value in alph.items():
#     print(key, value)

# alphabet = {'a': 1, 'b': 2, 'c': 3}
#
# alphabet["test"] = alphabet.pop("a")
# print(alphabet)

# сортиране по стойност !!!

a = {'a': 100, 'b': 2, 'c': 3}
# ако е нула сортира по ключ, 1 по стойност
print(sorted(a.items(), key=lambda kvp: kvp[0]))
print(sorted(a.items(), key=lambda kvp: kvp[1]))
# само ако стойноста е int:
print(sorted(a.items(), key=lambda kvp: -kvp[1]))
