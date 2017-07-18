import nrse_apat
from nrse_apat import get_app

app=get_app("init_db")

nrse_apat.database.init_db(app)
