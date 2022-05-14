# improving-image-quality-for-cv-task
no problem, it's easy

1. các bộ lọc, làm mịn ảnh (image smoothing)
- loại bỏ hạt nhiễu, làm mờ biên ảnh (biên ảnh là tập hợp các điểm có sự thay đổi đột ngột về mức xám)
- toán tử lân cận là pp pbien dùng làm , mịn ảnh:
   g(x,y)= T[f(x,y)]
    g(): ảnh đầu ra, 
    f(): ảnh đầu vào,
    T(): toán tử tác động lên f
- bộ l trung bình: mean filter : +gtr mức xám ảnh ra: gtr tb của vùng lân cận đầu vào
                              + loại bỏ nhiễu gauss, mất chi tiết và làm mờ biên 
- bl gauss: các hso cửa sổ lọc đc xd trên pân bố gauss 2d 
  
- bl trung vị

-bl bảo tồn biên;
  +bl song phương (bilateral filter): 
  + bl có hướng dẫn (guided filter)
                     
                     
                 
  
2. bl tăng độ sắc nét (image sharpening)
3. khôi phục ảnh (image restoration)
4. cân bằng biểu đồ tần số (histogram equalization)
5. phân ngưỡng (thresholding)
6. xl hình thái hoc (image morphology)
7. xử lý kt ảnh (image resize)
                 
