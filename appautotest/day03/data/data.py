import os

path = os.path.abspath(__file__)
print("绝对路径:"+path)

path1 = os.path.split(__file__)
print("（文件路径，文件名）："+path1[0]+path1[1])

path2 = os.path.dirname(__file__)
print("文件路径："+path2)

path3 = os.path.basename(__file__)
print("文件名："+path3)

path4 = os.path.join(path1[0],path1[1])
print("组合文件名："+path4)