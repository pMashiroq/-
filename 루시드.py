import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("루시드 활동중")


@client.event
async def on_message(message):
    if message.content.startswith("!루시드"):
        await message.channel.send("네 부르셨나요?")
    if message.content.startswith("!잘자"):
        await message.channel.send("네 편안한밤 되세요^^")
    if message.content.startswith("!바보"):
        await message.channel.send("꿈의 나라로 보내버립니다?^^")
    if message.content.startswith("!배고파"):
        await message.channel.send("식사 하고 오세요")
    if message.content.startswith("!안녕"):
        await message.channel.send("네~ 안녕하세요^^")
    if message.content.startswith("!심심해"):
        await message.channel.send("수면을 취하는거도 좋다 생각해요~")
    if message.content.startswith("!멍청이"):
        await message.channel.send("어머 꿈나라에서 누가 멍청이 인지 한번 볼가요^^?")
    if message.content.startswith("!힘들어"):
        await message.channel.send("힘들면 조금은 쉬면서 하세요")
    if message.content.startswith("!어때?"):
        await message.channel.send("저보다 약한놈한테 는 관심 없습니다.")
    if message.content.startswith("!뭐해?"):
        await message.channel.send("당신과 이야기 중입니다.")
    if message.content.startswith("!놀아줘"):
        await message.channel.send("꿈속의 성으로 와 주신다면 제 나비들이 놀아줄겁니다^^")
    if message.content.startswith("!검은 마법사"):
        await message.channel.send("하찮은 놈이 그분의 이름을 입에담지 마세요.")
    if message.content.startswith("!배부르다"):
        await message.channel.send("식사 맛있게 하셨나보네요^^")
    if message.content.startswith("!졸려"):
        await message.channel.send("당신의 꿈속에서 기다릴테니 주무세요^^")
    if message.content.startswith("!다녀올게"):
        await message.channel.send("기다릴테니 조심해서 다녀오세요~")
    if message.content.startswith("!일하기 싫다"):
        await message.channel.send("어머 일 하시나봐요 오늘하루도 힘내시고 조심히 다녀오세요~^^")
    if message.content.startswith("!작동 시간"):
        await message.channel.send("창조주 가 저를 계속 여기있게 해줄방법 을 찾고있어요^^")
    if message.content.startswith("!새로 왔어요"):
        await message.channel.send("어머 신입이군요 안녕하세요 군단장을 맡은 루시드 라 해요 잘 부탁드려요^^")
    if message.content.startswith("!아름다워"):
        await message.channel.send("저한테 그런말해도 아무것도 없습니다 0 .0")
    if message.content.startswith("!다녀왔어"):
        await message.channel.send("어머 다녀오셨어요?")
    if message.content.startswith("!끝났다"):
        await message.channel.send("수고했어요^^")
    if message.content.startswith("!하.."):
        await message.channel.send("힘내세요..")
    if message.content.startswith("!나 생일이야"):
        await message.channel.send("어머 생일이시군요 Happy Birthday 축하해요^^")
    if message.content.startswith("!노래해줘"):
        await message.channel.send("저는 질문답 봇이라 아야나상 이나 히드라상 을 이용 해주세요^^;;")
    if message.content.startswith("!도전장"):
        await message.channel.send("도전장 이라고여? 하하하 악몽의 가장 깊은 곳에서 당신을 기다릴게요")

client.run("NTczNDg4MTE5OTY2MzM0OTc5.XM0oQg.2YSDTCpeLhFIJTi84VeefYNu-Xs")
