# 房价走势分析

最近经常在大牛猫公众号看到关于《70个大中城市房价销售价格指数》的信息，但每次只看到一个月的环比同比数据，对实际的价格走势心里也没有一个大概，索性今天得空，在国家统计局网站上找了相关源数据，自己来统计一下。

首先源数据在这里：`https://www.stats.gov.cn/sj/`，但是这个网站是每个月发布一次，需要自己搜索网页把所有数据保存下来，我这里获取了2018年1月到2025年5月的商品房销售数据（我只搜到了18年开始的数据）
![](https://github.com/yooongchun/picx-images-hosting/raw/master/source.7axfqx42sy.webp)

拿到了数据我们就可以来看看情况了，首先，70个城市都包含哪些呢？
|   1  |   2  |   3  |   4  |  5   |    6 |   7  |
| --- | --- | --- | --- | --- | --- | --- |
| 三亚 | 上海 | 丹东 | 乌鲁木齐 | 九江 | 兰州 | 包头 |
| 北京 | 北海 | 南京 | 南充 | 南宁 | 南昌 | 厦门 |
| 合肥 | 吉林 | 呼和浩特 | 哈尔滨 | 唐山 | 大理 | 大连 |
| 天津 | 太原 | 宁波 | 安庆 | 宜昌 | 岳阳 | 常德 |
| 平顶山 | 广州 | 徐州 | 惠州 | 成都 | 扬州 | 无锡 |
| 昆明 | 杭州 | 桂林 | 武汉 | 沈阳 | 泉州 | 泸州 |
| 洛阳 | 济南 | 济宁 | 海口 | 深圳 | 温州 | 湛江 |
| 烟台 | 牡丹江 | 石家庄 | 福州 | 秦皇岛 | 蚌埠 | 襄阳 |
| 西宁 | 西安 | 贵阳 | 赣州 | 遵义 | 郑州 | 重庆 |
| 金华 | 银川 | 锦州 | 长春 | 长沙 | 青岛 | 韶关 |

至于为什么选这70个代表呢？别问，问就是我也不知道🥲🥲

不过倒是可以来看看这70个城市都分别分布在哪里
![](https://github.com/yooongchun/picx-images-hosting/raw/master/city-distribute.6m466f07by.png)

从上图看，大部分都分布在沿海城市，最亮眼的`乌鲁木齐`，一枝独秀喔！

## 房价走势

接下来我们就来看看这70个城市从18年以来的价格走势
![](https://github.com/yooongchun/picx-images-hosting/raw/master/image.6bhcdrt8rv.webp)

上图横坐标是时间，纵坐标是价格的百分比，以17年12月的价格系数为1开始计算，后续的价格都是相对该时间点的涨跌比。

我们从几个不同的角度来解读下这张价格走势图。

## top5和last5
首先，我们来看看截止25年5月涨跌幅最高和最低的5个城市分别是哪几个。

在不看答案之前，大家能猜出来前五是哪几个吗？说实话，后五我可能没感知，但是前五还是比较意外的，`西安、成都、银川`居然超过了公认的超一线`北上广深`成为前三甲，至于后5，因为平时也不关注，所以无所谓意外不意外。
![](https://github.com/yooongchun/picx-images-hosting/raw/master/image.1ap9m7oiz3.webp)
![](https://github.com/yooongchun/picx-images-hosting/raw/master/image.5c190m0dcl.webp)

## 北上广深
接着看看当之无愧的超一线`北上广深`的表现
![](https://github.com/yooongchun/picx-images-hosting/raw/master/image.2a5czebs69.webp)
说实话，绝对值肯定是高不少，但从涨跌比例来看，表现中规中矩，不过这个图上我倒是注意到了一个城市：`上海`，这个曲线简直了，一直稳步上扬，单独拎出来看看，大家就能发现上海的房价走势之坚挺了
![](https://github.com/yooongchun/picx-images-hosting/raw/master/image.4jodivz9gr.webp)

## 哪些城市反弹了？
再看看哪些城市开始反弹了，这里我们定义距离底部反弹至少1%才是有效反弹，可统计得7个城市符合要求：
|城市|触底时间|反弹百分比|
|--|--|--|
| 南宁 | 触底时间 2410 | 反弹1.21% |
| 南京 | 触底时间 2410 | 反弹1.40% |
| 厦门 | 触底时间 2409 | 反弹1.51% |
| 宁波 | 触底时间 2410 | 反弹1.91% |
| 太原 | 触底时间 2212 | 反弹2.11% |
| <span style="color:red">成都</span> | <span style="color:red">触底时间 2410</span> | <span style="color:red">反弹 3.04%</span> |
| <span style="color:red">杭州</span> | <span style="color:red">触底时间 2410</span> | <span style="color:red">反弹3.24%</span> |

`成都、杭州`这两个城市确实强，说实话从这几年身边同学、同事陆续从北京或到成都或到杭州也可瞥见一二，他俩首先出坑我并不意外！

![](https://github.com/yooongchun/picx-images-hosting/raw/master/image.1hshhoo7o7.png)
## 整体走势
最后，我们看下这70个城市平均后的整体走势
![](https://github.com/yooongchun/picx-images-hosting/raw/master/image.1hshhnzp0r.webp)
整体来看，这70个城市的房价指数在21年8月份达到最高值126%，然后就开始回撤，截止25年5月是114%。

今天分析所用到的数据我放在了github上，大家如有需要可在这里获取：
```shell
https://github.com/yooongchun/house-data
```
以上数据仅供参考，仅个人分析，难免有疏漏，不做正确性保证！


