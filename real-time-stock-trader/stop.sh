#!/usr/bin/env bash

# 停止kafka&spark容器集群
docker ps | grep -E 'kafka|spark' | awk '{print $1}' | xargs docker stop

# 停止数据发送模拟程序
ps | grep data_monitor | awk '{print $1}'| xargs kill