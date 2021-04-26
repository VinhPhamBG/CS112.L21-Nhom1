# **ĐỔI MỚI**
## **Yêu cầu bài toán:**
Thành phố quyết định chặt hạ hết n cây xanh hiện có trong thành phố để trồng chỉ một loại cây mới. Nhiệm vụ được giao cho Công ty Cây xanh thành phố. Do hạn chế về thiết bị Công ty chỉ tổ chức được 2 đội đốn hạ cây. Đội I hạ được a cây mỗi ngày, nhưng cứ mối ngày thứ k thì phải nghỉ để bảo dưỡng kỹ thuật, tức là đội I sẽ nghỉ vào các ngày k, 2k, 3k, . . . Đội II hạ được b cây mỗi ngày, nhưng cứ mỗi ngày thứ m thì phải nghỉ để bảo dưỡng kỹ thuật, tức là đội II sẽ nghỉ vào các ngày m, 2m, 3m, . . . Ở ngày nghỉ, số cây chặt hạ của đội sẽ là 0. Cả hai đội bắt đầu công việc vào cùng một ngày và làm việc song song với nhau.

Công việc trồng cây mới sẽ bắt đầu sau khi toàn bộ cây cũ đã bị đốn hạ.

Hãy xác định sau bao nhiêu ngày thì có thể bắt đầu việc trồng mới cây.

**Dữ liệu:** Vào từ thiết bị nhập chuẩn gồm một dòng chứa 5 số nguyên a, k, b, m và n (1 ≤ a, b ≤ 109, 2 ≤ k, m ≤ 1018, 1 ≤ n ≤ 1018).

**Kết quả:** Đưa ra thiết bị xuất chuẩn một số nguyên – số ngày tính được.

**Ví dụ:**

| Input| Output |
|---------|------|
| 2 4 3 3 25 | 7 |
## **Phân tích bài toán:**
**1. Abstraction:** Tìm chỉ số nhỏ nhất i của mảng A sao cho tổng giá trị từ 0 đến i của mảng A lớn hơn giá trị n cho trước

**2. Pattern Recognition:** Áp dụng thuật toán branch and bound. Đặc điểm nhận dạng: hi vọng tìm được giải pháp tốt nhất khi chọn 1 giá trị i nào đó

**3. Algorithm designed:
