from flask import Flask, request
import similarity
import traceback
app = Flask(__name__)


@app.route('/check',methods = ['POST'])
def result():
   if request.method == 'POST':
      try:
         result = None
         if request.json is not None:
            result = request.json.get('text', None)
         if result is None and request.form is not None:
            result = request.form.get('text', None)
         if result is None:
            return {'message':"text not sent"}, 400
         report_json  = similarity.report(str(result))
         response = {
            'text': result,
            'data': report_json
         }
         return response, 200
      except Exception as e:
         return {'message':traceback.format_exc()}, 500

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)
