#prompt user for words
#noun words
noun1 = input("Enter a noun (e.g., spoon, kettle): ")

#verb words
verb1 = input("Enter a verb (e.g., run, laugh): ")

#adjective verbs
adj1 = ("Enter an adjective (e.g., mad, dangerous): ")

#place: specific location
place1 = input("Enter a specific place (e.g., the lake, mountain): ")

#another adjective
adj2 = input("Enter a second adjective: ")

#plural noun
plural_noun1 = input("Enter a plural noun (e.g., shoes, oranges): ")

#ADD CONDITIONAL TOUCHES (IF/ELSE)

conditional_phrase = ""

# check if the user's first adjective is "scary"
if adj1.lower() == "scary":
    conditional_phrase = "It was the most terrifying discovery of the year!"
else:
    conditional_phrase = "The discovery brought joy and laughter to everyone."

#NUILD AND DISPLAY THE STORY
story = f"""
-------------------------------------------
*** YOUR COMPLETE MAD LIBS STORY ***
-------------------------------------------
The {adj1} adventurer decided to explore the ancient {noun1}.
He planned to {verb1} all the way to {place1}, but he found a
hidden chamber instead. This chamber contained a collection of
{adj2} {plural_noun1}.

{conditional_phrase}

He knew he would be famous!
"""

print(story)
