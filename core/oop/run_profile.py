# from profile   import Profile
'''
import class file profile.py as   import Profile
create a object in runanle file as runObj = Profile.UserProfile()   [UserProfile is class name in profile.py]
'''
from .profile import UserProfile

runObj = UserProfile()
runObj.display_name()
# print(__name__)
