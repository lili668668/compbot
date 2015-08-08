import random
cust = input("孤單寂寞覺得冷嗎？電腦陪你說說話\n說明遊戲規則，如果你說「我說XXX，你說OOO」，就表示你正在教電腦說話，記住，電腦是隻猴子，你要教電腦說話他才會回答你。因為他是隻聰明的猴子，所以他會儲存對話內容。另外你可以試試，教他很多不一樣的回答，例如「我說蘋果，你說紅紅」「我說蘋果，你說好吃」「我說蘋果，你說超難吃」。如果你要刪除某像對話可以這樣說「我說蘋果,你說好吃，你壞壞」。\n事不宜遲，快來教跟這隻猴子講話吧\n")

"""範例"""
a = ["好可愛","藍藍der"]
computer = { "哆拉A夢" : a }

#主程式
while True :
    if "我說" in cust and ",你說" in cust and ",你壞壞" in cust :
        print("有下去執行")
        (key,value) = (cust.split(",")[0],cust.split(",")[1])
        key = key.replace("我說","")
        value = value.replace("你說","")
        if "" == key or "" == value :
            print("你沒有輸入定義喔")
        else :
            if key in computer :
                if value in computer[key] :
                    computer[key] = computer[key].remove(value)
                    if computer[key] is None :
                        del computer[key]
                else :
                    print("你沒有輸入過這句話喔")
            else :
                print("你沒有輸入過這句話喔")
    elif "我說" in cust and ",你說" in cust :
        (key,value) = (cust.split(",")[0],cust.split(",")[1])
        key = key.replace("我說","")
        value = value.replace("你說","")
        if "" == key or "" == value :
            print("你沒有輸入定義喔")
        else :
            if key in computer :
                computer[key] += [value]
            else :
                computer[key] = [value]
    elif "" == cust :
        print("你並未輸入任何東西")
    else :
        try:
            print(random.choice(computer[cust]))
        except KeyError:
            print("抱歉你再說什麼我聽不懂，請用「我說XXX，你說OOO」來定義字句")
    cust = input()
