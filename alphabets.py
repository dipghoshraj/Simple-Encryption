class Alpabets():

    def lowercase(self):

        '''
        '''

        lowerwords = []

        for c in range(97, 123):
            lowerwords.append(chr(c))

        return lowerwords


    def uppercase(self):

        '''
        '''

        upperwords = []

        for c in range(65, 91):
            upperwords.append(chr(c))

        return upperwords
