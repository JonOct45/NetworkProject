
# In this file you can practice with Python. This is not graded nor handed. 

# print
# variables (static and dynamic)
# user input
# if statements 
# loops (find missing element in O(n))
# list, dictionaries and tuples 
# functions 
# classes
# inheritance 
import random
import math
# from Project.server import CDMA_Protocol

from server.CDMA_Protocol import CDMA_Protocol as CDMA

import hashlib

print("------------------BYTE AND HEX TESTING -------------------------")
message = "Hello World"

byte_array = bytearray(message, 'utf-8')

byte_list = []
print(byte_array)
for byte in byte_array:
    binary = bin(byte)
    for bit in binary:

        byte_list.append(bit)

print(byte_list)

# print(message.encode()[0])

def createCode(len_code):
    
    # code = []

    # for i in range(len_code):

    #     code.append(random.randint(0,1))

    code = [random.randint(0,1) for i in range(len_code)]

    return code
 
# code = createCode(10)
# print(code)
# code1 = createCode(10)
# print(code1)

# my_list = range(10, 17)
# my_list
# [10, 11, 12, 13, 14, 15, 16]

# summed = sum(my_list)

# print(summed)
# summed = sum(code)
# print(summed)
def check_ortho(code1, code2):

    # code = []

    # for i in range(len(code1)):
    
    #     ammount = code1[i] * code2[i]

    #     code.append(ammount)
    code = [(code1[i]*code2[i]) for i in range(len(code1))]
    
    if sum(code) == 0:
        print("Orthogonal")
        return True
    else:
        return False


         

def codes(num_users, len_code):

    code = []

    first_code = createCode(len_code)
    code.append(first_code)
    tempcode = []
    

    for i in range(num_users - 1):

        ortho = False
        while not ortho:

            tempcode = createCode(len_code)
            ortho = check_ortho(tempcode, code[i])
            
        code.append(tempcode)

    print(code)
  
def encode(data,code):

    encodedtest = [(bitdata^bitcode) for bitdata in data for bitcode in code]

    return encodedtest


def to_volts(bit):
        
    # if int(bit) == 1:
    #     return 1
    # else:
    #     return -1
    volted = [volt if volt == 1 else -1 for volt in bit] 
    return volted


def encodeAll(encodedData):

    frequency = [0]*len(encodedData)
        
    for data in encodedData:
        volted_data = to_volts(data)

        for i in range(len(volted_data)):

            frequency[i] += volted_data[i]
    print(sum(frequency))
    return frequency

data_list = codes(10,10)
print(data_list)
print()

"""
GCD and Prime Testing Code. 
"""
def generatePrime(x):

    while True:
        prime = random.randint(2,x)
        if relativePrime(prime, x):
            return prime

def relativePrime(x, y):

    if math.gcd(x,y) == 1:

        return True
    else:
        return False
        
def upperPrime(e, z):
    
        while True:
            prime = random.randint(2,2000)
            if (e*prime)%z == 1 and e != prime:
                return prime

def generateKey(x, y, z):
    return (z**x)%y

def generatePrivateKey(e, z):
    return (e**-1)%z

# print(generateKey(3,5,7))
# print(upperPrime(5,24))        
# print(relativePrime(19,102))
# print(generatePrime(102))
# print(math.gcd(8,10))




# class Testing:
    
#     @staticmethod
#     def TestMethod(word):
#         print(word)


# Testing.TestMethod("Hello World")
# """
# CDMA TESTING
# """
# temp = CDMA_Protocol()
# # print(temp.createCode(10))
# # print(CDMA_Protocol.createCode(10))
# # print(temp.is_orthogonal(temp.createCode(10), temp.createCode(10)))
# print("CDMA TESTING")

# print("Created Code is: {}".format(temp.codes(5, 10)))

# len_code = 10
# num_users = 5
# temp.codes(num_users,len_code)

# test_code = [0] * len_code
# for code in temp.code:
#     new_code = [tc * c for tc in test_code for c in code]

# print(f'The sum of allegedly orthogonal codes is: {sum(new_code)}')





#print(encodeAll(data_list))
#codes(5, 10)

# tom = encode([0,1,1], [1,0,0,1,1])
# print(tom)

# bitlist = [1,1,1,0,1]

# bittedlist = to_volts(bitlist)

# # for bit in bitlist:
# #     bittedlist.append(to_volts(bit))
# # print("This is Bitted List: {}".format(bittedlist))

# # bittedvolts = [to_volts(bit) for bit in bitlist]
# print(f'This is {bittedlist}')

# print(bittedlist)
# print (sum(bittedlist))

# codez = codes(5, 10)
# freq = [0]*10

# print(freq)
# print(createCode(10))


# """"Generating a Dictionary of Keys with Tuples as Values"""
# ZeroTuple = (0,0,0,0,0,0,0,0,0,0)


# dictionary = {"Client"+str(x): ZeroTuple for x in range(1,11)}
# print(dictionary)

# for x in range(7):

#     client = "Client"+str(x)
#     print(client)

# message = "Jonathan"
# res = ''
# for char in message:
#     res += ''.join(format(ord(char), '08b'))
# print(res)
# print(f"len str: {len(message)}\tlen convert: {len(res) / 8}")

# data1 = "Jonathan"
# code1 = temp.createCode(5)
# encoded = temp.encode(data1,code1)
# print(encoded)

# len_code = 10
# num_users = 3
# temp.codes(num_users,len_code)
# encoded_message = temp.encodeAll(data1)
# for char in data1:
#             res = ''.join(format(ord(char), '08b'))
#             print(res)
# message = temp.decode(encoded_message, temp.code[0])
# print(message)

#Generate a random 10 x 10 network map of users and distances between each other, keys are users and values are distances.

def generate_network(num_users):

    network = {}

    for i in range(num_users):
        network[i] = {}
        for j in range(num_users):
            if i != j:
                network[i][j] = random.randint(1,15)

    return network

#Generate a Routing Table for each user, keys are users and values are the next hop to reach that user.
#Get the routing table of this client with link state protocol

#Create a randomly generated 2D array of the network map, distance to self is 0, and distance to is fixed




def generate_routing_table(network, client):

    routing_table = {}

    for i in range(len(network)):
        if i != client:
            routing_table[i] = network[client][i]

    return routing_table

#Create a column header for the routing table
networked = generate_network(10)

column_header = "|  " + "  |  ".join(str(x) for x in range(len(networked))) + "  |"


def random_matrix(num_users):

    matrix = [[0]*num_users for x in range(num_users)]

    for i in range(num_users):

        for j in range(num_users):

            if i != j:

                matrix[i][j] = random.randint(1,15)
    
    for i in range(0,len(matrix)):

        for j in range(i, len(matrix)):

            matrix[j][i] = matrix[i][j]

    return matrix


    
# generate_map(matrix)
# matrix = random_matrix(10)
# print(f'Fixed Matrix : {matrix}')





names_list = ["Jonathan","Robert","Timothy", "Gregory", "Jenny", "Ralph"]

def create_network(names_list):
    
    #list = [[random.randint(1,second) for x in range(first)] for y in range(first)]
    matrix = random_matrix(len(names_list))

    listed = {names_list[x]: matrix[x] for x in range(len(names_list))}

    column_header = "| " + " |  ".join(x.center(2) for x in names_list) + "  |"
    table = "\t\t" + column_header + "\n"

    for key in listed:
        table += key.rjust(15) + ": "
        for value in listed[key]:
            table += "   " + str(value).center(2) + "   |  "
        table += "\n"
    return table

#Using linkstate protocol to generate a routing table for each user
#MEthod takes in a network matrice and list of names.

# def link_state_protocol(network, names_list):


#     header = "|  Destination  |          Path         |          Cost        |\n"

#     for x in names_list:
#         print(f'{x}')
#         print(f'{network[x]}')
#     pass


# #Compute routing table with Distance Vector Protocol
# def distance_vector_protocol(network, names_list):


#     pass
# matricees = create_network(names_list)
# print(matricees)

# print(create_matrix(10))
# print(column_header)
# print(generate_routing_table(generate_network(10), 0)) 
# print(generate_network(10))

# m = hashlib.md5()

# m.update(b"Jonathan")
# print(m.digest())
# m.digest_size
# print(m.hexdigest())

# #Created PGP Encryption

# data = PGP()

# n,e,d = data.RSA_encrypt()
# print(f"N: {n}, E: {e}, D: {d}")

# message1 = "Hello World"
# pubKey = data.PublicKeys(n,e, message1)
# print("Public Key: {}".format(pubKey))

# privKey = data.PrivateKeys(n,d, pubKey)
# print("Private Key: {}".format(privKey))

# eH, eS, dS = data.PGPClient(message1, n, e)
# print(f"eH: {eH}, eS: {eS}, dS: {dS}")

"""
CDMA TESTING / IMPLIMENTATION

"""
data = CDMA()

codes = data.create_code(10)
print(f"Codes: {codes}")

generated = data.generate_codes(2,10)
print(f"Generated: {generated}")

data1 = "What will you be doing today?"


freq = data.encode_all(data1)
print(f"Freq: {freq}")

decoded, m = data.decode(freq, generated[1])
print(f"Decoded: {decoded}")


