import goujian
import tools

danyuan_list = [goujian.danyuan(0, 0, 0, 0, 0)]
jiedian_list = {}
waili_list = []

def creat_jiedian(pos):
    jiedian_list[len(jiedian_list)]=pos
    pass

def creat_danyuan(l,EI,EA,dot_1,dot_2,a=None):
    if a is None:
        a = tools.angle(jiedian_list[dot_1],jiedian_list[dot_2])
    danyuan_list.append(goujian.danyuan(l=l,EI=EI,EA=EA,a=a,dot_1=dot_1,dot_2=dot_2))
    pass

def creat_waili(danyuan,leixin,F,c_1,c_2=0):
    pass