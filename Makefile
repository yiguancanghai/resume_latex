# Makefile for LaTeX Resume Pipeline
# 使用 latexmk 进行 PDF 编译

.PHONY: all tex pdf clean help

# 默认目标
all: pdf

# 渲染 LaTeX
tex:
	@echo "🔄 渲染 YAML 数据到 LaTeX..."
	python3 render.py

# 编译 PDF
pdf: tex
	@echo "🔄 编译 PDF..."
	latexmk -pdf -quiet -interaction=nonstopmode resume.tex
	@echo "✅ 生成完成: resume.pdf"

# 清理中间文件
clean:
	@echo "🧹 清理中间文件..."
	latexmk -C
	rm -f resume.tex *.fls *.fdb_latexmk *.aux *.log *.out *.synctex.gz
	@echo "✅ 清理完成"

# 显示帮助信息
help:
	@echo "LaTeX Resume Pipeline Makefile"
	@echo ""
	@echo "可用命令:"
	@echo "  make          - 生成 PDF (默认)"
	@echo "  make tex      - 仅渲染 LaTeX"
	@echo "  make pdf      - 渲染并编译 PDF"
	@echo "  make clean    - 清理中间文件"
	@echo "  make help     - 显示此帮助" 