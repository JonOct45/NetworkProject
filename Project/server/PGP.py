'''
This is going ot be the PGP for Option 6. 

'''
import hashlib
import math
import random


class PGP_protocol:


    """TESTING FUNCTIONS"""

    def Testing_Encryption(self, message, key):
        encrypted = (len(message)**key)%key
        return encrypted

    """END OF TESTING FUNCTIONS"""
    print("PGP Protocol")
    def RSA_encrypt(self):

        large_prime = 7
        small_prime = 5

        z_value = (large_prime - 1) * (small_prime - 1)
        n_value = large_prime * small_prime
        
        e_value = self.generatePrime(z_value) #This will be the Relative prime of z_value

        d_value = self.upperPrime(e_value, z_value)

        #Value for the Public Key
        c_value = 0
        #Value for the Private Key
        

        #Returning the Values of n, e, and d
        return n_value, e_value, d_value
    
    def generatePrime(self,x):

            while True:
                prime = random.randint(2,x)
                if self.relativePrime(prime, x):
                    return prime

    def relativePrime(self, x, y):
        print("Relative Prime")
        
        if math.gcd(x,y) == 1:
            return True
        else:
            return False

    def upperPrime(self,e, z):
    
        while True:
            prime = random.randint(2,2000)
            if (e*prime)%z == 1 and e != prime:
                return prime

    def PublicKeys(self,n_value, e_value, message):

        print(f"Message: {message}")
        encrypted = (len(message)**e_value)%n_value

        return encrypted


        '''Encrypted < (data^e_value mod n_value'''



    def PrivateKeys(self,encrypted, d_value, n_value):

        decrypted = (encrypted**d_value)%n_value

        return decrypted

        '''Decrypted < (data^d_value mod n_value'''



    def PGPClient(self,data, Nserver, eServer):
        hashMessage = hashlib.md5()
        secret_key = 0

        #Secretkey = randomkey
        secret_key = self.generatePrime(Nserver)

        print(f"Data: {data}")
        #HashMessage = Hash(data)
        hashMessaged = hashMessage.update(data.encode('utf-8'))
        print(f"Hashed Message: {hashMessaged}")

        #encryptedHashMessage = Ks(hashMessage)
        encryptedHashMessage = self.PublicKeys(Nserver, secret_key, hashMessage)
        print(f"Encrypted Hash Message: {encryptedHashMessage}")

        #encryptedSecretKey = PublicKey(Nserver, eServer, SecretKey)
        encryptedSecretKey = self.PublicKeys(Nserver, eServer, secret_key)
        print(f"Encrypted Secret Key: {encryptedSecretKey}")

        #DigitalSignature = PrivateKey(secret_key)
        digitalSignature = self.PrivateKeys(encryptedSecretKey, secret_key, Nserver)
        print(f"Digital Signature: {digitalSignature}")
        #Send the EncryptedHAshMessage, EncriptedSecretKey, and DigitalSignature to the server 

        return encryptedHashMessage, encryptedSecretKey, digitalSignature 

        
       


    

    def PGPServer(data, ClientPublicKey):
        Alldatat = 0


        #AllData = clientTransmission

        #Data = ClientPublicKey(Alldata[DigitalSignature])

        #SecretKey = PrivateKey(n,d,Alldata[EncryptedSecretKey])

        #HashMessage = secretKey(Alldata[EncryptedHashMessage])

        #CopyData = data 

        #tmpHashedMessage = Hash(CopyData)

        #if tmpHashedMessage == HashMessage:
        #    print("The message is authentic")
        
        '''
        data < ClientPublicKey(Alldata[DigitalSignature])

        secret_key = PrivateKey(n,d,Alldata[EncryptedSecretKey])

        HashMessge = secretKey(Alldata[EncryptedHashMessage])

        copydata = data

        tmpHashedMessage = Hash(copyData)

        if tmpHashedMessage == HashMessage:
            print data
        else:
            Drop the data and ask for retransmission

        end if:
        
        '''
        pass

    def header(self, message):
        headers = f'''Private key received from server and channel {message} was successfully created!
        ----------------------- Channel 23456 ------------------------

        All the data in this channel is encrypted
        
        General Admin Guidelines:
        1. #nina is the admin of this channel
        2. Type exit to terminate the channel (only for admins)
        
        General Chat Guidelines:
        1. Type #bye to exit from this channel. (only for non-admins users)
        2. Use #<username> to send a private message to that user.

        Waiting for other users to join...'''


        
        return headers
        