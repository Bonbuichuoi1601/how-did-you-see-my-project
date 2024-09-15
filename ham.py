def connect_string(a : str,b : str) -> str:
    return a + b

if __name__ == "__main__":
    a = str(input())
    b = str(input())
    c = connect_string(a,b)
    print(c)