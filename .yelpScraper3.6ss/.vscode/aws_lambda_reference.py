import json

# event is a Dictionary containing
def lambda_handler(event, context):
    testDict = { "TEST": {"event": {},"demo": {}}}
    print('\n'*5)
    print("* "*60)
    print(type(event))
    print(event['queryStringParameters']["url"])
    print(type(event['queryStringParameters']['url']))
    # print(event)
    print("* "*60)
    print('\n'*5)
    
    return {
        'statusCode': 200,
        'body': json.dumps({'Test': event['queryStringParameters']['url']})
        # 'body': json.dumps('Hello From Lambda': {"event": {event}}),
    }
