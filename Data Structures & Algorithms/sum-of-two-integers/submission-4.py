class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xFFFFFFFF
        
        def convert_bit(num, string):

            if num == 0:
                return string

            quotient = num // 2
            remainder = num % 2
            print("q", quotient)
            print("r", remainder)
            string += str(remainder)
            print("s", string)
            
            string = convert_bit(quotient, string)

            return string

        def fix_bit(string):
            missing_zero = 32 - len(string)
            string += "0" * missing_zero
            string = string[::-1]
            return string

        def twos_compliment(string):
            flipped = ''.join("1" if b == "0" else "0" for b in string)
            carry = 1
            result = ""

            for b in reversed(flipped):
                if b == "1" and carry == 1:
                    result = "0" + result
                    carry = 1
                elif b == "0" and carry == 1:
                    result = "1" + result
                    carry = 0
                else:
                    result = b + result
            return result
        
        def sum_bits(a_bits, b_bits):

            carry = 0
            res = ""

            for i in range(31, -1, -1):
                
                a_bit = int(a_bits[i])
                b_bit = int(b_bits[i])
                sum_bit = a_bit ^ b_bit ^ carry
                carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
                res = str(sum_bit) + res

            return res

        def bits_to_sum(bits):
            res = 0
            for i in range(31, -1, -1):
                if int(bits[i]) == 1:
                    num = pow(2, 31 - i)
                    res += num

            if bits[0] == "1":
                res -= pow(2 , 32)

            return res

        a_neg = a < 0
        a_bits = convert_bit(abs(a), "")
        a_bits = fix_bit(a_bits)
        if a_neg:
            a_bits = twos_compliment(a_bits)

        b_neg = b < 0
        b_bits = convert_bit(abs(b), "")
        b_bits = fix_bit(b_bits)
        if b_neg:
            b_bits = twos_compliment(b_bits)

        print("a_bits", a_bits)
        print("b_bits", b_bits)

        bit_sum = sum_bits(a_bits, b_bits)
        print("bit_sum", bit_sum)

        res = bits_to_sum(bit_sum)
        

        return res