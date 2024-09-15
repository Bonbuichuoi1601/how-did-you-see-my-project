from ham import connect_string

if __name__ == "__main__":
    a = str(input())
    b = str(input())
    c = connect_string(a,b)
    print(c)