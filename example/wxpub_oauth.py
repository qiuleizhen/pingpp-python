# -*- coding: utf-8 -*-

import pingpp


# 微信公众号平台的 App ID
wx_app_id = 'wx9283883h477376s'
# 微信公众号平台的 App Secret
wx_app_secret = 'da38db82d0e495a037aec19df178572b'

# -------
# 获取 openid
# 微信回调的页面，用于接收 code 来获取 openid
redirect_url = 'https://example.com/authorize'

oauth_url = pingpp.WxpubOauth.create_oauth_url_for_code(
    wx_app_id, redirect_url, False)
print(oauth_url)

# 在微信中打开 oauth_url，页面会跳转到 redirect_url，并带有参数 code
code = 'CODE_IN_URL_QUERY'
openid = pingpp.WxpubOauth.get_openid(
    wx_app_id, wx_app_secret, code)
print(openid)

# -------
# 获取 jsapi_ticket
jsapi_ticket = pingpp.WxpubOauth.get_jsapi_ticket(wx_app_id, wx_app_secret)
print(jsapi_ticket)
