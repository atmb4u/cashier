import unittest
from hashlib import md5
from cashier import Cashier ,cache

class cashier_tests(unittest.TestCase):
    """class for running unit tests on Cashier"""
    def setUp(self):
	self.cache_inst = Cashier(file_name="unit_testing")
    	self.cache_inst.clear()
    
    def test_CRUD_operation(self):
  	    """objective :to perform CRUD operations using cashier"""    
    
   	    test_set_1=['test_string_1','special_char_str ^@#$%&#*#%$^',\
              "big string jksaldjflkjlkjgn,zmnc,vmn,msnfm,mn,mn"]
   	    test_set_2=['test_string_2','special_char_str^@#$%&#*#%$^',\
              "big string jksaldjflkjlkjgn,zmnc,mn,msnfm,mn,mn"]
            try :
		  """create and read operations"""
		  for val in test_set_1 :
			  key=md5(val.encode('utf8')).hexdigest()
			  self.cache_inst.set(key,val)
			  assert self.cache_inst.get(key) in test_set_1,"missing value "
        
  	          """update operation"""
		  for val in test_set_1:
			  index_val=test_set_1.index(val)
			  key=md5(val.encode('utf8')).hexdigest()
			  self.cache_inst.set(key,test_set_2[index_val])
			  assert self.cache_inst.get(key) in test_set_2,"missing value"
        
	  	  """delete operation """
	  	  for val in test_set_1:
	  		key=md5(val.encode('utf8')).hexdigest()
	  		self.cache_inst.delete(key)
        
    	    except Exception as e:
      			print("something went wrong :",str(e))
      

if __name__ =="__main__" :
  unittest.main()

