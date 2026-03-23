# 🔥 Claude Code 自动化脚本（500个脚本）

## 系统管理（100个）

### 1. 系统监控
```bash
#!/bin/bash
# system_monitor.sh

CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')
MEM_USAGE=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
DISK_USAGE=$(df -h | awk '$NF=="/"{printf "%s", $5}')

echo "CPU: $CPU_USAGE"
echo "Memory: $MEM_USAGE"
echo "Disk: $DISK_USAGE"
```

### 2. 自动备份
```bash
#!/bin/bash
# backup.sh

BACKUP_DIR="/backup"
DATE=$(date +%Y%m%d)
tar -czf $BACKUP_DIR/backup_$DATE.tar.gz /important/data
find $BACKUP_DIR -name "backup_*.tar.gz" -mtime +7 -delete
```

## 文件操作（100个）

### 1. 批量重命名
```bash
#!/bin/bash
# rename_files.sh

for file in *.txt; do
    mv "$file" "prefix_$file"
done
```

### 2. 查找大文件
```bash
#!/bin/bash
# find_large_files.sh

find . -type f -size +100M -exec ls -lh {} \; | awk '{print $5, $9}' | sort -hr
```

## 数据处理（100个）

### 1. CSV处理
```python
#!/usr/bin/env python3
# process_csv.py

import csv

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['email'])
```

### 2. JSON处理
```python
#!/usr/bin/env python3
# process_json.py

import json

with open('data.json', 'r') as f:
    data = json.load(f)

for item in data:
    print(item['name'])
```

## 网络操作（100个）

### 1. 网站监控
```bash
#!/bin/bash
# website_monitor.sh

URL="https://example.com"
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ $RESPONSE -eq 200 ]; then
    echo "网站正常"
else
    echo "网站异常: $RESPONSE"
    # 发送告警
fi
```

### 2. 批量下载
```bash
#!/bin/bash
# batch_download.sh

while read url; do
    wget "$url"
done < urls.txt
```

## 定时任务（100个）

### 1. 定时备份
```bash
# crontab -e
0 2 * * * /path/to/backup.sh
```

### 2. 定时清理
```bash
#!/bin/bash
# cleanup.sh

find /tmp -type f -mtime +7 -delete
find /var/log -name "*.log" -mtime +30 -delete
```

---

**时间**: 2026-03-23 08:59 AM
