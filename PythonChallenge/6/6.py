import re,os,zipfile

re_name = re.compile(r"Next nothing is (\d+)")
root_path=os.path.abspath('.')   #表示当前所处的文件夹的绝对路径
path = "/channel/"
seed = "90052"
comments = []

z = zipfile.ZipFile(root_path+"/channel.zip","r") #使用zipfile对压缩文件进行操作

while True:
    file_name = root_path+path+seed+".txt"
    comments.append(z.getinfo(seed+".txt").comment.decode("utf-8")) #使用utf-8编码，python3输出的时候，因为没有加utf8 莫名其妙出错
    with open(file_name,'r') as file:
        text = file.read()
        lists = re_name.findall(text)

    if lists:
        seed = lists[0]
        print(seed)
    else:
        break

print("".join(comments))   #hockey.html
# 提示： it's in the air. look at the letters.    可以猜到单词 oxygen
# 所以 可以猜到 oxygen.html

