# hash table with double hashing
# this code only works if the table_size is at least 2*# of elements to add
# and it requires table_size to be a prime
class hash_table:

    # 2887 is a prime more than double the possible number of keys 1416
    def __init__(self, table_size):
        self.__table = [None] * table_size

    def hash2(self,key):
        hv2 = 1
        hv2 += len(self.__table)-3
        return hv2
    def hashfunction(self, key):
        hv = 0
        i = 1
        for c in key:
            hv += ord(c)**i
            i += 1
        return hv % len(self.__table)

        # hv = 0
        # for c in key:
        #     hv += ord(c)
        # hv //= len(key)
        # return hv % len(self.__table)

    def add(self, key):  # key is a string
        hv = self.hashfunction(key)
        collision_count = 0
        if self.__table[hv] == None:
            self.__table[hv] = key
        else:
            hv2 = self.hash2(key)
            # if not, look at hv+1, then hv+4, then hv+9 ...
            i = 1
            while True:
                collision_count += 1
                if self.__table[(hv + i * hv2) % len(self.__table)] == None:
                    self.__table[(hv + i * hv2) % len(self.__table)] = key
                    break
                i += 1

        return collision_count

    def search(self, key):
        hv = self.hashfunction(key)

        if self.__table[hv] == key:
            return True
        elif self.__table[hv] == None:
            return False
        else:
            hv2 = self.hash2(key)
            # if key is not at , look at hv+1, then hv+4, then hv+9 ...
            i = 1
            while True:
                if self.__table[(hv + i * hv2) % len(self.__table)] == key:
                    return True
                elif self.__table[(hv + i * hv2) % len(self.__table)] == None:
                    return False
                else:
                    i += 1

    def print_table(self):
        # print(f'{str(self.__table[109])}')

        for i in range(len(self.__table)):
            if self.__table[i] != None:
                print(f'{i} {str(self.__table[i])}')
            # else:
            #    print('empty')