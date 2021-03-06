import soundcloud
from util import hook
import re

@hook.api_key('soundcloud')

# create a client object with your app credentials
client = soundcloud.Client(client_id=api_key)

soundcloud_re = (r'(?:(https|http)?:\/\/(soundcloud.com)\/(.*)\/(.*))', re.I)

@hook.command('sc')
@hook.command
def soundcloud(search):
    "Usage: .soundcloud *trackname*"
    track = client.get('/tracks', q='search', order='hotness', streamable='true', limit=1)[0]
    return "*" + track.user["username"] + "*" + " | " + track.title + " | " + track.permalink_url

@hook.regex(*soundcloud_re)
def soundcloud_url(match):
    track = client.get('/resolve', url=match.group(0))
    return "*" + track.user["username"] + "*" + " | " + track.title
