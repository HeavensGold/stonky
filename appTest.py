from stonky.api import Api
import sys

api = Api()

result = api.get_quote(sys.argv[1])
print(result)

