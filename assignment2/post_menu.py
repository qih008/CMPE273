import boto3
import json

def lambda_handler(event, context):

  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('Pizza_Menu')
  #print table.name

  response = table.put_item(
      Item={
        "menu_id": event['menu_id'],
        "store_name": event['store_name'],
        "selection": event['selection'],
        "size": event['size'],
        "price": event['price'],
        "store_hours": event['store_hours']
      }
  )

  print "Post Successfully"
  print json.dumps(response, indent=4)
  return "200 OK"