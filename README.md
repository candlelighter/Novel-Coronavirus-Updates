附：新型冠状病毒感染/死亡历史数据图说明 (截至2020/1/27)
![Alt text](./20200127.png?raw=true "plot")

用半对数图可以直观地给出下面三个总体参数：

1：看出感染或死亡是否指数增长。直线的斜率代表了增长速度。从1/17 到1/27的数据看。病毒传染非常快，每6 天就增长10倍，也就是不到2天就翻一番。偏离直线是疫情得到控制的一个直观证据。

2：感染和死亡线的平行增长提供如下重要指标：纵向位移代表病死率。大约40倍的间隔表明病死率~1/40=2.5%。这比SARS的9%要弱一些。而且这个间隔在1/17到1/27之间没有大的变化，说明还没有有效的治疗方案。

3：横向位移与存活时间有关。当然这只是在致命的感染下，而且是诊断出以后。更准确的理解和预测需要拟合传染病动力学模型。


感染/死亡人数和感染/死亡的增长率(截至2020/1/31)。增长率定义为exp($\alpha$ t)上的系数。时间以天为单位。计算时平均了过去5天的数据，有一定延迟。增长率可大致翻译成：

0.099 七天翻一番

0.14 五天翻一番

0.23 三天翻一番

0.35 两天翻一番

![Alt text](./20200202.png?raw=true "plot")

GitHub下载连接 https://github.com/candlelighter/Novel-Coronavirus-Updates.

发布说明：

2020/2/1:  输出所有数据（从1/10以来）总的平均增长率。图写入.png文件。更新数据。澎湃新闻的 .csv文件从GB2312改回utf-8

2020/1/31：更新数据格式。澎湃新闻的 .csv文件从utf-8改成GB2312

2020/1/30: 增长率算法

2020/1/28：上载半对数画图 plot.py.附加说明。

由于个体差异的原因，上面的讨论不是医疗诊断和建议，不适合单个病人。大家自己把握。

=======================================================

### 新增确诊新型冠状病毒肺炎统计数据（每日更新）———— 最新一次更新时间：2月2日19:00

数据收集与更新不易。如使用数据请标注，疫情数据由**澎湃新闻美数课整理提供**。

如有疑问或发现问题，欢迎提交pull requests或者在issues下发表。

大家春节快乐，**身体健康**！

附：[新型冠状病毒感染肺炎病例实时地图](http://projects.thepaper.cn/thepaper-cases/839studio/feiyan/)
