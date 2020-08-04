import discord
import random as rnd
from bs4 import BeautifulSoup
import requests
from discord.ext import commands
from datetime import date,datetime
import calendar

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
async def isFriday(context):
    today = date.today()
    if(calendar.day_name[today.weekday()] == 'Friday'):
        await context.send("ITS FRIDAYY")
        await context.send("https://tenor.com/view/yakuza-kazuma-kiryu-goro-majima-disco-friday-gif-16566350")
    else:
        await context.send("It's not Friday :c")
        await context.send("https://tenor.com/view/pepe-why-pepe-the-frog-sad-crying-gif-16026853")
@client.command()
async def currTime(context):
    now = datetime.now()
    currentDay = date.today()
    currDate = currentDay.strftime("Today is %B %d, %Y")
    time_and_day = now.strftime("Time : %H:%M:%S")

    await context.send(currDate)
    await context.send(time_and_day)


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
    embed.add_field(name = "h!invserver", value = "Creates a permanent server invite")
    embed.add_field(name = "h!currTime", value = "gives current time") 
    embed.add_field(name = "h!isFriday", value = "is it friday") 
    embed.add_field(name = "h!ipermInv", value = "gets a perm invite to server") 
    embed.add_field(name = "h!ezmath", value = "evaluate an expression") 
    await context.send(content = None, embed = embed)





@client.command()
async def ezmath(context,eqn):
    await context.send(eval(str(eqn)))


@client.command()
async def permInv(context):
    await context.send("your invite code")

@client.command()
async def gm (context):
    await context.send("Good morning quarantine kids, stay inside and stay alive")


@client.command()
async def gn(context):
    await context.send("Good night people, go sleep now")



@client.command()
@commands.has_any_role('insert role')
async def bingme(context, usersearch):
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
@commands.has_any_role('Tech Support')
async def shutdown(context):
    await context.send("See ya, HPy gonna sleep now")
    await client.change_presence(activity=discord.Game(name='Currently Offline'), status=discord.Status.do_not_disturb)


#Moderation Commands
@client.command()
@commands.has_any_role('insert role')
async def delmsg (context, userarg):
    await context.channel.purge(limit = int(userarg))


@client.command()
@commands.has_any_role('insert role')
async def kickuser(context, user: discord.Member, *, userarg):
    await user.kick(reason = userarg)
    await context.send(f'Kicked {user.mention}')


@client.command()
@commands.has_any_role('insert role')
async def banuser(context, user: discord.Member, *, userarg):
    await user.ban(reason = userarg)
    await context.send(f'Banned {user.mention}')


@client.command()
@commands.has_any_role('insert role')
async def getboing(context, user:discord.Member, userarg):
    if int(userarg) > 999:
        await context.send("Stop pinging too much")
    else:
        for i in range(int(userarg)):
            await context.send(f'Pinged,  {user.mention}')




client.run("your token goes here")
