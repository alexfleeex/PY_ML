from PIL import Image
import numpy as np



img=Image.open(r"C:\Users\Alexey\Desktop\ВУЗ_ДОКИ\photo.jpg")
# img.show()

x=np.array(img, dtype=np.float32)

new_img=Image.fromarray(x.mean(axis=2))

new_img.show()