#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = "Allen Woo"
__readme__='''
################################################################################
1.本配置文件config_sample.py的内容全部复制(覆盖)到config.py
a.除了OVERWRITE_DB外, 其他配置都可以在平台管理端页面修改
b.启动网站/重启网站的时候，系统会自动合并数据库中保存的配置,实现本地配置文件配置与数据库一致.
c.如果你是开发人员,需要手动修改配置文件，请阅读下面说明

2.自动合并过程中:
a.对于本文件新增加的key会添加到数据库(value使用本地的)
b.本文文件没有的,而数据库有保存的key会在数据库删除
c.两边都存在的key, 则value使用数据库的

##如果你不想合并配置, 想用本地配置数据覆盖掉数据库中的配置数据,请修改变量OVERWRITE_DB

变量说明
*OVERWRITE_DB
启动系统时, 配置更新是否来自数据库, 以数据库中的value为主.
如果为True, 则完全以本文件数据上传到数据库中
如果为False, 按照上述[2.自动合并过程中],当次有效, 启动后会自动变为True

*CONFIG　
1.每个配置项中的__sort__作为在管理的显示的时候的排序使用, 如果不存在__sort__,表示该配置不可以在管理端配置
2.配置表,表中没有__restart__的项目将不会出现在管理端的设置中
###############################################################################
'''
# Danger: If True, the database configuration data will be overwritten
# 危险:如果为True, 则会把该文件配置覆盖掉数据库中保存的配置
OVERWRITE_DB = False
CONFIG = {
    "email": {
        "MAIL_USE_SSL": {
            "info": "是否使用SSL",
            "sort": 99,
            "type": "bool",
            "value": True
        },
        "MAIL_ASCII_ATTACHMENTS": {
            "info": "MAIL ASCII ATTACHMENTS",
            "sort": 99,
            "type": "bool",
            "value": True
        },
        "MAIL_SERVER": {
            "info": "邮箱服务器smtp",
            "sort": 99,
            "type": "string",
            "value": "smtp.mxhichina.com"
        },
        "MAIL_USERNAME": {
            "info": "邮箱用户名",
            "sort": 99,
            "type": "string",
            "value": "system@osroom.com"
        },
        "__sort__": 10,
        "MAIL_PASSWORD": {
            "info": "邮箱密码, 是用于发送邮件的密码",
            "sort": 99,
            "type": "password",
            "value": "<Your password>"
        },
        "MAIL_USE_TLS": {
            "info": "是否使用TLS",
            "sort": 99,
            "type": "bool",
            "value": False
        },
        "MAIL_DEFAULT_SENDER": {
            "info": "默认发送者邮箱　(显示名称, 邮箱地址)顺序不能调换",
            "sort": 99,
            "type": "list",
            "value": [
                "OSR DEMO",
                "system@osroom.com"
            ]
        },
        "MAIL_FOOTER": {
            "info": "发送邮件的页尾",
            "sort": 99,
            "type": "string",
            "value": "OSROOM开源网站系统"
        },
        "APP_LOG_URL": {
            "info": "在邮件中显示的LOGO图片URL(1.不填写则不显示.2.如果主题邮件发送html模板不支持，也不显示)",
            "sort": 99,
            "type": "string",
            "value": "https://avatars1.githubusercontent.com/u/14039952?s=460&v=4"
        },
        "MAIL_SUBJECT_SUFFIX": {
            "info": "发送邮件的标题后缀",
            "sort": 99,
            "type": "string",
            "value": "OSROOM"
        },
        "APP_NAME": {
            "info": "在邮件中显示的APP(WEB)名称(1.不填写则不显示.2.如果主题邮件发送html模板不支持，也不显示)",
            "sort": 99,
            "type": "string",
            "value": "OSR DEMO"
        },
        "__info__": "邮件发送参数设置（建议技术管理人员使用）",
        "__restart__": "must",
        "MAIL_PORT": {
            "info": "邮箱服务器端口",
            "sort": 99,
            "type": "int",
            "value": 465
        }
    },
    "post": {
        "TAG_MAX_NUM": {
            "info": "POST标签最大个数",
            "sort": 99,
            "type": "int",
            "value": 5
        },
        "MAX_LEN": {
            "info": "发布文章最多几个字符",
            "sort": 99,
            "type": "int",
            "value": 5000
        },
        "__sort__": 2,
        "GET_POST_CACHE_TIME_OUT": {
            "info": "获取多个post数据时, 缓存超时时间(s), 为0表示不缓存数据.<br><span style='color:red;'>只对获取已公开发布的, 并且不是当前用户发布的post有效</span>",
            "sort": 99,
            "type": "int",
            "value": 60
        },
        "TITLE_MAX_LEN": {
            "info": "文章Title最大长度",
            "sort": 99,
            "type": "int",
            "value": 50
        },
        "__restart__": "not_must",
        "NUM_PAGE": {
            "info": "每个页面获取几篇文章, 如果请求获取文章时指定了指定了per参数, 则此配置无效(此配置也对管理端无效)",
            "sort": 99,
            "type": "int",
            "value": 10
        },
        "NUM_PAGE_MAX": {
            "info": "每个页面最多获取几篇文章(此配置对管理端无效)",
            "sort": 99,
            "type": "int",
            "value": 30
        },
        "TAG_MAX_LEN": {
            "info": "POST标签最多几个字",
            "sort": 99,
            "type": "int",
            "value": 10
        },
        "BRIEF_LEN": {
            "info": "获取文章简要的字数",
            "sort": 99,
            "type": "int",
            "value": 80
        },
        "__info__": "文章内容设置"
    },
    "comment": {
        "NUM_PAGE_MAX": {
            "info": "每个页面最多获取几条评论(此配置对管理端无效)",
            "sort": 99,
            "type": "int",
            "value": 30
        },
        "INTERVAL": {
            "info": "控制评论频繁度时间(s)",
            "sort": 99,
            "type": "int",
            "value": 30
        },
        "NUM_PAGE": {
            "info": "每个页面获取几条评论, 如果请求获取评论时指定了指定了per参数, 则此配置无效(此配置也对管理端无效)",
            "sort": 99,
            "type": "int",
            "value": 10
        },
        "__sort__": 3,
        "TRAVELER_COMMENT": {
            "info": "游客评论开关,是否打开?",
            "sort": 99,
            "type": "bool",
            "value": False
        },
        "__restart__": "not_must",
        "MAX_LEN": {
            "info": "发布评论最多几个字符",
            "sort": 99,
            "type": "int",
            "value": 300
        },
        "NUM_OF_INTERVAL": {
            "info": "控制评论频繁度时间内最多评论几次",
            "sort": 99,
            "type": "int",
            "value": 3
        },
        "OPEN_COMMENT": {
            "info": "评论开关,是否打开评论功能?",
            "sort": 99,
            "type": "bool",
            "value": False
        },
        "__info__": "评论内容设置"
    },
    "weblogger": {
        "__restart__": "not_must",
        "SING_IN_LOG_KEEP_NUM": {
            "info": "登录日志保留个数",
            "sort": 99,
            "type": "int",
            "value": 30
        },
        "__info__": "操作日志设置",
        "USER_OP_LOG_KEEP_NUM": {
            "info": "用户操作日志保留个数",
            "sort": 99,
            "type": "int",
            "value": 30
        },
        "__sort__": 99
    },
    "login_manager": {
        "LOGIN_IN_TO": {
            "info": "登录成功后,api会响应数据会带上需要跳转到路由to_url",
            "sort": 99,
            "type": "string",
            "value": "/"
        },
        "OPEN_REGISTER": {
            "info": "开放注册",
            "sort": 99,
            "type": "bool",
            "value": True
        },
        "LOGIN_VIEW": {
            "info": "需要登录的页面,未登录时,api会响应401,并带上需要跳转到路由to_url",
            "sort": 99,
            "type": "string",
            "value": "/sign-in"
        },
        "__info__": "在线管理（建议技术管理人员使用）",
        "LOGIN_OUT_TO": {
            "info": "退出登录后,api会响应数据会带上需要跳转到路由to_url",
            "sort": 99,
            "type": "string",
            "value": "/"
        },
        "__sort__": 99,
        "__restart__": "not_must",
        "PW_WRONG_NUM_IMG_CODE": {
            "info": "同一用户登录密码错误几次后响应图片验证码, 并且需要验证",
            "sort": 99,
            "type": "int",
            "value": 5
        }
    },
    "content_inspection": {
        "TEXT_OPEN": {
            "info": "开启text检测.需要hook_name为content_inspection_text的文本检测插件",
            "sort": 99,
            "type": "bool",
            "value": True
        },
        "__info__": "内容检查配置(需要安装相关插件该配置才生效).<br>检测开关:<br>1.如果开启, 并安装有相关的自动检查插件, 则会给发布的内容给出违规评分.如果未安装自动审核插件,则系统会给予评分100分(属涉嫌违规,网站工作人员账户除外).<br>2.如果关闭审核，则系统会给评分0分(不违规)",
        "__sort__": 5,
        "__restart__": "not_must",
        "VEDIO_OPEN": {
            "info": "开启视频检测.需要hook_name为content_inspection_vedio的视频检测插件",
            "sort": 99,
            "type": "bool",
            "value": False
        },
        "IMAGE_OPEN": {
            "info": "开启图片检测.需要hook_name为content_inspection_image的图片检测插件",
            "sort": 99,
            "type": "bool",
            "value": False
        },
        "ALLEGED_ILLEGAL_SCORE": {
            "info": "内容检测分数高于多少分时属于涉嫌违规(0-100分,对于需要检查的内容有效)",
            "sort": 99,
            "type": "float",
            "value": 99
        },
        "AUDIO_OPEN": {
            "info": "开启音频检测.需要hook_name为content_inspection_audio的音频检测插件",
            "sort": 99,
            "type": "bool",
            "value": False
        }
    },
    "system": {
        "__info__": "其他web系统参数设置（建议技术管理人员使用）",
        "__sort__": 99,
        "TEMPLATES_AUTO_RELOAD": {
            "info": "是否自动加载页面(html)模板.开启后,每次html页面修改都无需重启Web",
            "sort": 3,
            "type": "bool",
            "value": True
        },
        "__restart__": "must",
        "MAX_CONTENT_LENGTH": {
            "info": "拒绝内容长度大于此值的请求进入，并返回一个 413 状态码(单位:Mb)",
            "sort": 1,
            "type": "float",
            "value": 50.0
        },
        "KEY_HIDING": {
            "info": "开启后,管理端通过/api/admin/xxx获取到的数据中，密钥类型的值，则会以随机字符代替.<br><span style='color:red;'>如某个插件配置中有密码, 不想让它暴露在浏览器, 则可开启.</span>",
            "sort": 2,
            "type": "bool",
            "value": True
        }
    },
    "key": {
        "SECRET_KEY": {
            "info": "安全验证码",
            "sort": 99,
            "type": "string",
            "value": "ceavewrvwtrhdyjydj"
        },
        "__restart__": "must",
        "SECURITY_PASSWORD_SALT": {
            "info": "安全密码码盐值",
            "sort": 99,
            "type": "string",
            "value": "ceavewrvwtrhdyjydj"
        },
        "__info__": "安全Key（建议技术管理人员使用）",
        "__sort__": 99
    },
    "py_venv": {
        "VENV_PATH": {
            "info": "python虚拟环境路径",
            "sort": 99,
            "type": "string",
            "value": "/home/work/project/venv3"
        }
    },
    "category": {
        "__restart__": "not_must",
        "CATEGORY_TYPE": {
            "info": "分类的品种只能有这几种",
            "sort": 99,
            "type": "dict",
            "value": {
                "视频库": "video",
                "图库": "image",
                "音频库": "audio",
                "文集": "post",
                "文本内容": "text",
                "其他": "other"
            }
        },
        "__info__": "Web参数设置",
        "__sort__": 7,
        "CATEGORY_MAX_LEN": {
            "info": "分类名称类型名最多几个字符",
            "sort": 99,
            "type": "int",
            "value": 15
        }
    },
    "site_config": {
        "HEAD_CODE": {
            "info": "用于放入html中<br><span style='color:red;'>head标签</span>内的js/css/html代码(如Google分析代码/百度统计代码)",
            "sort": 13,
            "type": "string",
            "value": ""
        },
        "TITLE_SUFFIX_ADM": {
            "info": "APP(Web)管理端Title后缀",
            "sort": 9,
            "type": "string",
            "value": "OSROOM管理端"
        },
        "__info__": "基础设置: APP(Web)全局数据设置<br>此模块所有的KEY值, 都可以直接请求全局Api(/api/global)获取.也可以直接在主题中使用Jinjia2模板引擎获取(g.site_global.site_config.XXXX)",
        "TITLE_SUFFIX": {
            "info": "APP(Web)Title后缀",
            "sort": 8,
            "type": "string",
            "value": "OSROOM开源Web DEMO"
        },
        "FOOTER_CODE": {
            "info": "用于放入html中<br><span style='color:red;'>body标签</span>内的js/css/html代码(如Google分析代码/百度统计代码)",
            "sort": 13,
            "type": "string",
            "value": ""
        },
        "__sort__": 1,
        "PC_LOGO_DISPLAY": {
            "info": "PC端用App name 还是Logo image 作为APP(Web)的Logo显示, 为空则显示Logo和App name<br>可填logo或name(需要主题支持)",
            "sort": 3,
            "type": "string",
            "value": "logo"
        },
        "STATIC_FILE_VERSION": {
            "info": "静态文件版本(当修改了CSS,JS等静态文件的时候，修改此版本号)",
            "sort": 12,
            "type": "int",
            "value": 20181024065925
        },
        "LOGO_IMG_URL": {
            "info": "APP(Web)Logo的URL",
            "sort": 2,
            "type": "string",
            "value": "/static/sys_imgs/osroom-logo.png"
        },
        "FRIEND_LINK": {
            "info": "友情链接:值(Value)格式为{'url':'友情链接', 'logo_url':'logo链接'}",
            "sort": 11,
            "type": "dict",
            "value": {
                "阿里云": {
                    "aliases": "阿里云",
                    "level": 1,
                    "icon_url": "",
                    "url": "www.aliyun.com"
                },
                "码云": {
                    "aliases": "码云",
                    "level": 1,
                    "icon_url": "",
                    "url": "www.aliyun.com"
                },
                "Github": {
                    "aliases": "Github",
                    "level": 1,
                    "icon_url": "",
                    "url": "www.aliyun.com"
                },
                "七牛云": {
                    "aliases": "七牛云",
                    "level": 1,
                    "icon_url": "",
                    "url": "www.aliyun.com"
                }
            }
        },
        "FAVICON": {
            "info": "APP(Web)favicon图标的URL",
            "sort": 10,
            "type": "string",
            "value": "/static/sys_imgs/osroom-logo.ico"
        },
        "APP_NAME": {
            "info": "APP(站点)名称,将作为全局变量使用在平台上",
            "sort": 1,
            "type": "string",
            "value": "OSR DEMO"
        },
        "__restart__": "not_must",
        "TITLE_PREFIX": {
            "info": "APP(Web)Title前缀",
            "sort": 6,
            "type": "string",
            "value": ""
        },
        "LOGO_IMG_URL_SECONDAEY": {
            "info": "APP(Web)Logo URL备用(需要主题支持)",
            "sort": 5,
            "type": "string",
            "value": "/static/sys_imgs/osroom-logo-2.png"
        },
        "TITLE_PREFIX_ADM": {
            "info": "APP(Web)管理端Title前缀",
            "sort": 7,
            "type": "string",
            "value": ""
        },
        "SITE_URL": {
            "info": "Web站点URL(如果没有填写, 则使用默认的当前域名首页地址)",
            "sort": 11,
            "type": "string",
            "value": "http://www.osroom.com"
        },
        "MB_LOGO_DISPLAY": {
            "info": "移动端用App name 还是Logo image 作为APP(Web)的Logo显示, 为空则App name优先<br>可填logo或name(需要主题支持)",
            "sort": 4,
            "type": "string",
            "value": "name"
        }
    },
    "babel": {
        "LANGUAGES": {
            "info": "管理端支持的语言",
            "sort": 99,
            "type": "dict",
            "value": {
                "en_US": {
                    "alias": "En",
                    "name": "English"
                },
                "zh_CN": {
                    "alias": "中文",
                    "name": "中文"
                }
            }
        },
        "__restart__": "must",
        "__sort__": 9,
        "__info__": "多语言设置",
        "BABEL_DEFAULT_LOCALE": {
            "info": "默认语言:可以是zh_CN, en_US等()",
            "sort": 99,
            "type": "string",
            "value": "zh_CN"
        }
    },
    "account": {
        "__info__": "账户设置",
        "USER_AVATAR_MAX_SIZE": {
            "info": "用户头像不能上传超过此值大小(单位Mb)的图片作头像",
            "sort": 99,
            "type": "float",
            "value": 10.0
        },
        "USERNAME_MAX_LEN": {
            "info": "用户名最大长度",
            "sort": 99,
            "type": "int",
            "value": 20
        },
        "__sort__": 6,
        "__restart__": "not_must",
        "DEFAULT_AVATAR": {
            "info": "新注册用户默认头像的URL",
            "sort": 99,
            "type": "string",
            "value": [
                "/static/admin/sys_imgs/avatar_default_1.png",
                "/static/admin/sys_imgs/avatar_default_2.png"
            ]
        },
        "USER_AVATAR_SIZE": {
            "info": "用户头像保存大小[<width>, <height>]像素",
            "sort": 99,
            "type": "list",
            "value": [
                "360",
                "360"
            ]
        }
    },
    "theme": {
        "__restart__": "not_must",
        "__info__": "主题配置",
        "CURRENT_THEME_NAME": {
            "info": "当前主题名称,需与主题主目录名称相同",
            "sort": 99,
            "type": "string",
            "value": "osr-style"
        }
    },
    "user_model": {
        "__restart__": "not_must",
        "__sort__": 99,
        "__info__": "用户Model",
        "EDITOR": {
            "info": "新用户默认编辑器类型rich_text或markdown",
            "sort": 99,
            "type": "string",
            "value": "rich_text"
        }
    },
    "name_audit": {
        "__restart__": "not_must",
        "__info__": "名称验证, 如用户名,分类名称",
        "AUDIT_PROJECT_KEY": {
            "info": "审核项目的Key(键),审核时会使用一个Key来获取审核规则,正则去匹配用户输入的内容",
            "sort": 99,
            "type": "dict",
            "value": {
                "username": "审核用户名",
                "class_name": "审核一些短的分类名称, 如category, tag"
            }
        },
        "__sort__": 8
    },
    "cache": {
        "__info__": "Web缓存参数设置（建议技术管理人员使用）",
        "CACHE_DEFAULT_TIMEOUT": {
            "info": "(s秒)默认缓存时间,当单个缓存没有设定缓存时间时会使用该时间",
            "sort": 99,
            "type": "int",
            "value": 600
        },
        "__sort__": 99,
        "__restart__": "must",
        "USE_CACHE": {
            "info": "是否使用缓存功能,建议开启",
            "sort": 99,
            "type": "bool",
            "value": True
        },
        "CACHE_TYPE": {
            "info": "缓存使用的类型,可选择redis,mongodb",
            "sort": 99,
            "type": "string",
            "value": "redis"
        },
        "CACHE_MONGODB_COLLECT": {
            "info": "保存cache的collection,当CACHE_TYPE为mongodb时有效",
            "sort": 99,
            "type": "string",
            "value": "osr_cache"
        },
        "CACHE_KEY_PREFIX": {
            "info": "所有键(key)之前添加的前缀,这使得它可以为不同的应用程序使用相同的memcached(内存)服务器.",
            "sort": 99,
            "type": "string",
            "value": "osr_cache"
        }
    },
    "seo": {
        "DEFAULT_KEYWORDS": {
            "info": "网站的页面默认关键词",
            "sort": 99,
            "type": "string",
            "value": "开源, 企业网站, 博客网站, 微信小程序, Web服务端"
        },
        "__info__": "针对网页客户端的简单的SEO配置<br>此模块所有的KEY值, 都可以直接请求全局Api(<br><span style='color:red;'>/api/global</span>)获取.<br>也可以直接在主题中使用Jinjia2模板引擎获取(<br><span style='color:red;'>g.site_global.site_config.XXXX</span>)",
        "__restart__": "not_must",
        "DEFAULT_DESCRIPTION": {
            "info": "网站的页面默认简单描述",
            "sort": 99,
            "type": "string",
            "value": "开源Web系统, 可以作为企业网站, 个人博客网站, 微信小程序Web服务端"
        },
        "__sort__": 4
    },
    "verify_code": {
        "MAX_NUM_SEND_SAMEIP_PERMIN_NO_IMGCODE": {
            "info": "同一IP地址,同一用户(未登录的同属同一匿名用户),允许每分钟在不验证[图片验证码]的时候,调用API发送验证码最大次数.<br>超过次数后API会生成[图片验证码]并返回图片url对象(也可以自己调用获取图片验证码API获取).<br>如果你的客户端(包括主题)不支持显示图片验证码,请设置此配置为99999999",
            "sort": 99,
            "type": "int",
            "value": 1
        },
        "MAX_IMG_CODE_INTERFERENCE": {
            "info": "图片验证码干扰程度的最大值",
            "sort": 99,
            "type": "int",
            "value": 40
        },
        "IMG_CODE_DIR": {
            "info": "图片验证码保存目录",
            "sort": 99,
            "type": "string",
            "value": "admin/verify_code"
        },
        "__info__": "验证码(建议技术管理员配置)",
        "MIN_IMG_CODE_INTERFERENCE": {
            "info": "图片验证码干扰程度的最小值,最小值小于10时无效",
            "sort": 99,
            "type": "int",
            "value": 10
        },
        "SEND_CODE_TYPE": {
            "info": "发送的验证码字符类型，与字符个数",
            "sort": 99,
            "type": "dict",
            "value": {
                "string": 0,
                "int": 6
            }
        },
        "__restart__": "not_must",
        "__sort__": 11,
        "MAX_NUM_SEND_SAMEIP_PERMIN": {
            "info": "同一IP地址,同一用户(未登录的同属一匿名用户), 允许每分钟调用API发送验证码的最大次数",
            "sort": 99,
            "type": "int",
            "value": 15
        },
        "EXPIRATION": {
            "info": "验证码过期时间(s)",
            "sort": 99,
            "type": "int",
            "value": 600
        }
    },
    "rest_auth_token": {
        "__info__": "Web参数设置",
        "__sort__": 99,
        "REST_ACCESS_TOKEN_LIFETIME": {
            "info": "给客户端发补的访问Token AccessToken的有效期",
            "sort": 99,
            "type": "int",
            "value": 172800
        },
        "__restart__": "not_must",
        "LOGIN_LIFETIME": {
            "info": "jwt 登录BearerToken有效期(s)",
            "sort": 99,
            "type": "int",
            "value": 2592000
        },
        "MAX_SAME_TIME_LOGIN": {
            "info": "最多能同时登录几个使用JWT验证的客户端,超过此数目则会把旧的登录注销",
            "sort": 99,
            "type": "int",
            "value": 3
        }
    },
    "upload": {
        "SAVE_DIR": {
            "info": "上传:保存目录,如何存在'/'则会自动切分创建子目录",
            "sort": 99,
            "type": "string",
            "value": "media"
        },
        "__info__": "文件上传配置（建议技术管理人员使用）",
        "__sort__": 99,
        "__restart__": "not_must",
        "UP_ALLOWED_EXTENSIONS": {
            "info": "上传:允许上传的文件后缀(全部小写),每个用英文的','隔开",
            "sort": 99,
            "type": "list",
            "value": [
                "xls",
                "xlxs",
                "excel",
                "txt",
                "pdf",
                "png",
                "jpg",
                "jpeg",
                "gif",
                "ico",
                "mp4",
                "rmvb",
                "avi",
                "mkv",
                "mov",
                "mp3",
                "wav",
                "wma",
                "ogg",
                "zip",
                "gzip",
                "tar"
            ]
        },
        "IMG_VER_CODE_DIR": {
            "info": "系统生成的图片验证码保存目录",
            "sort": 99,
            "type": "string",
            "value": "verifi_code"
        }
    },
    "session": {
        "PERMANENT_SESSION_LIFETIME": {
            "info": "永久会话的有效期.",
            "sort": 99,
            "type": "int",
            "value": 2592000
        },
        "SESSION_MONGODB_COLLECT": {
            "info": "Mongodb保存session的collection,当SESSION_TYPE为mongodb时有效",
            "sort": 99,
            "type": "string",
            "value": "osr_session"
        },
        "SESSION_PERMANENT": {
            "info": "是否使用永久会话",
            "sort": 99,
            "type": "bool",
            "value": True
        },
        "SESSION_TYPE": {
            "info": "保存Session会话的类型,可选mongodb, redis",
            "sort": 99,
            "type": "string",
            "value": "mongodb"
        },
        "__sort__": 99,
        "SESSION_KEY_PREFIX": {
            "info": "添加一个前缀,之前所有的会话密钥。这使得它可以为不同的应用程序使用相同的后端存储服务器",
            "sort": 99,
            "type": "string",
            "value": "osroom"
        },
        "__restart__": "must",
        "__info__": "Session参数设置（建议技术管理人员使用）"
    }
}