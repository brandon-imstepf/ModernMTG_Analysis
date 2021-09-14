# ModernMTG_Analysis
A multidimensional analysis of the Modern Format in Magic The Gathering

The goal of this project was to:
1. Learn through doing
2. Expand my knowledge of a game that I appreciate and play
3. Share that knowledge
4. Build my portfolio

All data gathered from https://mtgdecks.net/Modern and by extension https://www.cardhoarder.com/, https://www.cardkingdom.com/ and https://www.tcgplayer.com/.

This is by no means perfect, and I still learn each and every time I go back to this. I hope you enjoy and learn.

In the ever changing and hyper competitive meta of Magic: The Gathering, many destitute players find themselves making a tough decision: eat, or git gud? When the best decks are worth well over a thousand dollars, starving paperback jockeys look wherever they can to find value and still retain their sense of superiority. Well my little cretins, look no further.

I started this journey with a few basic questions.
1. What is the cheapest color to play in modern?
2. What is the cheapest converted mana cost?
3. Heck, what's the cheapest kind of deck to make???

I went to https://mtgdecks.net/Modern and found the top forty decks represented a significant majority of the meta, so I knew if I could analyze those deck archetypes, I could come to a solid conclusion. I then wrote a program that attempted to scrape the data from the website, but was unfairly and unjustly stopped by cloudflare protection. So instead I downloaded the webpage HTML of each deck archetype, and edited the code to scrape HTML locally -- which was fairly and justly successful.

The program I wrote scraped the Name, Name Length, Color, Converted Mana Cost and Rarity of each and every card played in the top forty decks in Modern MTG. It returned nearly 13,000 cards but after duplicates were deleted, only 2460 cards remained. With this data in hand and cleaned in Excel, I popped over the Tableu to visualize it. Ugly. Repulsive. Not fit for your average MTG art enjoyer. So I spent more time editing it by hand than I did programming, and truth be told it doesn't really show. I'm no artist or editor, but I hope you all appreciate it.

For those unfamaliar or need a refresher to understand the graph you are about to see:
  In Magic: The Gathering, almost every card costs Mana, a resource that is represented by five colors. Blue (U), Red (R), Black (B), Green (G) and White (W). 
  There is also "Generic Mana" which can come from *any* mana source and is usually a grey color. Let's take a look.

![color vs avg price v1 2](https://user-images.githubusercontent.com/86437248/133210189-6837ab3a-5ef6-40c3-b11c-3a345b890d6a.png)

As you can see, the cheapest mono-color to play is Red, the cheapest dual-color is Boros (Red/White) and the overall cheapest color combination to play is Abzan (Black/Green/White). Generally, the more varied the mana costs are, the harder it is to cast that card, therefore it is generally a much more powerful card. It explains the abrupt jump in cost, as stronger cards are worth more.
To explain the abrupt jump in cost with multicolored cards:
  Multicolored cards are harder to cast, therefore they are generally more powerful than cards which cost the same *amount* of mana but in fewer colors.
  Multicolored cards are also almost never Common rarity, so they are fewer in number and harder to get out of your pack when you open it.

Speaking of rarity, here's something most of you already know: 

![avg Price vs Rarity v2 0](https://user-images.githubusercontent.com/86437248/133210901-3eda5c33-23df-4adc-abc3-0570243a6b77.png)

Here we see the price of the average card of each rarity.
