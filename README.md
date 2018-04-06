# TestNet

> 一共 57+37+80+(6+83)=**263** 行

程序使用了**外部命令** `speedtest` 与 `ping -c 100 www.baidu.com`

在时延与丢包率的测量中，是向**百度**发包。运行程序前，应保证已经在测试的计算机上安装了**speedtest_cli**，安装方式如下：
> pip install speedtest_cli

## Upstream_Downstream_Rate.py 

> 一共 57 行

第一个版本，仅能用于测量网络的**上行速率**和**下行速率**，结果**保存于rate.log**。数据并**没有被处理**
> 使用两个线程，
> * 其中一个用于每隔interval_time的时间将time_to_run设置为true
> * 另一个线程用于根据是否time_to_run进行测速

## Upstream_Downstream_Rate_v2.py

> 一共 37 行

第二个版本，功能与第一个版本相同，但结果**保存于net_data.log**，该程序**不再使用线程**，而是每interval_time设置一个**时间阶**，在每阶执行一次 `speedtest`

## Upstream_Downstream_Rate_v3.py

> 一共 80 行

第三个版本，此版本开始测量时延与丢包率。

**增加了外部命令** `ping -c n www.baidu.com`，最后的数据保存在net_data.**md**中，数据被简单的处理，保存的形式为表格

## Upstream_Downstream_Rate_v4

> 一共 6+83=89 行

第四个版本，将主程序与类**分离**，将类单独作为一个module置于文件夹 `./tools` 中，该module命名为 `tool.py`

增加了一个start_end.conf文件，用于**设置测量网络质量的时间区间**，`tool.py` 中的类会自动读取该设置文件。

增加了异常处理，如果测量的时刻网络出现异常，程序将**跳过该时间**，在下一个时间阶测量网络。
