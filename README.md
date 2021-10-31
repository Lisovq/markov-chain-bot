# Fun markov-chain bot

Warn
---------
Bot cannot started without mc.api library, after seven months I can't find the mc.api library on PyPI and no some mentions in the Internet

About
---------
The bot was created out of nothing to do, based on the vkbottle framework with mc.api library.
Peewee ORM and sqlite3 driver are used as message storage.
Python3.9+

Run
---------
Firstly fill config.py file, after:
```
python3.9 app.py # run in longpoll mode
python3.9 callback.py # NOT CHECKED. Run in callback mode 
```

Libraries
----------
* vkbottle
* mc.api
* peewee
