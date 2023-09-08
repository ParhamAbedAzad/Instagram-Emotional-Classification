# Instagram-Emotional-Classification
Sentiment analysis has been a very important part of Natural language processing for the past decade, Although standard sentiment analysis is usually just between positive and negative, this project is intended to take this analysis one step further, and instead of extracting a yes or no, extract the exact emotions embedded in each text, and map each comment to a specific human emotion.
Moreover, we created a dataset of individual posts which you can use by cloning the project.
To achieve this goal, we first classify human emotions and divide them into a number of separate classes; the presence or absence of these emotions will be the optimal output of this system. Now the comments are taken from Instagram API and stored in a file, Then by designing a lexical system, we label some of these comments with different emotional classes according to their words.
![image](https://github.com/ParhamAbedAzad/Instagram-Emotional-Classification/assets/48606670/eba469cd-83b1-431c-8b53-5cb47a119a7f)

We do this in the Auto-labeler where we separate tweets that contain an emoji and label them automatically
![image](https://github.com/ParhamAbedAzad/Instagram-Emotional-Classification/assets/48606670/db0701e9-e2e0-4c36-906c-eb6866542a60)

Consequently, with the help of machine learning algorithms, we can train a general multi-label machine that can produce an output that consists of an eight-part vector. Thus, each part represents the presence of a separate emotion.
Thereafter, we will feed all of the comments of each post to the model and calculate the average of the outputs for each emotion. Hence, the resultant values can represent the number of emotions toward the posts, concluding the emotions surrounding individuals, companies, or even hashtags on Instagram. The results are visible in the figure below.
![image](https://github.com/ParhamAbedAzad/Instagram-Emotional-Classification/assets/48606670/9106b264-22b1-423e-98d7-1d46953b76a7)

At the end, we will run this model on two different persons. First of which, is an Instagram influencer which everyone loves. On the other hand the second person, a political figure who is in an unfavorable situation due to the COVID-19 pandemic and extreme economic challenges.

The final results align with our expectations as we can see in the figure below 
![image](https://github.com/ParhamAbedAzad/Instagram-Emotional-Classification/assets/48606670/2fa68ab8-ff60-46a4-a6ac-177f2e1e185b)
