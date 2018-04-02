# TestNet
程序使用了外部命令 `speedtest` 与 `ping -c 100 www.baidu.com`

在时延与丢包率的测量中，是向百度发包。运行程序前，应保证已经在测试的计算机上安装了speedtest_cli，安装方式如下：
> pip install speedtest_cli

## Upstream_Downstream_Rate.py 
第一个版本，仅能用于测量网络的上行速率和下行速率，结果保存于rate.log。数据并没有被处理
> 使用两个线程，
> * 其中一个用于每隔interval_time的时间将time_to_run设置为true
> * 另一个线程用于根据是否time_to_run进行测速

## Upstream_Downstream_Rate_v2.py
第二个版本，功能与第一个版本相同，但结果保存于net_data.log，该程序不再使用线程，而是每interval_time设置一个时间阶，在每阶执行一次 `speedtest`

## Upstream_Downstream_Rate_v3.py
第三个版本，增加了外部命令 `ping -c n www.baidu.com`，最后的数据保存在net_data.md中，数据被简单的处理，保存的形式为表格

## Upstream_Downstream_Rate_v4
第四个版本，将主程序与类分离，将类单独作为一个module置于文件夹 `./tools` 中，该module命名为 `tool.py`

增加了一个start_end.conf文件，用于设置测量网络质量的时间区间，`tool.py` 中的类会自动读取该设置文件。

增加了异常处理，如果测量的时刻网络出现异常，程序将跳过该时间，在下一个时间阶测量网络。
