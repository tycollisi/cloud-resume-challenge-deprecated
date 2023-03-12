import json

# import requests


def lambda_handler(event, context):
    # Get the HTTP method of the request
    http_method = event['httpMethod']

    # Define the headers to allow cross-origin requests
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, HEAD, POST, PUT, DELETE',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    # Handle CORS preflight request
    if http_method == 'OPTIONS':
        response = {
            'statusCode': 200,
            'headers': headers
        }
        return response

    # Handle regular request
    elif http_method == 'GET':
        # Your GET request handling logic here
        response_body = {
            'message': 'Hello, world!'
        }
        response = {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(response_body)
        }
        return response

    # Add handling for other HTTP methods as needed
