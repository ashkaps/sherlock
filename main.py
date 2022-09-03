import similarity
import traceback
import json

def check(text):
   '''
   The function checks for plagiarism in a text across web
   
   Parameters:
   - text (string) : value to search for plagiarism
   '''
   try:
      if text is None:
         return json.dumps({'message':"text not sent", 'code':400})
      report_json  = similarity.report(str(text))
      response = {
         'text': text,
         'data': report_json,
         'code':200
      }
      return json.dumps(response)
   except Exception as e:
      return json.dumps({'message':traceback.format_exc(), 'code':500})
