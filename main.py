# enter values
name = input("Enter a name: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
part_of_body = input("Enter a part of the body: ")
animals = input("Enter name of animal(Plural):")
adverb = input("Enter an adverb: ")
noun = input("Enter a noun: ")
colour = input("Enter a colour: ")

# set a story
story = f"Most doctors agree that {verb} a/an {adjective} form of exercise. {verb} a bicycle enables you to develop your {part_of_body} muscles as well as {adverb} increase the rate of a {part_of_body} beat. More {noun} around the world {verb} bicycles than drive {animals}. No matter what kind of {noun} you {verb}, always be sure to wear a/an {adjective} helmet. Make sure to have {colour} reflectors too!"

# print everything
print("Hello", name, "! here is your Mid Libs Story...")
print(story)