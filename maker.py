"名刺リストを作成する"
import random
from card import Card

# 100件作る
COUNT = 100

def make():
    # 名字一覧
    # http://home.r01.itscom.net/morioka/myoji/best200.html
    lns = ['佐藤','鈴木','高橋','田中','渡辺',
        '伊藤','山本','中村','小林','加藤']
    # 名前一覧
    # http://www.tonsuke.com/nebe4.html
    fns = ['大輔','健太','誠','直樹','拓也',
        '祐介','翔','雄太','和也','優',
        '愛','麻衣','恵','裕子','麻美',
        '美香','智美','美穂','麻衣子','友美']
    # 業界一覧
    bs = ['食品','水産','建設','住宅','繊維',
        '化学','薬品','鉄鋼','金属','鉱業']
    # 部署一覧
    ds = ['開発部','製造部','営業部','企画部',
        '総務部','経理部','人事部',
        '広報部','経営企画部']
    # 役職一覧
    ts = ['','主任','係長','課長','部長']
    # 乱数で100枚名刺を作る
    random.seed(2011)
    cards = []
    for i in range(100):
        # 氏名を作る
        ln = lns[random.randint(0,len(lns) - 1)]
        fn = fns[random.randint(0,len(fns) - 1)]
        name = "%s %s" % (ln,fn)
        # 社名を作る
        ln = lns[random.randint(0,len(lns) - 1)]
        b = bs[random.randint(0,len(bs) - 1)]
        company = "%s%s株式会社" % (ln,b)
        # 部署を作る
        d = ds[random.randint(0,len(ds) - 1)]
        # 役職を作る
        t = ts[random.randint(0,len(ts) - 1)]
        # 名刺を作る
        card = Card(i + 1,name,company,d,t)
        #
        cards.append(card)
    return cards
