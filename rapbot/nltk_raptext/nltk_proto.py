import nltk

from nltk.tokenize import word_tokenize

text = "Aw, yeah It's Eminem, baby
Back up in that motherfuckin' ass
One time for your motherfuckin' mind
We represent the 313—you know what I’m sayin'?
Yo, they don’t know shit about this, for the '96
Ayo, my pen and paper cause a chain reaction
To get your brain relaxin', the zany actin' maniac in action
A brainiac, in fact, son, you mainly lack attraction
You look insanely wack when just a fraction of my tracks runs
My rhymin' skills got you climbin' hills
I travel through your mind and chill your spine like siren drills
I'm slimin' grills of roaches with spray that disinfects
And twistin' necks of rappers 'til their spinal column disconnects
Put this in decks and check the monologue, turn your system up
Twist 'em up and indulge in the marijuana smog
This is the season for noise pollution contamination
Examination of more car-tunes than animation
My lamination of nar-er-ration, hits a snare and bass
On a track for duck rapper interrogation
When I declare invasion, there ain't no time to be starin' gazin'
I turn the stage into a barren wasteland
Bust it, I let the beat commence
So I can beat the sense in your elite defense
I got some meat to mince
Some fruit to stomp, and then two feet to rinse
I greet the gents and ladies, I spoil loyal fans
I foil plans and leave fluids leakin' like oil pans
My coiled hands around this microphone are lethal
One thought in my cerebral is deeper than a jeep-full of people
MC's are feeble, I came to cause some pandemonium
Battle a band of phony MC's and stand the lonely one
Imitator intimidator, stimulator
Simulator of data, eliminator
There's never been a greater since the burial of Jesus
Fuck around and catch all the venereal diseases
My thesis'll smash a stereo to pieces
My acappella releases classic masterpieces, through telekinesis
It eases you mentally, gently
Sentimentally, instrumentally
With entity, dementedly meant to be infinite
Man, I got evidence, I'm never dense
And I've been clever ever since
My residence was hesitant to do some shit that represents the MO
So I'm assumin' all responsibility
'Cause there's a monster real in me that always wants to kill MC's
Mic nestler, slammin' like a wrestler
Here to make a mess of a lyric-smugglin' embezzler
No one is specialer, my skill is intergialactical
I get cynical, act a fool then I send a crew back to school
I never packed a tool or acted cool, it wasn't practical
I'd rather let a tactical, tactful track tickle your fancy
In fact, I can't see, or can't imagine
A man who ain't a lover of beats or a fan of scratchin'
So this is for my family, the kid who had a cameo
On my last jam plus the man who never had a plan B
Be all you can be
‘Cause once you make an instant hit, I'm tensed a bit
And tempted when I see the sins my friends commit"

tokens = word_tokenize(text)
print(tokens)

# define a function with parts of tokenized speech
#def tokenized():
#    text = tokenize(text)
