#!/usr/bin/env python3
"""
render.py - 渲染 YAML 数据到 LaTeX 模板
使用 Jinja2 模板引擎将 data.yaml 中的数据渲染到 template.tex 生成 resume.tex
"""

import yaml
import jinja2
import pathlib
import sys

def main():
    try:
        # 读取 YAML 数据
        with open('data.yaml', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # 读取 LaTeX 模板
        with open('template.tex', encoding='utf-8') as f:
            template_source = f.read()
        
        # 创建 Jinja2 模板对象
        template = jinja2.Template(template_source, autoescape=False)
        
        # 渲染模板
        rendered_content = template.render(**data)
        
        # 写出 resume.tex
        pathlib.Path('resume.tex').write_text(rendered_content, encoding='utf-8')
        
        print("✅ 成功生成 resume.tex")
        
    except FileNotFoundError as e:
        print(f"❌ 文件未找到: {e}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"❌ YAML 解析错误: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 渲染失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 