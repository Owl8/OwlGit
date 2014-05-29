# -*- coding: utf-8 -*-

import sys
import random

def quest(questr, state):
	if state == 0:
		print "\n" + questr.decode('Shift_JIS')
		quest.answer = sys.stdin.readline()
		return 0
	else:
		if quest.answer.rstrip("\n") == questr:
			string = "正解"
			print string.decode('utf-8')
			return 1
		else:
			string = "不正解"
			print string.decode('utf-8')
			print questr
			return 0

if __name__ == '__main__':
	score = 0
	state = 0
	infilename = "a"
	filenamelist = []
	data = []
	datanum = 0
	quest.answer = ""
	while infilename != "":
		string = "読み込むファイル名を入力してください"
		print string.decode('utf-8')
		infilename = raw_input(">")
		filenamelist.append(infilename)
	filenamelist.remove('')

	for filename in filenamelist:
		readfile = open(filename, 'r')
		for readdata in readfile:
			data.append(readdata.rstrip('\n'))
			datanum += 1
		readfile.close()
	while True:
		state = 0
		score = 0
		string = "0.順次モード 1.ランダムモード それ以外:終了"
		print string.decode('utf-8')
		mode = input(">")
		if mode == 0:
			string = "日本語で出題されるので英訳して答えてください"
			print string.decode('utf-8')

			for nowdata in data:
				score += quest(nowdata, state)
				state = (state + 1) % 2
			string = '\n結果'
			print string.decode('utf-8')
			print "%d / %d\n" % (score, datanum / 2)
		elif mode == 1:
			string = "問題数を入力してください\n0未満の値を入れるかファイルの英文の合計より大きい値を入れるとすべてです."
			print string.decode('utf-8')
			question = input(">")
			if question < 0 or question > datanum:
				question = datanum
			startquenum = question
			while question > 0:
				if state == 0:
					questn = 2 * random.randint(0, question / 2)
				score += quest(data[questn], state)
				questn += 1
				if state == 1:
					question -= 1
					data.pop(questn - 1)
					data.pop(questn - 2)
				state = (state + 1) % 2
			string = "\n結果"
			print string.decode('utf-8')
			print "%d / %d\n" % (score, startquenum)
		else:
			break 
