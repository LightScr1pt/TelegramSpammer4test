# -*- coding: utf8 -*- 
try :#line:3
    from pyrogram import Client ,filters #line:4
    from pyrogram .errors import FloodWait #line:5
    from pyrogram .types import ChatPermissions #line:7
    import time #line:9
    from time import sleep #line:10
    import random #line:11
    #import webbrowser #line:12
except :#line:13
    import os #line:14
    os .system ('pip3 install Pyrogram')#line:15
    #os .system ('pip3 install webbrowser')#line:16
try :#line:19
    f =open ("config.ini")#line:20
    f .close ()#line:21
except IOError :#line:22
    f =open ('config.ini','w+')#line:23
    #webbrowser .open_new_tab ('https://my.telegram.org/auth')#line:24
    api =input ('Введите api_id\n>> ')#line:25
    api_hash =input ('Введите api_hash\n>> ')#line:26
    f .write ("[pyrogram]\napi_id = "+str (api )+"\napi_hash = "+str (api_hash ))#line:27
    f .close ()#line:28
print ('Это официальный продукт!\nScript by LIGHT HACKING')#line:31
app =Client ("my_account")#line:33
def echo (_OOO0OO0OO0O0OO000 ,OO00OO000000000OO ):#line:37
    O000OO0OOO0OOOO0O =OO00OO000000000OO .text #line:38
    OO00OOO0O000O0OOO =O000OO0OOO0OOOO0O #line:39
    OOO0OOO0OOOOO0O00 =""#line:40
    OOOOO00OOOOOOOO0O ="|"#line:41
    while (OOO0OOO0OOOOO0O00 !=O000OO0OOO0OOOO0O ):#line:43
        try :#line:44
            OO00OO000000000OO .edit (OOO0OOO0OOOOO0O00 +OOOOO00OOOOOOOO0O )#line:45
            sleep (0.05 )#line:46
            OOO0OOO0OOOOO0O00 =OOO0OOO0OOOOO0O00 +OO00OOO0O000O0OOO [0 ]#line:48
            OO00OOO0O000O0OOO =OO00OOO0O000O0OOO [1 :]#line:49
            OO00OO000000000OO .edit (OOO0OOO0OOOOO0O00 )#line:51
            sleep (0.05 )#line:52
        except FloodWait as OOO00O0O0OOOOOO00 :#line:54
            sleep (OOO00O0O0OOOOOO00 .x )#line:55
@app .on_message (filters .command ("t",prefixes =".")&filters .me )#line:57
def type (_OOO0OO00OO00O0OOO ,O00OO00O0O00OO0OO ):#line:58
    OO0O00O0000O00O00 =O00OO00O0O00OO0OO .text .split (".t ",maxsplit =1 )[1 ]#line:60
    OOOOO0O0OOOOOO0OO =OO0O00O0000O00O00 #line:61
    O0OOOOOOO0O0O00O0 =""#line:62
    OOO00O0000O00OOO0 ="|"#line:63
    while (O0OOOOOOO0O0O00O0 !=OO0O00O0000O00O00 ):#line:65
        try :#line:66
            O00OO00O0O00OO0OO .edit (O0OOOOOOO0O0O00O0 +OOO00O0000O00OOO0 )#line:67
            sleep (0.05 )#line:68
            O0OOOOOOO0O0O00O0 =O0OOOOOOO0O0O00O0 +OOOOO0O0OOOOOO0OO [0 ]#line:70
            OOOOO0O0OOOOOO0OO =OOOOO0O0OOOOOO0OO [1 :]#line:71
            O00OO00O0O00OO0OO .edit (O0OOOOOOO0O0O00O0 )#line:73
            sleep (0.05 )#line:74
        except FloodWait as O000O0OOOO0O0000O :#line:76
            sleep (O000O0OOOO0O0000O .x )#line:77
@app .on_message (filters .command ("hack",prefixes =".")&filters .me )#line:81
def hack (_OOO00O00O00OOO0O0 ,O0000OOOOO0OO000O ):#line:82
    O00O00OO0OOOOOOOO =O0000OOOOO0OO000O .chat .id #line:83
    O0O0OOOOOO0O0O000 =0 #line:85
    try :#line:87
    	O00OOOO0OO0O0OO00 ="👮‍ Иду взламывать пентагтон..."#line:89
    	O0000OOOOO0OO000O .edit (O00OOOO0OO0O0OO00 )#line:90
    	sleep (1 )#line:91
    except :#line:93
    	pass #line:94
    while (O0O0OOOOOO0O0O000 <100 ):#line:96
        try :#line:98
            O00OOOO0OO0O0OO00 ="Взлом жопы... "+str (O0O0OOOOOO0O0O000 )+"%"#line:100
            O0000OOOOO0OO000O .edit (O00OOOO0OO0O0OO00 )#line:101
            O0O0OOOOOO0O0O000 +=random .randint (1 ,3 )#line:103
            sleep (0.05 )#line:104
        except FloodWait as OOO00O000O0OOOO0O :#line:106
            sleep (OOO00O000O0OOOO0O .x )#line:107
    O0000OOOOO0OO000O .edit ("🟢 Успешно взломана!")#line:109
    sleep (1 )#line:110
    O0000OOOOO0OO000O .edit ("Поиск секретных данных... ")#line:112
    O0O0OOOOOO0O0O000 =0 #line:113
    while (O0O0OOOOOO0O0O000 <100 ):#line:115
        try :#line:116
            O00OOOO0OO0O0OO00 ="Поиск секретных данных... "+str (O0O0OOOOOO0O0O000 )+"%"#line:117
            O0000OOOOO0OO000O .edit (O00OOOO0OO0O0OO00 )#line:118
            O0O0OOOOOO0O0O000 +=random .randint (1 ,5 )#line:120
            sleep (0.10 )#line:121
        except FloodWait as OOO00O000O0OOOO0O :#line:123
            sleep (OOO00O000O0OOOO0O .x )#line:124
    try :#line:126
	    O00OOOOO00OO00O00 =[O0OOO00OOOOO000OO for O0OOO00OOOOO000OO in app .iter_chat_members (O00O00OO0OOOOOOOO )if O0OOO00OOOOO000OO .status not in ("administrator","creator")]#line:131
	    random .shuffle (O00OOOOO00OO00O00 )#line:133
	    OOO0OOOO00000O0O0 =random .randint (500 ,1900 )#line:134
	    O0000OOOOO0OO000O .edit ("Найденны данные что "+"["+O00OOOOO00OO00O00 [0 ].user .first_name +"](tg://user?id="+str (O00OOOOO00OO00O00 [i ].user .id )+")"+" гей...")#line:136
	    app .send_message (O0000OOOOO0OO000O .chat .id ,"👮‍ Вам призначена компенсация в "+str (OOO0OOOO00000O0O0 )+"$\n[ Забрать можно тут](t.me/lighthacking)",parse_mode ="markdown")#line:137
	    sleep (2 )#line:138
    except :#line:140
	    O0000OOOOO0OO000O .edit ("Найденны данные что ты гей...")#line:141
	    app .send_message (O0000OOOOO0OO000O .chat .id ,"👮‍ Вам призначена компенсация в "+str (OOO0OOOO00000O0O0 )+"$\n[ Забрать можно тут](t.me/lighthacking)",parse_mode ="markdown")#line:142
	    sleep (2 )#line:143
@app .on_message (filters .command ("thanos",prefixes =".")&filters .me )#line:149
def thanos (_OO0O000OO0O000O0O ,O0OOOOOO0000OOO00 ):#line:150
    OOO000OO0O000000O =O0OOOOOO0000OOO00 .text .split (".thanos ",maxsplit =1 )[1 ]#line:151
    O0OO000OO0000O000 =[O00O000000000OOO0 for O00O000000000OOO0 in app .iter_chat_members (OOO000OO0O000000O )if O00O000000000OOO0 .status not in ("administrator","creator")]#line:157
    random .shuffle (O0OO000OO0000O000 )#line:159
    app .send_message (OOO000OO0O000000O ,"Щелчок Таноса ... *щёлк*")#line:161
    for OOO0O0O00OOO00000 in range (len (O0OO000OO0000O000 )//2 ):#line:163
        try :#line:164
            app .restrict_chat_member (chat_id =OOO000OO0O000000O ,user_id =O0OO000OO0000O000 [OOO0O0O00OOO00000 ].user .id ,permissions =ChatPermissions (),until_date =int (time .time ()+86400 ),)#line:170
            app .send_message (OOO000OO0O000000O ,"Исчез "+O0OO000OO0000O000 [OOO0O0O00OOO00000 ].user .first_name )#line:171
        except FloodWait as O0O0O00O00O0000OO :#line:172
            print ("> waiting",O0O0O00O00O0000OO .x ,"seconds.")#line:173
            time .sleep (O0O0O00O00O0000OO .x )#line:174
    app .send_message (OOO000OO0O000000O ,"Но какой ценой?")#line:176
@app .on_message (filters .command ("spam",prefixes =".")&filters .me )#line:178
def spam (_OOOO0O0OO0O00O00O ,O00OO0O00O0OO0O00 ):#line:179
    OOO000O0O000O000O =O00OO0O00O0OO0O00 .chat .id #line:180
    try :#line:181
	    OOOO0O0OO0OO0OOOO =O00OO0O00O0OO0O00 .text .split (".spam ",maxsplit =1 )[1 ]#line:182
	    O00OO0O00O0OO0O00 .edit (OOOO0O0OO0OO0OOOO )#line:183
	    try :#line:185
		    O0O0OOOOO0O0000OO =[O0O000O0O0O0O0OO0 for O0O000O0O0O0O0OO0 in app .iter_chat_members (OOO000O0O000O000O )]#line:189
	    except :#line:190
		    while True :#line:191
			    try :#line:192
				    O000OO00000OO00OO =random .randint (1000 ,99999991900 )#line:193
				    app .send_message (OOO000O0O000O000O ,'Ты на '+str (O000OO00000OO00OO )+'% умственно осталый...')#line:194
			    except FloodWait as OOO00000O000O0O00 :#line:195
				    time .sleep (OOO00000O000O0O00 .x )#line:196
	    random .shuffle (O0O0OOOOO0O0000OO )#line:198
	    try :#line:200
	        for O0OO0000O00OO00OO in range (len (O0O0OOOOO0O0000OO )):#line:201
	            try :#line:202
	                app .send_message (OOO000O0O000O000O ,"Пиздуй на пару ["+O0O0OOOOO0O0000OO [O0OO0000O00OO00OO ].user .first_name +"](tg://user?id="+str (O0O0OOOOO0O0000OO [O0OO0000O00OO00OO ].user .id )+")"+'\n\n'+OOOO0O0OO0OO0OOOO )#line:203
	            except FloodWait as OOO00000O000O0O00 :#line:204
	                time .sleep (OOO00000O000O0O00 .x )#line:205
	    except :#line:206
	    	pass #line:207
    except :#line:208
	    O00OO0O00O0OO0O00 .edit ('Всем привет!')#line:209
	    O0O0OOOOO0O0000OO =[O0OO00O0OO0O0OOO0 for O0OO00O0OO0O0OOO0 in app .iter_chat_members (OOO000O0O000O000O )]#line:213
	    random .shuffle (O0O0OOOOO0O0000OO )#line:215
	    while True :#line:217
	        for O0OO0000O00OO00OO in range (len (O0O0OOOOO0O0000OO )):#line:218
	            try :#line:219
	                app .send_message (OOO000O0O000O000O ,"Доброе утро ["+O0O0OOOOO0O0000OO [O0OO0000O00OO00OO ].user .first_name +"](tg://user?id="+str (O0O0OOOOO0O0000OO [O0OO0000O00OO00OO ].user .id )+")")#line:220
	            except FloodWait as OOO00000O000O0O00 :#line:221
	                time .sleep (OOO00000O000O0O00 .x )#line:222
@app .on_message (filters .command ("pick",prefixes =".")&filters .me )#line:225
def pick (_O000O0O000OO0OOO0 ,OOOO00O0O00OOOO00 ):#line:226
	OO0OO0O000O0O00O0 =OOOO00O0O00OOOO00 .chat .id #line:227
	OOOO00O0O00OOOO00 .delete ()#line:229
	OO000OO00O0OO00O0 =[O0O0O00O00O000O0O for O0O0O00O00O000O0O in app .iter_chat_members (OO0OO0O000O0O00O0 )]#line:234
	OOOOO000OOO0OOOO0 =[]#line:236
	random .shuffle (OO000OO00O0OO00O0 )#line:238
	for OO0O0O0OO000000OO in range (len (OO000OO00O0OO00O0 )):#line:240
		OOOOO000OOO0OOOO0 .append ("["+OO000OO00O0OO00O0 [OO0O0O0OO000000OO ].user .first_name +"](tg://user?id="+str (OO000OO00O0OO00O0 [OO0O0O0OO000000OO ].user .id )+")")#line:241
	app .send_message (OO0OO0O000O0O00O0 ,time .strftime ("Сейчас %X",time .localtime ()))#line:243
	app .send_message (OO0OO0O000O0O00O0 ,'\n'.join (OOOOO000OOO0OOOO0 ))#line:245
@app .on_message (filters .command ("load",prefixes =".")&filters .me )#line:248
def load (_O0OO000O0000OO000 ,O0OOO00O0O000OO00 ):#line:249
    while True :#line:251
        try :#line:252
            O0O0OOOO00O0OO0O0 =['Я один из вас, поэтому тоже не выкупаю что там надо делать','Меня одного заебал этот спам?','Ну всё, пиздец','Я не знаю что делать блять','НЕЕЕТ!!!','Я же сказал..','Даже не просите...','Да не могу Я!!!','ДА ЧТО ВАМ НАДО','АХАХАХАХАХАХ, НЕТ','Это не обсуждается','Пофиксили, я думаю как можно..',':)','Не могу нечем помочь']#line:254
            O0OOO00O0O000OO00 .edit (random .choice (O0O0OOOO00O0OO0O0 ))#line:255
            sleep (2 )#line:256
        except FloodWait as OOO000O0OO00000O0 :#line:258
            sleep (OOO000O0OO00000O0 .x )#line:259
            O0OOO00O0O000OO00 .delete ()#line:260
            break #line:261
@app .on_message (filters .me )#line:263
def echo (_OOO000OOO000OO0OO ,OO0OOOOOOOO00O000 ):#line:264
    print (OO0OOOOOOOO00O000 )#line:265
    if OO0OOOOOOOO00O000 .text =="@ayatolover":#line:266
        OOO0O0OOOOO0O0O0O =OO0OOOOOOOO00O000 .chat .id #line:267
        app .send_message (OOO0O0OOOOO0O0O0O ,'Иди нахуй, спасибо, значит работает если высветилось, и не спамьте теперь..')#line:268
app .run ()
