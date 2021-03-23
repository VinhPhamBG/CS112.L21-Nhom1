# BOT - TRẠM THU PHÍ

## Yếu cầu bài toán:
BOT (Built-Operation-Transfer, có nghĩa: Xây dựng-Vận hành-Chuyển giao) là hình thức Chính phủ kêu gọi các công ty bỏ vốn xây dựng trước (Built) thông qua đấu thầu, sau đó khai thác vận hành một thời gian (Operation) và sau cùng là chuyển giao (Transfer) lại cho nhà nước sở tại.

Đường cao tốc xuyên quốc gia được xây dựng theo hình thức BOT. Công ty Đa quốc gia Modern Highway trúng thầu, chia toàn bộ con đường thành n đoạn. Theo tính toán của Công ty sau khi chuyển giao con đường cho chính phủ sở tại quản lý thì lãi thu được ở đoạn đường thứ i là ai, ai có thể dương, âm hoặc bằng 0, tức là với từng đoạn con có thể lãi, lỗ hoặc hòa vốn. Từng nhóm các đoạn đường liên tiếp nhau (gọi tắt là khoảng) được chia cho các công ty con thực hiện. Công ty con ASEAM Highway hiện đang có trụ sở ở nước sở tại được quyền chọn trước khoảng tùy ý (có thể là cả con đường).

Dĩ nhiên Ban Giám đốc ASEAM Highway muốn chọn khoảng bắt đầu từ đoạn p đến hết đoạn q mang lại lợi nhuận cao nhất hoặc lỗ ít nhất nếu không có khoảng nào cho lãi.

Hãy chỉ ra khoảng cần chọn và lãi thu được. Nếu có nhiều cách chọn thì chỉ ra cách chọn có p nhỏ nhất.

Dữ liệu: Vào từ thiết bị nhập chuẩn:

Dòng đầu tiên chứa số nguyên n (1 ≤ n ≤ 106),
Dòng thứ 2 chứa n số nguyên a1, a2, . . ., an (0 ≤ |ai| ≤ 109, i = 1 ÷ n).
Kết quả: Đưa ra thiết bị xuất chuẩn trên một dòng 2 số nguyên p, q và lãi thu được.

Ví dụ:


| INPUT | OUTPUT|
|-------|-------|
| 16                                     | 5 15 12 |
| 2 -4 5 -8 4 -1 -1 1 1 1 -2 2 4 -6 9 -4 |         |
 

 
