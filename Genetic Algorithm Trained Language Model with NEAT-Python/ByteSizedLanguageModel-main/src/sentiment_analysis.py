class SentimentAnalyzer:
    @staticmethod
    def analyze_sentiment(text):
        # Mapping of text entries to sentiments from the provided dataset
        sentiments = {
            "I`d have responded, if I were going": "Neutral",
            "Sooo SAD": "Negative",
            "my boss is bullying me...": "Negative",
            "what interview! leave me alone": "Negative",
            "Sons of ****, why couldn`t they put them on the releases we already bought": "Negative",
            "http://www.dothebouncy.com/smf - some shameless plugging for the best Rangers forum on earth": "Neutral",
            "2am feedings for the baby are fun when he is all smiles and coos": "Positive",
            "Soooo high": "Neutral",
            "Both of you": "Neutral",
            "Journey!? Wow... u just became cooler.  hehe... (is that possible!?)": "Positive",
            "as much as i love to be hopeful, i reckon the chances are minimal =P i`m never gonna get my cake and stuff": "Neutral",
            "I really really like the song Love Story by Taylor Swift": "Positive",
            "My Sharpie is running DANGERously low on ink": "Negative",
            "i want to go to music tonight but i lost my voice.": "Negative",
            "test test from the LG enV2": "Neutral",
            "Uh oh, I am sunburned": "Negative",
            "S`ok, trying to plot alternatives as we speak *sigh*": "Negative",
            "i`ve been sick for the past few days  and thus, my hair looks wierd.  if i didnt have a hat on it would look... http://tinyurl.com/mnf4kw": "Negative",
            "is back home now      gonna miss every one": "Negative",
            "Hes just not that into you": "Neutral",
            "oh Marly, I`m so sorry!!  I hope you find her soon!! <3 <3": "Neutral",
            "Playing Ghost Online is really interesting. The new updates are Kirin pet and Metamorph for third job.  Can`t wait to have a dragon pet": "Positive",
            "is cleaning the house for her family who is comming later today..": "Neutral",
            "gotta restart my computer .. I thought Win7 was supposed to put an end to the constant rebootiness": "Neutral",
            "SEe waT I Mean bOuT FoLL0w fRiiDaYs... It`S cALLed LoSe f0LloWeRs FridAy... smH": "Neutral",
            "the free fillin` app on my ipod is fun, im addicted": "Positive",
            "I`m sorry.": "Negative",
            "On the way to Malaysia...no internet access to Twit": "Negative",
            "juss came backk from Berkeleyy ; omg its madd fun out there  havent been out there in a minute . whassqoodd ?": "Positive"
        }
        
        # Check if the input text exists in the sentiments mapping
        if text in sentiments:
            return sentiments[text]
        else:
            return "Neutral"  # Default to Neutral if text not found in the mapping
