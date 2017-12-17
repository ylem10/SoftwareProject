from __init__ import app
from flask import request, render_template
import NNpredicter
import getExcelData,json


@app.route('/dataAnalyze')
def dataAnalyze():
    filename = request.args.get("filename")
    input_data = getExcelData.getExcelData(filename)
    result = NNpredicter.predicter_interface(filename)
    for i in range(len(result[0])):
        if result[0][i] <= 0.84:
            input_data[i]['result'] = '差'
        elif result[0][i] <= 0.88:
            input_data[i]['result'] = '良'
        elif result[0][i] <= 0.92:
            input_data[i]['result'] = '较好'
        elif result[0][i] <= 0.96:
            input_data[i]['result'] = '好'
        else:
            input_data[i]['result'] = '优'
    return render_template('webpages/user/analyzeResult.html', result=result, input_data=input_data)
