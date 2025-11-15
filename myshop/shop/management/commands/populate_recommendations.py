from django.core.management.base import BaseCommand
from shop.models import Product
from shop.recommender import Recommender


class Command(BaseCommand):
    help = 'Populate recommendation engine with sample data'
    
    def handle(self, *args, **options):
        # Get products
        pizza = Product.objects.get(title='Pizza')
        chicken_burger = Product.objects.get(title='Chicken Burger')
        chicken_roll = Product.objects.get(title='Chicken Roll')
        chicken_momo = Product.objects.get(title='Chicken Momo')
        large_fries = Product.objects.get(title='Large Fries')
        classic_coke = Product.objects.get(title='Classic Coke')
        coke_zero = Product.objects.get(title='Coke Zero')
        sprite = Product.objects.get(title='Sprite')
        monster = Product.objects.get(title='Monster')
        monster_white = Product.objects.get(title='Monster White')
        mirinda = Product.objects.get(title='Mirinda')
        fanta = Product.objects.get(title='Fanta')
        
        # Initialize recommender
        r = Recommender()
        
        # Add purchase patterns
        r.products_bought([pizza, classic_coke])
        r.products_bought([chicken_burger, large_fries, coke_zero])
        r.products_bought([chicken_roll, sprite])
        r.products_bought([chicken_momo, monster])
        r.products_bought([pizza, chicken_roll, fanta])
        r.products_bought([chicken_burger, large_fries, mirinda])
        r.products_bought([pizza, chicken_burger])
        r.products_bought([chicken_roll, chicken_momo])
        r.products_bought([large_fries, chicken_burger])
        r.products_bought([classic_coke, sprite])
        r.products_bought([monster, monster_white])
        r.products_bought([coke_zero, fanta, mirinda])
        r.products_bought([pizza, pizza, classic_coke])
        r.products_bought([chicken_burger, chicken_burger, large_fries])
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated recommendation engine with sample data')
        )