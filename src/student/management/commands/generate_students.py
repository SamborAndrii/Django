from django.core.management.base import BaseCommand, CommandError
from src.student.models import Student

class Command(BaseCommand):
    help = 'Generate N students'

    def add_arguments(self, parser):
        parser.add_argument('num_students', default=100, type=int)

    def handle(self, *args, **options):
        num_students = options['num_students']
        try:
            for _ in range(num_students):
                Student.generate_dummy()

        except Exception as ex:
            raise CommandError('Generate students failed: "%s"' % ex)

        self.stdout.write(self.style.SUCCESS('Successfully generated %d students' % num_students))