from ham import check_odd
if __name__ == "__main__": #chỉ chạy hàm check_odd trong main, lấy đầu ra để in kết quả
    n = int(input())
    if check_odd(n):
        print("chan")
    else: 
        print("le")
    bon=int(input())
    if check_odd(bon):
        print('le')
    else:
        print ('chan')