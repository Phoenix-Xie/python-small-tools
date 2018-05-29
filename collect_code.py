# coding=utf-8
from os import listdir, makedirs, system, getcwd
from os.path import splitext, exists
from shutil import move

collect_file_name = {
    "code": ['c', 'cpp'],
    "exclude": ['o', 'exe'],
}


def collectFile(dirpath, newfilename, collect_list):
    """
    将该路径下的所有后缀名正确的文件放入newfilename名字的文件
    :param dirpath: 工作路径
    :param newfilename: 新建文件夹名字
    :param collcet_list: 搜集列表
    :return: 无返回值
    """
    final_filename = dirpath + '\\' + newfilename
    if not exists(final_filename):
        makedirs(final_filename)
    for filename in listdir(dirpath):
        for collect_item in collect_list:
            collect_item = '.' + collect_item
            if splitext(filename)[1] == collect_item:
                move(dirpath + '\\' + filename, final_filename)


def printInfo():
    print("收集文件的后缀名为: \n")
    file_count = 1
    for i in collect_file_name:
        print(i, ':')
        collect_num = len(collect_file_name[i])
        c = 0
        for j in collect_file_name[i]:
            c += 1
            if c == collect_num:
                print(j + ";")
            else:
                print(j + ",",end='')


def menu():
    print("菜单：\n"
          "1. 设置文件路径\n"
          "2. 显示当前文件收集处理信息\n"
          "3. 新增分类文件及其收集文件的后缀名\n"
          "4. 删除设置的搜集文件\n"
          "5. 开始处理\n"
          "6.显示菜单\n"
          "0.退出\n")

if __name__ == '__main__':
    filedir = getcwd()
    menu()
    while True:
        try:
            opt = int(input("请输入操作:"))
        except Exception:
            system("cls")
            print("请输入正确操作")
            continue
        if opt == 0:
            break
        elif opt == 1:
            print("当前路径为：", filedir)
            newfiledir = input("输入文件路径,直接回车或输入0不修改")
            if newfiledir != '0' and newfiledir != "":
                filedir = newfiledir
        elif opt == 2:
            printInfo()
        elif opt == 3:
            while True:
                new_file_class = input("请输入分类文件夹名, 输入0结束：")
                if new_file_class == '0':
                    break
                suffix_str = input("输入该分类文件夹下的后缀名（每个后缀之间用空格隔开）\n")
                collect_file_name[new_file_class] = []
                for suffix in suffix_str.split(" "):
                    collect_file_name[new_file_class].append(suffix)
        elif opt == 4:
            printInfo()
            while True:
                delet_file_name = input("请输入需要删除的分类文件夹名字，输入0结束")
                if delet_file_name == '0':
                    break
                if delet_file_name in collect_file_name:
                    collect_file_name.pop(delet_file_name)
                else:
                    print("该文件不在其中")

        elif opt == 5:
            for i in collect_file_name:
                collectFile(filedir, i, collect_file_name[i])
            print("执行完毕")
        elif opt == 6:
            menu()
        else:
            print("请输入正确的操作数")

        x = input("按任意键继续\n")
