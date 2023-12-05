fo = open("gamelines.txt","w")
print("filename:", fo.name)
str = "test"
fo.write(str)

# 关闭文件
fo.close()