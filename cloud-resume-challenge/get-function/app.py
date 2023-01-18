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


def get_function(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cloud-resume-challenge')

    response = table.get_item(
        Key = {
            "ID" : "visitors"
        },
    )

    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Origins": "*",
        },
        "statusCode": 200,
        "body": json.dumps(response["Item"]["visitors"], indent=4, cls=DecimalEncoder),
    }
