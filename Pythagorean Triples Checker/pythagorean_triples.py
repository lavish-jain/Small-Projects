

class Triples:

    def __init__(self, side_a, side_b, side_c):
        self.a = int(side_a)
        self.b = int(side_b)
        self.c = int(side_c)

    def checkTriples(self):
        hyp, base, alt = self.__find_largest(self.a, self.b, self.c)
        if base**2 + alt**2 == hyp**2:
            return True
        return False

    def __find_largest(self, a, b, c):
        if a>=b and a>=c:
            hyp = a
            base = b 
            alt = c 
        elif b>=a and b>=c:
            hyp = b 
            base = a 
            alt = c
        else:
            hyp = c 
            base = b 
            alt = a 

        return hyp, base, alt 