
import discord
import asyncio
import random
import datetime
import os


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("--------------------")
    await client.change_presence(game=discord.Game(name='!도움말 / 팀나누기,투표용 봇', type=1))


@client.event
async def on_message(message):
    if message.content.startswith('!도움말'):
       await client.send_message(message.channel, " ```이 봇은 클랜Supreme에서 자체적으로 개발한 봇입니다.\n많은 이용 부탁드립니다.\n\n\n팀나누기 = !팀나누기 멤버1 멤버2/팀번호1 팀번호2\n\n투표 = !투표 투표내용/투표목록1/투표목록2\n\n주사위 = !주사위 2x6 (6면체 주사위를 2번 굴려라)\n\n골라 = !골라 짜장면 짬뽕\n\n음식추천 = !뭐먹지\n\n관리자호출 = !관리자\n\n도움말에 없는 숨겨진 명령어를 찾으면 소정의상품증정(베라싱글기프트콘)힌트는 관리자에게 DM ``` ")

    if message.content.startswith('!인재는잘생김'):
        await client.send_message(message.channel, "인정")

    if message.content.startswith('!개미새끼'):
        await client.send_message(message.channel, "노답")

    if message.content.startswith('!Supreme'):
        await client.send_message(message.channel, "화이팅!")

    if message.content.startswith('!다정이는귀엽다'):
        await client.send_message(message.channel, "인정")

    if message.content.startswith("!팀나누기"):
        team = message.content[6:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await client.send_message(message.channel, "  " + person[i] + "  " + " ➡ " + "  " + teamname[i] + "  ")

    if message.content.startswith("!투표"):
        vote = message.content[4:].split("/")
        await client.send_message(message.channel, "★투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await client.send_message(message.channel, "```" + vote[i] + "```")
            await client.add_reaction(choose, '👍')

    if message.content.startswith('!정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!주사위'):
        roll = message.content.split(" ")
        rollx = roll[1].split("x")
        dice = 0
        for i in range(1, int(rollx[0])+1):
            dice = dice + random.randint(1, int(rollx[1]))
        await client.send_message(message.channel, str(dice))

    if message.content.startswith('!골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, choiceresult)

    if message.content.startswith('!뭐먹지'):
        food = "짜장면 짬뽕 라면 밥 굶기 제육볶음 김밥 떡볶이 만두 순대 김치찌개 된장찌개 월남쌈 닭발 곱창 찜닭 햄버거 족발 보쌈 초밥 연어 고추장찌개 치킨 소고기 갈비 부대찌개 콩비지찌개 콩나물국 음료수 젤리 사탕 초콜릿 과자 빵 꼬막 삼겹살 소갈비 굴비 샥스핀 해파리냉채 김치전 감자탕 유산슬 떡갈비 3분카레 3분짜장 스테이크 함박스테이크 미트볼 계란후라이"
        foodchoice = food.split(" ")
        foodnember = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnember-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith('!관리자'):
        dd = "<@346287576237342720> <@370973274320011275>"
        choice = dd.split(" ")
        nember = random.randint(1, len(choice))
        result = choice[nember-1]
        await client.send_message(message.channel, result)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
