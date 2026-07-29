# Contributing / 贡献指南

Thank you for considering contributing to the Psychological Digital Twin skill pack! 

感谢你考虑对精神数字分身技能包做出贡献！

## How to Contribute / 如何贡献

### 🐛 Report Issues
- Open a [GitHub Issue](https://github.com/zhwenchao/jungian-soul-agent-skills/issues)
- Describe the problem and steps to reproduce
- Suggest how it could be improved

### 💡 Suggest Enhancements
- New archetype prompts? A prompt for a specific cultural context?
- Integration templates (Obsidian, Feishu, Notion)?
- A better dialogue technique for a specific skill?

### 🔀 Submit Pull Requests

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-idea`
3. Make your changes
4. Run the integrity checker: `python demo/run_local_demo.py`
5. Open a PR against `main`

### 🧪 Testing

Run the integrity checker before submitting:

```bash
python demo/run_local_demo.py
```

### 📝 Style Guide

- **All content must be bilingual** (English + Simplified Chinese) — the skill pack serves both audiences
- **Markdown**: Use standard GitHub-Flavored Markdown
- **Prompts**: Each prompt file needs: archetype definition, activation command, role setting, tone guide, dialogue strategy, cultural adaptation, hard boundaries
- **Profiles**: No real personal data in commits — use placeholder/example data only

## Code of Conduct / 行为准则

Be respectful. This project is about self-knowledge and growth — the community should reflect that.
