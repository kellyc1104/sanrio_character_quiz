"""Script to run some part of my project."""

# This adds the directory above to our Python path.
#   This is so that we can add import our custom python module code into this script.
import sys
sys.path.append('../')

# Imports the three functions from my_module.functions.
from my_module.functions import question_answer # importing my question_answer function from my_module.
from my_module.functions import final_score # importing my final_score function from my_module.
from my_module.functions import max_count # importing my max_count function from my_module.

# This is a list with indexes 0-10, 11 total indexes.
# Each index contains a string, containing a question followed by 5 answer choices label a, b, c, d, e.
question_prompts = [
    "Which personality trait would best describe yourself?\
    \na. rebellious\nb. honest and kind\nc. energetic\nd. smart\ne. laid back",
    
    "What do you like to do in your free time?\
    \na. write\nb. bake\nc. play sports\nd. singing\ne. sleep",
    
    "Which style best describes yourself?\
    \na. tomboy\nb. cute\nc. athleisure\nd. classy\ne. preppy",
    
    "What's your favorite food?\
    \na. any type of meat\nb. pound cake\nc. ice cream\nd. donuts\ne. pudding",
    
    "Where would you want to travel to?\
    \na. ghost town\nb. a magical forest\nc. the city\nd. the outdoors\ne. the local bakery",
    
    "What's your favorite color?\
    \na.black\nb. pink\nc. red\nd. green\ne. yellow",
    
    "What's your fatal flaw?\
    \na. jealousy\nb. shyness\nc. clumsy\nd. indecisive\ne. procrastinating",
    
    "Which activity would you rather do?\
    \na. ride motorcycles\nb. arts and crafts\nc. go on a road trip\nd. swim\
    \ne. go to the farmer's market",
    
    "Which animal would you choose as your spirit animal?\
    \na. tapir\nb. hamster\nc. baby duck\nd. frog\ne. golden retriever",
    
    "Which movie genre do you prefer?\
    \na. romance\nb. fantasy\nc. action\nd. comedy\ne. adventure",
    
    "What is your favorite accessory?\
    \na. funny hat\nb. flower in your hair\nc. nothing\nd. bow\ne. beret",
]

# Where we initialize each count variable to 0 and an empty dictionary so they can referenced within the functions.
character_dictionary = {}
kuromi_count = 0
melody_count = 0
pochacco_count = 0
keroppi_count = 0
pompompurin_count = 0

# We loop through every question prompt so we can input an answer for each question.
for item in question_prompts:
    print(item)
    question_answer()
    
# We find the character composition and the character that has the highest count.
# Take the dictionary from final_score to apply into max_count.
final_count = final_score()
max_character = max_count(final_count)

# Here we display your character composition, in percentages.
print("Here's your Sanrio composition!\n\
Kuromi:" + str(max_character["Kuromi"]) + "%\n\
My Melody:" + str(max_character["My Melody"]) + "%\n\
Pochacco:" + str(max_character["Pochacco"]) + "%\n\
Keroppi:" + str(max_character["Keroppi"]) + "%\n\
Pompompurin:" + str(max_character["Pompompurin"]) + "%")