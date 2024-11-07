import json 

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        num1 = body.get("num1")
        num2 = body.get("num2")

        if num1 is None or num2 is None:
            return{
                "statusCode":400,
                "body":json.dumps({
                    "message":"please provide num1 and num2"
                })
            }
        
        result = num1 + num2

        return{
            "statusCode":200,
            "body":json.dumps({
                "result":result
            })
        }
    
    except Exception as e:
        return{
            "statusCode":500,
            "body":json.dumps({
                "message":str(e)
            })
        }
        
def subtraction_handler(event, context):
    try:
        body = json.loads(event["body"])
        num1 = body.get("num1")
        num2 = body.get("num2")

        if num1 is None or num2 is None:
            return {
                "statusCode":400,
                "body":json.dumps({
                    "message":"please provide numbers"
                })
            }

        result = num1 - num2

        return {
            "statusCode":200,
            "body": json.dumps({
                "result": result
            })
        }
    
    except Exception as e:
        return{
            "statusCode":500,
            "body": json.dumps({
                "message":str(e)
            })
        }

