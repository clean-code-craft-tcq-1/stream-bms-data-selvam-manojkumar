#-------------------------------------------------------------------------------------------
#Includes 
#-------------------------------------------------------------------------------------------
import wrapper #use for Mocking
import re
import sys

#-------------------------------------------------------------------------------------------
#Functions 
#-------------------------------------------------------------------------------------------
#extract attribute list from input stream
def extract_attribute_list(input_stream_line):
    attribute_list=[]
    split_raw_data =re.split(",",input_stream_line)
    for raw_data in split_raw_data:
        matchObj = re.search( r'\"(.*)\"\s*:\s*([\d+.\d+]+|\d+)', raw_data, re.M|re.I)
        if(None!=matchObj):
           attribute_list.append([matchObj.group(1),float(matchObj.group(2))])
    return attribute_list

#store extracted attribute list to attribute database
def store_extracted_attribute_list_to_attribute_database(attribute_list,attribute_database):#call by reference->attribute_database
    for attribute in attribute_list:
        if(attribute[0] in attribute_database.keys()):
            attribute_database[attribute[0]].append(attribute[1])#Append value to attribute
        else:
            attribute_database[attribute[0]]=[attribute[1]]#Add new attribute with value
   
#Print receiver's output
def stream_receiver_output(attribute_database):
    wrapper.stream.count=0#Clearing wrapper counter for stream->print[Used for Mocking->Test]
    if(bool(attribute_database)):#Check if `attribute_database` is empty
        wrapper.stream ("{:<15} {:<10} {:<10} {:<15}".format('Attribute','Min','Max','Simple moving average of the last 5 values'))#wrapper:stream->print
        for attribute in attribute_database.keys():
            wrapper.stream ("{:<15} {:<10} {:<10} {:<15}".format(attribute, min(attribute_database[attribute]), max(attribute_database[attribute]), simple_moving_average_of_n_values(attribute_database[attribute],5)))#wrapper:stream->print

#Simple moving average of the last n values
def simple_moving_average_of_n_values(list, n):#returns None if n is not greater than zero  
    if(n>0):#Check for Divide by Zero error
        return (sum_of_last_n_values(list, n)/n)
    
#Sum of last n values
def sum_of_last_n_values(list, n):
    sum_of_n=0
    if((len(list)-(n-1))>0):
        for i in range(abs(len(list)-n),len(list)):
            sum_of_n=sum_of_n+list[i]
    return sum_of_n

#-------------------------------------------------------------------------------------------
#Main  
#-------------------------------------------------------------------------------------------              
if __name__ == '__main__':
    attribute_database ={}#key->Attribute,value->[,,,,]
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        attribute_list=extract_attribute_list(line)
        store_extracted_attribute_list_to_attribute_database(attribute_list,attribute_database )
        stream_receiver_output(attribute_database) 


