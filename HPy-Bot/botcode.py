import discord
import random as rnd
from bs4 import BeautifulSoup
import requests
from discord.ext import commands
from datetime import date,datetime
import calendar
import random
import os
import sys
t = open("TOKEN.txt", "r").read()

client = discord.Client()
client = commands.Bot(command_prefix= 'h!')

magicwords = ["It is certain.", "For sure.", "Without a doubt.", "Most likely.", "Signs point to yes.", "Ask again later.", "Better not tell you now.", " Cannot predict now.",  "Nope, ain't gonna happen", "Haha, that's funny", "No way", "Maybe"]


@client.event
async def on_ready():
    print('Bot is currently online')
    await client.change_presence(activity=discord.Game(name="h!helpme"))

@client.event
async def member_join(member):
    print(f'{member} has joined the server.')

@client.event 
async def member_leave(member):
    print(f'{member} has left the server')


# client command lines
@client.command()
# async def [command name] - type in prefix then command 
async def magic8ball(context, userarg):
    await context.send(rnd.choice(magicwords))



@client.command()
async def currTime(context):
    now = datetime.now()
    currentDay = date.today()
    currDate = currentDay.strftime("Today is %B %d, %Y")
    time_and_day = now.strftime("Time : %H:%M:%S")

    await context.send(currDate)
    await context.send(time_and_day)


@client.command()
async def diceroll(context, user:discord.Member):
    diceval_user = random.randrange(1,6,1)
    diceval_opponent = random.randrange(1,6,1)
    if(int(diceval_user)> int(diceval_opponent)):
        await context.send(f'You rolled {diceval_user} and opponent rolled {diceval_opponent}, they win')
    elif(int(diceval_user) == int(diceval_opponent)):
        await context.send(f'You rolled {diceval_user} and opponent rolled {diceval_opponent}, you have tied')
    else:
         await context.send(f'You rolled {diceval_user} and opponent rolled {diceval_opponent}, you win')




#Turn to embed menu
@client.command()
async def helpme(context):
    embed = discord.Embed(title = "Help Guide" , description = "List of commands")
    embed.add_field(name = "h!magic8ball", value = "Sends a random response to a question")
    embed.add_field(name = "h!gm", value = "Wish users good morning")
    embed.add_field(name = "h!gn", value = "Wish users good night") 
    embed.add_field(name = "h!bingme", value="Returns top 3 searches from bing [In Progress]")
    embed.add_field(name = "h!delmsg", value = "Deletes a set number of messages [Admin Only]") 
    embed.add_field(name = "h!getboing", value = "Pings User [Admin Only]") 
    embed.add_field(name = "h!currTime", value = "gives current time") 
    embed.add_field(name = "h!isFriday", value = "is it friday") 
    embed.add_field(name = "h!ipermInv", value = "gets a perm invite to server") 
    embed.add_field(name = "h!motivate", value = "motivates you") 
    embed.add_field(name = "h!rhyme", value = "gets rhyme") 
    
    #minigames
    
    #minigames
    embed.add_field(name = "h!diceroll", value = "rolls dice") 
    
    await context.send(content = None, embed = embed)







@client.command() 
async def bingme(context, *, usersearch):
    userarg = {"q":usersearch}
    link = requests.get("https://bing.com/search", params=userarg)


    soupLink  = BeautifulSoup(link.text, "html.parser")


    res = soupLink.find("ol",{"id" : "b_results"})


    chosen = res.findAll("li", {"class":"b_algo"})
   

    for obj in chosen[0:3]:
        objtxt = obj.find("a").text
        obj_href = obj.find("a").attrs["href"]
        await context.send(objtxt)
        await context.send(obj_href)
        


@client.command()
async def motivate(context, user:discord.Member):
    await context.send("DONT GIVE UP" + " https://www.youtube.com/watch?v=KxGRhd_iWuE ")




@client.command()
@commands.has_any_role('Bot Dev')
async def shutdown(context):
    await context.send("See ya, HPy gonna sleep now")
    await client.change_presence(activity=discord.Game(name='Currently Offline'), status=discord.Status.do_not_disturb)


#Moderation Commands
@client.command()
@commands.has_any_role('Admin')
async def delmsg (context, userarg):
    await context.channel.purge(limit = int(userarg))

@client.command()
async def rhyme(context, word, num):
    chosen_word = {"rel_rhy":word}

    request= requests.get('https://api.datamuse.com/words', chosen_word)

    json_rhyming = request.json()


    for each_rhyme in json_rhyming[0:int(num)]:
        await context.send(each_rhyme['word'])


@client.command()
@commands.has_any_role('Admin')
async def kickuser(context, user: discord.Member, *, userarg):
    await user.kick(reason = userarg)
    await context.send(f'Kicked {user.mention}')


@client.command()
@commands.has_any_role('Admin')
async def banuser(context, user: discord.Member, *, userarg):
    await user.ban(reason = userarg)
    await context.send(f'Banned {user.mention}')







client.run(t)
