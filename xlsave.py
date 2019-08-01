import xlrd
import xlwt


class Xl:
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet_1 = workbook.add_sheet('执法情况报表')
    worksheet_2 = workbook.add_sheet('检查情况汇总')

    def __init__(self, per, tel, dat, unt, **kargs):
        self.per = per
        self.tel = tel
        self.dat = dat
        self.unt = unt
        self.lists = kargs

    def head(self):
        sty_1 = xlwt.XFStyle()
        alignment_1 = xlwt.Alignment()
        font_1 = xlwt.Font()
        font_1.name = '方正小标宋简体'
        font_1.height = 20*20
        alignment_1.horz = 0x02
        sty_1.font = font_1
        sty_1.alignment = alignment_1

        sty_2 = xlwt.XFStyle()
        font_2 = xlwt.Font()
        font_2.name = '黑体'
        font_2.height = 20*16
        sty_2.font = font_2
        self.worksheet_1.col(1).width = 15000
        for i in range(2, 7):
            self.worksheet_1.col(i).width = 6000
        self.worksheet_1.write_merge(0, 0, 0, 6, self.unt+'执法检查报表', sty_1)
        self.worksheet_1.write(1, 1, '填报人：'+self.per, sty_2)
        self.worksheet_1.write(1, 3, '联系电话：'+self.tel, sty_2)
        self.worksheet_1.write(1, 5, '填报时间：'+self.dat, sty_2)
        self.worksheet_1.write(2, 0, '序号', sty_2)
        self.worksheet_1.write(2, 1, '检查企业', sty_2)
        self.worksheet_1.write(2, 2, '检查时间', sty_2)
        self.worksheet_1.write(2, 3, '执法人员数量', sty_2)
        self.worksheet_1.write(2, 4, '出动检查组', sty_2)
        self.worksheet_1.write(2, 5, '专家人数', sty_2)
        self.worksheet_1.write(2, 6, '是否责令停产', sty_2)

    def body(self):
        r = 3
        i = 1
        sty_3 = xlwt.XFStyle()
        font_3 = xlwt.Font()
        font_3.name = '仿宋_GB2312'
        font_3.height = 20*14
        sty_3.font = font_3
        for k in self.lists.keys():
            self.worksheet_1.write(r, 2, k, sty_3)
            self.worksheet_1.write(r, 0, i, sty_3)
            i += 1
            r += 1
            c = 2
            for v in self.lists[k]:
                self.worksheet_1.write(r, c, v, sty_3)
                c += 1

    def all(self):


        self.worksheet_2 = self.workbook.add_sheet('汇总')



