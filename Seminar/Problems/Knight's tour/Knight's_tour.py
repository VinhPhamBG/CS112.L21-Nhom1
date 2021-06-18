n, m = map(int, input().split()) # Nhập kích thước bàn cờ
start = input() # Nhập vị trí bắt đầu
S = [(ord(start[0]) - 97, int(start[1]) - 1)] # Chuyển start thành vị trí trong mảng: ví dụ chuyển a1 => (0, 0)
end = input() # Nhập vị trí kết thúc
end = (ord(end[0]) - 97, int(end[1]) - 1)

# Hướng đi ưu tiên ràng buộc cho máy
dx = [2, 1, 2, -1, 1, -1, -2, -2]
dy = [1, 2, -1, 2, -2, -2, 1, -1]

# In output
def Print(S):
    for i in S:
        print("{}{}".format(chr(i[0] + 97), i[1] + 1), end = ' ')

def backtracking(i, m, n, S):
    if i == m * n: # Nếu ta đã đi qua hết tất cả các nước đi trên bàn cờ.
        x = S[len(S) - 1] # Lấy vị trí cuối cùng của mảng để so sánh có trùng với vị trí kết thúc mà ta đã nhập.
        if x == end:
            Print(S)
            exit()
    else:
        locate = S[len(S) - 1] # Lấy vị trí hiện tại đang đứng
        for j in range(8): # Duyệt 8 nước đi tiếp theo theo thứ tự có sẵn
            x = locate[0] + dx[j]
            y = locate[1] + dy[j]
            if 0 <= x and x < m and 0 <= y and y < n: # Kiểm tra vị trí mới có vược ra khỏi bàn cờ hay không
                if (x, y) not in S: # Vị trí mới đã được đi qua chưa
                    S.append((x, y)) # Nếu chưa thì thêm vào mảng S
                    backtracking(i + 1, m, n, S[:]) # Gọi đệ quy lại để tìm nước đi mới
                    S.pop() # Nếu mà không có đường đi nào nữa ở bước backtracking trên thì ta sẽ pop vị trí hiện tại
                            # để tìm nước đi mới phù hợp.

backtracking(1, m, n, S)
if len(S) == 1: # Nếu mà không có đường đi phù hợp thì ta in ra Not Found
    print('Not Found')
