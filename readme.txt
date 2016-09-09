217_n_grams.txt: the 217 features of the data set after processing the Twitter data.

Data_process: file folder that contains java code which are used to process data
	DayToWeek.java: used to convert the number of date to real date time, and then change the date time into week+year format
	location_week.java: pick up all data that related to target location
	CountMR.java: Mapreduce to process the data, it return as week,year  total number of this date; feature:number of tweets related to this feature
	Normalization.java: normalize the output of CountMR by dividing the number of tweets contains each feature with the total number of tweets in this week.

Models: filed folder that contains python code which are used to build model and test the results
	ElasticNet.py: implement of elastic net regression model and test the performance of this model
	RidgeRegression.py: implement of ridge regression model and test the performance of this model
	LassoRegression.py: implement of lasso regression model and test the performance of this model
	MergeFile2.py: get the supersets of control areas, there are 551 control areas including all individual and supersets
	pearson_correlation_most.py: find the most correlated control are from the 551 candidates for target pilot area
	elastic_net_predict.py: use elastic net model to get the estimated ILI rates for chosen control area and target pilot area
	plot_linear_relationship.py: build a linear regression model for ILI rates in control area and pilot area prior vaccination campaign and projected ILI rates in pilot area during and after vaccination period.
	3_moving_average.py: get the result of 3 moving average of projected ILI rates and estimated ILI rate in vaccination area during and after the vaccination period.
	absolute_diff_relative_diff.py: two metrics to test the difference between projected ILI rates and estimated ILI rate. T-test to get the p-value of two ILI rates. 


