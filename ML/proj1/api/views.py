from flask import Blueprint , jsonify ,request
from . import db
from .model import pred_data
import pickle
import numpy as np
main = Blueprint('main', __name__)

mdl = pickle.load(open(r'C:\Users\dwive\Documents\ML\proj1\api\Pr_mdl.sav','rb'))



@main.route('/predict1',methods=['POST','GET'] )
def predict_disease():

    data = request.get_json(force=True)
   # console.log(data)
    data = [ x for x in data.values()]
    dt1 = np.array(data[:-3])
    dt2 = np.array(data[-3:])
    pd = mdl.predict(dt1)
    new_value = pred_data(name=dt2[0],gender=dt2[1],age=dt2[2],value=pd[0])
    db.session.add(new_value)
    db.session.commit()
    
    return jsonify({"value":pd[0]})

@main.route('/retrieve',methods=['POST','GET'] )
def predict_disease1():
    data1 = request.get_json(force=True)
    data1 = [ x for x in data1.values()]
    dis_list = pred_data.query.filter_by(name='tanush').all()
    ret_list = []
    for y in dis_list:
        ret_list.append({"value":(y.value)})
    return jsonify(ret_list)


    
  #  pd = Pred_data(city=data['city'],Temp=data['Temp'],Hum=data['Hum'],Prp=data['Prp'],Ws=data['Ws']) 
  #  jsonify({'value' : int(pd)})
    
    
      
