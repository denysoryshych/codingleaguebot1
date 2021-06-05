
import requests
from pprint import pprint
import config 

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup












def func1(tag):
	r = requests.get(
			f"https://codeforces.com/api/problemset.problems?tags={tag}"
		)

	data = r.json()
	for i in data['result']['problems']:
		dat1 = data['result']['problems'][0]
		pprint(dat1['tags'])




tag = "2-sat"
func1(tag)