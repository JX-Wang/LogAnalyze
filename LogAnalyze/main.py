# encoding:utf-8
"""
     分析log日志
===================
Date@2019/05/21
Author@wangjunxiong
"""
from statistical.statistical import generate_statistical
from charts.charts import generate_charts


class log_analyze(object):
    def __init__(self, logfilepath):
        self.filename = logfilepath
        pass

    def generate_target_file(self, method):
        """
        :param method:
        :return: 根据method生成第一阶段目标文件
        """
        print "文件预处理..."
        with open(self.filename, 'r') as self.f:
            if method is 1:
                rst = open("rst_1.txt", 'w')
                info = self.f.readlines()
                for item in info:
                    tmp = item.split(" ")
                    try:
                        flag = tmp[-1].index("：")
                        d = tmp[0][5:7] + tmp[0][-2:]
                        r = d + " " + tmp[1][:8] + " " + tmp[5][:-1] + " " + tmp[-1][flag+21:]
                        # print(flag)
                    except:
                        d = tmp[0][5:7] + tmp[0][-2:]
                        r = d + " " + tmp[1][:8] + " " + tmp[5][:-1] + " " + tmp[-1][-7:]
                    rst.write(r)
                rst.close()
            elif method is 2:
                rst = open("rst_2.txt", "w")
                info = self.f.readlines()
                for item in info:
                    tmp = item.split(" ")
                    if len(tmp) == 7:
                        try:
                            flag = tmp[-1].index("：")
                            r = tmp[0] + " " + tmp[1][:8] + " " + tmp[5][:-1] + " " + tmp[-1][flag+9:]
                            # print(flag)
                        except:
                            r = tmp[0] + " " + tmp[1][:8] + " " + tmp[5][:-1] + " " + tmp[-1][-7:]
                    elif len(tmp) == 8:
                        tmp = tmp[:-2]
                        r = tmp[0] + " " + tmp[1][:8] + " " + tmp[-1][:-1] + "\n"
                    rst.write(r)
                rst.close()

        self.generate_statistical_file()

    def generate_statistical_file(self):
        """
        :return: 根据第一阶段的目标文件生成统计文件
        """
        print "生成第一阶段目标文件..."
        generate_statistical().generate_start("rst_1.txt", polling=False)
        self.generate_chart()

    def generate_chart(self):
        """
        :return: 根据生成的统计文件产生图表
        """
        print "生成图表..."
        generate_charts().generate_data()
        pass

    def final_action(self):
        pass


if __name__ == '__main__':
    # 日志模式为  2019-05-20 14:18:15,126 - obtaining_domain_ns.py[line:178] - INFO: 线程数量：21,任务数量：100653
    # parser方法中使用 1 进行预处理
    # 日志模式包含 2019-05-20 14:26:16,569 - obtaining_domains_ip_cname_by_ns.py[line:82] - WARNING: 无法获取域名:www.sastt.pw 记录
    # parser方法中使用 2 进行预处理
    #filename = "obtaining_domain_ns.log"
    filename = "obtaining_domains_ip_cname_by_ns.log"  # 要处理的日志文件路径
    log_analyze(filename).generate_target_file(method=1)
