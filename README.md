# 撮合交易系统 

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

一个基于优先队列的股票交易撮合系统，实现买卖订单的自动匹配与交易执行。

## 📌 功能特性

- **用户管理**
  - 注册/登录系统
  - 查看交易历史
  - 订单状态追踪
  
- **核心交易功能**
  - 买入/卖出订单提交
  - 价格优先+时间优先撮合
  - 实时订单簿展示
  - 交易记录生成
  
- **扩展功能**
  - 多股票类型支持
  - 部分成交处理
  - 订单撤回功能
  - GUI可视化界面

## 🚀 快速启动

### 依赖环境
- Python 3.8+   - Python 3.8
- Tkinter（Python标准库）

### 安装运行
```bash   ”“bash
# 克隆仓库
git clone https://github.com/yourusername/trading-system.gitGit克隆https://github.com/yourusername/trading-system.git

# 进入项目目录
cd trading-system   cd交易系统

# 运行主程序
python Main.py
```

## 📂 文件结构

```
trading-system/
├── Main.py                # 程序入口 & GUI主界面
├── order.py               # 订单类定义与队列管理
├── PriorityQueue.py       # 最大/最小优先队列实现
├── Trade.py               # 交易记录处理模块
├── user.py                # 用户管理系统
├── login_gui.py           # 登录/注册界面
├── tests/                 # 单元测试目录
│   ├── test_queues.py     # 优先队列测试用例
│   └── test_trading.py    # 撮合逻辑测试
└── README.md
```

## 🧠 核心算法

### 优先级队列
- **买入订单**：最大堆实现（价格优先）
- **卖出订单**：最小堆实现（价格优先）

### 撮合逻辑
```python
while 买队列 and 卖队列:
    最高买价 >= 最低卖价时:
        取最小数量成交
        生成交易记录
        处理部分成交订单
    更新订单状态
```

## 🧪 运行测试

```bash
# 运行所有单元测试
python -m unittest discover tests/

# 单独测试优先队列
python tests/test_queues.py
```

## 🤝 贡献指南

1. Fork项目仓库
2. 创建特性分支 (`git checkout -b feature/awesome-feature`)
3. 提交修改 (`git commit -am 'Add some feature'`)
4. 推送分支 (`git push origin feature/awesome-feature`)
5. 创建Pull Request

## 📜 许可证

本项目基于 [MIT License](LICENSE) 发布。

---

> 📧 联系维护者：your.email@example.com  
> 🏫 山西大学初民学院 - 数据结构与算法实验项目组
