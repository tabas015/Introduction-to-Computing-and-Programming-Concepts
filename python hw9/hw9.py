
#Name = Fahia Tabassum
import random

#===========================================================================================================
# Purpose:
#   making a list of the first word in every sentence in that file, in order, including duplicates
# Input Parameter(s):
#   a string representing the name of a file
# Return Value(s):
#  a list of the first word in every sentence in that file, in order, including duplicates.
#============================================================================================================

def first_words(fname):
    fp = open(fname)
    text = fp.read()
    
    print(text)
    first_letter = []
    for line in text:
        a = line.split(' ')
        b = a[0]
        first_letter.append(b)
        fp.close()

    return first_letter
        

#===========================================================================================================
# Purpose:
#     getting a dictionary where the keys are each distinct word in the file (case matters),
#     and the value for any given key is a list of every word that follows that key
#     anywhere in the file, in order, including duplicates.
# Input Parameter(s):
#   a string representing the name of a file
# Return Value(s):
#     a dictionary where the keys are each distinct word in the file (case matters),
#     and the value for any given key is a list of every word that follows that key
#     anywhere in the file, in order, including duplicates.
#===========================================================================================================

def next_words(fname):
    fp = open(fname)
    text = fp.readlines()
    my_dic = {}

    first_letter = []
    d = first_letter

    for line in text:
            a = line.split(' ')
            for i in a:
                if i == '.\n':
                    i = '.'
                first_letter.append(i)
                
    for i in range(0,len(d)-1):
        key = d[i]
        if key != '.':
            val = d[i+1]
            if key not in my_dic:
                my_dic[key] = [val]
            else:
                my_dic[key].append(val)
    fp.close()
    return my_dic

    
#=====================================================================================================
# Purpose:
# Creating sentences one per line, based on that file, as described above.
# Input Parameter(s):
# a string representing the name of a file
# Return Value(s):
# prints 10 ‘sentences’, one per line, based on that file, as described above.
#=====================================================================================================

def fanfic(fname):
    first_word = first_words(fname)
    next_word = next_words(fname)
    paragraph = ''
    for line in range(10):
        a = random.choice(first_word)
        m = random.choice(next_word[a])
        sentence = ' '
        sentence = a + ' ' 
        while m != '.':
            sentence += m + ' '
            m = random.choice(next_word[m])
        print (sentence + '.')
            
#====================================================================================================
# Purpose:
#   Finding the memory usage of the file
# Input Parameter(s):
#  a nested dictionary representing a directory as explained above
# Return Value(s):
#   the total memory in bytes (an integer)
#===================================================================================================
def  total_txt_size(directory):
    my_dictionary = directory
    total_memory = 0
    for key in my_dictionary:
        if key[-4:] == '.txt':
            total_memory += my_dictionary[key]
        elif type(my_dictionary[key]) == dict:
            total_memory += total_txt_size(my_dictionary[key])
    return total_memory
    
