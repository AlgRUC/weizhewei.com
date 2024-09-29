import os
import sys
from PIL import Image 

# 检查命令行参数数量是否正确
if len(sys.argv) < 3:
    print("Usage: script.py input_directory output_directory")
    sys.exit(1)

# 获取命令行参数
input_dir = sys.argv[1]
output_dir = sys.argv[2]

# 如果输出目录不存在，则创建它
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 定义图片缩放尺寸
size = (400, 400)

# 列出指定目录下的所有文件
file_paths = os.listdir(input_dir)

# 遍历文件并处理
for infile in file_paths:
    filepath = os.path.join(input_dir, infile)
    # 检查是否为文件
    if os.path.isfile(filepath):
        try:
            # 打开图片文件
            im = Image.open(filepath)
            # 缩放图片
            im.thumbnail(size, Image.Resampling.LANCZOS)
            # 创建新的文件路径用于保存
            outfile = os.path.join(output_dir, infile)
            # 保存缩放后的图片
            im.save(outfile, "JPEG")
        except IOError:
            print(f"Cannot create thumbnail for '{infile}'")