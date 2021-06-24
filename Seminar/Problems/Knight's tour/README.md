# **KNIGHT'S TOUR**
## **I. Đề bài:**

**Quân mã trong cờ vua và bài toán Mã đi tuần:**
Mã đi tuần (hay hành trình của quân mã) là bài toán về việc di chuyển một quân mã trên bàn cờ vua (8 x 8). Quân mã được đặt ở một ô trên một bàn cờ trống nó phải di chuyển theo quy tắc của cờ vua để đi qua mỗi ô trên bàn cờ đúng một lần. Trong bài này, chúng tôi xin giới thiệu về bài toán thú vị này và những điều có thể khai thác được qua bài toán

•	Trong cờ vua, quân Mã là quân có cách đi phức tạp nhất. Xét một quân Mã đang đứng trên bàn cờ và tất cả các hình chữ nhật 2 x 3 nhận ô mà quân Mã đó đang đứng làm đỉnh. Quân Mã đó có thể đi tới các đỉnh khác màu với đỉnh nó đang đứng của bất kì hình chữ nhật 2 x 3 nào, miễn là đỉnh đó không nằm ngay cạnh đỉnh nó đang đứng.

•	Quân Mã có thể nhảy qua tất cả các quân khác để đến ô nó muốn, miễn là ô đó chưa bị ai chiếm giữ. Nói nôm na là quân Mã không bị cản. Khác với cờ tướng, nơi mà quân Mã có thể bị cản nếu có quân nào đứng ngay trước mặt nó, trong cờ vua, nước đi của quân Mã không có tính chất này.

•	Khi một quân Mã đứng ở cạnh bàn cờ, số nước đi có thể của nó sẽ bị thu hẹp xuống còn nhiều nhất là một nửa số nước đi ban đầu. Đặc biệt, nếu nó đứng ở một trong bốn góc bàn cờ, nó chỉ đi được tối đa hai nước. Câu nói “Mã ở rìa cũng giống như đồ trang trí” từ đây mà ra.

 ![image](https://user-images.githubusercontent.com/55485505/123203610-d7031b80-d4e0-11eb-975d-b82d6fb9d39e.png)


**Bài toán:**
Viết chương trình tìm lời giải cho bài toán mã đi tuần
Mỗi trạng thái là danh sách các ô mà mã đã đi qua. Từ một trạng thái, mã có thể thực hiện hành động nhảy đến một ô tiếp theo mà nó chưa đi qua. Các hành động này được đặc trưng bởi chênh lệch tọa độ (cột rồi tới dòng) giữa ô hiện tại mã đang đứng và ô nó sẽ nhảy tới.
Các hành động được phát sinh lần lượt theo thứ tự:  (2, 1), (1, 2), (2, -1), (-1, 2), (1, -2), (-1, -2), (-2, 1), (-2, -1).
Chương trình sẽ nhận vào trạng thái ban đầu gồm các thông tin là số dòng, số cột của bàn cờ, tọa độ ô đầu tiên mã đang đứng cùng toạ độ lúc con mã kết thúc. Và xuất ra màn hình trạng thái kết thúc.

**INPUT:**

- Hàng đầu tiên chứa 02 số nguyên dương: là kích thước bàn cờ (a x b)

- Hàng tiếp theo chứa một chuỗi ghi tọa độ ô đầu tiên mã đang đứng.

- Hàng cuối cùng chứa một chuỗi ghi tọa độ ô cuối cùng mã đang đứng.

**OUTPUT;**

- Danh sách các ô mã sẽ đi qua trong trạng thái kết thúc được tìm ra bởi phương pháp tìm theo chiều sâu.

- Nếu không tìm được danh sách nào xuất ra Not Found.

 **Ví dụ:**
 
![image](https://user-images.githubusercontent.com/55485505/123204267-e9ca2000-d4e1-11eb-8367-832de24db04b.png)

## **II.	Computational thinking**

### **1. Abstraction:**

Tìm đường đi của quân mã sao cho quân mã bắt đầu và kết thúc tại 1 điểm cho trước và quân mã phải đi hết tất cả các vị trí trên bản đồ (mỗi vị trí chỉ được qua 1 lần).  Rộng hơn là bài toán tìm đường đi Hamilton trong lý thuyết đồ thị với đỉnh là mỗi vị trí trên bàn cờ và cạnh của mỗi đỉnh nối với các đỉnh mà quân mã có thể đi đến. 

### **2. Decomposition:**

- Xây dựng nước đi cho quân mã.

- Kiểm tra tính hợp lệ của nước đi.

- Tìm đường đi cho quân mã.

###	**3. Pattern recognition:**

- Đây là bài toán tìm dường đi.

- Khi con mã không còn tìm thấy đường đi (tất cả các vị trí đi tới đều đã đi qua rồi) con mã sẽ quay lui để tìm một đường đi theo hướng mới -> sử dụng giải thuật **backtracking.**

### **4. Algorithm:**

**Mã giã:**

```[Python3]
Given a, b, start coordinate, end coordinate
Encode start coordinate and end coordinate
     #Exp: a1 => (0, 0)
Set S = [start coordinate]
Set dx = [2, 1, 2, -1, 1, -1, -2, -2]
Set dy = [1, 2, -1, 2, -2, -2, 1, -1]
Function Backtracking (i, m, n, S):
     If i == m * n:
          Set end = S[end index of array]
          If end == end coordinate:
			             Print found result
			             Exit function
     	Else:
		        Set locate = S[end index of array]
		        For loop in 8 iterative with j is loop variable:
			             Set x = locate[0] + dx[j]
			             Set y = locate[1] + dy[j]
		             	If knight still in the flag and (x, y) not in S:
				                 Add (x, y) into S
				                 Recursion Backtracking with (i+1, m, n, S)
				                 Pop end value in S
Call function Backtracking with (1, m, n, S)
If length of S == 1:
     Print Not Found
```
**Độ phức tạp:**

Độ phức tạp trong trường hợp xấu nhất là O(n(axb)) với a, b là kích thước bàn cờ.

