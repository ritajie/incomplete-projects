# 烂尾、停贷楼盘 的数据汇总

已上线：~~https://building.lulaolu.com~~ (被请喝茶了，网站已下线)

这个项目的目标是：统计`烂尾楼盘`和`停贷楼盘`。现在只统计了停贷楼盘，后续会补充更多数据。

![alt text](https://github.com/ritajie/incomplete-projects/blob/master/incomplete_projects/static/img/demo.png?raw=true)



## 数据从哪里来？
* 停贷楼盘：[GitHub - WeNeedHome](https://github.com/WeNeedHome/SummaryOfLoanSuspension)
* 烂尾楼盘：[人民网 - 领导留言板 - 住房和城乡建设部](http://liuyan.people.com.cn/threads/list?fid=5063&position=1)

这是我整理的结构化数据（JSON）
[📃 github_building_and_amap_building.json](https://github.com/ritajie/incomplete-projects/blob/master/incomplete_projects/config/github_building_and_amap_building.json)

## 后续工作
* 持续更新停贷数据
* 根据人民网的留言板，写一个词法分析（或者索性人工分析），找到业主投诉停工的楼盘，尽可能及时得更新烂尾数据。

欢迎大家一起来共享数据和代码！

这个世界会好的。
