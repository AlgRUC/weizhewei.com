import os
import sys
import face_recognition
from PIL import Image
import numpy as np

# 检查命令行参数数量是否正确
if len(sys.argv) < 3:
    print("Usage: script.py input_directory output_directory")
    sys.exit(1)

# 获取命令行参数
input_dir = sys.argv[1]
output_dir = sys.argv[2]

def golden_ratio_margin(top, right, bottom, left, image_shape, extra_margin=0.4):
    # 计算人脸框的宽度和高度
    width = right - left
    height = bottom - top
    
    # 找出较长的一边，作为正方形边长
    max_dim = max(width, height)
    
    # 计算总的正方形尺寸，确保包含黄金分割的边距
    square_size = int(max_dim * 1.618)
    
    # 增加额外的边距
    square_size_with_margin = int(square_size * (1 + extra_margin))
    
    # 计算中心点
    center_x = (left + right) // 2
    center_y = (top + bottom) // 2
    
    # 计算裁剪框的左上角坐标
    left = max(center_x - square_size_with_margin // 2, 0)
    top = max(center_y - square_size_with_margin // 2, 0)
    right = min(center_x + square_size_with_margin // 2, image_shape[1])
    bottom = min(center_y + square_size_with_margin // 2, image_shape[0])
    
    # 如果裁剪框的右下角超出了图像边界，则调整左上角的位置
    adjust_left = False
    adjust_top = False
    if right - left < square_size_with_margin:
        diff = square_size_with_margin - (right - left)
        left = max(left - diff // 2, 0)
        adjust_left = True
    if bottom - top < square_size_with_margin:
        diff = square_size_with_margin - (bottom - top)
        top = max(top - diff // 2, 0)
        adjust_top = True
    
    # 如果调整了左上角的位置，则再次检查裁剪框是否超出边界
    if adjust_left or adjust_top:
        right = min(left + square_size_with_margin, image_shape[1])
        bottom = min(top + square_size_with_margin, image_shape[0])

    return top, right, bottom, left

def process_images_in_directory(directory):
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        # 检查是否为图片文件
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(directory, filename)
            
            # 使用face_recognition加载图片并找到所有人脸位置
            image = face_recognition.load_image_file(filepath)
            face_locations = face_recognition.face_locations(image)
            
            # 获取图片的形状
            image_shape = image.shape
            
            # 对于每个人脸，应用黄金分割裁剪
            for i, face_location in enumerate(face_locations):
                top, right, bottom, left = face_location
                new_top, new_right, new_bottom, new_left = golden_ratio_margin(
                    top, right, bottom, left, image_shape, extra_margin=0.6)
                
                # 使用PIL来裁剪图片
                pil_image = Image.fromarray(image)
                cropped_image = pil_image.crop((new_left, new_top, new_right, new_bottom))
                
                cropped_image.save(os.path.join(output_dir, f'{i}_{filename}'))

if __name__ == "__main__":
    directory = input_dir
    process_images_in_directory(directory)
