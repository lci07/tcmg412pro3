from urllib.request import urlretrieve

url_path = "https://s3.amazonaws.com/tcmg476/http_access_log"
local_file = 'local_copy.log'

local_file, headers = urlretrieve(url_path, local_file)