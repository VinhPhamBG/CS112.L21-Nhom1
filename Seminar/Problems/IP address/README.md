# **IP ADDRESS**
## **I. Đề bài:**

Bạn Zinh đi cấu hình mạng cho tiệm net. Bạn ghi tài liệu lại cho chủ tiệm nhưng do dùng phần mềm gõ văn bản quá tốt mà các dấu chấm trong chuỗi ghi địa chỉ IP của các máy bị biến mất hết. Hãy giúp chủ quán đoán tất cả các địa chỉ IP có thể có từ một địa chỉ IP thiếu dấu chấm

**INPUT:** Chuỗi số nguyên S

**OUTPUT:** Ứng với mõi địa chỉ IP có thể được ghi bởi chuỗi S, xuất địa chỉ IP đó ra trên một dòng.

**Ví dụ:**

| INPUT | OUTPUT |
|-------|--------|
|23212222200|23.212.222.200|
|           |232.12.222.200|
|           |232.122.22.200|

## **II. Computational thinking:**
### **1. Abstraction:**
Cho 1 chuỗi gồm từ 4 đến 12 kí tự các số nguyên, them các dấu chấm vào chuỗi để có thể có được những địa chỉ IP hợp lý.
### **2. Decomposition:**

- Thêm dấu chấm vào chuỗi S vào mọi vị trí có thể 

- Kiểm tra xem chuỗi sau khi thêm dấu chấm có phải địa chỉ IP không , 2 điều kiện cần xét :

    + Gọi số ký tự mỗi byte là k thì 0 < k < 4
 
 	+ Gọi giá trị số nguyên của byte đó là h thì 0 ≤ h ≤ 255, nếu k = 1 thì h phải khác 0.
 	
### **3. Pattern recognition:**

- Vì cần phải xét tất cả trường hợp thêm dấu chấm nên thuật toán **Brute force** sẽ thích hợp nhất 

- Và để giảm bớt số lần duyệt bằng cách lưu các kết quả thêm dấu chấm trước đó, ta sẽ dùng **Backtracking**.
  
### **4. Algorithm design:**
Pseudo code

```[Python3]
function checkIP(s):
    Check if every byte of the IP address (x) is valid:
        + int(x) <= 255, or
        + len(x) > 1 and x == "0"
    if all bytes are valid, return true
    else return false

function addDot(s, i, j, k):
    s = s[:i] + "." + s[i:]
    s = s[:j] + "." + s[j:]
    s = s[:k] + "." + s[k:]
    return s

for loop : i = 1 -> len(s)
    for loop : j = i+1 -> len(s)
        for loop : k = j+1 -> len(s)
            newStr = addDot(s, i, j, k)
            if checkIP(newStr) == true:
                print(newStr)
```
