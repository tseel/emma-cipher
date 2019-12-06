import discord

colors = {
           "red": 0xff0000,
           "blue": 0x0000ff,
           "green": 0x00ff00,
           "yellow": 0xf4ba2b,
           "black": 0x000000,
           "white": 0xffffff,
           "whiteblack": 0xffffff,
           "purple": 0x780199,
           "brown": 0x592b00,
           "colorless": 0x8c8c8c
         }

# takes a card and creates an embed with all that card's information
# returns the created embed
def card_embed(card):
    image_url = "https://fecipher.jp/wp-content/uploads/cards/images/" + card["Imagefile"]
    card_name = card["Name"]
    char = card_name.split(",")[0].replace(" ", "_").replace("Fodlan", "Fódlan")
    char_url = "https://serenesforest.net/wiki/index.php/" + char + "_(Cipher)"
    color = discord.Colour(colors[card["Color"].lower()])
    embed=discord.Embed(title=card["Name"], color=color, url=char_url)
    embed.set_thumbnail(url=image_url)
    embed.add_field(name="Attack", value=card["Attack"], inline=True)
    embed.add_field(name="Support", value=card["Support"], inline=True)
    embed.add_field(name="Color", value=card["Color"], inline=True)
    embed.add_field(name="Cost", value=card["Cost"], inline=True)
    embed.add_field(name="Set", value=card["Set"], inline=True)
    embed.add_field(name="Rarity", value=card["Rarity"], inline=True)
    embed.add_field(name="Range", value=card["Range"], inline=True)
    embed.add_field(name="Class", value=card["Class"], inline=True)
    embed.add_field(name="Type", value=card["Type"], inline=False)
    if card["Skill#1"] != "-":
        embed.add_field(name="Skill #1", value=card["Skill#1"], inline=False)
    if card["Skill#2"] != "-":
        embed.add_field(name="Skill #2", value=card["Skill#2"], inline=False)
    if card["Skill#3"] != "-":
        embed.add_field(name="Skill #3", value=card["Skill#3"], inline=False)
    if card["Skill#4"] != "-":
        embed.add_field(name="Support Skill", value=card["Skill#4"], inline=False)
    return embed


# takes a card and creates an embed with that card's name and image
# returns the created embed
def image_embed(card):
    image_url = "https://fecipher.jp/wp-content/uploads/cards/images/" + card["Imagefile"]
    color = discord.Colour(colors[card["Color"].lower()])
    e=discord.Embed(title=card["Name"], color=color)
    e.set_image(url=image_url)
    return e

# takes a dataframe of cards and builds an embed to prompt for selection
# returns the created embed
def selection_embed(cards, query, start=0):
    CARDS_PER_PAGE = 7
    embed = discord.Embed(title="Results", color=colors["colorless"])
    entries = list()
    end = min(start+CARDS_PER_PAGE, len(cards.index-1))
    for i in range(start, end):
        card = cards.iloc[[i]].iloc[0]
        ls_num = i+1
        ls_num = str(ls_num%CARDS_PER_PAGE if ls_num%CARDS_PER_PAGE != 0 else CARDS_PER_PAGE)
        entries.append("`" + ls_num + ")` " + " - ".join([card["Name"], card["Cost"], card["Set"]]))
    entries.append("`0)` Cancel")
    embed.add_field(name=query, value="\n".join(entries), inline=True)
    embed.set_footer(text="{0}/{1}".format((start//CARDS_PER_PAGE)+1, (len(cards.index)//CARDS_PER_PAGE)+1))
    return embed
