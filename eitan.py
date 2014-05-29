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
			print u"正解"
			return 1
		else:
			print u"不正解"
			print questr
			return 0

if __name__ == '__main__':
	score = 0
	state = 0
	filenamelist = []
	data = []
	datanum = 0
	quest.answer = u""
	while True:
		print u"読み込むファイル名を入力してください"
		infilename = raw_input(">")
		filenamelist.append(infilename)
		if infilename == "":
			break
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
		print u"0.順次モード 1.ランダムモード それ以外:終了"
		mode = input(">")
		if mode == 0:
			print u"日本語で出題されるので英訳して答えてください"

			for nowdata in data:
				score += quest(nowdata, state)
				state = (state + 1) % 2
			string = '\n結果'
			print string.decode('utf-8')
			print "%d / %d\n" % (score, datanum / 2)
		elif mode == 1:
			print u"問題数を入力してください\n0未満の値を入れるかファイルの英文の合計より大きい値を入れるとすべてです."
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
			print u"\n結果"
			print "%d / %d\n" % (score, startquenum)
		else:
			break 
