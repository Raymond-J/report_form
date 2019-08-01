
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtCore
import re
from mainUI import Ui_MainWindow
import sys
import datetime

unitnames = ['大港街',
             '新城镇',
             '新城镇',
             '东疆保税港区综合监管和执法局',
             '高新区安监局',
             '南港安监局',
             '新城镇',
             '区综合监管和执法局',
             '杨家泊镇人民政府公共安全办公室',
             '新河街道办事处',
             '新村街道办事处',
             '南港安监局',
             '新北街道办事处',
             '寨上街安全办',
             '太平镇',
             '茶淀街道办事处',
             '北塘街道办事处',
             '区安全生产执法监察大队',
             '大沽街',
             '海滨街',
             '区安全生产监督管理局',
             '塘沽街道办事处',
             '杭州道街道办事处',
             '中新天津生态城安全生产监督管理局',
             '胡家园街',
             '中塘镇']
companylist = ['天津市滨海新区塘沽老弯道港发加油站有限责任公司',
               '天津市滨海新区塘沽光大加油站 ',
               '中国石化销售有限公司天津石油分公司滨海新胡路加油站',
               '中国石化销售有限公司天津石油分公司滨海上海道加油站',
               '天津远洋船舶供应有限公司',
               '天津开发区博达运输有限公司四号路加油站',
               '中国石化销售有限公司天津石油分公司滨海津塘路加油站',
               '中国石化销售有限公司天津石油分公司滨海中瑞加油站',
               '中国石化销售有限公司天津石油分公司滨海新滨加油站',
               '天津市塘沽港垦加油站',
               '中国石油化工股份有限公司天津石油分公司滨海桥东加油站',
               '中国石化销售有限公司天津石油分公司滨海新北加油站',
               '中国石化销售有限公司天津石油分公司滨海金三角加油站',
               '天津市塘沽协和加油服务有限公司',
               '天津大沽化工股份有限公司',
               '天津海晶科技发展有限公司',
               '天津瑞泰精细化工有限公司',
               '天津康顺化学有限公司',
               '天津大沽精细化工有限公司',
               '中国石化销售有限公司天津石油分公司滨海三环加油站',
               '天津中油滨海石油销售有限公司海滨大道津晋高速路分部',
               '天津中油滨海石油销售有限公司海滨大道上高路分部',
               '天津中油滨海石油销售有限公司滨海大道南疆一号分部',
               '天津中油滨海石油销售有限公司滨海大道南疆二号分部',
               '天津中油滨海石油销售有限公司海滨大道独流减河一号分部',
               '天津中油滨海石油销售有限公司海滨大道独流减河二号分部',
               '天津市滨海新区塘沽河南路才源加油站有限公司',
               '中国石化销售有限公司天津石油分公司塘沽兴化道加油站',
               '中国石化销售有限公司天津石油分公司滨海津沽路加油站',
               '中国石油天然气股份有限公司天津销售分公司塘沽东沽加油站',
               '中海油销售天津有限公司滨海新区东沽石油南路加油站',
               '中国石油化工股份有限公司天津石油分公司善门口油库',
               '天津市塘沽江海化工有限公司',
               '天津金聚丰化工涂料有限公司',
               '天津市秉发气体销售有限公司',
               '中国石化销售有限公司天津石油分公司塘沽河头加油站',
               '天津市滨海新区塘沽陈圈加油站',
               '天津市滨海新区塘沽胡家园加油站',
               '天津市塘沽蓝天加油站',
               '中国石油化工股份有限公司天津石油分公司滨海十四号桥加油站',
               '中国石化销售有限公司天津石油分公司滨海中心庄加油站',
               '中国石油化工股份有限公司天津石油分公司滨海于庄子加油站',
               '天津市滨海新区塘沽中心桥加油站有限公司',
               '中石化新海湾（天津）成品油销售有限公司滨海新区胡家园加油站',
               '天津市滨海新区塘沽宁车沽加油站',
               '天津塘沽中油华北滨海加油站有限公司',
               '天津乐金渤海化学有限公司PVC工厂（顺化道）',
               '天津市东大化工有限公司',
               '天津市塘沽渤海化工气体有限公司',
               '天津市临港气体有限公司',
               '天津市塘沽兴永旺气体销售有限公司',
               '中国石油天然气股份有限公司天津销售分公司塘沽永兴加油站',
               '中国石油化工股份有限公司天津石油分公司塘沽海门加油站',
               '壳牌华北石油集团有限公司响螺湾加油站',
               '中国石化销售有限公司天津石油分公司滨海水柜路加油站',
               '中国石油化工股份有限公司天津石油分公司滨海新城加油站',
               '中海油天津液化天然气有限责任公司（LNG）',
               '天津北方石油有限公司',
               '天津国际石油储运有限公司',
               '中国航油集团北方储运有限公司',
               '中国石化销售有限公司华北分公司天津储备库（新河库、南疆一号库、二号库）',
               '中国石化管道储运有限公司天津输油处塘沽油库',
               '中国石化集团石油商业储备有限公司天津分公司（天津实华原油储备基地）',
               '天津德海石油制品销售有限责任公司二号路加油站',
               '天津德海石油制品销售有限责任公司跃进路加油站',
               '天津德海石油制品销售有限责任公司临海路加油站',
               '天津恒港加油服务有限公司 ',
               '天津南疆加油站有限公司 ',
               '天津金港南疆商贸有限责任公司',
               '中国石化销售有限公司天津石油分公司滨海临港桥加油站',
               '中国石化销售有限公司天津石油分公司黄海北路加油站',
               '中国石化销售有限公司天津石油分公司天池路加油加气站',
               '中国石油天然气股份有限公司天津销售分公司塘沽北塘加油站',
               '天津市泰联石油贸易有限公司',
               '天津市塘沽金桥加油站',
               '天津长芦汉沽盐场有限责任公司',
               '天津市汉沽高分子化工助剂有限公司',
               '天津市滨海新区汉沽汉南路加油站有限责任公司',
               '中国石化销售有限公司天津石油分公司汉沽新开北路加油站',
               '中国石油天然气股份有限公司天津销售分公司汉沽文化街加油站',
               '中国石油天然气股份有限公司天津销售分公司汉沽汉通加油站',
               '中国石化销售有限公司天津石油分公司汉沽北海加油站',
               '天津市汉沽石油公司新华路加油站',
               '中国石化销售有限公司天津石油分公司汉沽芦汉路加油站',
               '天津市汉沽合佳化工有限责任公司',
               '天津市原龙化工有限公司',
               '天津市汉沽环皓化工有限公司',
               '天津市博创化工有限公司',
               '天津邦威涂料有限公司',
               '中国石油化工股份有限公司润滑油天津分公司',
               '天津市天诚化工有限公司',
               '天津市营通伟业物流有限公司',
               '天津市津华化工厂',
               '中国石油天然气股份有限公司天津销售分公司汉沽汉华加油站',
               '中国石油天然气股份有限公司天津销售分公司汉沽金华加油站',
               '天津中油滨海石油销售有限公司海滨大道双桥道服务部',
               '中国石油天然气股份有限公司天津销售分公司汉沽汉兴加油站',
               '中国石油天然气股份有限公司天津销售分公司汉沽汉旺加油站',
               '中国石油化工股份有限公司天津石油分公司汉沽涧河加油站',
               '中国石油化工股份有限公司天津石油分公司汉沽东风路加油站',
               '天津中油滨海石油销售有限公司海滨大道涧河一号服务区',
               '中国石油化工股份有限公司天津石油分公司汉沽太平路加油站',
               '中国石油化工股份有限公司天津石油分公司汉沽汉北路加油站',
               '天津海钰投资发展有限公司滨海新区寨上街新开南路加油站',
               '天津市天顺碱业有限公司',
               '天津云海裕森科工贸有限公司',
               '天津市雅图色彩工贸有限公司',
               '天津市汉沽双合压缩气有限公司',
               '天津市汉沽汉文压缩气有限公司',
               '天津市金美化工有限公司',
               '天津市君博加油站有限公司',
               '壳牌华北石油集团有限公司津汉公路李自沽加油站',
               '中国石化销售有限公司天津石油分公司九龙里加油站',
               '中国石油天然气股份有限公司天津销售分公司汉沽汉宇加油站',
               '中国石油天然气股份有限公司天津销售分公司汉沽汉清加油站',
               '天津海钰投资发展有限公司滨海新区茶淀街四纬路加油站',
               '中国石化销售有限公司天津石油分公司汉沽津汉路加油站',
               '中国石化销售有限公司天津石油分公司汉沽汉茶路加油站',
               '中国石化销售有限公司天津石油分公司汉沽茶淀西加油站',
               '天津市驰隆化工有限公司',
               '融兴瑞泰实业有限公司汉沽加油加气一站',
               '融兴瑞泰实业有限公司汉沽加油加气二站',
               '天津海钰投资发展有限公司滨海新区杨家泊镇唐津高速加油站',
               '天津海钰投资发展有限公司滨海新区杨家泊镇汉榆公路东加油站',
               '天津海钰投资发展有限公司滨海新区杨家泊汉榆公路加油站',
               '中国石油天然气股份有限公司天津销售分公司汉沽汉东加油站',
               '中国石油化工股份有限公司天津分公司',
               '中国石化集团资产经营管理有限公司天津石化分公司',
               '中国石油天然气股份有限公司东北销售大港分公司',
               '天津石化液化空气气体有限公司',
               '天津精华石化有限公司天泰分公司',
               '天津联博化工股份有限公司第一分公司',
               '中沙（天津）石化有限公司',
               '天津市燃料油公司',
               '液化空气（天津）有限公司',
               '天津联博化工股份有限公司',
               '天津林圣金海化工有限公司',
               '天津精华石化有限公司群力分公司',
               '中国石油天然气股份有限公司天津销售分公司大港贵和加油站',
               '天津中石化工物流有限公司加油站',
               '天津精华石化有限公司加油站',
               '中国石化销售有限公司天津石油分公司大港圣龙加油站',
               '中国石油天然气股份有限公司天津销售分公司大港乙烯加油站',
               '中国石油天然气股份有限公司天津销售分公司大港金马加油站',
               '中国石化销售有限公司天津石油分公司大港世纪大道加油站',
               '中国石化销售有限公司天津石油分公司大港津港路加油站',
               '天津市大港明珠加油站',
               '天津渤大硫酸工业有限公司',
               '天津市北斗星精细化工有限公司',
               '天津联力化工有限公司',
               '利安隆博华（天津）医药化工有限公司',
               '天津鲁华泓锦新材料科技有限公司',
               '天津嘉泰伟业化工有限公司',
               '天津渤化中河化工有限公司',
               '天津市敬业精细化工有限公司',
               '天津金伟晖生物石油化工有限公司',
               '长兴化学（天津）有限公司',
               '天津利海石化有限公司',
               '天津南开和成科技有限公司',
               '天津市合成材料工业研究所滨海新区分所',
               '天津天智精细化工有限公司滨海新区分公司',
               '天津德凯化工股份有限公司',
               '天津市陆港石油橡胶有限公司',
               '天津江东石油化工有限公司',
               '天津市欣宽化工有限公司',
               '天津海纳龙化工有限公司',
               '天津市奥邦树酯有限公司',
               '天津力生化工有限公司',
               '天津市科迈化工有限公司',
               '天津大港油田滨港石油科技集团有限公司（板一联合站）',
               '天津市华英商贸有限公司',
               '天津市港塘燃气销售有限公司',
               '天津市滨海新区大港机电公司',
               '天津市大港区鑫达化工厂',
               '天津鹏坤化工有限公司',
               '大港油田集团有限责任公司港北加油站',
               '中国石油化工股份有限公司天津石油分公司大港金角加油站',
               '天津市中油港益石油制品有限公司',
               '中国石油天然气股份有限公司天津销售分公司大港东海加油站',
               '天津市大港上古林加油站',
               '中国石油天然气股份有限公司天津销售分公司大港渔港加油站',
               '中国石化销售有限公司天津石油分公司大港华港加油站',
               '中国石油化工股份有限公司天津石油分公司大港兴渔加油站',
               '天津港石石化加油站有限公司',
               '中国石油天然气股份有限公司天津销售分公司大港环港加油站',
               '中国石化销售有限公司天津石油分公司大港官港加油站',
               '中国石油化工股份有限公司天津石油分公司大港津歧路加油站',
               '中国石油天然气股份有限公司天津销售分公司大港兴港加油站',
               '中国石化销售有限公司天津石油分公司大港港塘路加油站',
               '中国石油天然气股份有限公司天津销售分公司大港凯旋加油加气站',
               '天津市天通燃气有限公司',
               '中国石油天然气股份有限公司大港石化公司',
               '天津炼达集团有限公司（溶剂油厂）',
               '天津市金业化工有限公司',
               '中国石油天然气股份有限公司天津销售公司大港油库',
               '天津市大港兴源化工有限公司',
               '天津中油科远石油工程有限责任公司',
               '天津市奥博工业气体制造有限公司',
               '天津中贯工业气体有限公司 ',
               '大港油田集团有限责任公司第十二加油站',
               '中国石油天然气股份有限公司天津销售分公司大港远景加油站',
               '大港油田集团有限责任公司港南加油站',
               '大港油田集团有限责任公司港西加油站',
               '大港油田集团有限责任公司港中加油站',
               '中国石油天然气股份有限公司天津销售分公司大港康路加油站',
               '天津大港油田炼达加油站',
               '中国石油化工股份有限公司天津石油分公司大港环滨海加油站',
               '中国石油天然气股份有限公司天津销售分公司大港港八井加油站',
               '中国石油天然气股份有限公司天津销售分公司大港第十加油站',
               '中国石油天然气股份有限公司天津销售分公司大港海滨加油站',
               '大港油田集团有限责任公司港盛加油站',
               '中国石油化工股份有限公司天津石油分公司大港港中路加油站',
               '天津中兴联合石化有限公司',
               '中国石油化工股份有限公司天津石油分公司大港长虹加油站',
               '中国石油天然气股份有限公司天津销售分公司大港炜事通加油站',
               '中国石油天然气股份有限公司天津销售分公司大港油田创业路加油站',
               '中国石油股份有限公司天津销售分公司大港油田幸福路加油站',
               '天津辛得玛悬浮剂有限公司',
               '海赛（天津）特种材料有限公司',
               '中国石化集团石油商业储备有限公司天津分公司（大港商储库）',
               '天津滨海津华康德石油制品有限公司（现改名为天津市津能石油化工销售有限公司）',
               '天津市天元亨工贸有限公司',
               '天津市外环化工有限公司',
               '中国石油化工股份有限公司天津石油分公司大港油库',
               '天津市长征润滑油有限公司',
               '天津市众邦化工有限公司',
               '天津恩光科技有限公司',
               '天津市大港鸿达供销公司',
               '天津市大港区华浦化工厂',
               '天津市亚东化工有限公司',
               '天津市大港区天成化工厂',
               '天津市晟鑫化工有限公司',
               '天津石然化工有限公司',
               '天津市金东方化工有限公司',
               '天津市大港万码化工制剂厂',
               '天津海阔天平化工有限公司',
               '天津博克百胜科技有限公司',
               '天津市大港区顺发石油化工溶剂油厂',
               '天津市大港区富源物资有限公司',
               '天津宏芃泰工业气体有限公司',
               '天津市大港区万顺建材经营部（普通合伙）',
               '天津市滨海新达化工厂（普通合伙）',
               '天津市嵘搏化工销售有限公司',
               '天津市鑫博化工销售有限公司',
               '天津浩伦气体有限公司',
               '天津瑞森化工有限公司',
               '中国石化销售有限公司天津石油分公司大港好运加油站',
               '天津市滨海新区大港宏运加油站',
               '天津石油集团大港石油公司中塘联营加油站',
               '中国石化销售有限公司天津石油分公司大港大安加油站',
               '中国石化销售有限公司天津石油分公司大港兴渤加油站',
               '中国石油天然气股份有限公司天津销售分公司大港玉川加油站',
               '天津市大港金坛加油站',
               '天津市瑞福鑫化工有限公司',
               '中国石油天然气股份有限公司天津销售分公司大港刘庄加油站',
               '天津炜事达石油销售有限公司',
               '中国石化销售有限公司天津石油分公司大港窦庄子加油站',
               '中国石化销售有限公司天津石油分公司大港太平村加油站',
               '中国石化销售有限公司天津石油分公司大港新农加油站',
               '中国石化销售有限公司天津石油分公司大港顺达加油站',
               '中国石油化工股份有限公司天津石油分公司大港天大加油站',
               '中国石化销售有限公司天津石油分公司大港渤海加油站',
               '中国石化销售有限公司天津石油分公司大港华强加油站',
               '天津市高速公路经营开发有限公司津汕高速公路大港加油站一站',
               '天津市高速公路经营开发有限公司津汕高速公路大港加油站二站',
               '中国石化销售有限公司天津石油分公司大港徐庄子加油站',
               '中国石化销售有限公司天津石油分公司大港小王庄加油站',
               '台达化工(天津)有限公司',
               '天津天寰聚氨酯有限公司',
               'PPG涂料（天津）有限公司',
               '阿克苏诺贝尔涂料（天津）有限公司',
               '中远关西涂料化工(天津)有限公司',
               '雷可德高分子（天津）有限公司',
               '巴斯夫聚氨酯(天津)有限公司',
               '东海炭素（天津）有限公司',
               '石药信汇（天津）医药科技有限公司',
               '天津达一琦精细化工有限公司',
               '天津天药药业股份有限公司',
               '天津浩元精细化工股份有限公司',
               '先导颜料（天津）有限公司',
               '天津炜捷制药有限公司',
               '卡博特化工（天津）有限公司',
               '康龙化成（天津）药物制备技术有限公司',
               '比欧西气体(天津)有限公司',
               '天津利安隆新材料股份有限公司',
               '天津科瑞达涂料化工有限公司',
               '天津永富关西涂料化工有限公司',
               '藤仓化成涂料（天津）有限公司',
               '天津稳泰化工兴业有限公司',
               '精工油墨（天津）有限公司',
               '天津旭成电子有限公司',
               '天津中维药业有限公司',
               '天津市东旭物流有限公司',
               '天津积水化成品有限公司',
               '天津中航百慕新材料技术有限公司',
               '天津金耀生物科技有限公司',
               '天津中能锂业有限公司',
               '天津凯莱英制药有限公司',
               '天津劲鹰汽车技术有限公司',
               '天津泰普制药有限公司',
               '中国石化销售有限公司天津石油分公司开发区新兴加油站',
               '中国石化销售有限公司天津石油分公司开发区洞庭路加油站',
               '天津北方石油销售有限公司睦宁路加油站',
               '天津开发区银河加油站',
               '雪佛龙（天津）油品有限公司洞庭路加油站',
               '雪佛龙（天津）油品有限公司新城西路加油站',
               '天津港泰汽车服务有限公司',
               '中国石化销售有限公司天津石油分公司滨海新区新业街加油站',
               '中国石化销售有限公司天津石油分公司开发区黄海路加油站',
               '天津开发区南海加油站有限责任公司',
               '天津凯晟石油销售有限公司',
               '中国石油天然气股份有限公司天津销售分公司逸仙园加油站',
               '天津市塘沽大东加油站',
               '中国石化销售有限公司天津石油分公司滨海新港路加油站',
               '中国石化销售有限公司天津石油分公司滨海闸南路加油站',
               'PPG航空材料（天津）有限公司',
               '中航国际物流（天津）有限公司',
               '天津渤化永利化工股份有限公司',
               '天津乐金渤海化学有限公司',
               '天津大沽化工股份有限公司临港分厂',
               '天津渤海石化有限公司',
               '天津新龙桥工程塑料有限公司',
               '液化空气天津滨海有限公司',
               '液化空气永利（天津）有限公司',
               '天津仁泰化学工业股份有限公司',
               '天津乐金渤天化学有限责任公司',
               '天津渤化澳佳永利化工有限责任公司',
               '天津为尔客石油化工有限公司',
               '液化空气环渤海有限公司',
               '天津永利食用添加剂有限公司',
               '天津威而豪石油化工有限公司',
               '天津瀚诺威国际物流有限公司',
               '天津中油天保石油销售有限公司',
               '天津港保税区振华加油站',
               '天津港保税区港湾加油服务有限责任公司',
               '天津新泰石油化工有限公司',
               '天津博乐达商贸有限公司博华加油站',
               '天津临港湾石油制品有限公司渤海十路加油站',
               '中国石化销售有限公司天津石油分公司滨海浴场加油站',
               '中国石油集团工程技术研究有限公司海洋高新区分公司',
               '田村电子材料（天津）有限公司',
               '杜伦斯（天津）涂料有限公司',
               '天津市华鑫工业气体有限公司',
               '联合矿产（天津）有限公司',
               '壳牌华北石油集团有限公司迎水道华苑加油站',
               '天津海腾投资发展有限公司滨海科技园加油加气站',
               '壳牌华北石油集团有限公司工农加油站',
               '中国石油天然气股份有限公司天津销售分公司塘沽华山道加油站',
               '中海油销售天津有限公司创新大道加油加气站',
               '天津中油泰宇石油销售有限公司滨海科技园加油站',
               '天津博弘化工有限责任公司',
               '天津市瑞田化工有限公司',
               '天津壳牌石油储运有限公司',
               '天津环捷物流有限公司',
               '中国石化集团石油商业储备有限公司天津分公司',
               '科诺华麦修斯标识技术(天津)有限公司',
               '天津国储石油基地有限责任公司',
               '中石化天津液化天然气有限责任公司',
               '天津中油滨海石油销售有限公司海滨大道蔡家堡入口加油站',
               '中石化滨旅（天津）成品油销售有限公司海晨道加油站',
               '中国石油天然气股份有限公司天津销售分公司中生加油站',
               '中国石油天然气股份有限公司天津销售分公司中津大道加油站',
               '天津东疆保税港区德港石油制品服务有限公司东疆三号加油站',
               '天津东疆保税港区德港石油制品服务有限公司海铁大道加油站']
listname = {}


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_0.pressed.connect(self.button0)
        self.pushButton_1.pressed.connect(self.button1)
        self.pushButton_2.pressed.connect(self.button2)
        self.pushButton_3.pressed.connect(self.button3)
        self.pushButton_01.pressed.connect(self.button1)
        self.pushButton_02.pressed.connect(self.button2)
        self.pushButton_03.pressed.connect(self.button3)
        self.label_5.hide()
        self.label_6.hide()
        self.listWidget.hide()
        self.listWidget_3.hide()

        self.listWidget.itemClicked.connect(self.clicked_1)
        self.listWidget_3.itemClicked.connect(self.clicked_2)
        self.listWidget_2.itemClicked.connect(self.buttonEnabled)
        self.lineEdit_16.textChanged.connect(lambda: self.textchange_16(self.lineEdit_16.text(), unitnames))
        self.lineEdit_21.textChanged.connect(lambda: self.textchange_21(self.lineEdit_21.text(), companylist))
        self.lineEdit_15.setText(datetime.datetime.now().strftime('%Y-%m-%d'))

        self.pushButton_27.hide()
        self.pushButton_28.hide()
        self.pushButton_29.hide()
        self.pushButton_22.setEnabled(False)
        self.pushButton_24.setEnabled(False)
        self.pushButton_21.released.connect(self.clearlist)
        self.pushButton_22.released.connect(self.clearlist)
        self.pushButton_22.pressed.connect(self.dellist)
        self.pushButton_24.pressed.connect(self.updatelist)
        self.pushButton_24.released.connect(self.clearlist)
        self.pushButton_25.released.connect(self.newaddlist)
        self.pushButton_25.released.connect(self.clearlist)
        self.pushButton_26.released.connect(self.clearlist)
        self.pushButton_27.pressed.connect(self.updatelist)
        self.pushButton_27.released.connect(self.clearlist)
        self.pushButton_28.released.connect(self.clearlist)
        self.pushButton_28.pressed.connect(self.dellist)
        self.pushButton_29.pressed.connect(self.clearlist)
        self.pushButton_29.released.connect(self.buttonshow)
        self.listWidget_2.itemClicked.connect(self.infoview)

    def button0(self):
        self.stackedWidget.setCurrentIndex(0)

    def button1(self):
        self.stackedWidget.setCurrentIndex(1)

    def button2(self):
        self.stackedWidget.setCurrentIndex(2)

    def button3(self):
        self.stackedWidget.setCurrentIndex(3)

    def textchange_16(self, textvalue, list):
        self.listWidget.hide()
        self.listWidget.clear()
        h = 0
        for i in list:
            if textvalue and re.findall(textvalue, i):
                self.listWidget.addItem(i)
                h += 1
        if self.listWidget:
            self.listWidget.resize(250, h*30)
            self.listWidget.show()
            self.label_5.show()
            self.label_6.show()

    def clicked_1(self, item):
        self.lineEdit_16.setText(item.text())
        self.listWidget.hide()
        self.label_5.hide()
        self.label_6.hide()

    def textchange_21(self, textvalue, list):
        self.listWidget_3.hide()
        self.listWidget_3.clear()
        h = 0
        for i in list:
            if textvalue and re.findall(textvalue, i):
                if len(i) > 23:
                    a = i[0:22]+'\n'+i[22:]
                    self.listWidget_3.addItem(a)
                else:
                    self.listWidget_3.addItem(i)
                h += 1
        if self.listWidget_3:
            self.listWidget_3.resize(310, h * 25)
            self.listWidget_3.show()

    def clicked_2(self, item):
        self.lineEdit_21.setText(str(item.text()).replace('\n', ''))
        self.listWidget_3.hide()

    def buttonEnabled(self):
        self.pushButton_22.setEnabled(True)
        self.pushButton_24.setEnabled(True)

    def buttonshow(self):
        self.pushButton_27.hide()
        self.pushButton_28.hide()
        self.pushButton_29.hide()
        self.pushButton_25.show()
        self.pushButton_26.show()

    def infoview(self, item):
        key = str(item.text()).replace('\n', '')
        y = listname[key][0][0:4]
        self.lineEdit_21.setText(key)
        self.listWidget_3.hide()
        self.pushButton_25.hide()
        self.pushButton_26.hide()
        self.pushButton_27.show()
        self.pushButton_28.show()
        self.pushButton_29.show()
        self.lineEdit_23.setText(listname[key][1])
        self.lineEdit_24.setText(listname[key][2])
        self.lineEdit_25.setText(listname[key][3])
        self.lineEdit_26.setText(listname[key][4])
        self.lineEdit_27.setText(listname[key][5])
        if ord(listname[key][0][7]) == 47:
            m = listname[key][0][5:7]
            d = listname[key][0][8:]
        else:
            m = listname[key][0][5]
            d = listname[key][0][7:]

        self.lineEdit_22.setDateTime(QtCore.QDateTime(QtCore.QDate(int(y), int(m), int(d))))

    def dellist(self):
        listname.pop(self.lineEdit_21.text())
        self.listWidget_2.removeItemWidget(self.listWidget_2.takeItem(self.listWidget_2.currentRow()))
        self.pushButton_27.hide()
        self.pushButton_28.hide()
        self.pushButton_29.hide()
        self.pushButton_25.show()
        self.pushButton_26.show()
        self.pushButton_22.setEnabled(False)
        self.pushButton_24.setEnabled(False)

    def updatelist(self):
        listname[self.lineEdit_21.text()] = [self.lineEdit_22.text(), self.lineEdit_23.text(),
                                             self.lineEdit_24.text(), self.lineEdit_25.text(),
                                             self.lineEdit_26.text(), self.lineEdit_27.text()]
        self.pushButton_25.show()
        self.pushButton_26.show()
        self.pushButton_27.hide()
        self.pushButton_28.hide()
        self.pushButton_29.hide()
        self.pushButton_24.setEnabled(False)
        self.pushButton_22.setEnabled(False)

    def newaddlist(self):
        listname_value = [self.lineEdit_22.text(), self.lineEdit_23.text(),
                          self.lineEdit_24.text(), self.lineEdit_25.text(),
                          self.lineEdit_26.text(), self.lineEdit_27.text()]
        listname[self.lineEdit_21.text()] = listname_value
        namelength = len(self.lineEdit_21.text())
        if namelength > 15:
            a = self.lineEdit_21.text()[0:14] + '\n' + self.lineEdit_21.text()[14:]
            self.listWidget_2.addItem(a+'\n')
        else:
            self.listWidget_2.addItem(self.lineEdit_21.text()+'\n')

    def clearlist(self):
        self.lineEdit_21.clear()
        self.lineEdit_22.clear()
        self.lineEdit_23.clear()
        self.lineEdit_24.clear()
        self.lineEdit_25.clear()
        self.lineEdit_26.clear()
        self.lineEdit_27.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())