"""A collection of functions for doing my project."""

# Where we initialize each count variable to 0 and an empty dictionary so they can referenced within the functions.
character_dictionary = {}
kuromi_count = 0
melody_count = 0
pochacco_count = 0
keroppi_count = 0
pompompurin_count = 0

def question_answer():
    """Stores a count of how many answer inputs correpond to each character.
    
    Parameters
    ----------
    none
    
    Returns
    -------
    answer : int
        The result of increasing character count by one each
        time an answer input corresponds to the character, and storing
        each character count as a separate variable.
    
    """
    
    # Here we make the character counts global variables so they can be used in the functions.
    global kuromi_count
    global melody_count
    global pochacco_count 
    global keroppi_count 
    global pompompurin_count
    
    # A while loop lets us restart the loop if the input isn't a, b, c, d, or e.
    while True:
        
        # If input isn't a single letter a, b, c, d, or e, output an error message.
        # Break after the answer matches an if/elif statement so the loop can restart for the next question.
        question_answer = input()
        if question_answer == "a":
            kuromi_count += 1
            break
            
        elif question_answer == "b":
            melody_count += 1
            break
            
        elif question_answer == "c":
            pochacco_count += 1
            break
            
        elif question_answer == "d":
            keroppi_count += 1
            break
            
        elif question_answer == "e":
            pompompurin_count += 1
            break
            
        else:
            print("Oops, that's out of bounds! Please input a, b, c, d, or e!")
        continue
        
        
def final_score():
    """
    Calculates the character composition, in percentages.
    
    Parameters
    ----------
    none 
    
    Returns
    -------
    answer : int or float
        The result of character counts divided by the total 
        number of questions, then multiplied by 100 to yield a
        percentage value.
    
    """
    
    # Declare these global variables again so they can be updated inside the function.
    global character_dictionary
    global kuromi_count
    global melody_count
    global pochacco_count 
    global keroppi_count 
    global pompompurin_count
    
    # This calculates the character count over the total counts, from decimal to percentage form.
    kuromi_score = kuromi_count / 11 * 100
    melody_score = melody_count / 11 * 100
    pochacco_score = pochacco_count / 11 * 100
    keroppi_score = keroppi_count / 11 * 100
    pompompurin_score = pompompurin_count / 11 * 100

    # We use a dictionary so the max_count function can reference a character name key from the max_score it calculates.
    temporary_dictionary = {"Kuromi": kuromi_score, 
                        "My Melody": melody_score, 
                        "Pochacco": pochacco_score, 
                        "Keroppi": keroppi_score, 
                        "Pompompurin": pompompurin_score 
                        }
    
    # Assign the temporary dictionary to the global dictionary so it can be used in the next function.
    character_dictionary = temporary_dictionary
    return character_dictionary
      
    
def max_count(dictionary):
    """
    Comments on your top character.
    
    Parameters
    ----------
    dictionary: dict
        The source used to extract the maximum character count
        and maximum character count name from.
    
    Returns
    -------
    answer : str
        A sentence that results from concantenating two string 
        statements and the maximum character count name.
    
    """
    
    # Intialize variable as an string type so it can be concantenated as a string.
    max_key = ""
    
    # Here we loop through each key in the dictionary to find the largest value in the dictionary.
    for key in dictionary:
        
        # Any positive count will change the maximum count value.
        max_count = 0
        
        # The maximum count will only change if a dictionary value is greater than the maximum count.
        if dictionary[key] > max_count:
            max_count = dictionary[key]
            
            # Retrive the key corresponding to the maximum value's key.
            max_key = key
            
    # Display which character you are most like.
    print("The results are out! You are most like " + max_key + "!")
    return character_dictionary