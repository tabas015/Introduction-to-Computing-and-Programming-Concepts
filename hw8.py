## Your Name = Fahia Tabassum
## Your x500

#Part 1: get_data_list
#=====================================================================
# Purpose:
#   Extract the data from a CSV file as a list of rows
# Input Parameter(s):
#   fname is a string representing the name of a file
# Return Value:
#   Returns a list of every line in that file (a list of strings)
#   OR returns -1 if the file does not exist
#====================================================================
def get_data_list(fname):
    valid= False
    while not valid:
        try:
            fp = open(fname)
            valid = True
            line = fp.readlines()
            return line
            
        except FileNotFoundError:
            return -1
    
#Part 2: hw8_index
#=================================================================
# Purpose:
#   Determine which column stores the grades for hw8
# Input Parameter(s):
#   row1_str is a string containing the first row of data 
#   (the column titles) in the CSV file
# Return Value:
#   Returns the index of the column labelled 'hw8 Grade' (an integer)
#   OR returns -1 if there is no column labelled 'hw8 Grade'
#=================================================================
def hw8_index(row1_str):
    try:
        new_list = row1_str.split(",")
        a = new_list.index('hw8 Grade')
        return a
    except ValueError:
        return -1
    

#Part 3: alter_grade
#=================================================================
# Purpose:
#   Change the hw8 grade in your row string to '40'
# Input Parameter(s):
#   row_str is a string containing any row of data from the CSV file
#   idx is an index for the column you want to alter
# Return Value:
#   Returns a string identical to row_str, except with the column
#   at the given index changed to '40'
#=================================================================

def alter_grade(row_str,idx):
    new_list = row_str.split(",")
    new_list[idx] = '40'
    row_str = ",".join(new_list)
    return row_str

#Part 4: haxx
#===================================================================
# Purpose:
#   Alters a gradebook CSV file so that your score on hw8 is '40'
# Input Parameter(s):
#   fname is the file name of the gradebook file
# Return Value:
#   Returns False if the file isn't open
#   Returns False if the file doesn't contain a 'hw8 Grade' column
#   Otherwise, returns True
#==========================================
def haxx(fname):
    valid = False
    try:
        fp_in = get_data_list(fname)
        fp_out = open('copy_'+fname,'w')
        row1_str = fp_in[0]
        idx = hw8_index(row1_str)
        if idx == -1:
            return valid
        for line in fp_in:
            if 'Fahia Tabassum' not in line:
                fp_out.write(line)
            elif 'Fahia Tabassum' in line:
                fp_out.write(alter_grade(line,idx))

        fp_out.close()
        valid = True
        return valid 
            
    except TypeError:
        return valid
        
    except FileNotFoundError:
        
        return valid

   
            
