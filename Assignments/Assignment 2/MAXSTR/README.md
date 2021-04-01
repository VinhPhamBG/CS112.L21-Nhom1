# Khóa số

## Yêu cầu bài toán:

Để tăng độ an toàn chống hiện tượng cướp ngân hàng ngày càng phổ biến người ta dùng khóa số với mã mở khóa đơn giản nhưng rất hiệu quả. Trên cửa ra vào hiển thị một xâu khá dài các ký tự số. Các chữ số có thể di chuyển đổi chổ cho nhau hoặc bị xóa. Muốn mở khóa người ta phải di chuyển các chữ số và trong trường hợp cần thiết – xóa vài chữ số để nhận được xâu lớn nhất thỏa mãn điều kiện đã cài đặt. Điều kiện này được thay đổi thường xuyên. Hôm nay điều kiện đó là “Số nhận được phải chia hết cho 3”. Số nhận được có thể bắt đầu bằng các chữ số 0. Xâu “000” sẽ lớn hơn xâu “00”.

Hãy xác định khóa mở cửa.

* **Dữ liệu:** Vào từ thiết bị nhập chuẩn gồm một xâu ký tự số có độ dài lớn hơn 2 và không vượt quá 105.

* **Kết quả:** Đưa ra thiết bị xuất chuẩn xâu khóa mở cửa.

* **Ví dụ:**

| Inout | Output |
|-------|--------|
| 105   | 510    |

## Phân tích bài toán:

* **1. Abstraction:**
Cho mảng số nguyên n phần tử, tìm mảng con lớn nhất được sắp xếp giảm dần sao cho tổng các phần tử chia hết cho 3
* **2. Pattern Recognition:**
	
	Áp dụng thuật toán Vét cạn (Brute Force).
	Đặc điểm nhận dạng: cần duyệt qua tất cả các trường hợp độc lập để tìm được kết quả tốt nhất.
	
* **3. Algorithm designed:**

**Pseudocode:**

```[python 3]
Given _A
IF _A divided by 3 then the remainder is 1:
	FOR LOOP:
		IF in _A has the number _rE which devided by 3 then the remainder is 1 and _rE is the smallest :
			Delete _rE in _A
			Break FOR LOOP
		ELSE IF in _A has two numbers _rE1 and _rE2 which devided by 3 then the remainder is 2 and _rE1, _rE2 is the smallest:
			Delete _rE1, _rE2 in _A
ELSE IF _A divided by 3 then the remainder is 2:
	FOR LOOP:
		IF in _A has the number _rE which devided by 3 then the remainder is 2 and _rE is the smallest :
			Delete _rE in _A
			Break FOR LOOP
		ELSE IF in _A has two numbers _rE1 and _rE2 which devided by 3 then the remainder is 1 and _rE1, _rE2 is the smallest:
			Delete _rE1, _rE2 in _A
SORT _A
RETURN _A
```
* **4. Complexity:**
O(n)
