#!/bin/evn python
# -*-coding:utf8-*-
import pyttsx
engine = pyttsx.init()
# engine.say('Sally sells seashells by the seashore.')
# engine.say('The quick brown fox jumped over the lazy dog.')
#text = u'你好'
text = '你好'
print text
text = text.decode('utf8')
engine.say(text)
engine.runAndWait()
print 'aa'
print text

