import os
import sys

# Aggiungi il percorso al progetto
path = '/home/tuousername/fidelity-card-project'
if path not in sys.path:
    sys.path.append(path)

# Imposta le variabili d'ambiente
os.environ['DJANGO_SETTINGS_MODULE'] = 'fidelity_card_project.settings'

# Configura Stripe (importante!)
os.environ['STRIPE_SECRET_KEY'] = '51R7so3IXriYxpAfDr2El37AaxeWeaj8oWswkb2cyGlG11wzZFLd6LpfZRnRFmTQM5QDx4aWCQuqkX9jjSb0huYPl00mzFJhuzS'
os.environ['VITE_STRIPE_PUBLIC_KEY'] = '51R7so3IXriYxpAfDlTGUIkSBP1QlkqYsNCd19emBp235Wr7s4lVA8s1NuyIFpyXygL5kEUWMURSHwjO202ZVfhrG00ZTomwiFl'

# Attiva l'applicazione Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()