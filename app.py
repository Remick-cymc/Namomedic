from flask import *
from flask_restful import Api


app = Flask(__name__)

# make the app an api
api = Api(app)

from view.views import MemberSignup,MembersSignin,memberprofile

api.add_resource(MemberSignup, "/api/member_signup")
api.add_resource(MembersSignin, "/api/member_signin")
api.add_resource(memberprofile, "/api/member_profile")

if __name__ =='__main__':
    app.run(debug=True)