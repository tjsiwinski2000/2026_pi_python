

# Source : C:\Users\TJ\source\repos\Project-Notes\CLASSES\images-for-projects\10152026
# Destination: C:\Users\TJ\source\repos\2026_pi_python\pp_project\media\animals


# python manage.py shell 
# from animals.models import Animal

# create string , copy to clipboard, 
# TOOD pause, or create a big output file.
# ToDo how to get fun facts
Animal.objects.create(
    name="seal",
    image="animals/seal-mammal.jpg",
    caption="seal",
    funfacts="They can very in weight from 45 kg (99.2 pounds) being the smallest or 3,850 kg (8487.7 pounds) being the heaviest.\nFemale seals typically have longer life spans of 30 years where the males live for 25.\nSeals can sleep underwater.\nSeals can hold their breath for 2 hours.\nBaby seals can put on 2kg or 4.4 pounds a day."
)