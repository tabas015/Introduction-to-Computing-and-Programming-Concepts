def get_data_list(fname):
    valid= False
    while not valid:
        try:
            fp = open(fname)
            lines= fp.readlines()
            line = 0
            for line in lines:
                line += 1
                print(line,end='')
            fp.close()
        except FileNotFoundError:
            return -1

def hw8_index(row1_str):
    #fp = open(row1_str)
    new_list = row1_str.split(",")
            
            #a = new_list.index('hw8 Grade')
            #if new_list == a:
    print( new_list)
                
def alter_grade(row_str,idx):
    new_list = row_str.split(",")
    print( new_list)
    #a = new_list.index('idx')
    
    new_list[idx] = idx
    special_string = ",".join(new_list[idx])
    print(special_string)
    #idx1 = new_list.index(idx)
    #return (idx1)
    

    #Hint: Use .split and .join

    return
def haxx(fname):
    fp_in = open(fname)
    fp_out = open('copy_'+fname,'w')
    for line in fp_in:
        if 'secret' not in line:
            fp_out.write(line)
    fp_in.close()
    fp_out.close()
