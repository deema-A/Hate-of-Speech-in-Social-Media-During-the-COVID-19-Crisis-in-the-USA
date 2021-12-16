#!/bin/bash
pwd


for i in {1..9}
do
#  echo "Welcome $i times"
  fname="2020-09-0"${i}
  dfname="covidsep"
  cp '/Users/matthew/Documents/GitHub/covid19_twitter/dailies/'${fname}'/'${fname}'_top1000bigrams.csv'  "/Users/matthew/PycharmProjects/pythonProject4/${dfname}"
  cp '/Users/matthew/Documents/GitHub/covid19_twitter/dailies/'${fname}'/'${fname}'_top1000trigrams.csv'  "/Users/matthew/PycharmProjects/pythonProject4/${dfname}"
done

for i in {10..30}
do
#  echo "Welcome $i times"
  fname="2020-09-"${i}
  dfname="covidsep"
  cp '/Users/matthew/Documents/GitHub/covid19_twitter/dailies/'${fname}'/'${fname}'_top1000bigrams.csv'  "/Users/matthew/PycharmProjects/pythonProject4/${dfname}"
  cp '/Users/matthew/Documents/GitHub/covid19_twitter/dailies/'${fname}'/'${fname}'_top1000trigrams.csv'  "/Users/matthew/PycharmProjects/pythonProject4/${dfname}"
done

cd
