from flask import *
from flask_restful import Api


app = Flask(__name__)

# make the app an api
api = Api(app)

from view.views import MemberSignup,MembersSignin,memberprofile, AddDependants,ViewDependants,ViewLabTests,Bookings

api.add_resource(MemberSignup, "/api/member_signup")
api.add_resource(MembersSignin, "/api/member_signin")
api.add_resource(memberprofile, "/api/member_profile")
api.add_resource(AddDependants,"/api/add_dependants")
api.add_resource(ViewDependants,"/api/view_dependants")
api.add_resource(ViewLabTests,"/api/viewlab_test")
api.add_resource(Bookings,"/api/bookings")


if __name__ =='__main__':
    app.run(debug=True)