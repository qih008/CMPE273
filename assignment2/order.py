import boto3
import json
import time
import datetime

dynamodb = boto3.resource('dynamodb')
menu_table = dynamodb.Table('Pizza_Menu')
order_table = dynamodb.Table('Pizza_Order')

def post_order(event):
  response = order_table.put_item(
      Item={
        "order_id": event['order_id'],
        "menu_id": event['menu_id'],
        "customer_name": event['customer_name'],
        "customer_email": event['customer_email'],
        "order_status": "processing",
        "order": {
            "selection": "none",
            "size": "none",
            "costs": "none",
            "order_time": "none"
        }
      }
  )

  response = menu_table.get_item(
      Key = {'menu_id' : event['menu_id']}
  )
  selection = response['Item']['selection']
  message = ""
  for i in range(len(selection)):
    message += str(i+1) + ". " + selection[i] + ", "

  return_str = "Hi " + event['customer_name'] + ", please choose one of these selection: " + message[:-2]

  return {"Message" : return_str}

def put_order(event):
  response = order_table.get_item(
      Key = {'order_id' : event['order_id']}
  )
  order = response['Item']

  response = menu_table.get_item(
      Key = {'menu_id' : order['menu_id']}
  )
  menu = response['Item']

  index = int(event['input']) - 1
  if order['order']['selection'] == "none":
    order['order']['selection'] = menu['selection'][index]
    order_table.put_item(Item = order)
    message = ""
    for i in range(len(menu['size'])):
      message += str(i+1) + ". " + menu['size'][i] + ", "

    return_str = "Which size do you want? " + message[:-2]

  else:
    order['order']['size'] = menu['size'][index]
    order['order']['costs'] = menu['price'][index]
    order['order']['order_time'] = datetime.datetime.now().strftime("%m-%d-%Y@%H:%M:%S")
    order_table.put_item(Item = order)
    return_str = "Your order costs $" + menu['price'][index] + ". We will email you when the order is ready. Thank you!"

  return {"Message" : return_str}


def get_order(event):
  response = order_table.get_item(
      Key = {'order_id' : event['order_id']}
  )

  item = response['Item']
  print "Get successfully"
  return item

def lambda_handler(event, context):
  if event['method'] == "POST":
    return post_order(event)
  elif event['method'] == "PUT":
    return put_order(event)
  elif event['method'] == "GET":
    return get_order(event)

  return "No method found"