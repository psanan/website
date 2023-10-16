Category: Computing
Date: 2023-10-11
Title: The best iTunes replacement is VLC and a filesystem

I really loved iTunes when it first arrived on the scene in the early 2000s.

It became less and less fun over time. It became bloated and slow and buggy.
I don't remember exactly when I decided it would be worth the effort
to find something else, but key factors were that my library file became corrupted
on several occasions, and syncing to my phone or ipod never seemed to work
as quickly as it should. I would think "oh, I'll just sync some music before
going running," and half an hour later I still wouldn't have the files,
somehow.

Even though it's not the most popular business model now, there are lots of people
like me who have large collections of audio files, and treasure them like
people with LP collections do.

I really hate the idea of streaming, of not owning my own record collection,
because it's too important to me to rent, and my experiences with iTunes
and pretty much any large, complicated piece of software is that it's
eventually going to stop working and I'm going to lose my data.

I don't, actually, hate streaming anymore. It's like the radio was,
but better. You can hear anything, anytime. No one is gate keeping what you can listen to.
It doesn't treat artists well, though, so I think streaming needs to be a tool for discovery,
and you need to buy and own the stuff you really like and/or go to the artist's shows.
What I hate is the idea that streaming services are a way to manage your music collection -
I think that's a mistake.

Fortunately, there is bandcamp! I very much hope they stay as high quality as they have been,
despite a couple of recent changes in ownership. The point is that they don't have
to stick around for me to be happy to pay, them, though. They are selling
me normal audio files. I use their site for exploration, just like the streaming
sites. If and when they stop being useful, I hope there will be another way to
get audio files by paying the artists as directly as possible.

I digress, though. Since I've argued about how great it is to have all these files,
how are you going to play them?

You can probably still use Apple's Music.app (which is what iTunes turned into).
I've been burned too many times, though, to really consider it.

So I started looking for a better way. I tried a lot of stuff, so I'll recap some of it.

My general desires were:
- something simple enough for me to feel like I understand what it's doing
- ideally something FOSS
- Control my data. In particular, I want to be able to move it between players and interact with it as normal files, without being locked into a non portable or non standard data format.
- I want to control when data is transferred. I  don't want anymore "why isn't it syncing?" questions which i can't resolve, as I hope that various opaque and constantly-updating apps might work.
- A way to manage a large collection of playlists (in folders)
- To play all common audio formats, mostly mp3 and FLAC files.
- Some way to get music to my phone
- Convenient UIs to play music using the convenience of the operating system

I started out with mpd and ncmpcpp. This was quite fun, and these are nice tools,
as they will work *anywhere* (e.g. I got them runnin on a Raspberry Pi once).

However, as much as I love the no-mouse experience for almost everything, I want some point and click, here.
I want to be able to do things one handed while a party is going on.

I really liked the playlists in iTunes.
I haven't found anything that has playlists like iTunes does, in the sense that you
can have many of them, nested in directories, and you can be playing from any one of them,
not just some master playlist which you load in and out of.

I like a lot about Strawberry, but ultimately abanonded it for very similar reasons to ncmpcpp.
Playlists are still annoying, there is still a big slow-to-update database, and perhaps most importantly
it isn't well supported on Mac OS which I mostly use, day to day (e.g. I was very surprised there
was no search bar on the library before checking to find that this is due to a Qt bug).

I also like a lot about beets. This is just for organizing, though, and again, having
to deal with an opaque database just seemed like more trouble than it was worth.

When one is forced to get into scripting to do things like find and edit metadata,
ffmpeg (even when one has to scan through entire audio files) is the most useful tool.

I haven't looked heavily into full media system solutions like Plexamp or Jellyfin,
as they seem likely to be very complex, and I'm not looking for portability to arbitrary
devices, just being able to play some files and playlists on a couple.


So what am I using now?

## Local player - VLC

Locally (on my Apple laptop), the answer was in front of me the whole time: VLC.

This is built for videos, but (like ffmpeg) to have robust video support you need
robust audio support, and VLC can play anything. It's maintained by a veritable
army of French people, it's FOSS, it's available everywhere, and it's used
by huge numbers of people.

While VLC does have some sort of integrated media library, I am not using it.

There is no special database! It is really just this:
- My music directory, organized by (album) artist, then album.
- A directory of playlists, m3u files with lists of absolute paths into the music directory

This is enough for me. Even with iTunes, the overwhelming majority of the time
I navigated to music by artist, then album, or through playlists.

This is really nice in a lot of ways. My data is not specific to the player (VLC).
I already know how to do a lot with a file
system and text files. I can search, navigate, track (with git), back up, and
write scripts if it comes to that.


It's so simple that it's very portabile: the music files are standard music files,
and m3u files are just text files with lists of music files.

I can organize my library and playlists with standard tools I already know.
The music library is just directories and files. I can edit the playlists
with any text editor.

A very useful feature of Mac OS: open up TextEdit, and drag a file into it. The full file path appears!
You can build playlists from files this way. To build playlists from other playlists, you
can copy from text files. To build playlists from items in the VLC current playlist, the easiest is probably "Show in Finder"
and then drag the file into a text file.


VLC only has one playlist, which you can load tracks and m3us into. You can save the whole thing as an m3u.
This saves URIs, which is fine for VLC but creates some extra work later with my mobile scripts.
I would love the old iTunes experience, in which I created so many fun lists, but this way works
okay, there is no waiting around for a database, and I'm not locked into anything.

You can view and edit track metadata right in VLC.

For ratings, I just edit the comment fields of the files, adding 1 to 5 asterisks.
The purist in me sees this as very ugly. The media should be immutable, and
my personal usage of them should rely on data stored elsewhere. I'm ruining
checksums by editing files! But, there is nothing that I know of that relies
on comment fields, and the advantages of not having any auxiliary database are worth it.

There are some minor pain points due to the lack of any database.

File names may be such that
it may not be totally obvious what a given track is before you open it
(note you can make VLC the default to open audio and m3u files in Mac OS).
Searching the library by metadata may require some auxiliary tool.
If this ever really becomes an issue, I might look to a tool like Beets which helps clean up and
index a music collection, or perhaps VLC (or VLC 4) can do this with it's media library features.

Renaming or moving files also isn't so easy - if you do this you will break playlists unless you
update your m3u files.

Similarly, since I rely on absolute paths, I have a script to change the roots of all
paths in the m3u files (which I needed anyway for the mobile player approach below).
You could probably avoid this issue
by linking your media directory to a fixed path, and just updating the link if you
move your library.

There are lots of nice-to-haves that aren't here.
No play counts, recently played, or recently added information.
I don't miss these as much as I thought I might - probably because now that it's
so easy to hear almost any track I want a few times via streaming,
I'm only adding things to my library once I already like them to some extent,
so I know which playlist to add it to. (For instance, I have a monthly playlist
for whatever I come across that I like).


VLC 4 promises a big overhaul of the UI and may become more useful, or
might become more bloated - let's see. I assume that my existing minimalist workflow will
still work, and if it doesn't, there are plenty of ways to play m3u files.
(It also promises gapless playback!)


## Mobile player - Syncthing, Poweramp, and scripts

This is one of the "how is so hard?" topics. A phone is a little computer, right,
and computers can play audio files, right? So can I put my audio files on
my little pocket computer and listen to them?

I struggled so much to do this that I got an Android phone (Fairphone 4) when
my iPhone died.

The officially supported file transfer solution for Android is horrendous. Stay away.

Fortunately there is SyncThing. This solved the problem of
getting files to and from the phone.

To play music on the phone, I paid for the excellent PowerAmp (note there is a non-Google Play version).
This understands m3us with path relative to the directory they're in.

To generate the payload of music files and playlist files for the phone, I
had to do quite a bit of scripting.

Roughly, I start with a list of playlists from the playlists folder (which is
programmatically generated - many of playlists ahve the year in them, so I can
get all those fomr the current year, for example). Then, scripts run through all those playlists,
copying the required subset of music files to a staging location. The playlists themselves
are also saved there, after processing to remove prefixes from the paths, and convert any URIs to plain
file paths.

Once that's done, syncthing is used to sync the staging folder to the phone.
(Unfortunately, syncthing can't be running at the same time as the scripts).

I should note that there is a place for streaming, here. I stream things
on my phone all the time when discovering new music. But nothing is like
having my favorite files actually on the phone.
