#0507-2026
#Django finds this file  automatically through the management/commands/ folder structure.
#SYTNAX: python manage.py seed

from django.core.management.base import BaseCommand
from hangman.models import HangmanWord
RAW = ['undeservedkindness:By means of ______    _______ (two words) God brings salvation to all sorts of men (Tit 2.11), something that the prophets had spoken about. (1Pe 1.10) Replaced the Mosaic Law:hard',
'propitiatory:And he is a __________ sacrifice for our sins, yet not for ours only but also for the whole world’s:hard',
'Uzziah:Became famous for his military successes, attained with Jehovah’s help. Sad ending...High Priest Azariah, accompanied by 80 underpriests, immediately followed the king into the temple and censured him for an  unlawful act resulting in leprosy until the day of his death:hard',
'magnify:As time passes the distorted lens of imperfection could cause us to ________________ 🔎 the faults of our brothers instead of looking their overall spiritual qualities [WT03.15.2008 Do You View Others As Jehovah Does?]:hard',
'weight:Something that is self imposed, we have control, [Branch Visit 0419-2026]:hard',
'burden:Something that is imposed by devil and his world, makes us tired,[Branch Visit 0419-2026]:hard',
'load:Something we all need to carry (Galatians 6.5), our responsibility before God for our decisions and actions:hard',
'unreasonable:God has tender love for us and does not place _______________ demands on us [WT08.15.2004 Tired But Not Tiring Out]:hard',
'timeless:The Bible books of Proverbs and Ecclesiastes, which are part of the Hebrew Scriptures, contain ________ wisdom for living [hint ❌⌚] [JW.org FAQ]:hard',
'torah:The first five books of the Bible, five letters:hard',
'hearts:The Kingdom of God is is a real government in heaven, not a condition in the _________ of Christians:hard',
'name:Lift up your eyes to heaven and see. Who has created these things? It is the One who brings out their army by number; he calls them all by ________ Isaiah 40:26:hard',
'Jupiter:Earth benefits from a distant but giant protector​ the planet________ [Draw Close Chapter5]:hard',
'watercycle:All the streams flow into the sea, yet the sea is not full. To the place from which the streams flow, there they return so as to flow again, [Ecl1.7] this verse describes what scientific fact? [hint 🔁] [Draw Close Chapter5]:hard',
'wisdom:________ is not the same as knowledge. Computers can store enormous amounts of knowledge, but they dont have ___________. Nonetheless, knowledge and ________ are related. Accurate knowledge is essential to true __________. [Draw Close Chapter17]:hard',
'libraries:Scientists say that a human brain could contain all the information in all the worlds ___________ [Draw Close Chapter17]:hard'
]

#0503-2026 one time use script to populate database with hangman words
class Command(BaseCommand):
    help = 'Seed the HangmanWord table from raw colon-separated list'

    def handle(self, *args, **kwargs):
        created = 0
        for entry in RAW:
            word, hint, difficulty = entry.split(':', 2)
            HangmanWord.objects.create(word=word, hint=hint, difficulty=difficulty)
            created += 1

        self.stdout.write(
            self.style.SUCCESS(f'Done: {created} words added.')
        )