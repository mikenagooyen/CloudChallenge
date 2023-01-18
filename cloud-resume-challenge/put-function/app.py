import json
import boto3
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def put_function(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cloud-resume-challenge')

    table.update_item(
        Key = {
            "ID" : "visitors"
        },
        UpdateExpression = "set visitors = if_not_exists(visitors, :init) + :inc",
        ExpressionAttributeValues = {
            ":inc" : 1,
            ":init": 0
        },
    )
    
    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origins": "*",
        },
        "statusCode": 200,
    }