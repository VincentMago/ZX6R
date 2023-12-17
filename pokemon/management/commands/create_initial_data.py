# your_app/management/commands/create_initial_data.py
 
from django.core.management.base import BaseCommand
from cardquest.models import PokemonCard, Trainer
 
 
class Command(BaseCommand):
 help = 'Creates initial data for the application' #<-- description of the command
 
def handle(self, *args, **kwargs):
 self.create_pokemon_cards() # <-- where logic is implemented
 # self.create_trainers()
 
def create_pokemon_cards(self):
 # Create Pokemon Card instances
 card1 = PokemonCard(name="Pikachu", rarity="Rare", hp=60, card_type="Electric", attack="Thunder Shock", description="A mouse-like pokemon that can generate electricity.", weakness="Ground", card_number=25, release_date="1999-01-09", evolution_stage="Basic", abilities="Static")
 card1 = PokemonCard("Pikachu", "Rare", 60, ["Electric"], "Thunder Shock", "A mouse-like pokemon that can generate electricity.", ["Ground"], 25, "Basic", ["Static"])
 card2 = PokemonCard(name="Torchic", rarity="Common", hp=50, card_type="Fire", attack="Reckless Charge", description="a small, chick Pokémon with stubby, downy, yellow wings.", weakness="Rock, Ground, Water", card_number=14, release_date="2012-05-o9", evolution_stage="Basic", abilities="Blaze")
 card2 = PokemonCard("Torchic", "Common", 50, ["Fire"], "Reckless Charge", "a small, chick Pokémon with stubby, downy, yellow wings.", ["Rock, Ground, Water"], 14, "Basic", ["Blaze"] )
 card3 = PokemonCard(name="Lucario", rarity="Holo Rare", hp=120, card_type="Fighting", attack="Aura Sphere Volley", description="Blue, steel-fighting Pokemon with aura sensing powers.", weakness="Ground, Fire", card_number=79, release_date="2023-10-26", evolution_stage="Basic", abilities="Roaring Reslove")
 card3= PokemonCard("Lucario", "Holo Rare", 120, "Fighting", "Aura Sphere Volley", "Blue, steel-fighting Pokemon with aura sensing powers.",["Ground, Fire"], 79, "Basic", "Roaring Resolve")
 card1.save() #<-- save card1 to PokemonCard table
 card2.save()
 card3.save()
 self.stdout.write(self.style.SUCCESS('Successfully created Pokemon cards.')) #<-- display success message
 
def create_trainers(self):
 pass