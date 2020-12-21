from botUser import BotUser
from discord import Webhook, RequestsWebhookAdapter
from const import BOT_USER_PATH
import asyncio
import os

def main():
  botUser = loadBotUser()
  asyncio.get_event_loop().run_until_complete(botUser.stream_account_activity())

def getNewBotUser():
  accountID = input("Enter your TDA Account ID: ")
  webhookURL = input("Enter your webhook url: ")
  apiKey = input("Enter your TDA API Key: ")
  webhook = Webhook.from_url(webhookURL, adapter=RequestsWebhookAdapter())
  botUser = BotUser(webhook, accountID, apiKey)
  saveBotUser(botUser)
  return botUser

def loadBotUser():
  if os.path.exists(BOT_USER_PATH):
    botUserFile = open(BOT_USER_PATH, 'r')
    info = botUserFile.read().split(',')
    webhook = Webhook.from_url(info[0], adapter=RequestsWebhookAdapter())
    botUser = BotUser(webhook, info[1], info[2])
    botUserFile.close()
  else:
    botUser = getNewBotUser()

  return botUser

def saveBotUser(botUser):
  os.makedirs(os.path.dirname(BOT_USER_PATH), exist_ok=True)
  botUserFile = open(BOT_USER_PATH, 'w+')
  botUserFile.write(botUser.webhook.url + ',' + botUser.accountID + ',' + botUser.apiKey + ',')
  botUserFile.close()
  return

if __name__ == "__main__":
  main()