import json

talk_channels = [1032269058856472618,1032270687852838932,1032339192996450324]


#hay que reutilizar el codigo xd
#ADD PEOPLE TO LEVEL SYSTEM
def add_ppllvl(user, basexp = 0):
  with open("levels.json", "r") as f:
    users = json.load(f)

  if not f"{user.id}" in users:

    users[f"{user.id}"] = {}
    users[f"{user.id}"]["Exp"] = basexp
    users[f"{user.id}"]["Name"] = user.name

    with open("levels.json", "w") as f:
      json.dump(users, f, indent = 2)

#Add EXP
def add_xp(user, exp):
  with open("levels.json", "r") as f:
    users = json.load(f)

  if f"{user.id}" in users:
    users[f"{user.id}"]["Exp"] += int(exp)

    with open("levels.json", "w") as f:
      json.dump(users, f, indent = 2)

  else:
    add_ppllvl(user, int(exp))

#ActualLevelUser
def ActualLevel(user):
  with open("levels.json", "r") as f:
    file = json.load(f)  
  if f"{user.id}" in file:
    return file[f"{user.id}"]["Exp"] 
  else:
   add_ppllvl(user)
   return 0

#leaderboard
def leaderboardxp(server):
  users = []
  for member in server.members:
    for user in users:      
      if ActualLevel(member) >= ActualLevel(user) and not member in users:
        users.insert(users.index(user), member)
      elif user == users[-1] and not member in users:
        users.append(member) 
    if users == []:
      users.append(member)

  return users 
#Madre mia que funcion mas útil y bien escrita, ¿de donde la has sacado?
#lmao