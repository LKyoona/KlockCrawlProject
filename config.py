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
    'username': 'ignitesmodels',
    
    # 要爬取的用户名 (@后面的部分)
    'user_name': 'ignitesmodels',
    
    # 用户ID (在开发者工具中搜索"target_id"参数)
    'user_id': "11462354903"
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
    # CSRF token
    'x_csrf_token': '5r9CaMWrpVzSIg3VDym0zgvrT48pscR0',
    
    # Instagram claim
    'x_ig_www_claim': 'hmac.AR2lK-rlLlHOdXR9-cpi_PEXbfqNfAoi7IfUNhZk76tJdodm',
    
    # Cookies (完整字符串)
    'cookies': (
        'mid=YlFTTwALAAERy7VgxyADDyAuTKBb; '
        'ig_did=5016A6A1-AA23-44CB-A71B-883155F282AB; '
        'ig_nrcb=1; '
        'fbm_124024574287414=base_domain=.instagram.com; '
        'datr=i76gYqY1Dm_BZSlkbuz0iBUu; '
        'csrftoken=5r9CaMWrpVzSIg3VDym0zgvrT48pscR0; '
        'ds_user_id=33235544573; '
        'dpr=1.25; '
        'shbid="7644\05433235544573\0541710919295:01f7379de43662087227400eb012e26a73335f19f982c6c5d37f8b7f7370e12438fd0f51"; '
        'shbts="1679383295\05433235544573\0541710919295:01f77b2e3339735978f93f5836d275d731d46aedd083eda089a201ccf328dbf1c2402cd7"; '
        'sessionid=33235544573%3AA3pMPIDhviRJxc%3A18%3AAYfN9gj91Acnlos0x8-1EfwAMoXr7cfvdY0lJ8L3Vg; '
        'rur="NAO\05433235544573\0541710919489:01f724d49bb56dd03da53c7dd544ea56ad3b3695277439d6fe1fbf8504d61887fab683f1"'
    )
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