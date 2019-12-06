## 基础概念
Master
集群的控制节点，负责整个集群的管理和控制。一个master可以管理多个Node。master 还需要负责 Pod 的调度。

Node 
集群的工作节点，可以是VM或者物理机。工作负载主要是运行容器应用，因此它有两部分组成：1. Kubelet 进程，为了和 Kubernetes Master 通信。2.容器运行时,提供容器运行环境。一个Node上可以有多个Pod运行。Node需要负责Pod 的创建、启动、监控、重启、销毁。
kubectl get - list resources
kubectl describe - show detailed information about a resource
kubectl logs - print the logs from a container in a pod
kubectl exec - execute a command on a container in a pod

Pod
最基础的部署调度单元。Pod管理**应用**实例。一个Pod可以管理多个**容器**实例。一个Pod中的各种容器共享存储、IP地址等。

# 安装

```bash
brew install kubectl
```

## Linux
```bash
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
