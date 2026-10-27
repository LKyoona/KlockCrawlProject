# Klock Crawl Project

Python 数据采集与桌面小工具实践集。原来四个分支中的项目汇总到 `projects/`，原分支与历史提交保留。

## 项目导航

| 项目 | 技术与内容 | 状态 |
| --- | --- | --- |
| [Instagram](projects/instagram/) | Python / requests，图片与短视频采集 | 历史接口，配置改为环境变量 |
| [北京卫视下载器](projects/brtv-downloader/) | Tkinter / requests，桌面下载工具 | 运行前配置 FFmpeg 并验证接口 |
| [王者荣耀皮肤开盲盒](projects/honor-skin-box/) | Pygame / Pillow，Windows 桌面交互 | 保留原始素材与依赖 |
| [表情包下载器](projects/meme-downloader/) | requests，图片下载实践 | 历史接口，需自行验证 |

## 开始使用

各子项目独立运行，先进入其目录，建立虚拟环境，再安装该目录的 requirements.txt。不要在根目录混装全部依赖。

```powershell
cd projects/instagram
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Instagram 的配置与运行命令见 [使用说明](projects/instagram/USAGE.md)。其他子项目保留原始说明。原 Instagram 文档保存在 [docs](docs/instagram-original.md)。

## 维护范围

- 历史项目不保证第三方接口、旧依赖或登录方式仍然可用。
- CI 只检查语法，不运行采集，不访问第三方账号。
- 不提交 Cookie、令牌、下载内容或预编译 EXE。
- 历史提交曾包含会话配置；本次修改没有重写历史，请撤销旧会话并轮换凭据。
- 第三方图片、音频与游戏素材权利属于各自权利人，本次整理不为其追加开源授权。
