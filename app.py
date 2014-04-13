from mcapi.profile import get_uuid, get_profile
from flask import Flask, jsonify

app = Flask(__name__)

with app.app_context():
    import local_config
    app.config.from_object(local_config)
    
    @app.route('/player/<string:playername>/')
    def getUUID(playername):
        profiles = get_uuid(playername)
        if profiles is not None and len(profiles) > 0:
            return jsonify(profiles[0])
    @app.route('/uuid/<string:uuid>/')
    def getName(uuid):
        profile = get_profile(uuid)
        if profile is not None:
            return jsonify(profile)

if __name__ == "__main__":
    app.run(
        host=app.config.get('HOST', None),
        port=app.config.get('PORT', None)
    )

