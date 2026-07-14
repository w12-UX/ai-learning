# Dify 第一章：入门学习笔记

## 📌 什么是 Dify？

Dify 是一个开源的 **LLMOps（大语言模型运维）平台**，帮助开发者快速构建和部署 AI 应用。

### 核心特性
- 🧩 **可视化 AI 工作流编排** — 拖拽式搭建 AI 应用流程
- 🤖 **多模型支持** — 接入 OpenAI、Claude、通义千问等大模型
- 📚 **RAG 知识库** — 让 AI 结合自有文档回答问题
- 💬 **对话型应用** — 快速搭建聊天机器人/AI 助手
- 🔧 **插件机制** — 扩展 AI 功能

---

## 📁 项目结构

```
dify/
├── api/          # 后端 API（Python/Flask）
├── web/          # 前端（Next.js/TypeScript）
├── docker/       # Docker 部署配置
├── docs/         # 官方文档
├── sdks/         # 各语言 SDK
├── cli/          # 命令行工具
├── scripts/      # 脚本
└── packages/     # 共享包
```

---

## 🔧 部署方式

### 方式一：Docker 部署（推荐）
```bash
cd docker
docker-compose up -d
```

### 方式二：源码部署
- 后端：`cd api && pip install -r requirements.txt && flask run`
- 前端：`cd web && npm install && npm run dev`

---

## 🎯 应用场景
1. **智能客服** — 结合知识库的自动问答
2. **内容生成** — AI 写作、摘要、翻译
3. **数据分析** — 自然语言查询数据库
4. **教育辅导** — 个性化学习助手

---

## 📝 第一章小结
- 理解了 Dify 是什么以及能做什么
- 了解了项目的整体架构和目录结构
- 掌握了两种部署方式
- 明确了后续可以搭建的应用方向

---
*学习日期：2026 年 7 月 14 日*
