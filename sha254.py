
class SHA256:
    def __init__(self, root, controller):
        return
    
    h = ['0x6a09e667', '0xbb67ae85', '0x3c6ef372', '0xa54ff53a', '0x510e527f', '0x9b05688c', '0x1f83d9ab', '0x5be0cd19']

    K = ['0x428a2f98', '0x71374491', '0xb5c0fbcf', '0xe9b5dba5', '0x3956c25b', '0x59f111f1', '0x923f82a4','0xab1c5ed5', 
         '0xd807aa98', '0x12835b01', '0x243185be', '0x550c7dc3', '0x72be5d74', '0x80deb1fe','0x9bdc06a7', '0xc19bf174', 
         '0xe49b69c1', '0xefbe4786', '0x0fc19dc6', '0x240ca1cc', '0x2de92c6f','0x4a7484aa', '0x5cb0a9dc', '0x76f988da', 
         '0x983e5152', '0xa831c66d', '0xb00327c8', '0xbf597fc7','0xc6e00bf3', '0xd5a79147', '0x06ca6351', '0x14292967', 
         '0x27b70a85', '0x2e1b2138', '0x4d2c6dfc','0x53380d13', '0x650a7354', '0x766a0abb', '0x81c2c92e', '0x92722c85', 
         '0xa2bfe8a1', '0xa81a664b','0xc24b8b70', '0xc76c51a3', '0xd192e819', '0xd6990624', '0xf40e3585', '0x106aa070', 
         '0x19a4c116','0x1e376c08', '0x2748774c', '0x34b0bcb5', '0x391c0cb3', '0x4ed8aa4a', '0x5b9cca4f', '0x682e6ff3',
         '0x748f82ee', '0x78a5636f', '0x84c87814', '0x8cc70208', '0x90befffa', '0xa4506ceb', '0xbef9a3f7','0xc67178f2']

    # get the binary values of the input string
    # return value is a binary array
    @staticmethod
    def translate(message):
        # string chars to unicode values
        charCodes = [ord(c) for c in message]

        # unicode to 8-bit strings
        # remove the binary string indicator using bin(char)[2:]
        # fill with 0s to the left using zfill(8)
        bytes = []
        for char in charCodes:
            bytes.append(bin(char)[2:].zfill(8))

        bits = []
        for byte in bytes:
            for bit in byte:
                bits.append(int(bit))

        return bits
    
    # convert to bit values to hex values
    @staticmethod
    def b2Tob16(bitValue):
        # takes list of 32 bits and convert to string
        bitValue = ''.join([str(x) for x in bitValue])

        # create 4 bit chunks
        binaries = []
        for d in range(0, len(bitValue), 4):
            binaries.append('0b' + bitValue[d:d+4])

        # transform to hex and remove hex-indicator
        hexes = ''
        for b in binaries:
            hexes += hex(int(b,2))[2:]

        return hexes

    # add in 0s to the front to ensure uniform length
    @staticmethod
    def fill_zeros(bits, length=8, endian='LF'):
        l = len(bits)
        if endian == 'LE':
            for i in range(l, length):
                bits.append(0)
        else:
            while l < length:
                bits.insert(0, 0)
                l = len(bits)

        return bits

    # break the list of bits into fixed length
    @staticmethod
    def chunker(bits, chunk_length=8):
        chunked = []
        for b in range(0, len(bits), chunk_length):
            chunked.append(bits[b:b+chunk_length])
        return chunked
    
    @staticmethod
    def initializer(values):
        #convert from hex to python binary string (with cut bin indicator ('0b'))
        binaries = [bin(int(v, 16))[2:] for v in values]
        #convert from python string representation to a list of 32 bit lists
        words = []
        for binary in binaries:
            word = []
            for b in binary:
                word.append(int(b))
            words.append(SHA256.fill_zeros(word, 32, 'BE'))
        return words
    
    @staticmethod
    def preprocessMessage(message):
        # translate message into bits
        bits = SHA256.translate(message)
        # message length
        length = len(bits)
        # get length in bits of message (64 bit block)
        message_len = [int(b) for b in bin(length)[2:].zfill(64)]
        # if length smaller than 448 handle block individually otherwise
        # if exactly 448 then add single 1 and add up to 1024 and if longer than 448
        # create multiple of 512 - 64 bits for the length at the end of the message (big endian)
        if length < 448:
            # append single 1
            bits.append(1)
            #fill zeros little endian wise
            bits = SHA256.fill_zeros(bits, 488, 'LE')
            # add the 64 bits representing the length of the message
            bits = bits + message_len
            return [bits]
        elif 448 <= length <= 512:
            bits.append(1)
            bits = SHA256.fill_zeros(bits, 1024, 'LE')
            bits[-64:] = message_len
            return SHA256.chunker(bits, 512)
        else:
            bits.append(1)
            # loop until multiple of 512+64 bit message_len if message length exceeds 448 buts
            while (len(bits)+64 %512 != 0):
                bits.append(0)
            bits = bits + message_len
            return SHA256.chunker(bits, 512)
        
    #truth condition is integer 1
    @staticmethod
    def isTrue(x): return x == 1

    #simple if 
    @staticmethod
    def if_(i, y, z): return y if SHA256.isTrue(i) else z

    #and - both arguments need to be true
    @staticmethod
    def and_(i, j): return SHA256.if_(i, j, 0)
    @staticmethod
    def AND(i, j): return [SHA256.and_(ia, ja) for ia, ja in zip(i,j)] 

    #simply negates argument
    @staticmethod
    def not_(i): return SHA256.if_(i, 0, 1)
    @staticmethod
    def NOT(i): return [SHA256.not_(x) for x in i]

    #retrun true if either i or j is true but not both at the same time
    @staticmethod
    def xor(i, j): return SHA256.if_(i, SHA256.not_(j), j)
    @staticmethod
    def XOR(i, j): return [SHA256.xor(ia, ja) for ia, ja in zip(i, j)]

    #if number of truth values is odd then return true
    @staticmethod
    def xorxor(i, j, l): return SHA256.xor(i, SHA256.xor(j, l))
    @staticmethod
    def XORXOR(i, j, l): return [SHA256.xorxor(ia, ja, la) for ia, ja, la, in zip(i, j, l)]

    #get the majority of results, i.e., if 2 or more of three values are the same 
    @staticmethod
    def maj(i,j,k): return max([i,j,], key=[i,j,k].count)

    # rotate right
    @staticmethod
    def rotr(x, n): return x[-n:] + x[:-n]
    # shift right
    @staticmethod
    def shr(x, n): return n * [0] + x[:-n]

    #full binary adder
    @staticmethod
    def add(i, j):
        #takes to lists of binaries and adds them
        length = len(i)
        sums = list(range(length))
        #initial input needs an carry over bit as 0
        c = 0
        for x in range(length-1,-1,-1):
            #add the inout bits with a double xor gate
            sums[x] = SHA256.xorxor(i[x], j[x], c)
            #carry over bit is equal the most represented, e.g., output = 0,1,0 
            # then 0 is the carry over bit
            c = SHA256.maj(i[x], j[x], c)
        #returns list of bits 
        return sums
    
    @staticmethod
    def sha256(message): 
        k = SHA256.initializer(SHA256.K)
        h0, h1, h2, h3, h4, h5, h6, h7 = SHA256.initializer(SHA256.h)
        chunks = SHA256.preprocessMessage(message)

        for chunk in chunks:
            w = SHA256.chunker(chunk, 32)

            for _ in range(48):
                w.append(32 * [0])

            for i in range(16, 64):
                s0 = SHA256.XORXOR(SHA256.rotr(w[i-15], 7), SHA256.rotr(w[i-15], 18), SHA256.shr(w[i-15], 3) ) 
                s1 = SHA256.XORXOR(SHA256.rotr(w[i-2], 17), SHA256.rotr(w[i-2], 19), SHA256.shr(w[i-2], 10))
                w[i] = SHA256.add(SHA256.add(SHA256.add(w[i-16], s0), w[i-7]), s1)

            a = h0
            b = h1
            c = h2
            d = h3
            e = h4
            f = h5
            g = h6
            h = h7

            for j in range(64):
                S1 = SHA256.XORXOR(SHA256.rotr(e, 6), SHA256.rotr(e, 11), SHA256.rotr(e, 25) )
                ch = SHA256.XOR(SHA256.AND(e, f), SHA256.AND(SHA256.NOT(e), g))
                temp1 = SHA256.add(SHA256.add(SHA256.add(SHA256.add(h, S1), ch), k[j]), w[j])
                S0 = SHA256.XORXOR(SHA256.rotr(a, 2), SHA256.rotr(a, 13), SHA256.rotr(a, 22))
                m = SHA256.XORXOR(SHA256.AND(a, b), SHA256.AND(a, c), SHA256.AND(b, c))
                temp2 = SHA256.add(S0, m)
                h = g
                g = f
                f = e
                e = SHA256.add(d, temp1)
                d = c
                c = b
                b = a
                a = SHA256.add(temp1, temp2)
            h0 = SHA256.add(h0, a)
            h1 = SHA256.add(h1, b)
            h2 = SHA256.add(h2, c)
            h3 = SHA256.add(h3, d)
            h4 = SHA256.add(h4, e)
            h5 = SHA256.add(h5, f)
            h6 = SHA256.add(h6, g)
            h7 = SHA256.add(h7, h)

        digest = ''

        for val in [h0, h1, h2, h3, h4, h5, h6, h7]:
            digest += SHA256.b2Tob16(val)
        return digest
    