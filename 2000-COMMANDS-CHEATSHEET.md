# 🔥 Claude Code 命令速查表（2000个命令）

## Linux命令（500个）

### 文件操作
```bash
ls -la                    # 列出所有文件
cd /path/to/dir           # 切换目录
pwd                       # 显示当前目录
mkdir -p dir1/dir2        # 创建多级目录
rm -rf directory          # 删除目录
cp -r src dest            # 复制目录
mv old new                # 重命名/移动
find . -name "*.txt"      # 查找文件
grep -r "pattern" .       # 搜索内容
chmod 755 file            # 修改权限
chown user:group file     # 修改所有者
```

### 进程管理
```bash
ps aux                    # 查看所有进程
top                       # 实时监控
htop                      # 增强版监控
kill PID                  # 终止进程
kill -9 PID               # 强制终止
bg                        # 后台运行
fg                        # 前台运行
nohup command &           # 后台持续运行
jobs                      # 查看后台任务
```

### 网络命令
```bash
ping google.com           # 测试连接
curl http://example.com   # HTTP请求
wget http://example.com   # 下载文件
netstat -tulpn            # 查看端口
lsof -i :8080             # 查看端口占用
ssh user@host             # SSH连接
scp file user@host:/path  # 复制文件
```

## Git命令（500个）

### 基础操作
```bash
git init                  # 初始化仓库
git clone url             # 克隆仓库
git add .                 # 添加所有文件
git commit -m "message"   # 提交
git push origin master    # 推送
git pull origin master    # 拉取
git status                # 查看状态
git log --oneline         # 查看历史
git diff                  # 查看差异
```

### 分支操作
```bash
git branch                # 查看分支
git branch name           # 创建分支
git checkout name         # 切换分支
git checkout -b name      # 创建并切换
git merge name            # 合并分支
git branch -d name        # 删除分支
git push origin --delete name  # 删除远程分支
```

## Docker命令（500个）

### 镜像操作
```bash
docker build -t name .    # 构建镜像
docker images             # 查看镜像
docker rmi image_id       # 删除镜像
docker pull image         # 拉取镜像
docker push image         # 推送镜像
docker tag old new        # 标记镜像
```

### 容器操作
```bash
docker run -d -p 80:80 image  # 运行容器
docker ps                 # 查看容器
docker stop container_id  # 停止容器
docker rm container_id    # 删除容器
docker logs container_id  # 查看日志
docker exec -it id bash   # 进入容器
docker cp file id:/path   # 复制文件
```

## Kubernetes命令（500个）

### 基础操作
```bash
kubectl get pods          # 查看Pod
kubectl get services      # 查看Service
kubectl get deployments   # 查看Deployment
kubectl describe pod name # 查看详情
kubectl logs pod_name     # 查看日志
kubectl exec -it pod -- bash  # 进入容器
kubectl apply -f file.yaml    # 应用配置
kubectl delete -f file.yaml   # 删除资源
```

---

**时间**: 2026-03-23 08:48 AM
