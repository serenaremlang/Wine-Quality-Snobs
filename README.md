# Wine-Quality-Snobs
Building a wine classifier for wine makers to help plan physiochemical changes in wine making process.

Classification problem: [archive.ics.uci.edu/ml/datasets/wine+quality](https://archive.ics.uci.edu/ml/datasets/wine+quality)

* classification model for red one for white and try a combo (to show improved accuracy)
* supervised learning problem - have the labels




Front End
- Live plot
- Sliders to pick feature values to give wine quality prediction



Two things from list:

* Using CSS/HTML/bootstrap
* Pandas
* Plotly?



Can we find the perfect wine?



Data: [www3.dsi.uminho.pt/pcortez/wine/](http://www3.dsi.uminho.pt/pcortez/wine/)



Input variables (based on physicochemical tests): 
1 - fixed acidity
2 - volatile acidity  
3 - citric acid  
4 - residual sugar  
5 - chlorides  
6 - free sulfur dioxide  
7 - total sulfur dioxide  
8 - density  
9 - pH  
10 - sulphates  
11 - alcohol  
Output variable (based on sensory data):  
12 - quality (score between 0 and 10)


### To do:

* get list of known wine with physiochemical scores to populate the sliders and show quality scores
* Front end
	* mock up
	* sliders
	* Consumer page - simple
	* Wine maker page
	* Data page
		* basic plot of data - descriiptive stats
* build basic supervised baseline model
* build Neural Net
* Optimize and hypertune
* Link model to website (Flask? Heroku?)



How to host it?

* Flask?
* Heroku?
