
import requests
from pprint import pprint
import config 

import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup










import random

bot = Bot(token = config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())



# задача за рейтингом ----------------------------------------------------



class DataInput(StatesGroup):
	r = State()
		
logging.basicConfig(level = logging.INFO)


@dp.message_handler(commands = ['task_rating'])

async def echo(message: types.Message):
	await message.answer('Якого рейтингу?')
	await DataInput.r.set()

@dp.message_handler(state = DataInput.r)
async def func1(message: types.Message, state: FSMContext):
	rating = message.text
	ra = requests.get(
			f"https://codeforces.com/api/problemset.problems?"
		)

	data = ra.json()
	
	elements_count = 0
	elements_count_rat = 0
	want_zadacha_rat = random.randint(1,100)
	for i in data['result']['problems']:
		dat1 = data['result']['problems'][elements_count]
		if 'rating' in dat1:
			rat1 = str(dat1['rating'])
			rating = str(rating)
			id = dat1['contestId']
			index = dat1['index']
			if rat1 == rating:
				elements_count_rat += 1
				if elements_count_rat == want_zadacha_rat:
					await message.answer(f"https://codeforces.com/problemset/problem/{id}/{index}")
					break

		elements_count += 1
	await state.finish()





# задача за тегом ----------------------------------------------------

class DataInput(StatesGroup):
	t = State()


@dp.message_handler(commands = ['task_tag'])

async def tag1(message: types.Message):
	await message.answer('Тег задачі')
	await DataInput.t.set()

@dp.message_handler(state = DataInput.t)
async def tag2(message: types.Message, state: FSMContext):
	tag = message.text
	ra = requests.get(
			f"https://codeforces.com/api/problemset.problems?tags={tag}"
		)

	data = ra.json()

	

	want_zadacha_tag = random.randint(1,50)
	count_tag = 0

	for i in data['result']['problems']:
		dat1 = data['result']['problems'][count_tag]
		if count_tag == want_zadacha_tag:
			id = dat1['contestId']
			index = dat1['index']
			await message.answer(f"https://codeforces.com/problemset/problem/{id}/{index}")
			break
		count_tag+=1
	await state.finish()





# рейтинг користувача ----------------------------------------------------


class DataInput(StatesGroup):
	m = State()





@dp.message_handler(commands = ['rating'])

async def rating_user(message: types.Message):
	await message.answer('Введіть хендл користувача')
	await DataInput.m.set()

@dp.message_handler(state = DataInput.m)
async def give_rating_user(message: types.Message, state: FSMContext):
	handle = message.text
	r = requests.get(
			f"https://codeforces.com/api/user.info?handles={handle}"
		)

	data = r.json()
	rating = data['result'][0]['rating']
	rank = data['result'][0]['rank']
	if rank == 'expert':
		rank = 'Експерт'
	if rank == 'newbie':
		rank = 'Новачок'
	await message.reply(f"Рейтинг користувача {handle} = {rating}\n"
						f"Ранг користувача {handle} = {rank}"
		)
	
	await state.finish()









@dp.message_handler(commands = ['contests'])

async def rating_user(message: types.Message):
	r = requests.get(
			f"https://codeforces.com/api/contest.list?gym=false"
		)

	data = r.json()
	count_contest = 0
	for i in data:
		name = data['result'][count_contest]['name']
		time_start = data['result'][count_contest]['startTimeSeconds']
		time_start = datetime.utcfromtimestamp(time_start).strftime('%Y-%m-%d %H:%M:%S')
		await message.answer(f"{name}, початок {time_start} ")
		count_contest += 1
	

















@dp.message_handler(commands = ['tags'])

async def echo(message: types.Message):
	await message.answer(f"2-sat\n"
						 f"binary search  - Бінарний пошук \n"
						 f"bitmasks - Бітмаски \n"
						 f"brute force\n"
						 f"dp - Динамічне прогруммування \n"
						 f"constructive algorithms  - Конструктиви \n"
						 f"chinese remainder theorem - Китайська теорема про остачі \n"
						 f"data structures\n"
						 f"dfs and similar\n"
						 f"dsu - \n"
						 f"expression parsing\n"
						 f"fft\n"
						 f"flows\n"
						 f"games\n"
						 f"geometry - Геометрія \n"
						 f"graphs - Графи \n"
						 f"strings - Строки \n"



		)
















def func1(tag):
	r = requests.get(
			f"https://codeforces.com/api/problemset.problems?tags={tag}"
		)

	data = r.json()
	for i in data['result']['problems']:
		dat1 = data['result']['problems'][0]
		pprint(dat1['tags'])









if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)



