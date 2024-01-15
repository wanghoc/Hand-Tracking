python -m venv hocnoovjppro
pip install cvzone
pip install mediapipe

cd hocnoovjppro
Scripts\activate

Đoạn code trên sử dụng thư viện OpenCV (`cv2`), thư viện `cvzone` (được import từ `cvzone.HandTrackingModule`) và thư viện `socket` để thực hiện việc theo dõi và truyền dữ liệu về tọa độ các điểm mốc trên bàn tay qua mạng.
Thư viện cvzone là một gói thư viện xử lý ảnh và trí tuệ nhân tạo (AI) cho Python. 
Nó được xây dựng trên các thư viện OpenCV và Mediapipe
    + OpenCV là một thư viện mã nguồn mở cho xử lý ảnh và thị giác máy tính trong trí tuệ nhân tạo (AI)
    + Mediapipe là một thư viện mã nguồn mở của Google, được sử dụng để xây dựng các ứng dụng xử lý video và hình ảnh. Nó cung cấp các công cụ để phát hiện các đối tượng, nhận dạng khuôn mặt, phát hiện cử chỉ
Dưới đây là mô tả của đoạn code:

1. Import các thư viện cần thiết: `cv2` (OpenCV), `HandDetector` từ `cvzone.HandTrackingModule` và `socket`.
2. Thiết lập các tham số cho kích thước của video (chiều rộng và chiều cao).
3. Khởi tạo webcam (`cap`) và cài đặt kích thước của video đầu vào.
4. Khởi tạo đối tượng `HandDetector` để theo dõi tay trong video. `maxHands=1` chỉ định rằng chỉ theo dõi một bàn tay và `detectionCon=0.8` là ngưỡng nhận dạng, nếu mức độ tương đồng giữa các frame không đạt ngưỡng này thì bàn tay sẽ không được nhận dạng.
5. Tạo một đối tượng socket (`sock`) để truyền dữ liệu qua mạng, với địa chỉ IP và cổng của máy chủ được cài đặt là `("127.0.0.1", 5052)`.
6. Trong vòng lặp vô hạn (`while True`):
   - Đọc frame từ webcam.
   - Sử dụng `detector.findHands(img)` để tìm các điểm mốc trên bàn tay trong frame.
   - Nếu có tay được nhận dạng (`hands` không rỗng), lấy tọa độ của các điểm mốc (`lmList`) từ tay đầu tiên được nhận dạng. Chuyển đổi tọa độ của các điểm mốc để đảm bảo chúng nằm trong khoảng giới hạn của kích thước video.
   - Gửi dữ liệu tọa độ của các điểm mốc thông qua socket sử dụng `sock.sendto`.
   - Hiển thị frame với các điểm mốc đã được đánh dấu.
   - Chờ 1 miligiây (`cv2.waitKey(1)`) trước khi chuyển sang frame tiếp theo.

Lưu ý rằng đoạn mã này giả sử mạng đang sẵn sàng và đang lắng nghe ở địa chỉ IP và cổng đã chỉ định (`("127.0.0.1", 5052)`). Nếu máy chủ không sẵn sàng, hoặc có sự cố với mạng, có thể có lỗi khi gửi dữ liệu.
