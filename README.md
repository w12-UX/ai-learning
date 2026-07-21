# AI Learning 📚

AI 技术学习笔记与实践项目。从零开始学习 Dify 平台，涵盖 AI Agent、模型接入、提示词工程、RAG 知识库、Function Calling 与插件开发、工作流编排与 AI 助手实战。

---

## 📖 章节索引

| # | 章节 | 核心内容 | 日期 |
|---|------|---------|------|
| 1 | [AI Agent 与 Dify 入门](./dify/1.Dify第一章学习笔记.md) | AI Agent 概念、Dify 平台介绍、Docker 部署 | 2026-07-14 |
| 2 | [Ollama 与大模型接入](./dify/2.Dify第二章学习笔记.md) | Ollama 安装部署、本地模型接入、云端 API 接入 | 2026-07-14 |
| 3 | [提示词工程](./dify/3.Dify第三章学习笔记.md) | 提示词原理与技巧、Dify 提示词应用、金融文本抽取实战 | 2026-07-15 |
| 4 | [RAG 原理与知识库搭建](./dify/4.Dify第四章学习笔记.md) | RAG 检索增强生成原理、知识库三步搭建流程、LOL 游戏助手实战 | 2026-07-16 |
| 5 | [Function Calling 与插件开发](./dify/5.Dify第五章学习笔记.md) | Function Calling 原理、时间工具应用、天气查询自定义插件全流程 | 2026-07-16 |
| 6 | [工作流编排与 AI 助手实战](./dify/6.Dify第六章学习笔记.md) | 工作流编排概念、跨境电商答疑助手（工作流）、NLP2SQL 数据库查询（对话流） | 2026-07-17 |
| 7 | [Agent 应用发布与集成](./dify/7.Dify第七章学习笔记.md) | Agent 嵌入网站、API 封装发布、Postman 测试、Dify 五大模块总结 | 2026-07-21 |

---

## 🗺️ 学习路径

```
第1章 ──→ 第2章 ──→ 第3章 ──→ 第4章 ──→ 第5章 ──→ 第6章 ──→ 第7章
概念基础    模型接入    提示词      知识库      插件开发    工作流编排    发布集成
                     ↓           ↓           ↓           ↓
                  Dify 平台核心能力储备 ─────→ 两大实战项目
                                              ├── 跨境电商答疑助手 (Workflow)
                                              └── NLP2SQL 数据库查询 (Chatflow)
```

---

## 🏗️ 完整目录结构

```
📦 ai-learning/
├── 📄 README.md                        # 项目总入口（本文档）
│
└── 📂 dify/                            # Dify 学习笔记
    ├── 📝 1.Dify第一章学习笔记.md       # AI Agent 与 Dify 入门
    ├── 📝 2.Dify第二章学习笔记.md       # Ollama 与大模型接入
    ├── 📝 3.Dify第三章学习笔记.md       # 提示词工程
    ├── 📝 4.Dify第四章学习笔记.md       # RAG 原理与知识库搭建
    ├── 📝 5.Dify第五章学习笔记.md       # Function Calling 与插件开发
    ├── 📝 6.Dify第六章学习笔记.md       # 工作流编排与 AI 助手实战
    ├── 📝 7.Dify第七章学习笔记.md       # Agent 应用发布与集成
    │
    ├── 📂 images/                      # 截图与示意图（按章节分文件夹）
    │   ├── 📂 1/                       # 第一章：AI Agent 概述、架构图
    │   ├── 📂 2/                       # 第二章：Ollama 安装、API 接入流程
    │   ├── 📂 4/                       # 第四章：RAG 三段式流程
    │   ├── 📂 5/                       # 第五章：Function Call、插件、天气实战
    │   ├── 📂 6/                       # 第六章：Agent 工作原理、工作流类型
    │   ├── 📂 6.2/                     # 第六章跨境电商答疑助手（14 张截图）
    │   ├── 📂 6.3/                     # 第六章 NLP2SQL（24 张截图）
    │   └── 📂 7.1/                     # 第七章 API 发布与 Postman 测试截图
    │
    └── 📂 doc/                         # 配套参考文档（按章节分文件夹）
        ├── 📂 4/
        │   └── 📄 英雄联盟《芸阿娜》介绍.md       # 知识库素材：LOL 英雄攻略
        ├── 📂 5/
        │   ├── 📄 自定义天气查询插件完整教程.md  # FastAPI + localtunnel + Dify
        │   └── 🐍 main.py                       # 天气查询插件源码
        ├── 📂 6/
        │   ├── 📄 跨境电商答疑助手完整对话流.md  # 工作流节点配置与代码
        │   ├── 📄 NLP2SQL数据库查询工作流.md     # 对话流详细搭建步骤
        │   └── 📄 MySQL数据库操作教程.md         # 环境准备与建表
        └── 📂 7/
            ├── 📄 API接口的创建方式.md            # API 鉴权与接口调用说明
            └── 🗸 database_assistant.html         # 嵌入网站完整 HTML 模板
```

---

## 📎 配套文档

| 文档 | 所属章节 | 说明 |
|------|---------|------|
| [英雄联盟《芸阿娜》介绍.md](./dify/doc/4/英雄联盟《芸阿娜》介绍.md) | 第四章 | 知识库素材示例：LOL 英雄攻略文档，演示 RAG 知识库数据准备 |
| [自定义天气查询插件完整教程.md](./dify/doc/5/自定义天气查询插件完整教程.md) | 第五章 | 完整教程文档：FastAPI 后端 → localtunnel 穿透 → Dify Schema 配置 |
| [main.py](./dify/doc/5/main.py) | 第五章 | 天气查询插件 FastAPI 源码，包含 Bearer Token 认证与城市天气查询 |
| [跨境电商答疑助手完整对话流.md](./dify/doc/6/跨境电商答疑助手完整对话流.md) | 第六章 | 工作流案例完整文档：意图识别代码、RAG Prompt、闲聊 Prompt |
| [NLP2SQL数据库查询工作流.md](./dify/doc/6/NLP2SQL数据库查询工作流.md) | 第六章 | 对话流案例完整文档：SQL 生成、循环执行、ECharts 图表配置 |
| [MySQL数据库操作教程.md](./dify/doc/6/MySQL数据库操作教程.md) | 第六章 | 环境准备文档：建表语句、100 条测试数据插入、验证操作 |
| [API接口的创建方式.md](./dify/doc/7/API接口的创建方式.md) | 第七章 | API 鉴权方式与 Postman 调用步骤说明 |
| [database_assistant.html](./dify/doc/7/database_assistant.html) | 第七章 | Agent 嵌入网站完整 HTML 模板（含 Dify 嵌入 JS 代码） |

---

## 🛠️ 技术栈

| 技术 | 用途 |
|------|------|
| **Dify** | AI 应用开发平台（工作流编排、RAG 知识库、Agent 智能体） |
| **Ollama** | 本地大模型部署与管理 |
| **Docker** | Dify 平台容器化部署 |
| **FastAPI** | 自定义插件后端开发（Python） |
| **localtunnel** | 公网穿透，使 Dify 可调用本地 API |
| **MySQL** | NLP2SQL 案例数据库 |
| **ECharts** | 数据可视化图表生成 |
| **Qwen3-max** | NLP2SQL 案例中使用的大模型 |

---

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/w12-UX/ai-learning.git

# 进入 Dify 学习笔记目录
cd ai-learning/dify

# 从第一章开始阅读
# 每章包含：概述 → 知识点详解 → 实战案例 → 简答题 → 本章小结
```

建议按章节顺序阅读，每章末尾的参考文档可在 `doc/` 对应章节文件夹中找到。

---

*整理日期：2026 年 7 月 21 日*
