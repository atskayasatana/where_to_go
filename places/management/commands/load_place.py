import os
import requests

from django.core.management.base import BaseCommand
from django.conf import settings
from places.models import Place, Image
from urllib.parse import urlparse


class Command(BaseCommand):
    help = 'Загрузка новой локации в базу из файла JSON по ссылке'

    def add_arguments(self, parser):
        parser.add_argument('json_url', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            new_location_request = requests.get(*options['json_url'])
            new_location_request.raise_for_status()
            new_location_info = new_location_request.json()
            title = new_location_info['title']
            image_links = new_location_info['imgs']
            description_short = new_location_info['description_short']
            description_long = new_location_info['description_long']
            latitude = new_location_info['coordinates']['lat']
            longtitude = new_location_info['coordinates']['lng']

            new_location, created = Place.objects.get_or_create(
                title=title,
                description_short=description_short,
                description_long=description_long,
                latitude=latitude,
                longtitude=longtitude
            )

            if created:
                image_upload_path = os.path.join(settings.MEDIA_DIR, title)
                os.mkdir(path=image_upload_path)
                position_number = 1
                for image_link in image_links:
                    image_response = requests.get(image_link)
                    image_response.raise_for_status()
                    image_name = os.path.basename(urlparse(image_link).path)
                    with open(os.path.join(image_upload_path,
                                           image_name), 'wb+') as image_file:
                        image_file.write(image_response.content)
                        new_image = Image.objects.create(
                            place=new_location,
                            position_number=position_number,
                            title=title
                            )
                        new_image.image.save(title, image_file, save=True)
                        position_number += 1

        except requests.exceptions.JSONDecodeError:
            print('JSON decoding Error')
        except requests.HTTPError:
            print('Ошибка в запросе')
        except requests.ConnectionError:
            print("Ошибка соединения")
