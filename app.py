from flask import Flask, request, jsonify
import pickle
import pandas as pd
# import joblib


## Creating a Flask app
app = Flask(__name__)



@app.route ('/', methods = ['GET' , 'POST'])
def home():
    if(request.method == 'GET'):
        data = 'Hello World!'
        return jsonify ({'data':data})
    
    

@app.route('/predict/')
def price_predict():  
    
    model = pickle.load(open('model.pickle', 'rb'))

            
    Median_Family_Income = request.args.get('Median_Family_Income')   
    Number_Beds = request.args.get('Number_Beds')
    Number_Baths = request.args.get('Number_Baths')
    Population = request.args.get('Population')
    City_new = request.args.get('City_new')
    Pro_new = request.args.get('Pro_new') 
    Latitude = request.args.get('Latitude') 
    Longitude = request.args.get('Longitude') 
    
    
    test_df = pd.DataFrame({ 
        'City_new':[City_new], 'Number_Beds' :[Number_Beds],'Number_Baths':[Number_Baths],
        'Pro_new':[Pro_new],'Population':[Population],
        'Latitude':[Latitude],'Longitude':[Longitude],
        'Median_Family_Income' :[Median_Family_Income]
       
    })
    

    
    test_df1 = pd.DataFrame(data={ 
    'City_new':17, 'Number_Beds' :4,'Number_Baths':4,
    'Pro_new':1,'Population':90990,
    'Latitude':49.2167,'Longitude':-122.6000,
    'Median_Family_Income' :105000.0

}, index=[0])
    
    pred_price = model.predict(test_df1)
    
    return jsonify({'House Price' : str(pred_price)})

#    return jsonify({'key': City_new})
    
    
    
    


if __name__ == '__main__':
    app.run(debug=True, port=5000)