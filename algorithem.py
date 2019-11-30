from alphabets import Alpabets
from random import randint

m = Alpabets()

#print(m)

print(Alpabets().uppercase())


class Algo():

    def __init__(self):

        '''
        '''

        self.upperword =  Alpabets().uppercase()
        self.lowerword =  Alpabets().lowercase()


    def encrypt(self, keyword):

        '''
        '''

        #keyword = keyword.lower()
        key_length  = len(keyword)

        encrypt_list  =  []

        for x in keyword:

            key_key = randint(0,10)
            if x.isupper():
                key_index =  self.upperword.index(x)
                word_set = self.upperword
            if x.islower():
                key_index =  self.lowerword.index(x)
                word_set = self.lowerword

            encrypt_index  = key_index  +  key_key

            if encrypt_index > len(self.lowerword):
                print(encrypt_index)
                encrypt_index = encrypt_index -  randint(1,5)

            word = self.lowerword[encrypt_index] + word_set[key_key]
            encrypt_list.append(word)

        return ''.join(encrypt_list)


    def match(self, keyword, validator):

        '''
        '''

        key_len = len(keyword)
        encrypted_keyword = [keyword[i : i+2] for i in  range(0, len(keyword), 2)]

        x_keyword = []

        for key_key in encrypted_keyword:
            encrypted_key = self.lowerword.index(key_key[0])

            if key_key[1].isupper():
                random_key = self.upperword.index(key_key[1])
                word_set = self.upperword

            if key_key[1].islower():
                random_key = self.lowerword.index(key_key[1])
                word_set = self.lowerword


            if encrypted_key > random_key:
                x_key = encrypted_key -random_key

            else:
                 x_key = random_key - encrypted_key


            x_value  = word_set[x_key]

            x_keyword.append(x_value)
        validation_keyword  =  ''.join(x_keyword)


        if validation_keyword == validator:
            return True
        return False
