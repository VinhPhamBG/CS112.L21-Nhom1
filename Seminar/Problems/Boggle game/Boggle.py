# Hàm isWord kiểm tra xem liệu rằng tham số _string đưa vào có xuất hiện trong
# bộ từ điển dictionary hay không
# Để đơn giản, việc kiểm tra này sẽ được thực hiện theo hướng tìm tuyến tính
def isWord(_string, dictionary):
    #Thực hiện linear search cho tất cả các từ trong dictionary
    for i in range(0, len(dictionary)):
        if(_string == dictionary[i]):
            return True
    return False
# Hàm check là hàm dùng để "tỉa" các nhánh trong thuật toán Branch and Bound
# Nếu như chuỗi các ký tự ta đang xét không tồn tại ở bất kì phần tử nào trong dictionary thì trả về False
def check(dictionary, _string):
    # Thực hiện linear search
    for i in dictionary:
        if _string in i:
            return True
    return False
# Hàm đệ quy findWordsUtil dùng để kiểm tra và thêm các từ hợp lệ vào list kết quả_answer
def findWordsUtil(boggle, visited, dictionary, i, j, _string):
    global answer
    # Đánh dấu ô hiện tại trong visited là đã xét và thêm ký tự hiện tại vào chuỗi _string
    visited[str(i)][j] = True
    _string = _string + boggle[i][j]
    # Nếu str xuất hiện ở trong dictionary thì thêm chuỗi _string hiện tại vào list kết quả_answer
    if isWord(_string, dictionary):
        answer.append(_string)
    # Nếu đường đi hiện tại vẫn còn xét được
    # Xét tiếp tục 8 đỉnh (ký tự) liền kề đỉnh (ký tự) đang xét trong đồ thị (bảng) boggle
    if check(dictionary, _string):
        row = i -1
        while (row <= i +1) and (row < M):
            col = j -1
            while (col <= j +1) and (col < N):
                if (row >=0) and (col >=0) and not (visited[str(row)][col]):
                    findWordsUtil(boggle, visited,dictionary, row, col, _string)
                col +=1
            row +=1
    # Nếu không, xóa ký tự hiện tại ra khỏi chuỗi _string
    # và đánh dấu ô visited đang xét là False
    _string = _string[:-1]
    visited[str(i)][j] = False
# Hàm findWords dùng để xét tất cả các đỉnh (ký tự) trong đồ thị (bảng) boggle
def findWords(boggle, dictionary):
    # Đánh dấu tất cả các đỉnh (ký tự) là chưa xét_ False
    visited = dict()
    for i in range(len(boggle)):
        visited[str(i)] = [False]*(len(boggle[0]))
    # Khởi tạo chuỗi _string hiện tại
    _string = ''
    # Xét tất cả các đỉnh (ký tự) và tìm kiểm tất cả các đường đi (từ) có thể tạo ra được bắt đầu bởi đỉnh (ký tự) đó
    for i in range(0, M):
        for j in range(0, N):
            findWordsUtil(boggle, visited, dictionary, i, j, _string)
#Chương trình chính : 
answer = []

W = int(input())
dictionary = input().split()
M = int(input())
N = int(input())
boggle = list()
for i in range(M):
    boggle.append(input().split())
findWords(boggle, dictionary)
if len(answer) >0 :
    answer.sort()
    print(" ".join(answer))
else:
    print(0)