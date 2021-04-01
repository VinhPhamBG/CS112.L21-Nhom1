# H_index

## Yêu cầu bài toán:

Làm thế nào để đánh giá sự thành công của một nhà khoa học?  Dựa vào số bài báo được công bố hay dựa vào số lần một bài báo được trích dẫn tới ở công trình của những người khác? Cả hai tham số đó đều quan trọng.

Một bài báo có điểm số trích dẫn là c nếu nó được trích dẫn tới c lần trong các công trình của những nhà khoa học khác. Một trong số các cách đánh giá sự thành công của một nhà khoa học là tính chỉ số ảnh hưởng H_Index dựa trên sự kết hợp giữa số lượng bài báo và chỉ số trích dẫn của các bài báo đó.

Chỉ số H_Indexcủa một nhà khoa học bằng k lớn nhất nếu người đó có k bài báo, mỗi bài có điểm số trích dẫn không nhỏ hơn k. Ví dụ, một người có 10 bài báo, mỗi bài báo được trích dẫn không dưới 10 lần thì H_Index của người đó ít nhất là bằng 10.

Một người có n bài báo, bài báo thứ i có điểm trích dẫn là ci, i = 1 ÷ n. Hãy xác định H_Index của người đó.

**Dữ liệu:** Vào từ thiết bị nhập chuẩn:

* Dòng đầu tiên chứa một số nguyên n (1 ≤ n ≤ 5×105),
* Dòng thứ 2 chứa n số nguyên c1, c2, . . ., cn (0 ≤ ci ≤ 106, i = 1 ÷ n).

**Kết quả:** Đưa ra thiết bị xuất chuẩn một số nguyên – H_Index tìm được.

**Ví dụ:**

| Input    | Output |
|----------|--------|
|5         | 4      |
|8 5 3 4 10|        |

## Phân tích bài toán:

* **1. Abstraction:** 
Cho mảng n phần tử, tìm số k lớn nhất sao cho k phần tử trong mảng lớn hơn hoặc bằng k.
* **2. Pattern Recognition:**
*Kĩ thuật được áp dụng : Vét cạn.
*Đặc điểm nhận dạng : Cần duyệt tất cả phần tử trong mảng.
* **3. Algorithm designed:**

**Pseudo Code(Mã giả):**

```[python3]
Given array paper[n]
Sort paper
Set H_index = 0
WHILE LOOP:
        Break when H_index = n
        IF paper[H_index] <= H_index THEN : Break (Check if the H_index-th element is bigger than H_index or not)
        Increament H_index by 1
        
Return H_index
```
* **4. Complexity:**
O(n)

        
