import json


# This function will be deployed so that
# it can be invoked as an AWS Lambda function.
def lambda_handler(event, context):
	number = event["number"]
	squared = number ** 2

	response_body = {
		"message": "Success",
		"data": f"The square of {number} is {squared}."
	}

	response = {
		"isBase64Encoded": False,
		"statusCode": 200,
		"headers": {
			"Content-Type": "application/json"
		},
		"body": json.dumps(response_body)
	}

	return response
