# -*- coding: cp1252 -*-
import nltk
from nltk.tokenize import word_tokenize


def res():  
# Step 1 – Training data
 train = [
    ("Sensex, Nifty to open flat with negative bias","Negative"),
    ("Sensex plunges 4%","Negative"),
    ("Sensex crashes 4.5% over court battle","Negative"),
    ("Sensex plunges 7% after discontinuing Corex sale; Mcap erodes by Rs. 821 cr","Negative"),
    ("Sensex Bank dips by 1.44%, Moody's affirmed its rating","Negative"),
    (  "Sensex  slips 2%; plans to sell 13 residential properties","Negative"),
    ("Sensex slips below 7500 mark","Negative"),
    '''("Cairn India,ONGC and gail marginally higher","Positive"),
    ("SBI ends marginally up on BSE","Positive"),
    ("Modest MondayNifty ends above 7500 mark in choppy session","Positive"),
    ("Cupid zooms 10%","Positive"),
    ("Sun TV Network declares interim dividend; stock zooms 7%","Positive"),
    ("Daily Market Strategy Holding on! Sensex, Nifty to start upbeat","Positive"),
    ("Top 18 stocks in focus today: SBI, Tata Motors, SpiceJet","Positive"),
    ("Sensex, Nifty extend gains to 2nd week in a row","Positive"),
    ("Dividend delight! Bharat Forge, Welspun India others declare dividend","Positive"),
    ("Omaxe, Welspun India among 15 scrips that hit 52-week high","Positive"),
    ("Skipper soars after winning order from Power Grid","Positive"),
    ("Oil stocks end mixed; cabinet approves policy on hydrocarbon exploration","Positive"),
    ("Dalmia Bharat Sugar,Kellton Tech among 10 stocks that hit 52-week high","Positive"),
    ("Godrej Consumer acquires 39% additional stake in DGH Owned Style Industries; stock down","Positive"),
    ("Pipavav Defence rallies 11%","Positive"),
    ("Marsons gallops 10% on bagging EPC contract","Positive"),
    ("Va Tech Wabag gallops 7% on order win","Positive"),
    ("Mphasis rises 2.9%; BSE seeks clarification on Mint report","Positive"),
    ("VA Tech Wabag bags order worth Rs. 594 crore","Positive"),
    ("Strides Shasun to acquire 3 brands from Moberg Pharma for USD 10 Million","Positive"),
    ("HMT gallops 14.6%","Positive"),
    ("Daily Market Strategy - Another fine Friday start! Indices to open in green","Positive"),
    ("European indices gain as EU, UK reach deal in Brexit talks","Positive"),("Indian ADRs end higher on positive global cues","Positive"),("Nasdaq closes higher led by gains in tech shares","Positive"),("Major Asian indices inch higher","Positive"),("European indices rebound as profit booking wanes","Positive"),("Japan's Nikkei rebounds in the early trade","Positive"),("Dow Jones closes at record high","Positive"),("US Fed nominee comments and strong consumer data aid US indices to close at record highs","Positive"),("US Indices end higher; gold prices slip","Positive"),
    ("Indian ADRs end higher tracking strong US markets","Positive"),

    ("US benchmark Indices end lower","Negative"),
    ("US indices end off-lows; tax bill nears passage","Negative"),
    ("Asian markets subdued following tepid US close","Negative"),
    ("Most US indices end lower as FOMC indicates dovish stance","Negative"),
    ("Coal India crashes 7% despite hefty dividend; plans to buyback 5%","Negative"),
    ("Sasken gallops 20%; settles Protocol Stack IP dispute","Negative"),
    ("Falling low! Jammu & Kashmir Bank, Prestige Estates among 11 stocks that hit 52-week lows","Negative"),
    ("High value stocks tumble since January 2016","Negative"),
    ("Ramky Infrastructure, Sequent Scientific among 10 stocks that hit 52-week high","Negative"),
    ("Hot stocks: Reliance slumps 3%, Golden Tobacco gallops 11%","Negative"),
    ("Syndicate Bank ends flat; reports a Rs. 1000 crore scam","Negative"),
    ("Despite late recovery Metal stocks end in red; Vedanta dips 3%","Negative"),
    ("ICRA, Visagar Polytex among 15 scrips that hit 52-week low","Negative"),
    ("Mindtree slumps 9%; issues Q4 revenue warning","Negative"),
    ("Nifty slips below 7500 mark","Negative"),
    ("SBI releases Rs. 1465 crores to defence pensioners","Neutral"),
    ("Timing, rhyming and relative calm in the equity markets","Neutral"),
    ("Sebi bars wilful defaulters from raising public funds","Neutral"),
    ("Fine Friday finally! Nifty settles above 7500","Neutral"),
    ("JSPL tumbles 5%; Franklin Temp MF sells bonds","Negative"),
    ("Crompton Greaves accepted revised offer for sale of T&D assets","Neutral"),
    ("Why CONCOR is in the news today?","Neutral"),
    ("Yes Bank ends flat; appoints former CCI chairman Ashok Chawla","Neutral"),
    ("Sensex, Nifty end flat; BoB, SBI top Nifty losers","Neutral"),
    ("Thomas Cook signs strategic alliance with Western Union Business Solutions and DCB Bank","Neutral"),
    ("Asian indices end mixed; China Shanghai Composite slips","Neutral"),
    ("Asian indices mixed tracking weak cues from US markets","Neutral"),
    ("European Markets trade mixed on Thursday","Neutral"),
    ("Asian indices mixed ahead of key economic data","Neutral"),
    ("US shares end on a mixed note","Neutral"),
    ("Indian ADRs end on a mixed note on Friday","Neutral"),
    ("SpiceJet plunges 4%","Negative"),
    ("SpiceJet crashes 4.5% over court battle","Negative"),
    ("Pfizer plunges 7% after discontinuing Corex sale; Mcap erodes by Rs. 821 cr","Negative"),
    ("IDBI Bank dips by 1.44%, Moody's affirmed its rating","Negative"),
    (  "United Spirits slips 2%; plans to sell 13 residential properties","Negative"),
    ("Sensex, Nifty to open flat with negative bias","Negative"),
    ("Nifty hits 52 week high","Positive") ,
    ("Nifty hits 52 week low","Negative")'''
 ]
  
 # Step 2
 dictionary = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
  
 # Step 3
 t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in train]
  
 # Step 4 – the classifier is trained with sample data
 classifier = nltk.NaiveBayesClassifier.train(t)
  
 test_data = "Sensex"
 
 test_data_features = {word.lower(): (word in word_tokenize(test_data.lower())) for word in dictionary}
  
 result=(classifier.classify(test_data_features))
 return result
res()
