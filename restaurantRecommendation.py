import json
import csv
import linecache
import numpy as np
import random
import math
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import cross_validation
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA as sklearnPCA
import scipy

# This part of code creates a csv file consisting of 
# restaurant level features. It also prunes out 
# businesses that are not based on restaurants.
# Some features are described in the attributes
# of one business but are left out in others
# such attributes are initialized to zero.
# Categories are chosen based on WHich categories
# repeat the most number of times in the dataset.
data = []
tempArray = [] #Temporary array to read a line of data
with open('business.json') as infile:
	outfile = open("restaurants.csv","w")
	for line in infile:
		tempArray.append(json.loads(line))
		if "Restaurants" in tempArray[0]['categories'] :# Read business only if it is a restaurant
			data.append(json.loads(line))
			if 'Accepts Credit Cards' in data[0]['attributes'] :
				card = data[0]['attributes']['Accepts Credit Cards'] 	
			else : 
				card = 0
			if 'Has TV' in data[0]['attributes'] :
				ht = data[0]['attributes']['Has TV'] 	
			else : 
				ht = 0
			if 'Outdoor Seating' in data[0]['attributes'] :
				os = data[0]['attributes']['Outdoor Seating'] 	
			else : 
				os = 0
			if 'Delivery' in data[0]['attributes'] :
				deliv = data[0]['attributes']['Delivery'] 	
			else : 
				deliv = 0
			if 'Good For Groups' in data[0]['attributes'] :
				gg = data[0]['attributes']['Good For Groups'] 	
			else : 
				gg = 0
			if 'Smoking' in data[0]['attributes'] :
				if (data[0]['attributes']['Smoking']=="no") :
					smok = 0
				else:
					smok = 1	
			else : 
				smok = 0
			if 'Wi-Fi' in data[0]['attributes'] :
				if (data[0]['attributes']['Wi-Fi']=="no") :
					wifi = 0
				else:
					wifi = 1	
			else : 
				wifi = 0
			if 'Waiter Service' in data[0]['attributes'] :
				ws = data[0]['attributes']['Waiter Service'] 	
			else : 
				ws = 0
			if 'Alcohol' in data[0]['attributes'] :
				if (data[0]['attributes']['Alcohol']=="none") :
					al = 0
				else:
					al = 1	
			else : 
				al = 0
			if 'Noise Level' in data[0]['attributes'] :
				if (data[0]['attributes']['Noise Level']=="quiet") :
					nl = 0
				if (data[0]['attributes']['Noise Level']=="average") :
					nl = 1			
				else:
					nl = 2	
			else : 
				nl = 1
			if 'Price Range' in data[0]['attributes'] :
				price = data[0]['attributes']['Price Range']
			else : 
				price = 1
			if 'Good for Kids' in data[0]['attributes'] :
				gk = data[0]['attributes']['Good for Kids'] 	
			else : 
				gk = 0
			if 'Takes Reservations' in data[0]['attributes'] :
				tr = data[0]['attributes']['Takes Reservations'] 	
			else : 
				tr = 0
			if 'Take-out' in data[0]['attributes'] :
				to = data[0]['attributes']['Take-out'] 	
			else : 
				to = 0		
			if 'Good For' in data[0]['attributes'] :
				if 'lunch' in data[0]['attributes']['Good For'] :
					l = data[0]['attributes']['Good For']['lunch']
				else : 
					l = 0
				if 'dinner' in data[0]['attributes']['Good For'] :
					d = data[0]['attributes']['Good For']['dinner']
				else : 
					d = 0
				if 'brunch' in data[0]['attributes']['Good For'] :
					br = data[0]['attributes']['Good For']['brunch']
				else : 
					br = 0
				if 'breakfast' in data[0]['attributes']['Good For'] :
					brk = data[0]['attributes']['Good For']['breakfast']
				else : 
					brk = 0
				if 'latenight' in data[0]['attributes']['Good For'] :
					ln = data[0]['attributes']['Good For']['latenight']
				else : 
					ln = 0
				if 'dessert' in data[0]['attributes']['Good For'] :
					ds = data[0]['attributes']['Good For']['dessert']
				else : 
					ds = 0
			else : 
				l = 0
				d = 0
				br = 0
				brk = 0
				ln = 0
				ds = 0
			if 'Parking' in data[0]['attributes'] :
				if 'validated' in data[0]['attributes']['Parking'] :
					val = data[0]['attributes']['Parking']['validated']
				else : 
					val = 0
				if 'street' in data[0]['attributes']['Parking'] :
					stre = data[0]['attributes']['Parking']['street']
				else : 
					stre = 0
				if 'garage' in data[0]['attributes']['Parking'] :
					gar = data[0]['attributes']['Parking']['garage']
				else : 
					gar = 0
				if 'valet' in data[0]['attributes']['Parking'] :
					valet = data[0]['attributes']['Parking']['valet']
				else : 
					valet = 0
				if 'lot' in data[0]['attributes']['Parking'] :
					lot = data[0]['attributes']['Parking']['lot']
				else : 
					lot = 0
			else : 
				lot = 0
				valet = 0
				gar = 0
				stre = 0
				val = 0
			if 'Ambience' in data[0]['attributes'] :
				if 'touristy' in data[0]['attributes']['Ambience'] :
					tour = data[0]['attributes']['Ambience']['touristy']
				else : 
					tour = 0
				if 'classy' in data[0]['attributes']['Ambience'] :
					clas = data[0]['attributes']['Ambience']['classy']
				else : 
					clas = 0
				if 'casual' in data[0]['attributes']['Ambience'] :
					cas = data[0]['attributes']['Ambience']['casual']
				else : 
					cas = 0
				if 'upscale' in data[0]['attributes']['Ambience'] :
					ups = data[0]['attributes']['Ambience']['upscale']
				else : 
					ups = 0
				if 'divey' in data[0]['attributes']['Ambience'] :
					div = data[0]['attributes']['Ambience']['divey']
				else : 
					div = 0
				if 'romantic' in data[0]['attributes']['Ambience'] :
					rom = data[0]['attributes']['Ambience']['romantic']
				else : 
					rom = 0
				if 'hipster' in data[0]['attributes']['Ambience'] :
					hip = data[0]['attributes']['Ambience']['hipster']
				else : 
					hip = 0
				if 'trendy' in data[0]['attributes']['Ambience'] :
					trnd = data[0]['attributes']['Ambience']['trendy']
				else : 
					trnd = 0
				if 'intimate' in data[0]['attributes']['Ambience'] :
					intt = data[0]['attributes']['Ambience']['intimate']
				else : 
					intt = 0
			else : 
				intt = 0
				hip = 0
				trnd = 0
				rom = 0
				div = 0
				ups = 0
				cas = 0
				clas = 0
				tour = 0
			if 'Sports Bars' in data[0]['categories'] :
				sb = 1
			else:
				sb = 0
			if 'Steakhouses' in data[0]['categories'] :
				sth = 1
			else:
				sth = 0
			if 'Seafood' in data[0]['categories'] :
				sea = 1
			else:
				sea = 0	
			if 'Delis' in data[0]['categories'] :
				Del = 1
			else:
				Del = 0	
			if 'Chicken Wings' in data[0]['categories'] :
				cw = 1
			else:
				cw = 0
			if 'Sushi Bars' in data[0]['categories'] :
				sus = 1
			else:
				sus = 0	
			if 'Japanese' in data[0]['categories'] :
				jap = 1
			else:
				jap = 0
			if 'Cafes' in data[0]['categories'] :
				caf = 1
			else:
				caf = 0
			if 'Breakfast & Brunch' in data[0]['categories'] :
				bfb = 1
			else:
				bfb = 0	
			if 'American (New)' in data[0]['categories'] :
				amn = 1
			else:
				amn = 0
			if 'Chinese'  in data[0]['categories'] :
				chin = 1
			else:
				chin = 0
			if 'Burgers'  in data[0]['categories'] :
				burg = 1
			else:
				burg = 0			
			if 'Italian'  in data[0]['categories'] :
				itl = 1
			else:
				itl = 0
			if 'Food'  in data[0]['categories'] :
				foo = 1
			else:
				foo = 0
			if 'Sandwiches' in data[0]['categories'] :
				san = 1
			else:
				san = 0
			if 'American (Traditional)' in data[0]['categories'] :
				at = 1
			else:
				at = 0
			if 'Bars' in data[0]['categories'] :
				bar = 1
			else:
				bar = 0
			if 'Mexican' in data[0]['categories'] :
				mex = 1
			else:
				mex = 0
			if 'Nightlife' in data[0]['categories'] :
				ntl = 1
			else:
				ntl = 0
			if 'Pizza' in data[0]['categories'] :
				piz = 1
			else:
				piz = 0
			if 'Fast Food' in data[0]['categories'] :
				faf = 1
			else:
				faf = 0
			outfile.write("%s,%d,%f,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n"%(data[0]['business_id'],data[0]['review_count'],data[0]['stars'],card,ht,os,deliv,gg,smok,wifi,ws,al,nl,price,gk,tr,to,l,d,br,brk,ln,ds,lot,valet,gar,stre,val,intt,hip,trnd,rom,div,ups,cas,clas,tour,sb,sth,sea,Del,cw,sus,jap,caf,bfb,amn,chin,burg,itl,foo,san,at,bar,mex,ntl,piz,faf))
			data = []
		tempArray = []
outfile.close()


#code for randomly generating train and test data
x_temp=[]
y_temp=[]
#creating a random array of size 10000 each containing a value from 1 to 100000
random_data = random.sample(range(100000), 10000)
with open('Train.csv', 'w') as outfile: #getting train datta into Train.csv
	with open('Test.csv', 'w') as outfile1:#getting test datta into Test.csv
		train=csv.writer(outfile)
		test=csv.writer(outfile1)
		i=0
		for j in random_data:
			#read jth line
			line = linecache.getline('review.json', j)
			y_temp.append(json.loads(line))
			x_temp.append(y_temp[0]['user_id'])
			x_temp.append(y_temp[0]['business_id'])
			x_temp.append(y_temp[0]['stars'])
			y_temp=[]
			#taking first 6000 values as train data
			if i<6000:
				train.writerow(x_temp)
			# taking next 4000 values as test data
			elif i<10000:
				test.writerow(x_temp)
			else:
				break
			i=i+1
			x_temp=[]

#code for predicting 
top=36
bottom=58


# read restaurants data
restaurants=pd.read_csv('restaurants.csv',header=None)
Y=restaurants.values
#mapping restaurant to its attributes
res_data={}
for i in range(len(Y)):
	restaurant=Y[i][0]
	a=[]
	
	for j in range(1,len(Y[i])):
		a.append(Y[i][j])
	res_data[restaurant]=a



#Reading the train dataset 
traindata = pd.read_csv('Train.csv',header=0)

train_data = traindata.values

user_visit_count = {}
user_average_rating = {}

# This is used to find average rating and the number of times a user frequented
# different categories of restaurants (Sushi, American, Indian, etc)
for i in range(len(train_data)):
	user=train_data[i][0]
	res=train_data[i][1]
	# no of stars given by the user to restaurant 'res'
	review=train_data[i][2]
	if res in res_data:
		if user in user_visit_count: # Data on user already present
			for var in range(top,bottom): # Iterate over the types of restaurants
				if(res_data[res][var-top]==1): # If this restaurant has the feature
					# Increase visit count and update average rating
					user_visit_count[user][var-top]=user_visit_count[user][var-top]+1 
					user_average_rating[user][var-top]=user_average_rating[user][var-top]+review
		else:# New user, initialize data and update visit count
			user_array=[]
			for var in range(top,bottom):
				user_array.append(0)
			user_visit_count[user]=user_array
			user_average_rating[user]=user_array
			for var in range(top,bottom):
				if(res_data[res][var-top]==1):
					user_visit_count[user][var-top]=user_visit_count[user][var-top]+1
					user_average_rating[user][var-top]=user_average_rating[user][var-top]+review

# Find avrage rating given by the user to different kinds of restaurants
for key in user_visit_count:
	for var in range(top,bottom):
		if(user_visit_count[key][var-top]!=0):
			user_average_rating[key][var-top]=user_average_rating[key][var-top]/user_visit_count[key][var-top]

phi=[]
y=[]
testLen = 0
# Creating the final feature matrix
for i in range(len(train_data)):
	user=train_data[i][0]
	restaurant=train_data[i][1]
	review=train_data[i][2]
	a_temp=[]
	if restaurant in res_data:
		# Appending user level features
		for j in range(0,bottom-top):
			a_temp.append(user_average_rating[user][j])
		current_res=res_data[restaurant]
		# Appending resataurant level features
		for j in range(len(current_res)):
			a_temp.append(current_res[j])
		phi.append(a_temp)
		# If user review is >= 2.5 then reccomend the restaurant
		if(review>2):
			y.append(1)
		else:
			y.append(0)


# Standardize the featue matrix to make it a distribution with mean 0 and variance 1
phi_std = StandardScaler().fit_transform(phi)

# Use PCA to select features which account for 98% of the variance
phi_pca = sklearnPCA(n_components=0.98)
# Fit the standardized feature matrix onto the eigen vectors
phi_sklearn = phi_pca.fit_transform(phi_std)

# Use logistic regression to train over the dataset
log=linear_model.LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1,
 class_weight='balanced', random_state=None, solver='liblinear', max_iter=400, multi_class='ovr', verbose=0).fit(phi_sklearn,y)






testData = pd.read_csv('Test.csv',header=0)

newphi=[] # Feature matrix for test data

Xnew = testData.values
for i in range(len(Xnew)):
	user=Xnew[i][0]
	restaurant=Xnew[i][1]
	a_temp=[]
	if restaurant in res_data:
		if user in user_average_rating: # If information regarding user is present based on train data
			# Appending user level features
			for j in range(0,bottom-top):
				a_temp.append(user_average_rating[user][j])
		else:
			# Initialize all user level features to 2.5
			for j in range(0,bottom-top):
				a_temp.append(2.5)
		current_res=res_data[restaurant]
		# Appending resataurant level features
		for j in range(len(current_res)):
			a_temp.append(current_res[j])
		newphi.append(a_temp)

# Standardize the featue matrix to make it a distribution with mean 0 and variance 1	
newphi_std = StandardScaler().fit_transform(newphi)

# Fit the standardized feature matrix onto the eigen vectors
newphi_sklearn=phi_pca.transform(newphi_std)

# Predict wether or not to reccomend the restaurant for new user
ans=log.predict(newphi_sklearn)


# Calculate error in the prediction
j=0
error=0
for i in range(len(Xnew)):
	restaurant=Xnew[i][1]
	if restaurant in res_data:
		if((Xnew[i][2]>2 and ans[j]==0) or (Xnew[i][2]<=2 and ans[j]==1)): # Made a wrong prediction
			error=error+1
		j=j+1
error = (error*100)/len(newphi)
error=np.round(error,decimals=2)
print("The prediction accuracy is:",100-error,"%")