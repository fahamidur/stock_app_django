# myapp/management/commands/load_data.py
import json
from datetime import datetime
from django.core.management.base import BaseCommand
from myapp.models import StockData

class Command(BaseCommand):
    help = 'Load stock data from JSON file into the database'

    def handle(self, *args, **options):
        file_path = 'data/stock_market_data.json'  # Adjust the file path accordingly

        with open(file_path, 'r') as file:
            data = json.load(file)

            for entry in data:
                # Convert date string to datetime object
                entry_date = datetime.strptime(entry['date'], '%Y-%m-%d').date()

                # Remove commas from numeric fields before converting
                high_value = float(entry['high'].replace(',', ''))
                low_value = float(entry['low'].replace(',', ''))
                open_value = float(entry['open'].replace(',', ''))
                close_value = float(entry['close'].replace(',', ''))

                # Volume is an integer, so remove commas and convert
                volume_value = int(entry['volume'].replace(',', ''))

                # Create or update a StockData object
                StockData.objects.update_or_create(
                    date=entry_date,
                    trade_code=entry['trade_code'],
                    defaults={
                        'high': high_value,
                        'low': low_value,
                        'open': open_value,
                        'close': close_value,
                        'volume': volume_value,
                    }
                )

                self.stdout.write(self.style.SUCCESS(f'Data loaded: {entry_date}, {entry["trade_code"]}'))

        self.stdout.write(self.style.SUCCESS('Stock data loaded successfully'))
