import random
import pickle

#初始化
flag = False
computer = {}
try :
    pic = open("CompbotDB.pkl" , "rb")
    computer = pickle.load(pic)
except (EnvironmentError , pickle.PicklingError) as err :
    print("載入錯誤")
    flag = True
finally :
    if pic is not None :
        pic.close()
if flag:
    SystemExit

#處理定義字串
def dealWithString(string):
    if string.count(",") > 1 and string.count("我說") > 1 and string.count("你說") > 1 :
        print("語法錯誤,請勿出現兩個以上的\",和我說你說\"")
        return (None,None)
    else :
        (key,value) = (string.split(",")[0],string.split(",")[1])
        key = key.split("我說")[1]
        value = value.split("你說")[1]
        if "" == key or "" == value :
            print("你沒有定義任何東西")
            return (None,None)
    return (key,value)

#初始輸入
<<<<<<< HEAD
cust = input("孤單寂寞覺得冷嗎？電腦陪你說說話\n說明遊戲規則，如果你說「我說XXX,你說OOO」，就表示你正在教電腦說話，記住，電腦是隻猴子，你要教電腦說話他才會回答你。因為他是隻聰明的猴子，所以他會儲存對話內容。另外你可以試試，教他很多不一樣的回答，例如「我說蘋果,你說紅紅」「我說蘋果,你說好吃」「我說蘋果,你說超難吃」。如果你要刪除某像對話可以這樣說「我說蘋果,你說好吃,你壞壞」。\n事不宜遲，快來教跟這隻猴子講話吧\n打「結束」結束\n")
=======
cust = input("孤單寂寞覺得冷嗎？電腦陪你說說話\n說明遊戲規則，如果你說「我說XXX，你說OOO」，就表示你正在教電腦說話，記住，電腦是隻猴子，你要教電腦說話他才會回答你。因為他是隻聰明的猴子，所以他會儲存對話內容。另外你可以試試，教他很多不一樣的回答，例如「我說蘋果，你說紅紅」「我說蘋果，你說好吃」「我說蘋果，你說超難吃」。如果你要刪除某像對話可以這樣說「我說蘋果,你說好吃，你壞壞」。\n事不宜遲，快來教跟這隻猴子講話吧\n打「結束」結束\n")
>>>>>>> 5108fb943a9696433799904c4b17d9b96103c932

#主程式
while True :
    if "我說" in cust and ",你說" in cust and ",你壞壞" in cust :
        (key,value) = dealWithString(cust)
        if (key,value) != (None,None) :
            if key in computer :
                if value in computer[key] :
                    computer[key].remove(value)
                    if computer[key] is None :
                        del computer[key]
                else :
                    print("你沒有輸入過這句話喔")
            else :
                print("你沒有輸入過這句話喔")
    elif "我說" in cust and ",你說" in cust :
        (key,value) = dealWithString(cust)
        if (key,value) != (None,None) :
            if key in computer :
                if value not in computer[key]:
                    computer[key] += [value]
                else:
                    print("此定義已有")
            else :
                computer[key] = [value]
    elif "" == cust :
        print("你並未輸入任何東西")
    elif "結束" in cust:
        break
    else :
        try:
            print(random.choice(computer[cust]))
        except KeyError:
            print("抱歉你再說什麼我聽不懂，請用「我說XXX,你說OOO」來定義字句")
    cust = input()

#序列化
try :
    pic = open("CompbotDB.pkl" , "wb")
    pickle.dump(computer,pic)
except (EnvironmentError , pickle.PicklingError) as err :
    print("輸出錯誤")
finally:
    if pic is not None :
        pic.close()

