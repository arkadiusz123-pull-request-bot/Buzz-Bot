# config file, duh

# Your branch, ex: https://api.github.com/repos/beestation/beestation-13
downstream = "https://api.github.com/repos/Soldier101/Soldier101-Station"

# their branch; the branch you're mirroring FROM
upstream = "https://api.github.com/repos/tgstation/tgstation"

# your (or the bot's) github info
username = "you@example.com"  # email could also go here
password = "VerySecurePassword"  # password, duh


# The bot's master code repo, if you change the bot's code, YOU MUST ADD YOUR OWN REPO HERE, 
# Or you violate the license
repo = "https://github.com/arkadiusz123-pull-request-bot/Buzz-Bot"

# toggle extra features
make_Changelogs = True  # automatically generate a changelog based on the cl tags in pull requests. (WIP, not done yet)
debug_mode = False  # whether or not to display debugging info
