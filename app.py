from methods import *


app = Flask(__name__)

# load the trained machine learning model
model = pickle.load(open("RML2016.10a_dict.pkl",'rb'), encoding="latin1")

@app.route('/', methods=['GET'])
def predict():
    # get the input data from the request
    # data = request.get_json(force=True)
    x_data = load_dataset(model)
    partition_data()
    

    # transform the input data into a numpy array
    # predict_input = [np.array(list(data.values()))]
    
    # make the prediction
    # prediction = model.predict(predict_input)
    
    # return the prediction as a JSON response
    # output = {'prediction': int(prediction[0])}
    return jsonify(x_data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)