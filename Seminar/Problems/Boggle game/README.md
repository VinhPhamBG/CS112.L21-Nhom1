# **BOGGLE GAME**
## **1. Đề bài**
Thành và Trí là hai người bạn sống chung Ký túc xá với nhau. Vào một ngày mưa gió không có gì làm, hai bạn quyết định cùng nhau chơi trò chơi tìm chữ. Luật chơi như sau:
-	Trí sẽ tạo ra một bảng  M*N chứa các chữ cái viết hoa từ A-Z
-	Thành sẽ tạo ra một bộ từ điển chứa W các từ viết hoa
-	Cuối cùng, hai người sẽ cùng tìm các từ trong từ điển có xuất hiện trong bảng bẳng cách nối các ký tự trong bảng lại với nhau
-	Điều kiện : Hai chữ cái liên tiếp được nối phải liền kề nhau (có thể theo chiều dọc, ngang hoặc chéo)
Tuy nhiên, vì chậm chạm hơn, nên Trí toàn thua. Là một sinh viên CNTT, Trí quyết định viết một đoạn chương trình để hỗ trợ mình. Hãy giúp Trí viết một chương trình bằng Python để giải quyết bài toán trên

* **Input:**

- Dòng 1:  Số nguyên W
-	Dòng 2: W từ viết hoa khác nhau, ngăn cách nhau bởi khoảng trắng
-	Dòng 3: Số nguyên M
-	Dòng 4: Số nguyên N
-	M dòng tiếp theo, mỗi dòng chứa N chữ cái viết hoa, ngăn cách bởi khoảng trắng


* **Output:** 

Các từ xuất hiện trong từ điển thỏa mãn luật chơi, mỗi từ in cách nhau bởi khoảng trắng, sắp xếp theo bảng chữ cái (A->Z)

**VD:**

| INPUT | OUTPUT	|
|-------|---------|
|4| FOR YOU YOU |
|YOU WHAT NAME FOR| |
|3| |
|3| |
|Y F R| |
|H O U| |
|K S U| |
 
* **Giải thích:**

 ![image](https://user-images.githubusercontent.com/55485505/123190961-b0d28100-d4ca-11eb-9b6a-1aca988c9eb8.png)

# **2.	Computer thinking**

## **a.	Abstraction:**

- Ta có:
●	Dictionary là mảng các từ
●	Board là ma trận hai chiều các ký tự
- Cần tìm: Các từ có trong Dictionary xuất hiện trong mảng hai chiều Board bằng cách nối các ký tự lân cận trong này

## **b.	Decomposition:**
-	Tìm đường nối các đỉnh liền kề nhau ( ký tự ) trong mảng hai chiều Board tạo thành các từ khác nhau
-	Kiểm tra các từ vừa tạo thành liệu có xuất hiện trong mảng một chiều dictionary hay không

## **c.	Pattern recognition:**

-	Bài toán tương tự như các bài toán tìm đường đi trong  đồ thị. 
 Cụ thể:
●	Ta có các đỉnh là các ký tự trong bảng Board
●	Ta có các cạnh là các từ được ghép từ các đỉnh gần kề nhau trong bảng Board
●	Mục tiêu: Tìm đường đi thỏa mãn điều kiện cho trước
-	Hơn nữa, đồ thị sẽ được duyệt theo thuật toán BFS( Breadth first search ), duyệt qua nút gốc và khám phá tất cả các nút lân cận nó và có thể kết hợp thêm thuật toán Branch and Bound để giảm thiểu độ phức tạp
 Cụ thể:
●	Bài toán yêu cầu xét các nút ( ký tự ) lân cận 
●	Khi duyệt các đỉnh, xem xét đường đi ( từ vừa tạo ) liệu có thể xuất hiện trong mảng dictionary không, nếu có thì tiếp tục duyệt, nếu không thì dừng => giảm độ phức tạp
## **d. Algorithm:**
'''[Python3]
Given W, dictionary, M, N and boggle
Set visited[M][N] = False
For each element e in boggle:
	string = ""
	Create function findWords with parameters: boggle, visited,
dictionary, string, e:
		Set visited's element corresponding to e = True
		string = string + e
		If string appear in dictionary:
			add string to ans
		Consider all elements around current element
			For each e2 in elements:
				If visited's element corresponding to e2 == 
False:
					recall function findWords with 
parameters: boggle, visited, dictionary, string, e2:
		Delete the last letter of string
		Set visited corresponding to current element = False
If length of ans == 0:
	print 0
Else:
	sort ans
	print ans
'''
