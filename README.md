# 🤖 自动化代码审查 Agent

基于通义千问 (Qwen) 大模型打造的 GitHub 自动化代码审查机器人。旨在通过 AI 辅助开发，提高代码质量和团队开发效率。

📋 项目简介

本项目是一个轻量级的自动化工作流脚本，能够监听 Pull Request 事件，自动分析代码变更（Diff），并利用通义千问大模型生成专业的代码审查意见。

 🚀 核心功能

-自动审查：当开发者提交代码时，自动触发审查流程。
- 智能建议：识别潜在的 Bug、代码异味及性能优化点。
- 无缝集成：基于 GitHub Actions 运行，无需额外服务器。
- 模型驱动：使用通义千问 `qwen-plus` 模型，提供高质量的中文审查反馈。

 🛠️ 技术栈

- 语言: Python 3.9+
- 核心库: `openai` (兼容模式), `PyGithub`
- AI 模型: 通义千问 (Qwen)
- 部署: GitHub Actions

 ⚙️ 快速开始

1. 配置环境变量

在项目根目录创建 `.env` 文件，填入你的 API Key：
`bash
DASHSCOPE_API_KEY=your_api_key_here
GITHUB_TOKEN=your_github_token
2.安装依赖
pip install -r requirements.txt
3.运行脚本
python main.py
