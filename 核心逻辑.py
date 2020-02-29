# import re
import datetime
def query_mohu(s,datacolums_list):
    # 模糊查询，包含关系
    res_list = []
    for row in datacolums_list:
        for col in row:
            if s in col:
                idx = datacolums_list.index(row)
                # print(datacolums_list[idx][0] + datacolums_list[idx][1])
                res_list.append(datacolums_list[idx][0] + datacolums_list[idx][1])
    return res_list


def is_duowei(li):
    # 多维返回true
    for l in li:
        if isinstance(l,list):
            return True
        else:
            return False


def strto(s):
    # 查询字符预处理;去空格、去制表符、中文括号转英文、字母变大写
    s=s.replace(' ','')
    s=s.replace('\t','')
    s=s.replace('（','(')
    s=s.replace('）',')')
    s=s.upper()
    return s

def get_bianhao(t):
    # 抓取编号规则；抓到返回编号，否则返回原值
    try:
        import re
        p = re.compile(r'[GgJjYy][AaBbGgDdFf][ /JjTt]?[Tt]? ?/?[Tt]? ?\d{2,6}\.?\d{0,4}-\d{2,4}')
        r = p.findall(t)
        return r[0]
    except IndexError:
        return False


def get_2colums(data_list):
    # 获取数据库前两列
    list_col=[]
    for r in data_list:
        list_row=[r[0],r[1]]
        list_col.append(list_row)
    return list_col

def query_row(s,colums_list):
    # 查询字符串所在的行号
    list_rowindex=[]
    for row in colums_list:
        for col in row:
            if col==s:
                list_rowindex.append(colums_list.index(row))
    return list_rowindex

# 丢进有效行，返回计算好时间的结果列表
def  get_jieguolist(row,time_tiaojian,data_list):
    # 返回值列表设计：["完整名称","废止状态","可用情况","生效时间","代替情况","自定义库判断"]
    if row is None:
        print("查无此条目，检查输入编号或名称是否正确")
    else:
        # print(r)

        bianhao = data_list[row][0]                            # 标准编号
        biaozhun_name = data_list[row][1]                      # 标准名称

        shishi_time = data_list[row][2]                        # 实施时间
        feizhi_time = data_list[row][3]                        # 废弃时间
        shishi_time = datetime.datetime.strptime(shishi_time, "%Y-%m-%d %H:%M:%S")
        if feizhi_time!='None':
            feizhi_time = datetime.datetime.strptime(feizhi_time, "%Y-%m-%d %H:%M:%S")
        biaozhun_zhuangtai = data_list[row][4]                 # 标准状态
        daitiqingkuang = data_list[row][5]                     # 代替情况
        is_diy = data_list[row][6]                         # 自定义库区分
        wanzheng_name = bianhao + biaozhun_name                # 完整名称 3

         # 有效时间连接处理
        if feizhi_time is None:
            feizhi_time2=""
        else:
            feizhi_time2=str(feizhi_time).split(" ")[0].replace("-",".")
        shishi_time2=str(shishi_time).split(" ")[0].replace("-",".")

        youxiao_time = shishi_time2 + "~" + feizhi_time2
        # 返回值列表设计：["完整名称","废止状态","可用情况","生效时间","代替情况","自定义库判断"]
        list_res = []
        if biaozhun_zhuangtai == "作废":
            # 废止
            if time_tiaojian < shishi_time:
                # a.情况,废止-不可用
                list_res = [wanzheng_name, "废止", "不可用，此时规范还未实施", youxiao_time, daitiqingkuang, is_diy]
                return list_res
            elif time_tiaojian >= shishi_time and time_tiaojian < feizhi_time:
                # b.情况,废止-可用
                list_res = [wanzheng_name, "废止", "可用", youxiao_time, daitiqingkuang, is_diy]
                return list_res
            elif time_tiaojian >= feizhi_time:
                # c.情况,废止-不可用
                list_res = [wanzheng_name, "废止", "不可用，规范已废弃", youxiao_time, daitiqingkuang, is_diy]
                return list_res
        else:
            # 现行
            if time_tiaojian < shishi_time:
                # d.情况,有效-不可用
                list_res = [wanzheng_name, "有效", "不可用，此时规范还未实施", youxiao_time, daitiqingkuang, is_diy]
                return list_res
            elif time_tiaojian >= shishi_time:
                # e.情况,有效-可用
                list_res = [wanzheng_name, "有效", "可用", youxiao_time, daitiqingkuang, is_diy]
                return list_res



def get_rowlist(s,time_tiaojian,datacolums_list,data_list):
    # 主逻辑开始
    s = strto(s)
    # print('原值:', s)
    bianhao = get_bianhao(s)

    # 判断是否抓到编号
    if bianhao != False:
        # print('抓到编号:', bianhao)
        strname = s.replace(bianhao, '')
        if strname != '':
            print('剩余名称:', strname)
        print('用编号查行号开始-------------------------------')
        row = query_row(bianhao, datacolums_list)
        if row:
            print('行号：', row)
            print('开始执行名称检查---------------------------')
            if data_list[row[0]][1] == strname:
                print('正常；a')
                jieguo_list = get_jieguolist(row[0], time_tiaojian, data_list)
                print('a情况:', jieguo_list)
                jieguo_list.insert(0, s)
                jieguo_list.insert(1, '正常')
                print(jieguo_list)
                return jieguo_list
            else:
                print('名称错误，标红；b')
                jieguo_list = get_jieguolist(row[0], time_tiaojian, data_list)
                print('b情况:', jieguo_list)
                # 错误类型判断------------
                if strname=='':
                    err='缺少名称'
                else:
                    err='名称错误'
                    # ----------------------
                jieguo_list.insert(0, s)
                jieguo_list.insert(1, err)
                print(jieguo_list)
                return jieguo_list
        else:
            print('用编号没查到', row)
            print('尝试用剩余名称查询--------------------------')
            row = query_row(strname, datacolums_list)
            if row:
                if len(row) == 1:
                    print('查到一个结果;编号错误c，标红', row)
                    jieguo_list = get_jieguolist(row[0], time_tiaojian, data_list)
                    print('c情况:', jieguo_list)
                    jieguo_list.insert(0, s)
                    jieguo_list.insert(1, '编号错误')
                    print(jieguo_list)
                    return jieguo_list
                else:
                    # -----------------------------------------------这是原来【查询多个结果】的功能，先停用
                    # print('查到多个结果;编号错误d，标红', row)
                    # res_list = []
                    # for r in row:
                    #     jieguo_list = get_jieguolist(r, time_tiaojian, data_list)
                    #     jieguo_list.insert(0, s)
                    #     jieguo_list.insert(1, '编号错误 ')
                    #     print(jieguo_list)
                    #     res_list.append(jieguo_list)
                    # print(res_list)
                    # return res_list
                    # -----------------------------------------------------------
                    # print('新功能，是否包含查询值----------')
                    ql = query_mohu(strname, datacolums_list)
                    if ql:
                        ql = '找到相似值：' + str(ql)
                    else:
                        ql = ''
                    res_list = [s, '编号错误', ql, '', '', '', '', '']
                    return res_list
            else:
                print('用剩余名也没查到e；红', row)
                print('启动模糊查询，是否包含查询值----------')
                ql=query_mohu(s, datacolums_list)
                if ql:
                    ql='找到相似值：'+str(ql)
                else:
                    ql = ''
                res_list=[s,'规范不存在',ql,'','','','','']
                return res_list

    else:
        # print('没抓到编号，开始用全值  |' + s + '|  查询-----------------')
        row = query_row(s, datacolums_list)
        if row:
            if len(row) == 1:
                print('查到一个结果;', row)
                jieguo_list = get_jieguolist(row[0], time_tiaojian, data_list)
                print('f情况:', jieguo_list)
                jieguo_list.insert(0, s)
                jieguo_list.insert(1, '缺少编号')
                print(jieguo_list)
                return jieguo_list
            else:
                # print('查到多个结果;', row)
                # res_list = []
                # for r in row:
                #     jieguo_list = get_jieguolist(r, time_tiaojian, data_list)
                #     jieguo_list.insert(0, s)
                #     jieguo_list.insert(1, '找到多个结果')
                #     print(jieguo_list)
                #     res_list.append(jieguo_list)
                # print(res_list)
                # return res_list
                ql = query_mohu(s, datacolums_list)
                if ql:
                    ql = '找到相似值：' + str(ql)
                else:
                    ql = ''
                res_list = [s, '缺少编号', ql, '', '', '', '', '']
                return res_list
        else:
            # print('查不到结果，标红', row)
            ql = query_mohu(s, datacolums_list)
            if ql:
                ql='找到相似值：'+str(ql)
            else:
                ql = ''
            res_list = [s, '规范不存在', ql, '', '', '', '','']
            return res_list


if __name__=='__main__':
    import 标准库
    import 自定义库
    # 合并数据库处理---------------------
    bz=标准库.biaozhun_list
    diy=自定义库.diy_list
    del diy[0]    #删除标题
    data_list=bz+diy
    # print(data_list)
    datacolums_list=get_2colums(data_list)
    # print(datacolums_list)

    str_p = '2012-01-30'
    time_tiaojian = datetime.datetime.strptime(str_p, '%Y-%m-%d')

    # s="YD/T 5113-2005	WDM光缆通信工程网管系统设计规范"  #a
    # s="YD/T 5113-2005	WDM光缆通统设计规范"  #b
    # s="YD/T 5113-2888	WDM光缆通信工程网管系统设计规范"  #c
    # s="YD/T 5113-2888	通信局（站）防雷与接地工程验收规范"  #d
    # s="YD/T 5113-2888	WDM光缆通信设计规范"  #e
    # s="WDM光缆通信工程网管系统设计规范"
    # s="光缆通信"
    s='2008'

    l=get_rowlist(s,time_tiaojian,datacolums_list,data_list)
    # l=query_mohu(s,datacolums_list)
    print(l)

