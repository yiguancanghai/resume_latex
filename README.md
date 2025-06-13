# LaTeX Resume Generator

基于 [sb2nov/resume](https://github.com/sb2nov/resume) 的简历生成器,使用 YAML 数据驱动 LaTeX 模板。

## 特点

- 使用 YAML 存储简历数据,方便维护和更新
- 基于 sb2nov/resume 的 LaTeX 模板,美观专业
- 支持 GitHub Actions 自动生成 PDF
- 使用 Jinja2 模板引擎渲染 LaTeX

## 使用方法

1. 克隆仓库:
```bash
git clone https://github.com/yourusername/resume-latex.git
cd resume-latex
```

2. 编辑 `data.yaml` 文件,填入你的简历信息

3. 本地生成 PDF:
```bash
make
```

4. 或使用 GitHub Actions 自动生成:
   - Fork 本仓库
   - 编辑 `data.yaml`
   - 提交更改,触发 Actions 自动生成 PDF

## 文件结构

- `data.yaml` - 简历数据
- `template.tex` - LaTeX 模板
- `resume.cls` - LaTeX 样式类
- `render.py` - 渲染脚本
- `Makefile` - 构建脚本

## 依赖

- Python 3.6+
- LaTeX (推荐使用 TeX Live)
- latexmk

## 许可证

MIT License 