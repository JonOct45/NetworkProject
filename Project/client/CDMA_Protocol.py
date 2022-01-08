

import random

class CDMA_Protocol:

    def __init__(self):
        self.code_set = None
        self.num_users = None

    """
    Randomly samples a binary code of length len_code.
    """
    def create_code(self, len_code: int) -> list:
        coded = [random.randint(0,1) for _ in range(len_code)]
        return coded

    """
    Checks if two codes are orthogonal
    """
    def is_orthogonal(self, code1: list, code2: list) -> bool:
        code = [(code1[i]*code2[i]) for i in range(len(code1))]
        
        if sum(code) == 0:
            return True
        else:
            return False

    #Generate codes for each user
    def generate_codes(self,num_users: int, len_code: int) -> list:

        self.code_set = []
        self.num_users = num_users
        
        for i in range(num_users):
            initial_code = [0] * len_code
            initial_code[i] = 1
            self.code_set.append(initial_code)
        return self.code_set

 
    #Encoding data using the CDMA protocol with a code
    def encode(self, data: str, code: list) -> list:
        res = ''

        for char in data:
            res += ''.join(format(ord(char), '08b'))

        encodedData = [(int(bitdata)^bitcode) for bitdata in res for bitcode in code]
        
        return encodedData

  
    #Encoding a message using CDMA protocol with the set of codes.
    def encode_all(self, message: str) -> list:
        utf_len = 8 # utf-8 encoding
        encoding_length = len(message) * utf_len * len(self.code_set[0])
        volt_encoded =  encoding_length * [0] # blank encoding
        
        for code in self.code_set:
            encoded = self.encode(message, code)
            volt_encoded = [volt + enc_volt for volt, enc_volt in zip(volt_encoded, self.to_volts(encoded))]

        return volt_encoded

    """
    Decodes the frequency using the specified code
    """
    #Decoding the frequency using the specified code
    def decode(self, frequency: list, code: list) -> list:
        data = []
        data_list = []
        code = self.to_volts(code)
        code_len = len(code)

        for i in range(len(frequency) // code_len):    
            batch = frequency[i*code_len:(i*code_len)+code_len]
            decode = [b*c for b, c in zip(batch, code)]
            result = sum(decode) // code_len
           

            data.append(result)
            if len(data) == 8:
                data_list.append(data)
                data = []

        bits = [self.to_bits(data) for data in data_list]
        # print(f'bits: {bits}')
        
        b = [[str(bit) for bit in c] for c in bits]
        b = [''.join(c) for c in b ]
        # print(f'b is: {b}')
        message = bytes([int(x, 2) for x in b]).decode('utf-8')
    
        return message

    """
    Convert the data list bit to volts, takes in a list of bits
    """
    def to_volts(self, bit: list) -> list:
        volted = [-1 if volt == 1 else 1 for volt in bit]
        # print(f'The Voltages of the code is {volted}')
        return volted

    """
    Convert the data from volts to bits.
    """
    def to_bits(self, volts: list) -> list:
        result = [1 if volt < 0 else 0 for volt in volts]
        return result



# class CDMA_Protocol:

#     def __init__(self):

#         self.code1 = self.codes(2,10)

#     #Create a random code for the user
    
#     def createCode(self,len_code):
    
#         coded = [random.randint(0,1) for i in range(len_code)]

#         return coded


#     #Check if the code is orthogonal to the other codes
#     def is_orthogonal(self,code1,code2):

#         code = [(code1[i]*code2[i]) for i in range(len(code1))]
    
#         if sum(code) == 0:
            
#             print("Orthogonal")
 
#             return True
#         else:
#             return False

#     #Generating Codes for the users\
    
#     def codes(self,num_users, len_code):

#         self.code = []
#         self.num_users = num_users
#         self.first_code = self.createCode(len_code)

#         self.code.append(self.first_code)
        
#         self.tempcode = []
    

#         for i in range(num_users - 1):

#             self.ortho = False
#             while not self.ortho:

#                 self.tempcode = self.createCode(len_code)
                
#                 for code in self.code:
#                     self.ortho = self.is_orthogonal(self.tempcode, code)
#                     if self.ortho == False:
#                         break

#             self.code.append(self.tempcode)

#         print(self.code)
#         return self.code
    

#     #Encoding data from one of the users, returns a list of encoded bits
#     def encode(self,data,code):
#         res = ''

#         for char in data:
#             res += ''.join(format(ord(char), '08b'))

#         encodedData = [(int(bitdata)^bitcode) for bitdata in res for bitcode in code]
      
#         #print(f'res_len: {len(res)}\tencode_len: {len(encodedData)}\tcode_len: {len(code)}')
#         #assert(len(encodedData)==len(res)*len(code))
        
#         return encodedData

#     def encodeAll(self,message):
#         volt_encoded = len(message)*8*len(self.code[0]) * [0]
#         for code in self.code:
#             encoded = self.encode(message, code)
#             volt_encoded = [volt + enc_volt for volt, enc_volt in zip(volt_encoded, self.to_volts(encoded))]

#         return volt_encoded
    

   

#     #Convert the data list bit to volts, takes in a list of bits
#     def to_volts(self,bit):
     
#         volted = [volt if volt == 1 else -1 for volt in bit]
#         print(f'The Voltages of the code is {volted}')
#         return volted


#     def decode(self,frequency, code):
#         self.data = []
#         codeIndex = 0

#         self.code_volts = [self.to_volts(x) for x in code]

#         for volt in frequency:

#             if codeIndex == len(code):
#                 codeIndex = 0

#             result = volt*code[codeIndex]
#             self.data.append(result)

#         return self.data

#     def decode(self,frequency, code):
#         data = []
#         data_list = []
#         code = self.to_volts(code)
#         for i in range(len(frequency) // len(code)):    
#             batch = frequency[i*len(code):i*len(code)+len(code)]
            
#             decode = [b*c for b, c in zip(batch, code)]
#             result = sum(decode) // len(code)

#             data.append(result)
#             if len(data) == 8:
#                 data_list.append(data)
#                 data = []
        
#         bits = [self.to_bits(data) for data in data_list]
#         print(f'bits: {bits}')
#         b = [[str(bit) for bit in c] for c in bits]
#         b = [''.join(c) for c in b ]
#         print(f'b is: {b}')
#         message = bytes([int(x, 2) for x in b]).decode('utf-8')
    
#         return message
    
#     def to_bits(self, volts):
#         result = [volt if volt == 1 else 0 for volt in volts]
#         return result