
import requests  # 发送请求
from bs4 import BeautifulSoup  # 解析网页
import pandas as pd  # 存取csv
from time import sleep  # 等待时间

music_name = []  # 专辑名称
music_url = []  # 专辑链接
music_star = []  # 专辑评分
music_star_people = []  # 评分人数
music_singer = []  # 歌手
music_pub_date = []  # 发行日期
music_type = []  # 类型
music_media = []  # 介质
music_style = []  # 曲风


def get_music_info(url, headers):
	"""
	获取豆瓣音乐详情数据
	:param url: 爬取地址
	:param headers: 爬取请求头
	:return: None
	"""
	res = requests.get(url, headers=headers)
	soup = BeautifulSoup(res.text, 'html.parser')
	for music in soup.select('.item'):
		name = music.select('.pl2 a')[0].text.replace('\n', '').replace('                ', ' ').strip()  # 专辑名称
		music_name.append(name)
		url = music.select('.pl2 a')[0]['href']  # 专辑链接
		music_url.append(url)
		try:
			star = music.select('.rating_nums')[0].text  # 电影评分
		except:
			star = ''
		music_star.append(star)
		star_people = music.select('.pl')[1].text  # 评分人数
		star_people = star_people.strip().replace(' ', '').replace('人评价', '').replace('(\n', '').replace('\n)',
		                                                                                                 '')  # 数据清洗
		music_star_people.append(star_people)
		music_infos = music.select('.pl')[0].text.strip()  # 歌手、发行日期、类型、介质、曲风
		print('music_infos is:')
		print(music_infos)
		if name == 'Garden of Dreams Bandari - Garden Of Dreams / 班得瑞 - 梦花园':
			singer =None
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[0]
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[1]
			music_type.append(type)
			media = music_infos.split(' / ')[2]
			music_media.append(media)
			style = music_infos.split(' / ')[3]
			music_style.append(style)
		elif name == '孙燕姿:直来直往(铁盒装 3CD)' or name == '中国音乐大全·古琴卷':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = None
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[1]
			music_type.append(type)
			media = music_infos.split(' / ')[2]
			music_media.append(media)
			style = music_infos.split(' / ')[3]
			music_style.append(style)
		elif name=='0332' or name=='我的秘密情人 新歌加精選 / My Secret Lover, Jerry Yan' or name=='silent roar' or name=='土巴海尔的眼泪' or name=='後會有期 The Long Goodbye' or name == 'S.E.N.S神思者:故宫三部曲 Palace Memories'or name=='花火が瞬く夜に'or name=='柴可夫斯基：芭蕾舞剧“天鹅湖”、“睡美人”、“胡桃夹子”组曲'or name=='Por Una Cabeza':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = None
			music_type.append(type)
			media = music_infos.split(' / ')[2]
			music_media.append(media)
			style = music_infos.split(' / ')[3]
			music_style.append(style)
		elif name =='一日入秋'or name =='落梦池'or  name =='AM'or name =='Clear Eyes - Single'or name =='Freeek! (Woman) 怪胎'or name =='Lapislatsulia'or name =='琵琶劇唱〜鶴田錦史の世界'or name =='Комбат'or name =='郊区的鸟 电影原声大碟'or name =='Living Room Songs'or name=='江上清风游'or name=='3颗猫饼干 三颗猫饼干 / Three Cat Cookies'or name=='Rain after Summer'or name=='《仙剑奇侠传》电视原创配乐--麦振鸿作品 仙劍奇俠傳-電視原創音樂專輯'or name=='和煦的糖果风'or name=='爱情呼叫转移':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[2]
			music_type.append(type)
			media = None
			music_media.append(media)
			style = music_infos.split(' / ')[3]
			music_style.append(style)
		elif name=="Atlas: Space 1" or name=="0306" or name=="Lost Trails" or name=="Gallantry Bower" or name=="Kveikur" or  name=="Living Room Songs" or name=="Singles" or name=="Near Light: All B​-​Sides" or name=="Rainy Airport" or   name=="Explosions on the Ground" or  name=="Maar" or name=="Drifting Ever Shifting" or name=="Strawberry" or name=="& Yet & Yet" or name=="Decades And Decisions" or name=="RQTN" or  name=="Passenger" or name=="Rain" or name=="All Is Full Of Love" or name=="Breezing+2(紙ジャケット仕様)" or name=="LUBE. Davay Za... Davay Za..." or name=="影秋" or name=="Aboogi" or  name=="American Pie-Best of" or name=="姥姥" or  name=="吴门琴韵 上 吳門琴韻" or name=="空山寂寂" or name=="Ten Summoner's Tales" or name=="Labor In Vain" or name=="A Wishful Way" or name=="Light On The Path" or name=="I'm Your Fan" or name=='Prophets, Seers & Sages the Angels of the Ages' or name=='凪のあすから ORIGINAL SOUNDTRACK 1' or  name=='Hometown' or  name=='十二国記 - 夜想月雫～Piano Memories 十二国记 - 夜想月雫～Piano Memories'or name=='また夏を追う' or name=='When I Drifted I Heard A Faint Melody' or name=='The Severely Departed' or name=='Atlas: Oceans' or name=='甘心不甘心'or name=='Believe [Deluxe Limited Edition]' or name=='笑说想' or name=='I Believe (Give a Little Bit)'or name=='Bangerz (Deluxe Version) 青春大暴走' or name=='So Much (For) Stardust' or name == '沧海一声笑 · 国韵版 《新笑傲江湖》手游主题曲'or name=='Time... 忧伤还是快乐'or name=='Age of Innocence'or name=='River Flows In You'or name=='陰陽師'or name=='星空'or name=='River Flows In You'or name=="I'm Home"or name=='Heaven Blue':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[2]
			music_type.append(type)
			media = music_infos.split(' / ')[3]
			music_media.append(media)
			style =None
			music_style.append(style)
		elif name=='THE CELEBRATIONS' or name=='Everyone Who Pretended To Like Me Is Gone' or name=='飛・び・ま・す' or name=='下北むつの子守歌' or name=='Verisäkeet' or name=='小夜曲' or name=='Insight III' or name=='蓝色多瑙河' or name=='Insight III' or name=='兰2 兰2' or name=='菠萝菠萝蜜'or name == '水边的阿狄丽娜'or name=='Oakland Zone':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = None
			music_type.append(type)
			media = music_infos.split(' / ')[2]
			music_media.append(media)
			style =None
			music_style.append(style)
		elif name == '八点半开始思考人生':
			singer =music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type =None
			music_type.append(type)
			media = None
			music_media.append(media)
			style =music_infos.split(' / ')[2]
			music_style.append(style)
		elif name == '钗头凤':
			singer =music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type =music_infos.split(' / ')[2]
			music_type.append(type)
			media = None
			music_media.append(media)
			style =None
			music_style.append(style)
		elif name == '理查德·克莱德曼经典钢琴曲50首':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = None
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[1]
			music_type.append(type)
			media = music_infos.split(' / ')[2]
			music_media.append(media)
			style =None
			music_style.append(style)
		elif name == '秋日私语(HD':
			singer =None
			music_singer.append(singer)
			pub_date = None
			music_pub_date.append(pub_date)
			type =None
			music_type.append(type)
			media = None
			music_media.append(media)
			style =None
			music_style.append(style)
		elif name == '秋日私语(HD'or name=='Песни нашего века. Часть первая':
			singer = None
			music_singer.append(singer)
			pub_date = None
			music_pub_date.append(pub_date)
			type = None
			music_type.append(type)
			media = None
			music_media.append(media)
			style = None
			music_style.append(style)
		elif name == 'Close to You':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[3]
			music_type.append(type)
			media = music_infos.split(' / ')[4]
			music_media.append(media)
			style = music_infos.split(' / ')[5]
			music_style.append(style)
		elif name == '雪歌 邰肇玫创作专辑':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[2]
			music_type.append(type)
			media = music_infos.split(' / ')[4]
			music_media.append(media)
			style = music_infos.split(' / ')[5]
		elif name == 'H.E.R'or name == '时间的蜜 音乐肖像2015'or name == 'Радио Африка Radio Africa'or name=='璀璨人间'or name=='Лошадь белая':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = None
			music_type.append(type)
			media = None
			music_media.append(media)
			style = None
			music_style.append(style)
		elif name == 'Under a Violet Moon':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[3]
			music_type.append(type)
			media = music_infos.split(' / ')[4]
			music_media.append(media)
			style = music_infos.split(' / ')[5]
			music_style.append(style)
		elif name == 'Songs From The Inverted Womb [RARE]':
			singer = None
			music_singer.append(singer)
			pub_date = None
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[0]
			music_type.append(type)
			media = music_infos.split(' / ')[1]
			music_media.append(media)
			style = None
			music_style.append(style)
		elif name == 'In the Aeroplane Over the Sea 鹏程万里':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[3]
			music_type.append(type)
			media = music_infos.split(' / ')[4]
			music_media.append(media)
			style = music_infos.split(' / ')[5]
			music_style.append(style)
		elif name == 'SHOCK':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[3]
			music_type.append(type)
			media = music_infos.split(' / ')[4]
			music_media.append(media)
			style = None
			music_style.append(style)
		elif name == '浮躁' or name == '3颗猫饼干 三颗猫饼干 / Three Cat Cookies':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = None
			music_type.append(type)
			media = music_infos.split(' / ')[2]
			music_media.append(media)
			style = music_infos.split(' / ')[3]
			music_style.append(style)
		elif name == '陪我歌唱 苏打绿台北小巨蛋演唱会Live Cd:陪我歌唱':
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[2]
			music_type.append(type)
			media = music_infos.split(' / ')[3]
			music_media.append(media)
			style = None
			music_style.append(style)

		else:
			singer = music_infos.split(' / ')[0]
			music_singer.append(singer)
			pub_date = music_infos.split(' / ')[1]
			music_pub_date.append(pub_date)
			type = music_infos.split(' / ')[2]
			music_type.append(type)
			media = music_infos.split(' / ')[3]
			music_media.append(media)
			style = music_infos.split(' / ')[4]
			music_style.append(style)


def save_to_csv(csv_name):
	"""
	数据保存到csv
	:return: None
	"""
	df = pd.DataFrame()  # 初始化一个DataFrame对象
	df['专辑名称'] = music_name
	#df['专辑链接'] = music_url
	df['专辑评分'] = music_star
	df['评分人数'] = music_star_people
	df['歌手'] = music_singer
	df['发行日期'] = music_pub_date
	df['类型'] = music_type
	df['介质'] = music_media
	df['曲风'] = music_style
	df.to_csv(csv_name, encoding='utf_8_sig')  # 将数据保存到csv文件


if __name__ == "__main__":
	# 定义一个请求头(防止反爬)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
	# 开始爬取豆瓣数据

	for i in range(12):
		page_url = 'https://music.douban.com/tag/%E6%B5%81%E8%A1%8C?start={}&type=T'.format(str(i * 20))
		print('开始爬取第{}页，地址是:{}'.format(str(i + 1), page_url))
		get_music_info(page_url, headers)
		sleep(1)  # 等待1秒(防止反爬)

	for i in range(7):
		page_url = 'https://music.douban.com/tag/%E7%BA%AF%E9%9F%B3%E4%B9%90?start={}&type=T'.format(str(i * 20))
		print('开始爬取第{}页，地址是:{}'.format(str(i + 1), page_url))
		get_music_info(page_url, headers)
		sleep(1)  # 等待1秒(防止反爬)

	for i in range(12):
		page_url = 'https://music.douban.com/tag/%E6%B0%91%E8%B0%A3?start={}&type=T'.format(str(i  * 20))
		print('开始爬取第{}页，地址是:{}'.format(str(i + 1), page_url))
		get_music_info(page_url, headers)
		sleep(1)  # 等待1秒(防止反爬)

	for i in range(5):  # 爬取共10页，每页25条数据
		page_url = 'https://music.douban.com/tag/pop?start={}&type=T'.format(str(i*20))
		print('开始爬取第{}页，地址是:{}'.format(str(i + 1), page_url))
		get_music_info(page_url, headers)
		sleep(1)  # 等待1秒(防止反爬)

	for i in range(12):  # 爬取共10页，每页25条数据
		page_url = 'https://music.douban.com/tag/%E5%90%8E%E6%91%87?start={}&type=T'.format(str(i*20))
		print('开始爬取第{}页，地址是:{}'.format(str(i + 1), page_url))
		get_music_info(page_url, headers)
		sleep(1)  # 等待1秒(防止反爬)



save_to_csv(csv_name="musicDouban250.csv")
