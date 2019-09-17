在Spark 上使用流数据训练一个回归器？

使用 open, high, low =》 close 


每次迭代都会带来模型的更新？
还是每天更新模型(离线更新）。
流数据的predict 容易解决。
流式的训练并不容易。每分钟都更新模型 -- 对生产环境的持续部署能力提出了很高的要求。那么是否有必要呢？
没有必要。对大多数场景而言，秒级别的模型更新是不需要的。如果需要，那么证明这个模型对输入数据非常敏感 -- 这往往意味着模型泛化能力不够。
不过自动化的模型更新仍然是有趣的课题。

实时的模型指标更新倒是可以。

参考文献
1. [Databricks: using-mllib-with-structured-streaming](https://docs.databricks.com/_static/notebooks/using-mllib-with-structured-streaming.html)
2. 