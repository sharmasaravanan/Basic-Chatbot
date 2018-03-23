# -*- coding: utf-8 -*-
from flask import Flask, request, render_template,url_for, redirect
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from weather import Weather, Unit
from PyDictionary import PyDictionary
from datetime import date
import holidayapi
import wikipedia
import holidays
import pyjokes
import sys,os,time

app = Flask(__name__)
chatterbot = ChatBot("Iniya")
weather = Weather(unit=Unit.CELSIUS)
hapi = holidayapi.v1('da4e7a21-2b5e-42ad-9698-ee5721db8100')
dictionary=PyDictionary()

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'GET':
		return render_template('chat.html')
	elif request.method == 'POST':
                user=request.form['you']
                if user=="let's ask":
                        response="Yeah!!! shoot your question...."
                elif user.find('iniya')==0:
                        response=wikipedia.summary(user[5:], sentences=1,auto_suggest=True, redirect=True)
                elif user.find('weather')==0:
                        location = weather.lookup_by_location(user[11:])
                        condition = location.condition()
                        tem=(condition.temp()).encode('ascii','ignore')
                        response= tem+" Celcsius"
                elif user.find('define')==0:
                        c=dictionary.meaning(user[6:])
                        response=c['Noun'][0]
                elif user=="crack a joke":
                        response=pyjokes.get_joke()
                elif user.find("holidays")==0:
                        years=user[12:]
                        d=holidays.CA(years=int(years))
                        response="You have %d holidays in the year %d"%(len(d),int(years))
                else:
                        response = chatterbot.get_response(user)
                kwargs = {
                        'bot':response,
                }
                return render_template('chat.html', **kwargs)


if __name__ == '__main__':
    app.run()
