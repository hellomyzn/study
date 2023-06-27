"""
絶対パスと相対パスのURL
"""

print("standardLibrary:",__name__)

import lesson_package.talk.animal

lesson_package.talk.animal.sing()
print("lesson:", __name__)
