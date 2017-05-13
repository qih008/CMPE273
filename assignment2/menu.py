import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Pizza_Menu')

def get_menu(event):
  response = table.get_item(
      Key = {'menu_id' : event['menu_id']}
  )

  item = response['Item']
  print "Get successfully"
  return item

def delete_menu(event):
  response = table.delete_item(
      Key = {'menu_id' : event['menu_id']}
  )
  print "Delete successfully"
  return "200 OK"

def put_menu(event):
  response = table.update_item(
      Key = {'menu_id' : event['menu_id']},
      UpdateExpression = "set selection = :s",
      ExpressionAttributeValues = {
          ':s' : event['selection']
      },
      ReturnValues = "UPDATED_NEW"
  )
  print "Put successfully"
  return "200 OK"


def lambda_handler(event, context):
  if event['method'] == "GET":
    return get_menu(event)
  elif event['method'] == "DELETE":
    return delete_menu(event)
  elif event['method'] == "PUT":
    return put_menu(event)

  return "No method found"