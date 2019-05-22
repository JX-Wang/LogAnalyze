# encoding:utf-8
"""
生成统计文件
==============
Date@2019/05/21
Author@wangjunxiong
"""


class generate_statistical(object):
    """generate statistical documents"""
    def __init__(self):
        """
        :param src_file:
        :return statistical_file
        """

    def generate_start(self, src_file, polling=True):
        """..."""
        if polling:
            pass
        else:
            m_rst = open('rst_m.txt', 'w')
            with open(src_file, 'r') as f:
                lines = f.readlines()
                m_info_count, m_warn_count = 0, 0
                line = lines[0].split()
                last_m, last_h, last_d = int(line[1][3:5]), int(line[1][:2]), int(line[0])
                self.m, self.h, self.d = last_m, last_h, last_d
                for line in lines[1:]:
                    line = line.split()
                    time, info = line[0] + " " + line[1], line[2]
                    print time
                    if (int(time[-5:-3]) - last_m) in [1, -59]:
                        m_txt = str(last_m) + " " + str(m_info_count) + " " + str(m_warn_count)
                        print >> m_rst, m_txt
                        print m_txt
                        # m_info_count, m_warn_count, last_m = 0, 0, int(time[-5:-3])
                        m_info_count, m_warn_count, last_m = 0, 0, int(time[-5:-3])
                        # last_m, last_h, last_d = int(line[1][3:5]), int(line[1][:2]), line[0][5:]
                        # print int(time[-5:-3]), last_m
                    elif (int(time[-5:-3]) - last_m) not in [0, 1, -59]:  # 存在程序中断，时间节点跳跃的情况
                        m_txt = str(last_m) + " " + str(m_info_count) + " " + str(m_warn_count)
                        print >> m_rst, m_txt
                        print m_txt
                        if last_m == 59:
                            m_info_count, m_warn_count, last_m = 0, 0, 0
                            last_h += 1
                        else:
                            m_info_count, m_warn_count, last_m = 0, 0, last_m + 1
                    else:
                        if info == "INFO":
                            m_info_count += 1

                        else:
                            m_warn_count += 1
            m_rst.close()
        self.h_commit()
        self.d_commit()

    def m_commit(self, data):
        pass

    def h_commit(self):
        """
        :format  minutes, info, warn
        """
        rst_h = open('rst_h.txt', 'w')
        with open('rst_m.txt', 'r') as f:  # 使用分析完之后的初始版本的分钟文件获得小时文件
            lines = f.readlines()
            # print lines[0].split()[1:]
            info, warn = [int(i) for i in lines[0].split()[1:]]
            for line in lines[1:]:
                tmp_m, tmp_info, tmp_warn = [int(i) for i in line.split()]
                if self.m == tmp_m:
                    txt = str(self.h) + " " + str(info) + " " + str(warn)
                    print >> rst_h, txt
                    if self.h != 23:
                         self.h += 1
                    else:
                         self.h = 0
                    info, warn = 0, 0
                info += tmp_info
                warn += tmp_warn
            txt = str(self.h) + " " + str(info) + " " + str(warn)
            print >> rst_h, txt
        rst_h.close()

    def d_commit(self):
        rst_d = open('rst_d.txt', 'w')
        with open('rst_h.txt', 'r') as f:  # 使用分析完之后的初始版本的分钟文件获得小时文件
            lines = f.readlines()
            info, warn = [int(i) for i in lines[0].split()[1:]]
            for line in lines[1:]:
                tmp_h, tmp_info, tmp_warn = [int(i) for i in line.split()]
                if tmp_h == 0:
                    # print self.d, type(self.d)
                    txt = str(self.d) + " " + str(info) + " " + str(warn)
                    print >> rst_d, txt
                    info, warn = 0, 0
                    self.d += 1
                info += tmp_info
                warn += tmp_warn
            txt = str(self.d) + " " + str(info) + " " + str(warn)
            print >> rst_d, txt
        rst_d.close()


if __name__ == '__main__':
    generate_statistical().generate_start("../rst_1.txt", polling=False)
    #generate_statistical().h_commit()


