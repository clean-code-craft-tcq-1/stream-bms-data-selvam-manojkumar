import unittest
import Receiver


class ReceiverTest(unittest.TestCase):
  #Test for Sum of last n values
  def test_for_sum_of_last_value(self):#Positive senario ::sum of last value::n =1
    test_input=[1,2,3]
    self.assertTrue(Receiver.sum_of_last_n_values(test_input,1)==3)#Returns->3
    
  def test_for_sum_of_last_two_values(self):#Positive senario :: sum of last two value::n = 2
    test_input=[1,2,3]
    self.assertTrue(Receiver.sum_of_last_n_values(test_input,2)==5)#Returns->2+3

  def test_for_sum_of_zero_values(self):#Negative senario :: last n values,where n=0
    test_input=[1,2,3]
    self.assertTrue(Receiver.sum_of_last_n_values(test_input,0)==0)#Returns->0[no last elements]

  def test_for_input_value_grater_than_length_list(self):#Negative senario :: last n values,where n grater than length of input_list
    test_input=[1,2,3]
    self.assertTrue(Receiver.sum_of_last_n_values(test_input,5)==0)#Returns->0[since 'n' is greater then length of list]

  def test_for_sum_of_values_in_empty_List(self):#Negative senario :: Empty list
    test_input=[]
    self.assertTrue(Receiver.sum_of_last_n_values(test_input,3)==0)#Returns->0[Empty list]
 
  def test_for_sum_of_negative_values(self):#Positive senario 
    test_input=[-1,-2,-3]
    self.assertTrue(Receiver.sum_of_last_n_values(test_input,3)==-6)#Returns->-1-2-3[Empty list]
    
 
  #Test for Simple moving average of the last n values
  def test_for_simple_moving_average_of_last_value(self):#Positive senario ::verage last value
    test_input=[1,2,3]
    self.assertTrue(Receiver.simple_moving_average_of_n_values(test_input,1)==3) #Returns->3/1
    
  def test_for_simple_moving_average_of_last_five_value(self):#Positive senario ::average_of_last_two_value
    test_input=[1,2,3,4,5]
    self.assertTrue(Receiver.simple_moving_average_of_n_values(test_input,5)==3)#Returns->(1+2+3+4+5)/5::2.5
 
  def test_for_simple_moving_average_of_value_less_than_one(self):#Negative senario :: last n values,where n is less then 1
    test_input=[1,2,3]
    self.assertTrue(Receiver.simple_moving_average_of_n_values(test_input,0)== None)#Returns->None
    
 
  #Test for streaming receiver output
  def test_receiver_output_for_empty_stream(self):#Negative senario :: when there is no attribute_database
    attribute_database ={}#Invalid Input->Empty dict BMS attribute data base
    Receiver.stream_receiver_output(attribute_database)
    self.assertTrue(Receiver.wrapper.stream.count==0)#Checking stream->print is called zero times

  def test_receiver_output_for_one_attribute_stream(self):#Positive senario :: when there is one attribute_database
    attribute_database ={"Temperature": [10,20] }#One attribute :: 2 reading
    Receiver.stream_receiver_output(attribute_database)
    self.assertTrue(Receiver.wrapper.stream.count==2)#Checking stream->print is called 2 times[1 for attribute's values + 1 for table header]
   
  def test_receiver_output_for_more_than_one_attribute_stream(self):#Positive senario
    #when there is three attribute_database
    #simple moving average of the last 5 values->Range=5 
    attribute_database ={"Temperature": [10,20,30,40],#Temperature::first attribute::4 reading [Range-1]
                     "SOC": [12,22,32,42,52], #state of Charge::Second attribute::5 reading [Range]
                     "Charg_rate" :[13,23,33,43,53,63]#Charging rate::third attribute::5 reading [Range+1]
                     }
    Receiver.stream_receiver_output(attribute_database)
    self.assertTrue(Receiver.wrapper.stream.count==4)#Checking stream->print is called 4 times [3 for attribute's values + 1 for table header]
    

  #Test extract attribute list from input stream
  def test_not_to_extract_attribute_list_for_empty_line(self):#Empty line
    input_line=""#test_input
    expected_output=[]#Empty list
    self.assertTrue(Receiver.extract_attribute_list(input_line)==expected_output) #No attribute list is extracted  
    
  def test_to_extract_one_attribute_list(self):#line->one attribute
    input_line='{"Temperature": 10 }'#test_input
    expected_output=[["Temperature", 10.0]]
    self.assertTrue(Receiver.extract_attribute_list(input_line)==expected_output) #Extact one attribute list

  def test_to_extract_multiple_attribute_list(self):#line->multiple attribute
    input_line='{"Temperature": 10 , "SOC": 11.0 ,wrong or in-valid attribute formate, "Charg_rate": 12.32}'#test_input
    expected_output=[["Temperature", 10.0] ,#first attribute::int 
                ["SOC", 11.0 ] ,#Second attribute::float 
                ["Charg_rate", 12.32]#third attribute::float 
                ] 
    self.assertTrue(Receiver.extract_attribute_list(input_line)==expected_output) #three attribute are extracted

  #Test store extracted attribute list to attribute database
  def test_not_to_store_extracted_attribute_database_for_empty_attribute_list(self):#Negative senario 
    attribute_list=[]#test_input
    attribute_database={}#test_input+output ::Pass by reference
    Receiver.store_extracted_attribute_list_to_attribute_database(attribute_list,attribute_database)
    self.assertFalse(bool(attribute_database)) #No attribute is added to attribute_database
    
  def test_add_extracted_attribute_database_for_new_attribute_list(self):#Positive senario ::Add new atribute to attribute_database
    attribute_list=[["Temperature",10]]#test_input
    actual_attribute_database={}#test_input+output ::Pass by reference
    expected_attribute_database={"Temperature":[10]}#Expected output
    Receiver.store_extracted_attribute_list_to_attribute_database(attribute_list,actual_attribute_database)
    self.assertTrue(actual_attribute_database==expected_attribute_database) #New attribute is added to attribute_database

  def test_append_extracted_attribute_database_for_attribute_list(self):#Positive senario ::append read atribute  to attribute_database
    attribute_list=[["Temperature",20],#test_input->Append attribute
                    ["SOC",30]]#test_input->add attribute
    actual_attribute_database={"Temperature":[10]}#test_input+output ::Pass by reference
    expected_attribute_database={"Temperature":[10,20],#20 will be appended to Temperature #Expected output
                             "SOC":[30]}#SOC will be added to attribute_database with 30 
    Receiver.store_extracted_attribute_list_to_attribute_database(attribute_list,actual_attribute_database)
    self.assertTrue(actual_attribute_database==expected_attribute_database) #New attribute is added to attribute_database

                   
if __name__ == '__main__':
  unittest.main()
