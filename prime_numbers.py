class PrimeCounter:
    """a fast way to find prime numbers between the desired period"""

    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.start_backup = self.start  # for __str__ return , cuz changing self.start
        self._primes = []

    def __iter__(self):
        self._primes.clear()
        self.start = self.start_backup
        return self

    def __next__(self):
        while 1:
            if self.start >= self.end:
                raise StopIteration("no more prime num found")
            if PrimeCounter(self.start, self.end, self.step).is_prime():
                item = self.start
                self._primes.append(item)
                self.start += self.step
                return item
            self.start += self.step

    def __len__(self):
        return len(self._primes)

    def __str__(self):
        """if user calls obj before iteration we iterate auto inside"""
        self.fill_primes()
        return str(self._primes)[1:-1]  # slicing to delete [] signs

    def __add__(self, other):
        """to merge primes of 2 objects"""
        self.fill_primes()
        other.fill_primes()
        return self._primes + other._primes

    def is_prime(self):
        for n in range(2, (self.start // 2) + 1):
            if self.start % n == 0:
                return False
        return True if self.start > 1 else False

    def fill_primes(self):
        """activates iter then next then _primes get full per calling"""
        for _ in self:
            pass


def main():
    print("\nfrom negative number means 'Quit'")
    while 1:
        a = int(input("\nfrom : "))
        if a < 0:
            break
        b = int(input("to : "))
        s = int(input("step : "))
        print("primes :", end=" ")
        for item in PrimeCounter(a, b, s):
            print(item, end=" ")
        print()
    print("\ntake care of yourself :)")

if __name__ == "__main__": main()

