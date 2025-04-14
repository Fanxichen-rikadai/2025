import cv2
import matplotlib.pyplot as plt

#读取图片
image_path1 = "C:/Users/86142/Desktop/python/gazou/1.png"
image_path2 = "C:/Users/86142/Desktop/python/gazou/mask.png"

image1 = cv2.imread(image_path1)
image2 = cv2.imread(image_path2)

images = [image1,image2]

for img in images:
 plt.imshow(img)
 plt.axis('off')
 plt.show()

#算出image1的中心坐标
original_shape = image1.shape
[y,x,z] = original_shape
x1= int(x/2)
y1= int(y/2)
print(f"中心座標は[{x1},{y1}]")

#image1中间列的坐标值以及他们的画素值
Xc = []
Yc = []
pixels = []
image1grey = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
for i in range(int(y)):
 pixel = image1grey[i,int(x1)]
 print(f"({x1,i})点のピクセルは{pixel}")
 Xc.append(int(x1))
 Yc.append(i)
 pixels.append(pixel)

 #导出到excel
import pandas as pd
df = pd.DataFrame({
  "Xc":Xc,
  "y":Yc,
  "pixel":pixels
 })
save_path = "C:/Users/86142/Desktop/output_pixels.xlsx"
df.to_excel(save_path,index=False)
print(df)

#输出image2涂白部分坐标
Xc2 = []
Yc2 = []
pixels2 = []

image2grey = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
[h, w] = image2grey.shape  # 高度和宽度

for i in range(h):       # 遍历所有 y（行）
    for j in range(w):   # 遍历所有 x（列）
        pixel2 = image2grey[i, j]
        if pixel2 == 255:
            print(f"({j},{i})点のピクセルは{pixel2}")
            Xc2.append(j)
            Yc2.append(i)
            pixels2.append(pixel2)

# 导出Excel
import pandas as pd
df2 = pd.DataFrame({
    "Xc": Xc2,
    "y": Yc2,
    "pixel": pixels2
})
save_path2 = "C:/Users/86142/Desktop/output2_pixels.xlsx"
df2.to_excel(save_path2, index=False)
print(df2)

# 取出 image2 为白色的所有位置，对应到 image1 的像素值（灰度）
X_white_all = []
Y_white_all = []
Pixel_from_image1 = []

image1grey = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2grey = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
[h, w] = image2grey.shape

for i in range(h):
    for j in range(w):
        if image2grey[i, j] == 255:
            pixel1 = image1grey[i, j]
            X_white_all.append(j)
            Y_white_all.append(i)
            Pixel_from_image1.append(pixel1)
            print(f"[{j},{i}] は白い，同じ位置で image1 のピクセルは {pixel1}")

# 保存为 Excel 或 CSV
df_pixels = pd.DataFrame({
    "x": X_white_all,
    "y": Y_white_all,
    "image1_pixel": Pixel_from_image1
})
save_excel = "C:/Users/86142/Desktop/image1_pixels_from_mask_white.xlsx"
save_csv = "C:/Users/86142/Desktop/image1_pixels_from_mask_white.csv"
df_pixels.to_excel(save_excel, index=False)
df_pixels.to_csv(save_csv, index=False)





