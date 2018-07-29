import config
import error
import save
import buzzapi

# run this file before running main.py for the first time

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

print("Requesting upstream json")
upstream_json = buzzapi.get_from_repo(upstream+"/pulls?per_page=100", username, password)

for x in upstream_json:
    write_to_oldnumbers.append(x['id'])

save.file_overwrite('saves/old_numbers.txt', write_to_oldnumbers)
