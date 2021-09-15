# ModernMTG_Analysis
A multidimensional analysis of the Modern Format in Magic The Gathering

The goal of this project was to:
1. Learn through doing
2. Expand my knowledge of a game that I appreciate and play
3. Share that knowledge
4. Build my portfolio

All data gathered from https://mtgdecks.net/Modern and by extension https://www.cardhoarder.com/, https://www.cardkingdom.com/ and https://www.tcgplayer.com/.

This is by no means perfect, and I still learn each and every time I go back to this. I hope you enjoy and learn.

In the ever changing and hyper competitive meta of Magic: The Gathering, many destitute players find themselves making a tough decision: eat, or git gud? When the best decks are worth well over a thousand dollars, starving paperback jockeys look wherever they can to find value and still retain their sense of superiority. By analyzing the top deck archetypes in the Modern format, I believed I could find a  representative snapshot of the financial landscape of Magic: The Gathering.

I started this journey with a few basic questions.
1. What is the cheapest color to play in modern?
2. What is the cheapest converted mana cost?
3. Heck, what's the cheapest kind of deck to make???

I went to https://mtgdecks.net/Modern and found the top forty decks represented a significant majority of the meta, so I knew if I could analyze those deck archetypes, I could come to a solid conclusion. I then wrote a program that attempted to scrape the data from the website, but was unfairly and unjustly stopped by cloudflare protection. So instead I downloaded the webpage HTML of each deck archetype, and edited the code to scrape HTML locally -- which was fairly and justly successful.

The program I wrote scraped the Name, Name Length, Color, Converted Mana Cost and Rarity of each and every card played in the top forty decks in Modern MTG. It returned nearly 13,000 cards but after duplicates were deleted, only 2460 cards remained. With this data in hand and cleaned in Excel, I popped over the Tableu to visualize it. Ugly. Repulsive. Not fit for your average MTG art enjoyer. So I spent more time editing it by hand than I did programming, and truth be told it doesn't really show. I'm no artist or editor, but I hope you all appreciate it.

For those unfamaliar or need a refresher to understand the graph you are about to see:
  1. In Magic: The Gathering, almost every card costs Mana, a resource that is represented by five colors. Blue (U), Red (R), Black (B), Green (G) and White (W). 
  2. There is also "Generic Mana" which can come from *any* mana source and is usually a grey color. Let's take a look.

![color vs avg price v1 2](https://user-images.githubusercontent.com/86437248/133210189-6837ab3a-5ef6-40c3-b11c-3a345b890d6a.png)

As you can see, the cheapest mono-color to play is Red, the cheapest dual-color is Boros (Red/White) and the overall cheapest color combination to play is Abzan (Black/Green/White). Generally, the more varied the mana costs are, the harder it is to cast that card, therefore it is generally a much more powerful card. On top of that, multicolored cards are rarely Common or uncommonly Uncommon in rarity. It explains the abrupt jump in cost, as stronger cards are worth more. 

Speaking of rarity (not the mind melter of a sentence), I also extrapolated the rarity of each card and put it against the average price. As this graph isn't as loaded as the last,  I also included the count of each card that belongs to that specific rarity which is located below each bar.

To explain some of these prices before you see them for those unfamiliar or forgetful:
1. When you open a Magic: The Gathering booster pack physically, it will contain 15 cards. One basic land, ten common cards, three uncommon cards, and one is either a rare or mythic rare (you are less likely to open a mythic rare than a rare).

![avg Price vs Rarity v2 0](https://user-images.githubusercontent.com/86437248/133210901-3eda5c33-23df-4adc-abc3-0570243a6b77.png)

When I first saw this data, I was surprised as I expected the Commons to be cheaper, as most usually are worth less than an American quarter. However, because these commons belong to the best decks in the format, they are very good commons. Highly prized, but still common. 

Next, let's look at the converted mana cost of each card versus it's average price.
1. The "Converted Mana Cost" or "CMC" for short is the total amount of mana one would spend casting (aka playing) that card. 

![CMC vs Average Price 1 0 reverse gradient](https://user-images.githubusercontent.com/86437248/133364864-776d38b6-4d06-49d6-9711-b5eebd26c903.png)

Of the top 2460 cards, there were barely any that costed more than 6 mana. The few that are so mana-heavy break the bank, costing more than the previous numbers combined. These cards are powerful, and methods exist in the game to cast these spells *without* paying their mana cost. Otherwise, by the time you have enough mana to cast such spells, you would usually have lost the game.

Last but not least, a graph that helps nobody. You've already read this far, so you're forced to see the next one.

![name length vs average price 2](https://user-images.githubusercontent.com/86437248/133369055-262d3ec8-a42d-4c81-8a77-83fbef53befc.png)

As you can see, the cheapest cards in the game are the ones with the fewest letters. (Except for 31 characters, which is comprised of Sunhome, Fortress of the Legion and Asmoranomardicadaistinaculdacar.) 

So what do you do with this information? I'm not naiive enough to give any of you a concrete answer based on this data. The game I've been playing for more than 20 years now is far too nuanced to be 'solved' by analyzation. Sure, from the data you've seen here today, you could build an Abzan deck of the lowest CMC's possible with the shortest card names possible and all of the lowest rarity. You *could* build it, but you probably won't win with it. 

However, there is information to be gathered here. If you really are looking for ways not to break your bank and still get those dubs, a guide like this is a great place to start. As mentioned before, this analysis only took from the top FOURTY (40) deck archetypes in Modern MTG. Far more cards could be analyzed, but with the constraints I was placed under, most likely wouldn't have impacted the analysis in a major way.

In conclusion, use this data with a grain of salt, as creating a great deck requires many complex ingredients -- one of those ingredients being salt. Take a pinch of this analysis and use it when you craft your next deck, so you don't craft your way into bankruptcy.

Thank you.
