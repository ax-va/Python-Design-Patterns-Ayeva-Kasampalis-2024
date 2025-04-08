import json


# This function will be deployed so that
# it can be invoked as an AWS Lambda function.
def lambda_handler(event, context):
    try:
        # Distinguish between URL call and direct call
        body = json.loads(event.get("body", "{}")) if "body" in event else event

        number = body.get("number")
        if number is None:
            return {
                "statusCode": 400,
                "body": json.dumps(
                    {
                        "error": "Missing 'number' in request body",
                        "event": event,
                        "type(event)": str(type(event)),
                        "body": body
                    }
                )
            }

        result = number * number

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "result": result,
                    "event": event,
                    "type(event)": str(type(event)),
                    "body": body
                }
            )
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(
                {
                    "error": str(e),
                    "event": event,
                    "type(event)": str(type(event))
                }
            )
        }
