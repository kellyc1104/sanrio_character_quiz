#!/usr/bin/env python
# coding: utf-8

# # Sanrio Character Quiz

# Welcome to the Sanrio Character Quiz! Find out which Sanrio character you are based on this quiz!
# 
# This quiz consists of 11 multiple choice questions; for each question displayed, type in 'a', 'b', 'c', 'd', or 'e' as your answer. A Sanrio character composition will be displayed upon completion of the quiz, as well as which Sanrio character you most resemble. The composition includes percentages of how similar you are to each Sanrio character. 

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[ ]:


from my_module.functions import question_answer # importing my question_answer function from my_module.
from my_module.functions import final_score # importing my final_score function from my_module.
from my_module.functions import max_count # importing my max_count function from my_module.


# In[ ]:


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


# In[ ]:


# We loop through every question prompt so we can input an answer for each question.
for item in question_prompts:
    print(item)
    question_answer()
    
# We find the character composition and the character that has the highest count.
# Take the dictionary from final_score to apply into max_count.
final_count = final_score()
max_character = max_count(final_count)

# Here we display your character composition, in percentages.
print("Here's your Sanrio composition!\nKuromi:" + str(max_character["Kuromi"]) + "%\nMy Melody:" + str(max_character["My Melody"]) + "%\nPochacco:" + str(max_character["Pochacco"]) + "%\nKeroppi:" + str(max_character["Keroppi"]) + "%\nPompompurin:" + str(max_character["Pompompurin"]) + "%")
