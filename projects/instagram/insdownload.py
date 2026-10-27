import re
import requests
import time
import os
from config import FOLDER_NAME, USER_NAME, USER_ID, COOKIES, END_PAGE, X_CSRF_TOKEN, X_IG_WWW_CLAIM
from urllib.parse import unquote

# 禁用SSL警告
# 保留 requests 默认 TLS 证书验证。


class InstagramDownloader:
    def __init__(self):
        self.headers = {
            'cookie': COOKIES,
            'referer': f'https://www.instagram.com/{USER_NAME}/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-asbd-id': '198387',
            'x-csrftoken': X_CSRF_TOKEN,
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': X_IG_WWW_CLAIM,
        }
        self.setup_workspace()

    def setup_workspace(self):
        """创建并进入工作目录"""
        try:
            os.makedirs(FOLDER_NAME, exist_ok=True)
        except Exception as e:
            print(f"创建目录时出错: {e}")
        finally:
            os.chdir(FOLDER_NAME)

    def get_first_page(self):
        """获取第一页内容"""
        url = 'https://i.instagram.com/api/v1/users/web_profile_info/'
        params = {'username': USER_NAME}

        try:
            response = requests.get(url=url, headers=self.headers, params=params, timeout=30)
            print(response.text)
            response.raise_for_status()
            json_data = response.json()

            end_cursor = json_data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            media_list = json_data['data']['user']['edge_owner_to_timeline_media']['edges']

            self.process_media(media_list, page_num=1)
            return end_cursor
        except Exception as e:
            print(f"获取第一页时出错: {e}")
            return None

    def get_next_page(self, next_page, page_num):
        """获取后续页面内容"""
        if page_num > END_PAGE:
            return None

        url = f'https://www.instagram.com/graphql/query/?query_hash=69cba40317214236af40e7efa697781d&variables={{"id":"{USER_ID}","first":12,"after":"{next_page}"}}'

        try:
            response = requests.get(url=url, headers=self.headers, timeout=30)
            response.raise_for_status()
            json_data = response.json()

            end_cursor = json_data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            media_list = json_data['data']['user']['edge_owner_to_timeline_media']['edges']

            self.process_media(media_list, page_num)
            return end_cursor
        except Exception as e:
            print(f"获取第{page_num}页时出错: {e}")
            return None

    def process_media(self, media_list, page_num):
        """处理媒体列表"""
        media_urls = []

        for media_data in media_list:
            node = media_data['node']

            # 处理视频
            if node.get('is_video') and node.get('video_url'):
                media_urls.append(('video', node['video_url']))

            # 处理单张图片
            elif node.get('display_url'):
                media_urls.append(('image', node['display_url']))

            # 处理多图/视频合集
            if 'edge_sidecar_to_children' in node:
                for child in node['edge_sidecar_to_children']['edges']:
                    child_node = child['node']
                    if child_node.get('is_video') and child_node.get('video_url'):
                        media_urls.append(('video', child_node['video_url']))
                    elif child_node.get('display_url'):
                        media_urls.append(('image', child_node['display_url']))

        self.download_media(media_urls, page_num)

    def download_media(self, media_urls, page_num, retry_count=3):
        """下载媒体文件"""
        for media_type, url in media_urls:
            for attempt in range(retry_count):
                try:
                    response = requests.get(url, headers=self.headers, timeout=30, stream=True)
                    response.raise_for_status()

                    # 从URL提取文件名
                    if media_type == 'video':
                        filename = self.extract_filename(url, '.mp4')
                    else:
                        filename = self.extract_filename(url, '.jpg')

                    # 保存文件
                    with open(filename, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)

                    print(f"成功下载: {filename}")
                    break
                except Exception as e:
                    if attempt == retry_count - 1:
                        print(f"下载失败: {url}, 错误: {e}")
                    else:
                        time.sleep(2)  # 重试前等待

        print(f"完成第{page_num}页的下载!")

    def extract_filename(self, url, extension):
        """从URL中提取安全的文件名"""
        # 解码URL编码的字符
        decoded_url = unquote(url)

        # 尝试从URL中提取文件名
        if extension == '.mp4':
            match = re.search(r'/([^/?]+\.mp4)', decoded_url)
            if match:
                return match.group(1)
        else:
            match = re.search(r'/([^/?]+)\.(jpg|jpeg|png)', decoded_url, re.I)
            if match:
                return f"{match.group(1)}{extension}"

        # 如果无法从URL提取，使用时间戳作为文件名
        return f"ig_media_{int(time.time())}{extension}"

    def run(self):
        """运行下载器"""
        start_time = time.time()
        print("开始下载Instagram内容...")

        end_cursor = self.get_first_page()
        if not end_cursor:
            print("无法获取初始页面内容，程序终止")
            return

        page_num = 2
        while page_num <= END_PAGE and end_cursor:
            end_cursor = self.get_next_page(end_cursor, page_num)
            page_num += 1
            time.sleep(1)  # 避免请求过于频繁

        print(f"下载完成! 总耗时: {time.time() - start_time:.2f}秒")


if __name__ == '__main__':
    if not all((USER_NAME, USER_ID, COOKIES, X_CSRF_TOKEN)):
        raise SystemExit('请先设置 Instagram 环境变量，详见 USAGE.md。')
    downloader = InstagramDownloader()
    downloader.run()