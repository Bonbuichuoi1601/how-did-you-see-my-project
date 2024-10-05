
def add_to_list():
    n = int(input("Co bao nhieu phan tu trong mang:"))
    arr = []
    for i in range (0,n):
        arr.append(int(input(f"Phan tu thu {i}:")))

    print(arr)
    for index,element in enumerate(arr):
        print(index, element)

if __name__ == "__main__":
    add_to_list()

# 1,2,3,4,-5,2,3,-6
# ket qua 4

# 1,2,3,6,5,2,4,-6,-7,2,3,-5
# ket qua 7