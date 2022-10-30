# text-mining

Please read the [instructions](instructions.md).

### Project Overview 

I used a Wikipedia page ***"Five-year plans of China"***. Primarily I exercised *list/dictionaries/tuples* functions to process the text, used *NLTK* module to analyze it, and used *Pandas* & *Matplotlib* to draw the histogram. In particular, this text of my choice contains different sections in the order of time period, which makes it an excellent learning material for list/dictionary/tuple exercises. The nature of the text also makes it interesting to learn content-wise. For exmaple, I could learn how the Five-Year plans of China have evolved overtime and the period characteristics of the country's development. Therefore, I hoped to learn about the historic aspect of China's five-year plans and how China has changed its goal overtime. 

### Implementation

Because Wikipedia intoduces the content by numbered plans, the text is first broken down the text into sections and packed into a dictionary (including nested dictionaries) then polished to eliminate any unnecessary components. Because the text content is time sensitive, I created a function that prints out a *China Plan calendar*. Then I mainly used *NLTK* to conduct the text analysis. Text is further simplized and packed into lists or dictionaries of frequencies for further convenient use. For *get_hist()*, I frist used the original words but changed to using simplified words in order to narrow down the words. 

For the **word frequency** part, I wanted to show the word frequencies using a visual histogram. At first, I was deciding whether to base this *draw_freqency_dstr()* function on *simply_words() or get_hist(), or rank_most_common()*. Becasue I was learning NLTK at the moment, I fist chose to use a whole text which can easly done by NLTK. However, I found that logically it is better to base the histogram on *rank_most_common()* -- it feels more natural to show a plot along with the list of words that appear the most. The histogram below shows the top 20 meaningful words that appear the most throughout the whole text. (I also drew the histogram for early plans and later plans in the testing code.) 
![image](https://user-images.githubusercontent.com/112499907/198900435-dcbcab8e-0170-438a-997c-9aa7e14c0844.png)
The figure below is a word frequency histogram for later plans. 
![image](https://user-images.githubusercontent.com/112499907/198901029-3891b550-b093-4037-bcad-b301cb4c91f3.png)


After testing the overall word frequency, I decided to test how this frequency changes throughout the text (across different plan periods) using the **stemmed words analysis** and **dispersion plot**. At last, I added a **sentiment analysis** and a **similiarity analysis** for fun. 
For the **word frequency** part, I wanted to show the word frequencies using a visual histogram. At first, I was deciding whether to base this *draw_freqency_dstr()* function on *simply_words() or get_hist(), or rank_most_common()*. Becasue I was learning NLTK at the moment, I fist chose to use a whole text which can easly done by NLTK. However, I found that logically it is better to base the histogram on *rank_most_common()* -- it feels more natural to show a plot along with the list of words that appear the most. After testing the overall word frequency, I decided to test how this frequency changes throughout the text (across different plan periods) using the **stemmed words analysis** and **dispersion plot**. At last, I added a **sentiment analysis** and a **similiarity analysis** for fun. 


### Results 

#### Sentiment Analysis & Plan Calendar 
First, from the **sentiment analysis**, I found that the overall sentiment is very neutral. Early, mid, or later plans all got the similar results. Later plans score the highest in nuetrality, while the early plans are highest in both extremes (neg and pos). Second, by listing out the plans and the year periods side by side, it is easy to notice that there is no Fourth Plan. It is reasonable to speculate that this may has to do with avoidance of using number four in the Chinese culture. 

#### Stemmed Words Analysis 
Then I compared stemmed words to narrow down the word collection in order to better get an idea of what meanings are expressed across three different stages (early, mid, and late). By comparing early plans and later plans, I found that words like "environment", "ecosystem", "conserve", "carbon", "pollution", "Taiwan", "southwest", and "nuclear" only appear in the later plans, which suggests the country's near goals are shifting towards clean energy and environmental sustainability. Taiwan issue, nuclear energy development, as well as extensive development in the southwest are more of issues in the recent years. In contrast, words like "market", "industry", "reform", "economy", "communist", "manufacture", "highway", and "transport" appear in both periods, indicating those concepts have been long-term embedded in the national devlopment strategies.

#### Dispersion Plot 
![image](https://user-images.githubusercontent.com/112499907/198900393-8c1c8d5e-4575-4517-ac82-05b31124e6a2.png)

Simliarly, I made a **dispersion plot** using NLTK to test some iconic words in text. The dispersion plot shows where each word appear in the text. This is particularly applicable to this text because this text introduces the plans by time period. Words like "ecosystems", "environment", and "carbon" appear later in the text as expected from the stemmed words comparison. "Technology" is mentioned throughout the text, indicating technology has been a core in the national devlopment goals. Same with "infrastructure". However, words like "agriculture" and "industrial" are frequently mention in the early-mid period but less frequently brought up in the later plans. This pattern is especially notable for "agriculture", which only appears once post mid-plans. This suggests the industrial shift from agriculture to third-tier indurtries like "healthcare", which only appear in the later plans. 


### Reflection

Extracting the text and learning about the **NLTK module** was an interesting process. I would improve the integrity of different functions. For example, I am still exploring what I can do with the **SOP tree** (which got deleted after realizing it does not add value to my overall anslysis). I think I structured the testing plan fairly well that each plan is defined and divided into three groups (early, mid, and later), which makes testing easier. I wished I could learn thoroughly about different function I could use for text analysis and plan my function accordingly. Because I explored different functions along the way, I created many functons that I tought was not very relevent to the the text itself. For example, I created functions that count total different words and an SOP analysis using NLTK tagging, which I later realized the number of different words or the SOP tree does not add any meaning to the my interpretation of the text. Therefore, I deleted a lot of functions--even some complex ones. 
