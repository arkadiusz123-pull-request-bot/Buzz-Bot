import config
import error
import save
import buzzapi
from save import log as print

print("Initializing... ")
print("Wiping old logs...")
save.file_overwrite('saves/error.log', '')
save.file_overwrite('saves/main.log', '')
write_to_oldnumbers = []
print("Loading config...")
upstream = config.upstream
if not upstream or upstream == "":
    error.error_fatal("Upstream value blank or unsupplied.", "Upstream value blank or unsupplied.")
else:
    print("Loaded upstream")

downstream = config.downstream
if not downstream or downstream == "":
    error.error_fatal("Downstream value blank or unsupplied.", "Upstream value blank or unsupplied.")
else:
    print("Loaded downstream")

username = config.username
if not username or username == "":
    error.error_fatal("Username value blank or unsupplied.", "Upstream value blank or unsupplied.")
else:
    print("Loaded username")

password = config.password
if not password or password == "":
    error.error_fatal("Password value blank or unsupplied.", "Upstream value blank or unsupplied.")
else:
    print("Loaded password")

bot_repo = config
if not bot_repo or bot_repo == "":
    bot_repo = "https://github.com/CthulhuOnIce/Buzz-Bot"

print("Loading files...")
oldnumbers = save.file_2_list("saves/old_numbers.txt")
print("loaded saves/old_numbers.txt")

print("Requesting upstream json")
upstream_json = buzzapi.get_from_repo(upstream+"/pulls?per_page=100", username, password)

print("requesting downstream json")
downstream_json = buzzapi.get_from_repo(downstream+"/pulls?per_page=100", username, password)

count = 0
for x in upstream_json:
    if not str(x['id']) in oldnumbers:
        print("Merging PR - "+str(x['number']))

        # This is a mess, TODO: Fix this mess.
        request = {
            "title": "[MIRROR]: "+str(x['title']),

            "body": "Original Author: " + str(x["user"]["login"]) + "\n"
            + "Original PR Link: " + str(x["html_url"]) +
            "\n\n" + str(x["body"])+"\n\n\n<sub><sup>I am a bot, beep boop! [Download Me!]("+str(bot_repo)+") </sub></aup>",

            "head": x["head"]["label"],

            "base": "master",

            "maintainer_can_modify": False
        }

        # try again next time the script is run, should we hit a rate limit
        # this could also be caused by an invalid password
        ratelimitcheck = buzzapi.push_to_repo(downstream+"/pulls", username, password, request)

        try:
            void = ratelimitcheck['message']
            print(void)
            print("Couldn't mirror PR -- likely a rate limit, will be retried next runtime")

        except:
            write_to_oldnumbers.append(x['id'])
            print(ratelimitcheck['url'])
            count = count + 1

    else:
        write_to_oldnumbers.append(x['id'])
print("Merged "+str(count)+" Pr's")
save.file_overwrite('saves/old_numbers.txt', write_to_oldnumbers)
