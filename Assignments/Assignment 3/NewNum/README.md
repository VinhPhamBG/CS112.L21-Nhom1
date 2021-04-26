# SỐ NGUYÊN MỚI

## Yêu cầu bài toán:
Cho số nguyên dương n có không quá 100 chữ số. Hãy xác định số nguyên lớn nhất m chia hết cho 3 và khác n ở đúng một chữ số.

**Dữ liệu:** Vào từ thiết bị chuẩn gồm một dòng chứa số nguyên n có không quá 100 chữ số và không chứa các số 0 không có nghĩa.

**Kết quả:** Đưa ra thiết bị chuẩn số nguyên m tìm được.

**Ví dụ:**

| INPUT | OUTPUT |
|-------|--------|
|123    |723     |

## Phân tích bài toán:

* **1. Pattern Recognition:**
Áp dụng thuật toán Tham lam (Greedy approach)
* **2. Algorithm designed:**

**Pseudo code(Mã giả):**

```[python3x]
Given an interger n 
Set n_str = string(n)
Set k = 3 - n % 3
Set i = 0

WHILE LOOP:
    IF int(n[i]) + 3 + k <= 9 (Check if we can change the i-th place to meet the condition - the highest number divisible by 3. This condition is the same at the one below but this can jump to the target a little bit fast)
    THEN
        Set n_str[i] = n_str[i] + 3
        Set n = int(n_str)
        Continue
    
    c
    THEN
        Set n_str[i] = str(int(n_str[i] + k))
        Set n = int(n_str)
        Break 
    
    Set i = i + 1 (Increase i to go to next place value because we can't change anything at i-th place)
END```
