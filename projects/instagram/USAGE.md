# Instagram 使用说明

推荐入口：`insdownload.py`。中文文件名脚本保留为旧版参考，尚未全面现代化。

```powershell
$env:INSTAGRAM_USERNAME = "your_authorized_target"
$env:INSTAGRAM_USER_ID = "target_user_id"
$env:INSTAGRAM_COOKIE = "your_current_cookie"
$env:INSTAGRAM_CSRF_TOKEN = "your_current_csrf_token"
$env:INSTAGRAM_WWW_CLAIM = "your_current_claim"
python insdownload.py
```

可选 `INSTAGRAM_OUTPUT` 默认为 downloads。程序不会自动加载 .env。仅处理你有权访问与保存的内容；站点接口可能已经变化，以本页配置方式为准。
