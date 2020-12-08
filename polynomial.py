class Polynomial:

    def __init__(self, *args):
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, list):
                self.coefficients = arg
            elif isinstance(arg, dict):
                degree = max(arg.keys())
                self.coefficients = [arg[power] if power in arg else 0 for power in range(degree+1)]
            elif isinstance(arg, Polynomial):
                self.coefficients = arg.coefficients[:]
            else:
                self.coefficients = [arg]
        else:
            self.coefficients = [*args]

        power = self.degree()
        while power > 0 and not self.coefficients[power]:
            self.coefficients.pop()
            power -= 1

    def degree(self):
        return len(self.coefficients) - 1

    def __repr__(self):
        answer = 'Polynomial ['
        answer += ', '.join([str(x) for x in self.coefficients])
        answer += ']'
        return answer

    def __str__(self):
        s = ''
        l = len(self.coefficients)
        for i in range(l):
            power = l - i - 1
            if self.coefficients[power] != 0:
                u = (abs(self.coefficients[power]) != 1 or power == 0)
                s += ' + ' * (self.coefficients[power] > 0 and power != l - 1)
                s += ' ' * (self.coefficients[power] < 0 and power != l - 1)
                s += '-' * (self.coefficients[power] < 0)
                s += ' ' * (self.coefficients[power] < 0 and power != l - 1)
                s += str(abs(self.coefficients[power])) * u
                s += 'x' * (power >= 1) + ('^' + str(power)) * (power >= 2)
        return s

    def __eq__(self, other):
        other = Polynomial(other)
        return self.coefficients == other.coefficients

    def __add__(self, other):
        other = Polynomial(other)
        min_degree = min(self.degree(), other.degree())
        summed = [self.coefficients[i] + other.coefficients[i] for i in range(min_degree+1)]
        summed += self.coefficients[min_degree+1:]
        summed += other.coefficients[min_degree+1:]
        print(self.coefficients)
        print(other.coefficients)
        print(summed)
        return Polynomial(summed)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + other * -1

    def __rsub__(self, other):
        return -1 * (self - other)

    def __call__(self, x):
        return sum(x ** power * self.coefficients[power] for power in range(self.degree()+1))

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            l = (len(self.coefficients)) * (len(other.coefficients) - 1) + 1
            answer = [0 for i in range(l)]
            for i in range(len(self.coefficients)):
                mult = self.coefficients[i]
                for j in range(len(other.coefficients)):
                    answer[i + j] += other.coefficients[j] * mult
        else:
            answer = [x * other for x in self.coefficients]
        return Polynomial(answer)

    def __rmul__(self, other):
        return self * other

    def __iter__(self):
        answer = [(a, b) for a, b in enumerate(self.coefficients)]
        return iter(answer)

    def __next__(self):
        return next(self)


class RealPolynomial(Polynomial):
    def find_root(self):
        a = 1
        while True:
            if self(-a) * self(a) < 0:
                break
            else:
                a = a * 2
        a, b = -a, a
        while True:
            if abs(self(a)) < 1e-6:
                return a
            if abs(self(b)) < 1e-6:
                return b
            c = (a + b) / 2
            if abs(self(c)) < 1e-6:
                return c
            else:
                if self(a) * self(c) < 0:
                    a, b = a, c
                else:
                    a, b = c, b


if __name__ == '__main__':
    pass
