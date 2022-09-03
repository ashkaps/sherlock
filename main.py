import similarity
import traceback

def check(text):
   '''
   '''
   try:
      if text is None:
         return {'message':"text not sent"}, 400
      report_json  = similarity.report(str(text))
      response = {
         'text': text,
         'data': report_json
      }
      return response, 200
   except Exception as e:
      return {'message':traceback.format_exc()}, 500
