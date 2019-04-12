# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-8-9.
 * QQ 405367236
"""
import random
from faker import Factory

fake = Factory().create('zh_CN')


def random_phone_number():
    """随机手机号"""
    return fake.phone_number()


def random_name():
    """随机姓名"""
    return fake.name()


def random_name_female():
    """name_female()：男性全名"""
    return fake.name_female()


def random_name_male():
    """name_male()：女性全名"""
    return fake.name_male()


def random_user_name():
    """随机用户名"""
    return fake.user_name()


def random_ssn():
    """身份证"""
    return fake.ssn()


def random_address():
    """随机地址"""
    return fake.address()


def random_email():
    """随机email"""
    return fake.email()


def random_country():
    """随机国家"""
    return fake.country()


def random_country_code():
    """随机国家编码"""
    return fake.country_code()


def random_district():
    """随机区"""
    return fake.district()


def random_coordinate():
    """随机地理坐标"""
    return fake.geo_coordinate()


def random_latitude():
    """随机地理坐标(纬度)"""
    return fake.latitude()


def random_longitude():
    """随机地理坐标(经度)"""
    return fake.longitude()


def random_numerify():
    """随机三位数"""
    return fake.numerify()


def random_postcode():
    """随机邮编"""
    return fake.postcode()


def random_province():
    """随机省份"""
    return fake.province()


def random_street_address():
    """随机街道地址"""
    return fake.street_address()


def random_street_name():
    """随机街道名"""
    return fake.street_name()


def random_company():
    """随机公司名（长）"""
    return fake.company()


def random_company_suffix():
    """随机公司名（后缀）"""
    return fake.company_prefix()


def random_company_prefix():
    """随机公司名（前缀）"""
    return fake.company_prefix()


def random_company_suffix():
    """随机公司性质"""
    return fake.company_suffix()


def random_jod():
    """随机职位"""
    return fake.job()


def random_card_number():
    """随机信用卡卡号"""
    return fake.credit_card_number()


def random_card_provider():
    """随机信用卡类型"""
    return fake.credit_card_provider()


def random_card_security_code():
    """随机信安全码"""
    return fake.credit_card_security_code()


def random_currency_code():
    """随机货币编码"""
    return fake.currency_code()


def random_century():
    """随机世纪"""
    return fake.century()


def random_mac_address():
    """随机MAC地址"""
    return fake.mac_address()


def random_domain_name():
    """随机域名"""
    return fake.domain_name()


def random_ipv4():
    """随机IPV4地址"""
    return fake.ipv4()


def random_uri():
    """随机URI地址"""
    return fake.uri()


def random_url():
    """随机URL地址"""
    return fake.url()


def random_uri():
    """随机URI地址"""
    return fake.uri()

def random_digit():
    """0~9随机数"""
    return fake.random_digit()

def random_int(a, b):
    """0~9随机数"""
    return fake.random_int(a, b)

def random_color():
    """随机颜色名"""
    return fake.color_name()

def random_sentence():
    """生成一句话"""
    return fake.sentence()


def random_word():
    """生成词语"""
    return fake.word()


def random_paragraphs():
    """生成多个段落，通过参数nb来控制段落数，返回数组"""
    return fake.paragraphs()

def random_credit_card():
    # 生成信用卡号
    return fake.credit_card_number()

def random_past_date():
    # 随机生成已经过去的日期
    return fake.past_date()

def random_future_date():
    # 随机生成未来日期
    return fake.future_date()

















def random_str(min_chars=0, max_chars=8):
    """长度在最大值与最小值之间的随机字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)


def factory_generate_ids(starting_id=1, increment=1):
    """ 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment。 """
    def generate_started_ids():
        val = starting_id
        local_increment = increment
        while True:
            yield val
            val += local_increment
    return generate_started_ids


def factory_choice_generator(values):
    """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """
    def choice_generator():
        my_list = list(values)
        # rand = random.Random()
        while True:
            yield random.choice(my_list)
    return choice_generator


if __name__ == '__main__':
    print(random_phone_number())
    print(random_name())
    print(random_address())
    print(random_email())
    print(random_ipv4())
    print(random_card_number())

    print(random_str(min_chars=6, max_chars=80))
    id_gen = factory_generate_ids(starting_id=0, increment=2)()
    for i in range(5):
        print(next(id_gen))

    choices = ['John', 'Sam', 'Lily', 'Rose']
    choice_gen = factory_choice_generator(choices)()
    for i in range(5):
        print(next(choice_gen))
"""
1.什么是Faker

    Faker是一个Python包，开源的GITHUB项目，主要用来创建伪数据，使用Faker包，无需再手动生成或者手写随机数来生成数据，只需要调用Faker提供的方法，即可完成数据的生成。

    项目地址：https://github.com/joke2k/faker

2.安装Faker

    方法一：

        pip install faker

    方法二：

        通过上方提供的github地址，来下载编译安装。

3.Faker的使用

    引用包：

        from faker import Faker

    初始化：

        f=Faker(locale='zh_CN')

    关于初始化参数locale：为生成数据的文化选项，默认为en_US，只有使用了相关文化，才能生成相对应的随机信息（比如：名字，地址，邮编，城市，省份等）

可选择的文化信息：

ar_EG - Arabic (Egypt)

ar_PS - Arabic (Palestine)

ar_SA - Arabic (Saudi Arabia)

bg_BG - Bulgarian

cs_CZ - Czech

de_DE - German

dk_DK - Danish

el_GR - Greek

en_AU - English (Australia)

en_CA - English (Canada)

en_GB - English (Great Britain)

en_US - English (United States)

es_ES - Spanish (Spain)

es_MX - Spanish (Mexico)

et_EE - Estonian

fa_IR - Persian (Iran)

fi_FI - Finnish

fr_FR - French

hi_IN - Hindi

hr_HR - Croatian

hu_HU - Hungarian

it_IT - Italian

ja_JP - Japanese

ko_KR - Korean

lt_LT - Lithuanian

lv_LV - Latvian

ne_NP - Nepali

nl_NL - Dutch (Netherlands)

no_NO - Norwegian

pl_PL - Polish

pt_BR - Portuguese (Brazil)

pt_PT - Portuguese (Portugal)

ru_RU - Russian

sl_SI - Slovene

sv_SE - Swedish

tr_TR - Turkish

uk_UA - Ukrainian

zh_CN - Chinese (China)

zh_TW - Chinese (Taiwan)

然后即可使用系统提供的方法：



一段简单的测试代码
f.name()  #生成姓名

f.address() #生成地址

4.常用方法一览

city_suffix()：市，县

country()：国家

country_code()：国家编码

district()：区

geo_coordinate()：地理坐标

latitude()：地理坐标(纬度)

longitude()：地理坐标(经度)

lexify()：替换所有问号（“？”）带有随机字母的事件。

numerify()：三位随机数字

postcode()：邮编

province()：省份

street_address()：街道地址

street_name()：街道名

street_suffix()：街、路

random_digit()：0~9随机数

random_digit_not_null()：1~9的随机数

random_element()：随机字母

random_int()：随机数字，默认0~9999，可以通过设置min,max来设置

random_letter()：随机字母

random_number()：随机数字，参数digits设置生成的数字位数

color_name()：随机颜色名

hex_color()：随机HEX颜色

rgb_color()：随机RGB颜色

safe_color_name()：随机安全色名

safe_hex_color()：随机安全HEX颜色

bs()：随机公司服务名

company()：随机公司名（长）

company_prefix()：随机公司名（短）

company_suffix()：公司性质

credit_card_expire()：随机信用卡到期日

credit_card_full()：生成完整信用卡信息

credit_card_number()：信用卡号

credit_card_provider()：信用卡类型

credit_card_security_code()：信用卡安全码

currency_code()：货币编码

am_pm()：AM/PM

century()：随机世纪

date()：随机日期

date_between()：随机生成指定范围内日期，参数：start_date，end_date取值：具体日期或者today,-30d,-30y类似

date_between_dates()：随机生成指定范围内日期，用法同上

date_object()：随机生产从1970-1-1到指定日期的随机日期。

date_this_month()：

date_this_year()：

date_time()：随机生成指定时间（1970年1月1日至今）

date_time_ad()：生成公元1年到现在的随机时间

date_time_between()：用法同dates

future_date()：未来日期

future_datetime()：未来时间

month()：随机月份

month_name()：随机月份（英文）

past_date()：随机生成已经过去的日期

past_datetime()：随机生成已经过去的时间

time()：随机24小时时间

timedelta()：随机获取时间差

time_object()：随机24小时时间，time对象

time_series()：随机TimeSeries对象

timezone()：随机时区

unix_time()：随机Unix时间

year()：随机年份

file_extension()：随机文件扩展名

file_name()：随机文件名（包含扩展名，不包含路径）

file_path()：随机文件路径（包含文件名，扩展名）

mime_type()：随机mime Type

ascii_company_email()：随机ASCII公司邮箱名

ascii_email()：随机ASCII邮箱

ascii_free_email()：

ascii_safe_email()：

company_email()：

domain_name()：生成域名

domain_word()：域词(即，不包含后缀)

email()：

free_email()：

free_email_domain()：

f.safe_email()：安全邮箱

f.image_url()：随机URL地址

ipv4()：随机IP4地址

ipv6()：随机IP6地址

mac_address()：随机MAC地址

tld()：网址域名后缀(.com,.net.cn,等等，不包括.)

uri()：随机URI地址

uri_extension()：网址文件后缀

uri_page()：网址文件（不包含后缀）

uri_path()：网址文件路径（不包含文件名）

url()：随机URL地址

user_name()：随机用户名

isbn10()：随机ISBN（10位）

isbn13()：随机ISBN（13位）

job()：随机职位

paragraph()：随机生成一个段落

paragraphs()：随机生成多个段落，通过参数nb来控制段落数，返回数组

sentence()：随机生成一句话
word()：随机生成词语

sentences()：随机生成多句话，与段落类似

text()：随机生成一篇文章（不要幻想着人工智能了，至今没完全看懂一句话是什么意思）
words()：随机生成多个词语，用法与段落，句子，类似

binary()：随机生成二进制编码

boolean()：True/False

language_code()：随机生成两位语言编码

locale()：随机生成语言/国际 信息

md5()：随机生成MD5

null_boolean()：NULL/True/False

password()：随机生成密码,可选参数：length：密码长度；special_chars：是否能使用特殊字符；digits：是否包含数字；upper_case：是否包含大写字母；lower_case：是否包含小写字母

sha1()：随机SHA1

sha256()：随机SHA256

uuid4()：随机UUID

first_name()：

first_name_female()：女性名

first_name_male()：男性名

first_romanized_name()：罗马名

last_name()：

last_name_female()：女姓

last_name_male()：男姓

last_romanized_name()：

name()：随机生成全名

name_female()：男性全名

name_male()：女性全名

romanized_name()：罗马名

msisdn()：移动台国际用户识别码，即移动用户的ISDN号码

phone_number()：随机生成手机号

phonenumber_prefix()：随机生成手机号段

profile()：随机生成档案信息

simple_profile()：随机生成简单档案信息
随机生成指定类型数据：

pybool()：

pydecimal()：

pydict()：

pyfloat()：left_digits=5 #生成的整数位数,

                  right_digits=2 #生成的小数位数,

                  positive=True #是否只有正数

pyint()：随机整数

pyiterable()

pylist()

pyset()

pystr()

pystruct()

pytuple()



ssn()：生成身份证号

chrome()：随机生成Chrome的浏览器user_agent信息

firefox()：随机生成FireFox的浏览器user_agent信息

internet_explorer()：随机生成IE的浏览器user_agent信息

opera()：随机生成Opera的浏览器user_agent信息

safari()：随机生成Safari的浏览器user_agent信息

linux_platform_token()：随机Linux信息

user_agent()：随机user_agent信息

"""