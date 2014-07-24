# -*- coding: utf-8 -*-

# 英単語練習プログラムCSVファイル用 

import sys
import os
import random

def screenclear():
	if os.name == "nt": # Windows 
		os.system("CLS")
	else: # not Windows 
		os.system("clear")

def quest(questdata):
	global repeat
        problem = questdata.split(',')
        screenclear()
	print problem[0].decode("utf-8")
	answer = sys.stdin.readline()
	if answer.rstrip("\n") == problem[1]:
		print u"正解"
		raw_input("-- press Enter key --")
		return 1
	else:
		if answer.rstrip("\n") == "/quit":
			exit(0)
		print u"不正解"
		print problem[1]
		raw_input("-- press Enter key --")
		if (repeat == 'y'):
			quest(questdata)
		return 0

def fileread():
	global data
	filenamelist = []
	filename = " "
	datanum = 0
	while filename != "":
		print u"読み込むファイル名を入力してください"
		filename = raw_input(">")
		filenamelist.append(filename)
	filenamelist.remove('')
	for filename in filenamelist:
		try:
			readfile = open(filename, 'r')
		except IOError:
			print "Can't readfile. " + filename
			continue
		for readdata in readfile:
			data.append(readdata.rstrip('\n'))
			datanum += 1
		readfile.close()
		return datanum

if __name__ == '__main__':
	data = []
	quest.answer = u""
	datanum = fileread()
	while True:
		score = 0
		print u"0.順次モード 1.ランダムモード それ以外:終了"
		mode = raw_input(">")
                if mode == "0" or mode == "1":
			print u"間違えた時に問題を繰り返しますか?" 
			repeat = raw_input("(y/n)\n>")
                else:
			exit(0)
		if repeat == "reset":
			datanum = fileread()
			continue
		if (len(data) == 0):
			break
		if mode == "0":
		        print u"日本語で出題されるので英訳して答えてください"
		        raw_input("-- press Enter key --")
			for nowdata in data:
				score += quest(nowdata)
			screenclear()
			print u"\n結果"
			print "%d / %d\n" % (score, datanum)
		elif mode == "1":
			randdata = list(data)
			print u"問題数を入力してください\n0未満の値を入れるかファイルの英文の合計より大きい値を入れるとすべてです."
			numofquestion = input(">")
		        print u"日本語で出題されるので英訳して答えてください"
		        raw_input("-- press Enter key --")
			if numofquestion < 0 or numofquestion > datanum:
				numofquestion = datanum
			startquenum = numofquestion
			while numofquestion > 0:
				questn = random.randint(0, len(randdata) - 1)
				score += quest(randdata[questn])
				numofquestion -= 1
				randdata.pop(questn)
			screenclear()
			print u"\n結果"
			print "%d / %d\n" % (score, startquenum)
		else:
			break 
