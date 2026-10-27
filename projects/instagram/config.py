"""
Instagram 数据爬取配置文件

使用说明：
1. 修改 TARGET_USER 部分为目标用户信息
2. 根据需要调整 SETTINGS 中的参数
3. 更新 AUTHENTICATION 中的认证信息
"""

# ======================
# 目标用户配置
# ======================
TARGET_USER = {
    # 保存内容的文件夹名称
    'username': os.environ.get('INSTAGRAM_OUTPUT', 'downloads'),
    
    # 要爬取的用户名 (@后面的部分)
    'user_name': os.environ.get('INSTAGRAM_USERNAME', ''),
    
    # 用户ID (在开发者工具中搜索"target_id"参数)
    'user_id': os.environ.get('INSTAGRAM_USER_ID', '')
}

# ======================
# 爬取设置
# ======================
SETTINGS = {
    # 要爬取的页数 (每页约12个媒体文件)
    'end_page': 3,
    
    # 请求延迟 (秒，避免被封)
    'request_delay': 1,
    
    # 下载失败重试次数
    'max_retries': 3
}

# ======================
# 认证信息 (需定期更新)
# ======================
AUTHENTICATION = {
    # 从环境变量读取认证信息，不要提交真实会话凭据。
    'x_csrf_token': os.environ.get('INSTAGRAM_CSRF_TOKEN', ''),
    'x_ig_www_claim': os.environ.get('INSTAGRAM_WWW_CLAIM', ''),
    'cookies': os.environ.get('INSTAGRAM_COOKIE', ''),
}

# ======================
# 常量 (通常不需要修改)
# ======================
CONSTANTS = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'x_ig_app_id': '936619743392459',
    'x_asbd_id': '198387'
}

# ======================
# 导出变量 (兼容旧代码)
# ======================
FOLDER_NAME = TARGET_USER['username']
USER_NAME = TARGET_USER['user_name']
USER_ID = TARGET_USER['user_id']
END_PAGE = SETTINGS['end_page']
X_CSRF_TOKEN = AUTHENTICATION['x_csrf_token']
X_IG_WWW_CLAIM = AUTHENTICATION['x_ig_www_claim']
COOKIES = AUTHENTICATION['cookies']
# 兼容旧版脚本变量。
Username = FOLDER_NAME
x_ig_www_claim = X_IG_WWW_CLAIM
x_instagram_ajax = os.environ.get("INSTAGRAM_AJAX", "")
