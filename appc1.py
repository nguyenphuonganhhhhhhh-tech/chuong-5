import streamlit as st

# Thiết lập cấu hình trang hiển thị trực quan
st.set_page_config(page_title="Kiểm tra Quang sinh học", page_icon="☀️", layout="centered")

# --- DỮ LIỆU PHẦN I: 100 CÂU HỎI TRẮC NGHIỆM ---
quiz_data = [
    {"q": "Câu 1. Nguồn năng lượng chủ yếu của muôn vật trên Trái Đất là gì?", "ops": ["A. Địa nhiệt", "B. Bức xạ mặt trời", "C. Năng lượng hạt nhân", "D. Năng lượng gió"], "ans": "B"},
    {"q": "Câu 2. Phản ứng có sự tham gia của ánh sáng được gọi là gì?", "ops": ["A. Phản ứng oxy hóa khử", "B. Phản ứng quang sinh", "C. Phản ứng trùng hợp", "D. Phản ứng thủy phân"], "ans": "B"},
    {"q": "Câu 3. Quang sinh học nghiên cứu các quá trình xảy ra trong cơ thể sống dưới tác dụng của loại bức xạ nào?", "ops": ["A. Tia X và tia gamma", "B. Sóng vô tuyến", "C. Ánh sáng nhìn thấy và tia tử ngoại", "D. Tia hồng ngoại và sóng radio"], "ans": "C"},
    {"q": "Câu 4. Đâu KHÔNG phải là một trong các định hướng nghiên cứu chính của quang sinh học?", "ops": ["A. Quang hợp và sinh tổng hợp tạo năng lượng", "B. Tiếp nhận thông tin", "C. Phát quang sinh học", "D. Di truyền học phân tử"], "ans": "D"},
    {"q": "Câu 5. Ai là người đưa ra bản chất bức xạ điện từ của ánh sáng, và vào năm nào?", "ops": ["A. Einstein, 1905", "B. Maxwell, 1865", "C. Planck, 1900", "D. Newton, 1687"], "ans": "B"},
    {"q": "Câu 6. Tốc độ ánh sáng trong chân không là bao nhiêu?", "ops": ["A. 3.000 km/s", "B. 30.000 km/s", "C. 300.000 km/s", "D. 3.000.000 km/s"], "ans": "C"},
    {"q": "Câu 7. Bước sóng (\u03bb) được định nghĩa là gì?", "ops": ["A. Số dao động trong một giây", "B. Khoảng cách giữa hai đỉnh sóng", "C. Thời gian thực hiện một dao động", "D. Biên độ dao động của sóng"], "ans": "B"},
    {"q": "Câu 8. Công thức liên hệ giữa bước sóng (\u03bb), tần số (\u03bd) và tốc độ ánh sáng (c) là:", "ops": ["A. \u03bb + \u03bd = c", "B. \u03bb/\u03bd = c", "C. \u03bb\u03bd = c", "D. \u03bb - \u03bd = c"], "ans": "C"},
    {"q": "Câu 9. Theo thang sóng điện từ, ánh sáng nhìn thấy có bước sóng trong khoảng nào?", "ops": ["A. 10\u207b\u00b1 cm \u2013 0,76 \u03bcm", "B. 0,76 \u03bcm \u2013 0,39 \u03bcm", "C. 0,39 \u03bcm \u2013 10\u207b\u00b2 \u03bcm", "D. 10\u207b\u00b2 \u03bcm \u2013 10\u207b\u2075 \u03bcm"], "ans": "B"},
    {"q": "Câu 10. Loại bức xạ nào có bước sóng dài nhất trong thang sóng điện từ được liệt kê?", "ops": ["A. Tia tử ngoại", "B. Tia hồng ngoại", "C. Sóng vô tuyến điện", "D. Tia Rơnghen"], "ans": "C"},
    {"q": "Câu 11. Ánh sáng màu đỏ có bước sóng nằm trong khoảng nào (nm)?", "ops": ["A. 760 \u2013 630", "B. 630 \u2013 600", "C. 600 \u2013 570", "D. 500 \u2013 450"], "ans": "A"},
    {"q": "Câu 12. Màu sắc nào có bước sóng ngắn nhất trong bảng màu sắc ánh sáng nhìn thấy?", "ops": ["A. Đỏ", "B. Vàng", "C. Lam", "D. Tím"], "ans": "D"},
    {"q": "Câu 13. Theo Anhstanh (Einstein), chùm sáng được hiểu là gì?", "ops": ["A. Một dòng liên tục không gián đoạn", "B. Chùm hạt, mỗi hạt là 1 photon", "C. Một loại sóng cơ học", "D. Dòng điện tử tự do"], "ans": "B"},
    {"q": "Câu 14. Công thức tính năng lượng của photon là:", "ops": ["A. E = mc\u00b2", "B. E = h\u03bd = hc/\u03bb", "C. E = \u00bdmv\u00b2", "D. E = F.d"], "ans": "B"},
    {"q": "Câu 15. Hằng số Planck (h) có giá trị xấp xỉ bao nhiêu?", "ops": ["A. 6,62.10\u207b\u00b3\u2074 J.s", "B. 3.10\u2078 J.s", "C. 9,8 J.s", "D. 1,6.10\u207b\u00b9\u2079 J.s"], "ans": "A"},
    {"q": "Câu 16. Quá trình hấp thụ ánh sáng về bản chất là quá trình gì?", "ops": ["A. Hóa học thuần túy", "B. Vật lý lượng tử thuần túy", "C. Cơ học cổ điển", "D. Sinh học thuần túy"], "ans": "B"},
    {"q": "Câu 17. Phương trình mô tả một nguyên tử/phân tử hấp thụ lượng tử ánh sáng là:", "ops": ["A. A + h\u03bd \u2192 A*", "B. A* \u2192 A + h\u03bd", "C. A + B \u2192 AB", "D. A \u2192 A\u207a + e\u207b"], "ans": "A"},
    {"q": "Câu 18. Một nguyên tử/phân tử A chỉ hấp thụ lượng tử ánh sáng có đặc điểm gì?", "ops": ["A. Bất kỳ bước sóng nào", "B. Bước sóng xác định, tương ứng với hiệu năng lượng giữa trạng thái cơ bản và kích thích", "C. Chỉ bước sóng trong vùng tử ngoại", "D. Chỉ bước sóng của ánh sáng trắng"], "ans": "B"},
    {"q": "Câu 19. Trạng thái cơ bản của phân tử thường là trạng thái nào?", "ops": ["A. Triplet", "B. Singlet (spin điện tử ghép đôi song song ngược hướng)", "C. Ion hóa", "D. Bán kích thích"], "ans": "B"},
    {"q": "Câu 20. Trạng thái kích thích của phân tử có thể là:", "ops": ["A. Chỉ singlet", "B. Chỉ triplet", "C. Singlet hoặc triplet", "D. Không xác định được"], "ans": "C"},
    {"q": "Câu 21. Ở trạng thái triplet, đặc điểm spin của điện tử là:", "ops": ["A. Ghép đôi song song ngược hướng", "B. Không được ghép đôi", "C. Không có spin", "D. Ghép đôi cùng hướng"], "ans": "B"},
    {"q": "Câu 22. Theo nguyên tắc chọn lọc trong hấp thụ ánh sáng, bước chuyển nào có xác suất cao hơn?", "ops": ["A. Singlet \u2192 Triplet", "B. Triplet \u2192 Singlet", "C. Các bước chuyển có độ bội giống nhau (singlet\u2192singlet, triplet\u2192triplet)", "D. Tất cả các bước chuyển có xác suất như nhau"], "ans": "C"},
    {"q": "Câu 23. Vì sao phổ hấp thụ không phải là vạch mà là một dải phổ liên tục?", "ops": ["A. Vì ánh sáng luôn là dải liên tục", "B. Vì ngoài mức năng lượng electron chính còn có các mức năng lượng dao động và quay nhỏ hơn", "C. Vì phân tử luôn ở trạng thái ion hóa", "D. Vì nhiệt độ môi trường luôn thay đổi"], "ans": "B"},
    {"q": "Câu 24. Ai là người đưa ra định luật liên hệ giữa hấp thụ ánh sáng với nồng độ, cường độ và độ xuyên sâu vào năm 1852?", "ops": ["A. Lambert", "B. Beer", "C. Planck", "D. Einstein"], "ans": "B"},
    {"q": "Câu 25. Công thức nào biểu diễn định luật Lambert-Beer về cường độ ánh sáng truyền qua?", "ops": ["A. I = I\u2080 + kCl", "B. I = I\u2080.e\u207b\u1d4f\u1d9c\u1d4c", "C. I = I\u2080/kCl", "D. I = I\u2080 - kCl"], "ans": "B"},
    {"q": "Câu 26. Mật độ quang (D) được tính theo công thức nào?", "ops": ["A. D = ln(I/I\u2080)", "B. D = ln(I\u2080/I) = kcl", "C. D = I\u2080 - I", "D. D = I/I\u2080"], "ans": "B"},
    {"q": "Câu 27. Trong công thức D = kcl, hệ số k được gọi là gì?", "ops": ["A. Hằng số Planck", "B. Hệ số hấp thụ phân tử", "C. Hệ số khúc xạ", "D. Hằng số Avogadro"], "ans": "B"},
    {"q": "Câu 28. Hệ số hấp thụ phân tử (k) là mật độ quang của:", "ops": ["A. Một lớp dày 10 cm chứa dung dịch 1M", "B. Một lớp dày 1 cm chứa dung dịch 1M của 1 hợp chất", "C. Một lớp dày 1 mm chứa dung dịch bất kỳ", "D. Toàn bộ thể tích dung dịch"], "ans": "B"},
    {"q": "Câu 29. Hệ số hấp thụ phân tử k có phụ thuộc vào cường độ ánh sáng chiếu vào không?", "ops": ["A. Có, tỉ lệ thuận", "B. Có, tỉ lệ nghịch", "C. Không phụ thuộc", "D. Chỉ phụ thuộc ở nồng độ cao"], "ans": "C"},
    {"q": "Câu 30. Khi nồng độ phân tử vượt ngưỡng nhất định, điều gì xảy ra?", "ops": ["A. Hệ số hấp thụ không đổi", "B. Tương tác phân tử gây hiệu ứng hấp thụ mới, thay đổi hệ số hấp thụ", "C. Ánh sáng ngừng bị hấp thụ", "D. Dung dịch trở nên trong suốt hoàn toàn"], "ans": "B"},
    {"q": "Câu 31. Độ xuyên qua (T) được định nghĩa là:", "ops": ["A. T = I\u2080/I", "B. T = I/I\u2080", "C. T = I\u2080 - I", "D. T = I\u2080 x I"], "ans": "B"},
    {"q": "Câu 32. Mối liên hệ giữa độ xuyên qua T và mật độ quang D là:", "ops": ["A. T = D", "B. T = e\u207b\u1d30", "C. T = e\u1d30", "D. T = 1/D"], "ans": "B"},
    {"q": "Câu 33. Khi hệ dung dịch có nhiều thành phần (hệ phức tạp), mật độ quang tổng D có tính chất gì?", "ops": ["A. Tính nhân", "B. Tính cộng hợp (D = D1 + D2 + D3 +\u2026)", "C. Tính chia", "D. Không xác định được"], "ans": "B"},
    {"q": "Câu 34. Độ hấp thụ (Ih/I\u2080), trong đó Ih = I\u2080 - I, tương ứng với đại lượng nào sau đây?", "ops": ["A. T", "B. D", "C. (1 - T)", "D. kcl"], "ans": "C"},
    {"q": "Câu 35. Định luật Lambert-Beer đúng với loại hệ nào?", "ops": ["A. Hệ dị thể (không đồng nhất)", "B. Hệ đồng nhất", "C. Hệ keo", "D. Hệ có nhiều pha rắn-lỏng"], "ans": "B"},
    {"q": "Câu 36. Trong sơ đồ chuyển đổi mức năng lượng, ký hiệu S\u2080 đại diện cho:", "ops": ["A. Trạng thái triplet kích thích", "B. Trạng thái singlet cơ bản", "C. Trạng thái ion hóa", "D. Trạng thái tự do"], "ans": "B"},
    {"q": "Câu 37. Trong sơ đồ mức năng lượng, S\u2081 và S\u2082 là:", "ops": ["A. Các trạng thái triplet", "B. Các trạng thái singlet kích thích (mức 1 và mức 2)", "C. Trạng thái cơ bản của nguyên tử", "D. Trạng thái ion âm"], "ans": "B"},
    {"q": "Câu 38. T (Triplet) trong sơ đồ chuyển hóa năng lượng nằm ở vị trí năng lượng như thế nào so với S\u2081?", "ops": ["A. Cao hơn S\u2081", "B. Thấp hơn S\u2081", "C. Bằng S\u2081", "D. Không xác định"], "ans": "B"},
    {"q": "Câu 39. Đâu KHÔNG phải là một trong các con đường chuyển hóa năng lượng hấp thụ của phân tử được nêu trong bài?", "ops": ["A. Mất nhiệt", "B. Phát huỳnh quang", "C. Phân bào", "D. Quang hóa"], "ans": "C"},
    {"q": "Câu 40. Đơn vị nào sau đây KHÔNG được dùng để đo năng lượng photon trong bài giảng?", "ops": ["A. eV", "B. erg", "C. Kcal", "D. Newton"], "ans": "D"},
    {"q": "Câu 41. Sự phát huỳnh quang là quá trình phân tử chuyển từ trạng thái nào xuống trạng thái cơ bản?", "ops": ["A. T (Triplet)", "B. S\u2081 (Singlet 1)", "C. S\u2082 (Singlet 2)", "D. Ion hóa"], "ans": "B"},
    {"q": "Câu 42. Thời gian tồn tại của trạng thái S1 (liên quan đến huỳnh quang) vào khoảng:", "ops": ["A. Nano giây", "B. Mili giây", "C. Giây", "D. Giờ"], "ans": "A"},
    {"q": "Câu 43. Huỳnh quang chỉ xảy ra khi nào?", "ops": ["A. Sau khi tắt ánh sáng kích thích một thời gian dài", "B. Trong thời gian chiếu sáng mẫu", "C. Chỉ vào ban đêm", "D. Không phụ thuộc thời gian chiếu sáng"], "ans": "B"},
    {"q": "Câu 44. Theo quy luật Stock, cực đại phổ huỳnh quang so với cực đại phổ hấp thụ:", "ops": ["A. Ngắn hơn (dịch về bước sóng ngắn)", "B. Dài hơn (dịch về bước sóng dài)", "C. Bằng nhau hoàn toàn", "D. Không liên quan"], "ans": "B"},
    {"q": "Câu 45. Quy luật Levin phát biểu điều gì?", "ops": ["A. Phổ huỳnh quang không phụ thuộc bước sóng kích thích", "B. Phổ huỳnh quang đối xứng với phổ hấp thụ", "C. Phổ huỳnh quang trùng khớp hoàn toàn với phổ hấp thụ", "D. Phổ huỳnh quang luôn có cường độ lớn hơn phổ hấp thụ"], "ans": "B"},
    {"q": "Câu 46. Quy luật Vavilov phát biểu điều gì?", "ops": ["A. Phổ huỳnh quang phụ thuộc mạnh vào bước sóng kích thích", "B. Phổ phát huỳnh quang không phụ thuộc vào bước sóng kích thích", "C. Phổ hấp thụ không phụ thuộc bước sóng kích thích", "D. Không có mối liên hệ nào giữa hấp thụ và huỳnh quang"], "ans": "B"},
    {"q": "Câu 47. Phát lân quang là quá trình phân tử chuyển từ trạng thái nào xuống trạng thái cơ bản?", "ops": ["A. S\u2081 \u2192 S\u2080", "B. T\u2081 \u2192 S\u2080", "C. S\u2082 \u2192 S\u2081", "D. S\u2080 \u2192 T\u2081"], "ans": "B"},
    {"q": "Câu 48. Vì sao chất phát lân quang vẫn phát sáng sau khi tắt ánh sáng kích thích?", "ops": ["A. Vì trạng thái triplet có thời gian sống dài hơn singlet", "B. Vì trạng thái singlet có thời gian sống dài hơn triplet", "C. Vì ánh sáng bị phản xạ lại nhiều lần", "D. Vì phân tử tiếp tục hấp thụ ánh sáng môi trường"], "ans": "A"},
    {"q": "Câu 49. Thời gian sống của phân tử ở trạng thái triplet vào khoảng:", "ops": ["A. 10\u207b\u2079 giây", "B. 10\u207b\u2077 \u2013 10\u207b\u00b3 giây (và lâu hơn)", "C. Vài phần nghìn của nano giây", "D. Không thể xác định"], "ans": "B"},
    {"q": "Câu 50. Vì sao bước chuyển liên quan đến trạng thái triplet có xác suất nhỏ?", "ops": ["A. Vì liên quan đến sự thay đổi spin (quay)", "B. Vì năng lượng quá lớn", "C. Vì phân tử quá nhỏ", "D. Vì không có ánh sáng kích thích"], "ans": "A"},
    {"q": "Câu 51. Phổ lân quang so với phổ huỳnh quang và phổ hấp thụ dịch chuyển về phía nào?", "ops": ["A. Bước sóng ngắn hơn", "B. Bước sóng dài hơn", "C. Không thay đổi vị trí", "D. Biến mất hoàn toàn"], "ans": "B"},
    {"q": "Câu 52. Ở trạng thái triplet, do điện tử không được ghép đôi nên khả năng gì tăng cao?", "ops": ["A. Khá năng phát huỳnh quang", "B. Khả năng tham gia phản ứng quang hóa", "C. Khả năng phản xạ ánh sáng", "D. Khả năng dẫn điện"], "ans": "B"},
    {"q": "Câu 53. Di chuyển năng lượng giữa các phân tử được mô tả bằng phương trình nào?", "ops": ["A. A + h\u03bd \u2192 A*", "B. M1* + M2 \u2192 M1 + M2*", "C. A* \u2192 A + h\u03bd", "D. A + B \u2192 AB*"], "ans": "B"},
    {"q": "Câu 54. Bản chất của quá trình di chuyển năng lượng là gì?", "ops": ["A. Một quá trình hóa học có biến đổi cấu trúc", "B. Một quá trình vật lý không kèm theo biến đổi hóa học", "C. Một phản ứng oxy hóa khử", "D. Một phản ứng phân ly"], "ans": "B"},
    {"q": "Câu 55. Điều kiện đầu tiên để di chuyển năng lượng theo cơ chế cộng hưởng cảm ứng xảy ra là gì?", "ops": ["A. Phân tử nhận năng lượng phải phát quang được", "B. Phân tử nhường năng lượng phải phát quang được", "C. Cả hai phân tử đều phải ở trạng thái cơ bản", "D. Nhiệt độ môi trường phải rất thấp"], "ans": "B"},
    {"q": "Câu 56. Điều kiện về phổ để di chuyển năng lượng hiệu quả là gì?", "ops": ["A. Phổ hấp thụ của chất cho phải trùng phổ hấp thụ của chất nhận", "B. Phổ phát quang của chất cho và phổ hấp thụ của chất nhận phải giao thoa", "C. Hai chất phải có cùng khối lượng phân tử", "D. Không cần điều kiện về phổ"], "ans": "B"},
    {"q": "Câu 57. Hiệu suất di chuyển năng lượng tỉ lệ nghịch với khoảng cách theo hàm mũ bậc mấy?", "ops": ["A. 2", "B. 3", "C. 4", "D. 6"], "ans": "D"},
    {"q": "Câu 58. Với khoảng cách 10 \u00c5 giữa hai phân tử, hiệu suất di chuyển năng lượng vào khoảng bao nhiêu?", "ops": ["A. Trên 50%", "B. Dưới 10%", "C. Chính xác 100%", "D. Bằng 0%"], "ans": "A"},
    {"q": "Câu 59. Quá trình di chuyển năng lượng luôn đi theo chiều nào?", "ops": ["A. Từ mức năng lượng thấp đến mức năng lượng cao", "B. Từ mức năng lượng cao ở chất cho đến mức năng lượng thấp hơn ở chất nhận", "C. Ngẫu nhiên, không theo chiều nào cố định", "D. Chỉ xảy ra khi hai mức năng lượng bằng nhau"], "ans": "B"},
    {"q": "Câu 60. So sánh thời gian sống: huỳnh quang (nano giây) và lân quang, phát biểu nào đúng?", "ops": ["A. Huỳnh quang có thời gian sống dài hơn lân quang", "B. Lân quang có thời gian sống dài hơn huỳnh quang", "C. Hai loại có thời gian sống bằng nhau", "D. Không thể so sánh được"], "ans": "B"},
    {"q": "Câu 61. Cơ sở của quá trình quang sinh là gì?", "ops": ["A. Các phản ứng nhiệt hóa", "B. Các phản ứng quang hóa", "C. Các phản ứng phân hạch", "D. Các phản ứng trùng hợp"], "ans": "B"},
    {"q": "Câu 62. Các giai đoạn của phản ứng quang hóa theo thứ tự là:", "ops": ["A. Giai đoạn tối \u2192 giai đoạn sáng \u2192 sản phẩm", "B. Giai đoạn sáng \u2192 giai đoạn tối \u2192 phân tử giàu năng lượng tham gia phản ứng tiếp theo", "C. Chỉ có giai đoạn sáng", "D. Chỉ có giai đoạn tối"], "ans": "B"},
    {"q": "Câu 63. Quy tắc Grotthuss (Grotguc) phát biểu điều gì?", "ops": ["A. Mọi photon chiếu tới đều gây biến đổi quang hóa", "B. Chỉ những photon được hấp thụ mới gây ra biến đổi quang hóa", "C. Photon không có vai trò trong phản ứng quang hóa", "D. Chỉ photon tử ngoại mới gây biến đổi quang hóa"], "ans": "B"},
    {"q": "Câu 64. Quy tắc Bunsen-Roscoe (Bunzen Rocko) phát biểu điều gì?", "ops": ["A. Nếu tích cường độ ánh sáng với thời gian chiếu sáng không đổi thì lượng sản phẩm không đổi", "B. Lượng sản phẩm luôn tỉ lệ nghịch với cường độ ánh sáng", "C. Thời gian chiếu sáng không ảnh hưởng đến sản phẩm", "D. Cường độ ánh sáng không ảnh hưởng đến tốc độ phản ứng"], "ans": "A"},
    {"q": "Câu 65. Định luật Van't Hoff trong quang hóa phát biểu điều gì?", "ops": ["A. Tốc độ phản ứng quang hóa tỉ lệ nghịch với tốc độ hấp thụ ánh sáng", "B. Tốc độ phản ứng quang hóa được xác định bằng tốc độ hấp thụ ánh sáng", "C. Tốc độ phản ứng không liên quan đến ánh sáng", "D. Chỉ áp dụng cho phản ứng trong bóng tối"], "ans": "B"},
    {"q": "Câu 66. Quy luật Einstein-Stark phát biểu điều gì?", "ops": ["A. Mỗi photon hấp thụ có thể gây ra vô số biến đổi", "B. Sau khi hấp thụ mỗi photon chỉ gây 1 biến đổi vật lý hay hóa học", "C. Photon không gây biến đổi nào", "D. Cần ít nhất 10 photon mới gây 1 biến đổi"], "ans": "B"},
    {"q": "Câu 67. Theo thuyết bia (target theory), tác dụng quang hóa chỉ xảy ra khi nào?", "ops": ["A. Phân tử hấp thụ bất kỳ lượng tử nào", "B. Lượng tử phải xuyên đúng \"bia\" (target) của phân tử", "C. Phân tử ở trạng thái lỏng", "D. Nhiệt độ đạt mức tối đa"], "ans": "B"},
    {"q": "Câu 68. Trong công thức \u03c6 = \u03c3/S, \u03c3 được gọi là gì?", "ops": ["A. Suất lượng tử", "B. Thiết diện quang hóa (thiết diện quang sinh)", "C. Hằng số Planck", "D. Hệ số hấp thụ phân tử"], "ans": "B"},
    {"q": "Câu 69. Diện tích \"bia\" so với tiết diện hấp thụ của phân tử như thế nào?", "ops": ["A. Lớn hơn nhiều", "B. Nhỏ hơn nhiều", "C. Bằng nhau", "D. Không liên quan"], "ans": "B"},
    {"q": "Câu 70. Phổ hoạt động của phản ứng quang hóa mô tả điều gì?", "ops": ["A. Sự phụ thuộc của cấu trúc phân tử vào nhiệt độ", "B. Sự phụ thuộc tốc độ tương đối của phản ứng quang hóa vào bước sóng ánh sáng kích thích", "C. Sự phụ thuộc của khối lượng phân tử vào áp suất", "D. Sự phân bố không gian của các phân tử"], "ans": "B"},
    {"q": "Câu 71. Nếu chỉ có một chất tham gia phản ứng quang hóa, phổ hoạt động có dạng như thế nào so với phổ hấp thụ?", "ops": ["A. Hoàn toàn khác nhau", "B. Trùng với dạng phổ hấp thụ của phân tử đó", "C. Ngược pha với phổ hấp thụ", "D. Không liên quan"], "ans": "B"},
    {"q": "Câu 72. Phản ứng phân ly quang hóa A-B \u2192 (A-B)* có thể cho ra các sản phẩm nào?", "ops": ["A. Chỉ A* + B", "B. A* + B, hoặc A\u207a + B\u207b, hoặc A + B", "C. Chỉ ion A\u207a và B\u207b", "D. Chỉ tạo ra nhiệt"], "ans": "B"},
    {"q": "Câu 73. Phản ứng \"Nhị hợp\" A* + A \u2192 A*---A \u2192 A2 thuộc loại phản ứng quang hóa nào?", "ops": ["A. Phản ứng phân ly", "B. Phản ứng kết hợp", "C. Phản ứng chuyển proton", "D. Phản ứng đảo nhóm"], "ans": "B"},
    {"q": "Câu 74. Phản ứng A* + B \u2192 A\u207a + B\u207b thuộc loại phản ứng nào?", "ops": ["A. Phản ứng chuyển điện tử (quang oxy hóa khử)", "B. Phản ứng chuyển proton", "C. Phản ứng phân ly", "D. Phản ứng đảo nhóm"], "ans": "A"},
    {"q": "Câu 75. Trong quang sinh, chỉ số hiệu ứng sinh vật trên một đơn vị cường độ ánh sáng kích thích (\u02e7/I\u2011\u2080) phụ thuộc vào yếu tố nào theo bước sóng?", "ops": ["A. Chỉ phụ thuộc nhiệt độ", "B. Phụ thuộc vào phổ hấp thụ của chất trực tiếp tham gia phản ứng gây hiệu ứng quang sinh", "C. Không phụ thuộc bước sóng", "D. Chỉ phụ thuộc vào áp suất khí quyển"], "ans": "B"},
    {"q": "Câu 76. Quang hợp là quá trình biến đổi năng lượng gì thành năng lượng gì?", "ops": ["A. Năng lượng hóa học thành năng lượng điện từ", "B. Năng lượng điện từ của mặt trời thành năng lượng hóa học dưới dạng chất hữu cơ", "C. Năng lượng nhiệt thành năng lượng cơ học", "D. Năng lượng hạt nhân thành năng lượng ánh sáng"], "ans": "B"},
    {"q": "Câu 77. Phương trình tổng quát của phản ứng quang hợp là:", "ops": ["A. CH2O + O2 \u2192 CO2 + H2O + hv", "B. CO2 + H2O + hv \u2192 CH2O + O2", "C. CO2 + O2 \u2192 CH2O + H2O", "D. H2O + hv \u2192 H2 + O2 (chỉ riêng nước)"], "ans": "B"},
    {"q": "Câu 78. Theo giả thuyết của Baie (Baeyer) năm 1870, sản phẩm trung gian của quang hợp được cho là:", "ops": ["A. Glucose trực tiếp", "B. Fomaldehyt (thông qua CO)", "C. Axit lactic", "D. ATP"], "ans": "B"},
    {"q": "Câu 79. Giả thuyết của Baeyer (1870) có giá trị như thế nào hiện nay?", "ops": ["A. Vẫn hoàn toàn đúng và được áp dụng", "B. Chỉ mang ý nghĩa lịch sử vì không tìm ra khả năng hấp thụ CO và không tìm ra fomaldehyt", "C. Đã được chứng minh hoàn toàn chính xác bằng thực nghiệm hiện đại", "D. Bị bác bỏ hoàn toàn ngay khi công bố"], "ans": "B"},
    {"q": "Câu 80. Theo lý thuyết, cần bao nhiêu photon ánh sáng đỏ (650 nm) để xảy ra phản ứng quang hợp?", "ops": ["A. 1 photon", "B. 3 photon", "C. 8 photon", "D. 12 photon"], "ans": "B"},
    {"q": "Câu 81. Thực nghiệm cho thấy cần tối thiểu bao nhiêu photon để tạo ra 1 phân tử O2?", "ops": ["A. 1-2 photon", "B. 3 photon", "C. 4-12 photon", "D. Trên 20 photon"], "ans": "C"},
    {"q": "Câu 82. Vì sao hiệu suất quang hợp tính toán không thể đạt 100%?", "ops": ["A. Do CO2 trong khí quyển quá ít", "B. Do mất mát năng lượng: mất nhiệt ở giai đoạn vật lý và mất năng lượng ở các giai đoạn quang hóa", "C. Do nước không đủ để phản ứng", "D. Do nhiệt độ quá cao"], "ans": "B"},
    {"q": "Câu 83. Trong quang hợp, \"Phản ứng sáng\" tạo ra sản phẩm nào sau đây?", "ops": ["A. Glucose (C6H12O6)", "B. O2, ATP và NADPH2 (từ phân ly nước)", "C. Chỉ có CO2", "D. Chỉ có nhiệt"], "ans": "B"},
    {"q": "Câu 84. \"Phản ứng tối\" (Chu trình Calvin) sử dụng CO2 và năng lượng để tạo ra:", "ops": ["A. O2", "B. C6H12O6 (glucose)", "C. H2O", "D. ATP"], "ans": "B"},
    {"q": "Câu 85. Chuỗi vận chuyển điện tử trên màng thylakoit bao gồm 3 phức hợp nào?", "ops": ["A. PSI, PSII, ATP synthase", "B. PSI, phức hợp Cytochrome bf, PSII", "C. Chỉ có PSI và PSII", "D. NADH dehydrogenase, Cytochrome c, ATP synthase"], "ans": "B"},
    {"q": "Câu 86. Dòng electron do ánh sáng bơm các proton qua màng thylakoit tạo ra điều gì?", "ops": ["A. Một gradien điện hóa, dùng để tổng hợp ATP", "B. Trực tiếp tạo ra glucose", "C. Phân hủy CO2 ngay lập tức", "D. Không tạo ra hiệu ứng nào đáng kể"], "ans": "A"},
    {"q": "Câu 87. Sắc tố quang hợp nào chứa nguyên tử Mg ở trung tâm vòng pyrrole?", "ops": ["A. Carotenoit", "B. Chlorophyll (diệp lục)", "C. Phycocyanobilin", "D. Xanthophyll"], "ans": "B"},
    {"q": "Câu 88. Beta-caroten là loại sắc tố gì và gặp ở đâu?", "ops": ["A. Sắc tố phụ carotenoit, gặp ở tảo và thực vật cao cấp", "B. Sắc tố chính, chỉ gặp ở vi khuẩn", "C. Sắc tố duy nhất trong quang hợp", "D. Không liên quan đến quang hợp"], "ans": "A"},
    {"q": "Câu 89. Fucoxantin là sắc tố phụ của nhóm nào và gặp ở đâu?", "ops": ["A. Nhóm chlorophyll, gặp ở thực vật bậc cao", "B. Nhóm carotenoit, gặp trong một số ngành tảo", "C. Nhóm phycobilin, gặp ở vi khuẩn lam", "D. Không thuộc nhóm sắc tố nào"], "ans": "B"},
    {"q": "Câu 90. Đâu là điểm khác biệt cơ bản giữa chlorophyll a, chlorophyll b và bacteriochlorophyll a?", "ops": ["A. Số nguyên tử Mg trung tâm", "B. Các nhóm thế (nhóm chức) gắn trên vòng pyrrole", "C. Khối lượng phân tử bằng nhau nên không có khác biệt", "D. Không có khác biệt gì"], "ans": "B"},
    {"q": "Câu 91. Phát quang hóa học (chemiluminescence) là gì?", "ops": ["A. Ánh sáng phát ra không liên quan đến phản ứng hóa học", "B. Dạng ánh sáng kèm theo phản ứng hóa học", "C. Chỉ xảy ra ở nhiệt độ rất thấp", "D. Chỉ xảy ra trong chân không"], "ans": "B"},
    {"q": "Câu 92. Cơ chế phát quang ở đom đóm liên quan đến 2 thành phần chính nào?", "ops": ["A. Chlorophyll và ATP", "B. Luciferin và Luciferase", "C. NADH và FMN", "D. Hemoglobin và oxy"], "ans": "B"},
    {"q": "Câu 93. Phản ứng đầu tiên trong cơ chế phát quang đom đóm là:", "ops": ["A. Luciferin + ATP \u2192 luciferyl adenylate + PPi", "B. Luciferin + O2 \u2192 oxyluciferin trực tiếp", "C. FMNH2 + O2 \u2192 FMN + hv", "D. ATP + O2 \u2192 ADP + hv"], "ans": "A"},
    {"q": "Câu 94. Hiệu suất phát quang ở đom đóm vào khoảng bao nhiêu?", "ops": ["A. 10-20%", "B. 30-50%", "C. 80-90%", "D. 100%"], "ans": "C"},
    {"q": "Câu 95. Đom đóm thuộc họ côn trùng nào?", "ops": ["A. Formicidae", "B. Lampyridae", "C. Culicidae", "D. Apidae"], "ans": "B"},
    {"q": "Câu 96. Trong phản ứng phát quang khi hoạt hóa thể thực bào, chất nào được sinh ra nhiều khi tế bào bị kích hoạt?", "ops": ["A. CO2", "B. O2\u207b (superoxide)", "C. N2", "D. H2"], "ans": "B"},
    {"q": "Câu 97. Enzyme nào có mặt ở neutrophile giúp xúc tác phản ứng tạo ClO\u207b từ H2O2 và Cl\u207b?", "ops": ["A. Catalase", "B. Myeloperoxidase", "C. Luciferase", "D. Superoxide dismutase"], "ans": "B"},
    {"q": "Câu 98. Chất nào thường được thêm vào để làm tăng độ nhạy của phép đo phát quang bạch cầu (tăng độ nhạy khoảng 20 lần)?", "ops": ["A. Zymosan", "B. Luminol", "C. SiO2", "D. Glucose"], "ans": "B"},
    {"q": "Câu 99. Trong nghiên cứu lâm sàng, cường độ phát quang hóa học của leukocyte tăng cao nhất ở nhóm bệnh nhân nào?", "ops": ["A. Người bình thường", "B. Thiếu máu cục bộ mãn", "C. Hoại tử cơ tim", "D. Không có sự khác biệt giữa các nhóm"], "ans": "C"},
    {"q": "Câu 100. SiO2 được sử dụng trong thí nghiệm phát quang thực bào với mục đích gì?", "ops": ["A. Tăng khả năng thực bào", "B. Kiểm tra khả năng sống của macrophage (test độc tính)", "C. Làm giảm phát quang xuống 0", "D. Thay thế cho luminol"], "ans": "B"}
]

# --- DỮ LIỆU PHẦN II: 25 CÂU HỎI ĐIỀN TỪ ---
fill_data = [
    {"q": "1. Ánh sáng thực chất là một bức xạ điện tử, theo phát hiện của __________ vào năm 1865.", "ans": "Maxwell"},
    {"q": "2. Công thức liên hệ giữa bước sóng, tần số và tốc độ ánh sáng là: \u03bb\u03bd = __________.", "ans": "c"},
    {"q": "3. Theo Anhstanh, chùm sáng là chùm hạt, mỗi hạt được gọi là một __________ – lượng tử ánh sáng.", "ans": "photon"},
    {"q": "4. Công thức tính năng lượng photon là: E = h\u03bd = __________.", "ans": "hc/\u03bb", "alt": ["hc/lambda"]},
    {"q": "5. Quá trình A + h\u03bd \u2192 A* mô tả sự __________ ánh sáng của nguyên tử/phân tử.", "ans": "hấp thụ"},
    {"q": "6. Trạng thái cơ bản của phân tử, khi spin của các điện tử ghép đôi song song và ngược hướng, được gọi là trạng thái __________.", "ans": "singlet"},
    {"q": "7. Trạng thái kích thích mà spin của điện tử không được ghép đôi được gọi là trạng thái __________.", "ans": "triplet"},
    {"q": "8. Định luật __________ mô tả mối quan hệ giữa sự hấp thụ ánh sáng, nồng độ vật chất và độ xuyên sâu của tia sáng.", "ans": "Lambert-Beer", "alt": ["Lambert Beer"]},
    {"q": "9. Công thức D = kcl biểu diễn __________ của một dung dịch.", "ans": "mật độ quang", "alt": ["độ hấp thụ quang học"]},
    {"q": "10. Độ xuyên qua T được tính bằng công thức T = __________ (theo I và I\u2080).", "ans": "I/I\u2080", "alt": ["I/I0"]},
    {"q": "11. Khi hệ có nhiều thành phần, mật độ quang tổng có tính chất __________, nghĩa là D = D1 + D2 + D3 + ...", "ans": "cộng hợp", "alt": ["cộng tính"]},
    {"q": "12. Bức xạ lượng tử do phân tử phát ra khi chuyển từ trạng thái S1 xuống trạng thái cơ bản được gọi là sự phát __________.", "ans": "huỳnh quang"},
    {"q": "13. Theo quy luật __________, cực đại phổ huỳnh quang dài hơn so với cực đại phổ hấp thụ.", "ans": "Stock"},
    {"q": "14. Theo quy luật __________, phổ huỳnh quang không phụ thuộc vào bước sóng ánh sáng kích thích.", "ans": "Vavilov"},
    {"q": "15. Sự phát quang xảy ra khi phân tử chuyển từ trạng thái kích thích triplet xuống trạng thái cơ bản (T1 \u2192 S0) được gọi là __________.", "ans": "phát lân quang", "alt": ["lân quang"]},
    {"q": "16. Quá trình truyền năng lượng không phát quang từ phân tử này sang phân tử khác được gọi là quá trình __________.", "ans": "di chuyển năng lượng", "alt": ["truyền năng lượng"]},
    {"q": "17. Hiệu suất di chuyển năng lượng tỉ lệ nghịch với khoảng cách theo hàm mũ bậc __________.", "ans": "6"},
    {"q": "18. Theo quy tắc __________, chỉ những photon được hấp thụ mới gây ra những biến đổi quang hóa.", "ans": "Grotthuss", "alt": ["Grotguc"]},
    {"q": "19. Theo quy luật __________, sau khi hấp thụ mỗi photon chỉ gây ra 1 biến đổi vật lý hay hóa học.", "ans": "Einstein-Stark"},
    {"q": "20. Trong thuyết bia, đại lượng \u03c3 được gọi là __________ (thiết diện quang sinh).", "ans": "thiết diện quang hóa"},
    {"q": "21. Quang hợp là quá trình biến đổi năng lượng điện từ của mặt trời thành năng lượng hóa học dưới dạng __________, kèm theo giải phóng dưỡng khí (O2).", "ans": "chất hữu cơ", "alt": ["CH2O"]},
    {"q": "22. Chu trình __________ là giai đoạn phản ứng tối của quang hợp, sử dụng CO2 để tạo ra glucose.", "ans": "Calvin"},
    {"q": "23. Sắc tố quang hợp chính, có chứa Mg ở trung tâm, gồm chlorophyll a, chlorophyll b và __________ a.", "ans": "bacteriochlorophyll"},
    {"q": "24. Cơ chế phát quang ở đom đóm dựa trên phản ứng giữa __________ và enzyme Luciferase.", "ans": "luciferin"},
    {"q": "25. Enzyme __________ có ở neutrophile, xúc tác phản ứng giữa H2O2 và Cl\u207b để tạo ClO\u207b.", "ans": "Myeloperoxidase"}
]

# --- QUẢN LÝ TRẠNG THÁI (SESSION STATE) ---
if 'answers_a' not in st.session_state:
    st.session_state.answers_a = [None] * len(quiz_data)
if 'answers_b' not in st.session_state:
    st.session_state.answers_b = [""] * len(fill_data)

# --- THIẾT KẾ SIDEBAR MENU ---
st.sidebar.title("☀️ Tùy chọn học tập")
menu = st.sidebar.radio("Chuyển nhanh tới phần:", ["Phần I: Trắc nghiệm (100 câu)", "Phần II: Điền từ (25 câu)"])

# --- GIAO DIỆN CHÍNH ---
st.title("☀️ BÀI KIỂM TRA ÔN TẬP QUANG SINH HỌC")
st.caption("Giao diện chấm điểm tự động thực thời bám sát tài liệu gốc: 'Câu hỏi chương 3.docx'")
st.markdown("---")

# 1. LOGIC XỬ LÝ PHẦN I: TRẮC NGHIỆM TỰ ĐỘNG CHẤM NGAY
if menu == "Phần I: Trắc nghiệm (100 câu)":
    st.header("📝 PHẦN I \u2013 TRẮC NGHIỆM CHẤM ĐIỂM TỨC THÌ")
    st.info("Hệ thống hiển thị kết quả đúng/sai kèm đáp án ngay sau khi bạn tích chọn phương án.")

    def render_quiz_range(start_idx, end_idx, title):
        st.subheader(title)
        for i in range(start_idx, end_idx):
            item = quiz_data[i]
            saved_idx = st.session_state.answers_a[i]
            
            user_choice = st.radio(
                item["q"], 
                item["ops"], 
                index=saved_idx, 
                key=f"mcq_{i}", 
                horizontal=True
            )
            
            if user_choice is not None:
                st.session_state.answers_a[i] = item["ops"].index(user_choice)
                
                # Cắt ký tự đầu tiên (A, B, C, D) để đối chiếu đáp án chính xác
                if user_choice[0] == item["ans"]:
                    st.success(f"✅ Đúng! Đáp án chính xác là: **{item['ans']}**")
                else:
                    st.error(f"❌ Chưa chính xác. Đáp án đúng là: **{item['ans']}**")
            st.markdown("<hr style='margin: 10px 0px; border-top: 1px dashed #bbb;'>", unsafe_allow_html=True)

    render_quiz_range(0, 15, "A. Đại cương về ánh sáng và quang sinh học (Câu 1–15)")
    render_quiz_range(15, 40, "B. Hấp thụ ánh sáng và Định luật Lambert-Beer (Câu 16–40)")
    render_quiz_range(40, 60, "C. Huỳnh quang – Lân quang – Di chuyển năng lượng (Câu 41–60)")
    render_quiz_range(60, 75, "D. Quang hóa học (Câu 61–75)")
    render_quiz_range(75, 90, "E. Quang hợp (Câu 76–90)")
    render_quiz_range(90, 100, "F. Phát quang hóa học và Phát quang sinh học (Câu 91–100)")

# 2. LOGIC XỬ LÝ PHẦN II: ĐIỀN TỪ CHẤM ĐIỂM KHI ẤN ENTER
elif menu == "Phần II: Điền từ (25 câu)":
    st.header("✏️ PHẦN II \u2013 ĐIỀN TỪ / CỤM TỪ TỰ ĐỘNG CHẤM")
    st.info("Điền nội dung thích hợp vào chỗ trống và nhấn phím **Enter** trên bàn phím để kiểm tra kết quả.")
    
    for i, item in enumerate(fill_data):
        input_text = st.text_input(item["q"], value=st.session_state.answers_b[i], key=f"fld_{i}").strip()
        st.session_state.answers_b[i] = input_text
        
        if input_text != "":
            student_ans = input_text.lower()
            correct_ans = item["ans"].lower()
            
            # Logic kiểm tra so khớp đáp án chính xác hoặc các phương án phụ quy ước sẵn (không phân biệt hoa/thường)
            is_match = (student_ans == correct_ans)
            if "alt" in item:
                for alt_text in item["alt"]:
                    if student_ans == alt_text.lower():
                        is_match = True
                        
            if is_match:
                st.success(f"✅ Chính xác! Đáp án đúng: **{item['ans']}**")
            else:
                st.error(f"❌ Sai rồi. Đáp án chính xác phải là: **{item['ans']}**")
        st.write("")