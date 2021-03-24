# TẢO BIỂN

## Yêu cầu bài toán:
Tảo biển sinh sản rất nhanh khi có môi trường thuận lợi với chúng và có những loài còn tiết ra môi trường những chất độc hại.

Một loại tảo nâu trong môi trường nước bị ô nhiễm nặng sinh sản theo quy luật sau:

Ngày đầu tiên (ngày 0) có n cá thể ở mức 1,
Ở mỗi ngày tiếp theo, mỗi cá thể mức i sinh ra i cá thể mức 1, các cá thể mới sinh sẽ sinh sôi, phát triển từ ngày hôm sau.
Bản thân các cá thể mức i phát triển thành mức i+1 và chu kỳ phát triển trong ngày chấm dứt.
Hãy xác định sau k ngày trong nước biển có bao nhiêu cá thể.

* **Dữ liệu:** Vào từ thiết bị nhập chuẩn gồm một dòng chứa 2 số nguyên n và k (1 ≤ n ≤ 1000, 1 ≤ k ≤ 1017).

* **Kết quả:** Đưa ra thiết bị xuất chuẩn một số nguyên – số lượng cá thể  tảo theo mô đun 109+7.

* **Ví dụ:**

| Input | Output |
|-------|--------|
| 3 2   | 15     |

## Phân tích bài toán:
* **1. Abstration:** 
Tìm số fibonaci của 2k, mà bắt đầu dãy fibonaci là 2 số n (Fi[0] = n, Fi[1] = n) (n, k nhập từ bàn phím)

* **2. Pattern Recognition:** 
Quy hoạch động, dãy số Fibonaci.

* **3. Algorithm designed:** 

```[python3]
    Input: n, k
    Set M = 1000000007
        F1, F2 = n
        Fn = F1 + F2
        i = 3
        M = 10^9 + 7
    While Loop (i < 2*k +1):
        F1 = F2 % M
        F2 = Fn % M
        Fn = (F1 + F2) % M
        i += 1 

    result = Fn
```

* **4. Đánh giá độ phức tạp thuật toán:** 
O(k)

* **5. Programming:**
