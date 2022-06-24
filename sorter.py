def f(product, t):
    if t == "name":
        return product.name
    elif t == "code":
        return product.code


class Bubble:  # сортування бульбашка 1
    def sort(self, a, t):
        l = len(a)
        for i in range(l):
            for j in range(l-1):
                x, y = f(a[j], t), f(a[j+1], t)
                if x > y:
                    a[j], a[j+1] = a[j+1], a[j]


class Shaker:  # сортування шейкер 2
    def sort(self, a, t):
        def swap(i, j):
            a[i], a[j] = a[j], a[i]

        upper = len(a) - 1
        lower = 0

        no_swap = False
        while (not no_swap and upper - lower > 1):
            no_swap = True
            for j in range(lower, upper):
                if f(a[j+1], t) < f(a[j], t):
                    swap(j+1, j)
                    no_swap = False

            upper = upper - 1
            for j in range(upper, lower, -1):
                if f(a[j-1], t) > f(a[j], t):
                    swap(j-1, j)
                    no_swap = False


class Minimal:  # Сортування методом мінімальних елементів 3
    def sort(self, a, t):

        upper = len(a)

        for i in range(upper):
            min = i

            for j in range(i + 1, upper):
                if f(a[j], t) < f(a[min], t):
                    min = j

            a[i], a[min] = a[min], a[i]


class Selection:  # Сортування методом вставки 4
    def sort(self, a, t):
        l = len(a)
        for i in range(l-1):
            m, j = i, i+1
            while j < l:
                if f(a[j], t) < f(a[m], t):
                    m = j
                j = j + 1
            a[i], a[m] = a[m], a[i]

class Shell: # Сортування методом Шелла 5
    def sort(self, a, t):           
        n = len(a)
        h = n // 2
        while h > 0:
            for i in range(h, n):
                temp = a[i]
                j = i
                while j >= h and f(a[j - h], t) > f(temp, t):
                    a[j] = a[j - h]
                    j -= h
    
                a[j] = temp
            h = h // 2

class Quick: # швидкого сортування 6
    def sort(self, a, t):     
        b = self._sort(a, t)
        for i in range(len(b)):
            a[i] = b[i]

    def _sort(self, a, t):
        lower, equal, greater = [], [], []

        if len(a) > 1:
            pivot = f(a[0], t) # обираємо перший елемент з масиву
            for v in a: # зрівюємо перший елемент зі всіма іншими в масиві
                x = f(v, t)
                if x < pivot: # перевіряємо чи перший елемент більше за інший і записуємо його в масив менших
                    lower.append(v) 
                elif x == pivot: # перевіряємо чи перший елемент рівний іншому в масив однакових
                    equal.append(v)
                elif x > pivot: # перевіряємо чи перший елемент менше за інший і записуємо його в масив більших
                    greater.append(v)
            
            return self._sort(lower, t) + equal + self._sort(greater, t) # заново сортуємо три масиви рекурсивно
        
        return a

# Сортировка пирамидой 7
class Heap:
    def sort(self, a, t):
        n = len(a)
        for i in range(n//2, -1, -1):
            self.sift_down(a, i, n, t)
        for i in range(n-1, 0, -1):
            a[i], a[0] = a[0], a[i]
            self.sift_down(a, 0, i, t)

    def sift_down(self, a, i, n, t):
        while 2*i+1 < n:
            j = 2*i+1
            if j+1 < n and f(a[j+1], t) > f(a[j], t):
                j += 1
            if f(a[j], t) > f(a[i], t):
                a[i], a[j] = a[j], a[i]
                i = j
            else:
                break