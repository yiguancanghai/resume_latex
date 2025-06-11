# 演示说明

## 🎉 项目创建完成！

您的自动化PDF简历流水线已经成功搭建。以下是演示步骤：

### 1. 本地渲染测试

```bash
# 渲染YAML数据到LaTeX
python3 render.py
# 或者
make tex

# 查看生成的LaTeX文件
cat resume.tex
```

### 2. 修改简历数据

编辑 `data.yaml` 文件：
```bash
vim data.yaml
```

然后重新渲染：
```bash
make tex
```

### 3. 部署到GitHub（推荐）

```bash
# 初始化Git仓库
git init
git add .
git commit -m "Initial commit: LaTeX resume pipeline"

# 推送到GitHub
git remote add origin https://github.com/你的用户名/resume-latex.git
git push -u origin main
```

### 4. 云端自动编译

推送到GitHub后：
1. 访问仓库的 Actions 页面
2. 查看自动运行的构建任务
3. 下载生成的 `resume-pdf` artifact

### 5. 本地PDF编译（可选）

如果系统安装了LaTeX：
```bash
make pdf
```

## 📋 项目检查清单

- ✅ `data.yaml` - 简历数据文件
- ✅ `template.tex` - LaTeX模板文件  
- ✅ `render.py` - Python渲染脚本
- ✅ `requirements.txt` - Python依赖
- ✅ `Makefile` - 本地构建工具
- ✅ `.github/workflows/build.yml` - GitHub Actions配置
- ✅ `README.md` - 项目文档
- ✅ `.gitignore` - Git忽略文件

## 🔄 日常使用流程

1. 编辑 `data.yaml`
2. `git add data.yaml`
3. `git commit -m "update work experience"`
4. `git push`
5. 等待GitHub Actions完成
6. 下载新的PDF

就是这么简单！🚀 