
### 新增确诊新型冠状病毒肺炎统计数据（每日更新）———— 最新一次更新时间：1月27日09:40

数据收集与更新不易。如使用数据请标注，疫情数据由**澎湃新闻美数课整理提供**。

如有疑问或发现问题，欢迎提交pull requests或者在issues下发表。

大家春节快乐，**身体健康**！

附：[新型冠状病毒感染肺炎病例实时地图](http://projects.thepaper.cn/thepaper-cases/839studio/feiyan/)

=======================================

下载连接 https://github.com/candlelighter/Novel-Coronavirus-Updates. 

2020/1/28：上载半对数画图 plot.py.附加说明。

用半对数图可以直观地给出下面三个总体参数：

1：看出感染或死亡是否指数增长。直线的斜率代表了增长速度。从1/17 到1/27的数据看。病毒传染非常快，每6 天就增长10倍，也就是不到2天就翻一番。偏离直线是控制有效的一个直观证据。

2：感染和死亡直线的平行增长提供如下重要指标：纵向位移代表病死率。大约40倍的间隔表明病死率~1/40=2.5%。这比SARS的9%要弱一些。而且这个间隔在1/17到1/27之间没有大的变化，说明还没有有效的治疗方案。

3：横向位移与存活时间有关。当然这只是在致命的感染下，而且是诊断出以后。更准确的理解和预测需要拟合传染病动力学模型。

由于个体差异的原因，上面的讨论不是医疗诊断和建议，不适合单个病人。大家自己把握。

附：新型冠状病毒感染/死亡历史数据图 (截至2020/1/27)
![Alt text](./20200127.png?raw=true "plot")

下图包括了感染/死亡人数和感染/死亡的增长率。增长率是平均了过去5天的数据，有一定延迟。 增长率0.07, 0.26, 0.41各意味十天，三天和两天翻一番（1.07**10=1.26**3=1.41**2=2）
![Alt text](./20200130.png?raw=true "plot")
