#string concatenation is how we put strings together to create a new string.

youtuber = "bryan beck" #some string variable

# a few wats to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")#cleaninest way to express string concatenation
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
fame_person = input("Fame_person: ")
madlib = f"I love coding and application development so {adj}! Software development is a {verb1} and I strongly recommend you {verb2} as well like you want to become {fame_person}!"

print(madlib)