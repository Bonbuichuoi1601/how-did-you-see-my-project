# add to list
def add_to_list():
    n = int(input("Co bao nhieu phan tu trong mang:"))
    arr = []
    for i in range (0,n):
        arr.append(int(input(f"Phan tu thu {i}:")))

    print(arr)
    for element in arr:
        print(element)

if __name__ == "__main__":
    add_to_list()