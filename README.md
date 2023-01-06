# Pro_xy
 Tor Proxy over socks using Python, Stem and Flask
 
 # Installation
- clone the repo
```cmd
git clone https://github.com/0-harshit-0/pro_xy.git
```
- install the necessary python libraries
```cmd
pip install flask stem requests argparse
```

# Setup
NOTE: in case of windows use 'py' instead of 'python3'

## Setting up tor
- open with default settings (port:65432 & MaxCircuitDirtiness:60)
```cmd
python3 tor.py
```
- opening on windows instad of linux
```cmd
python3 tor.py -pl 1
```

- open with different port (example: port:65000)
```cmd
python3 tor.py -p 65000
```

- open with different dirtiness (example: MaxCircuitDirtiness:30)
```cmd
python3 tor.py -t 30
```

- open with different combinations (example: MaxCircuitDirtiness:30, port:65000, platform:windows)
```cmd
python3 tor.py -pl 1 -p 65000 -t 30
```

## Setting up Flask(API)
- start flask application with default port (port:65432)
```cmd
python3 main.py
```

- start flask application with different port (65000)
```cmd
python3 main.py -p 65000
```

# Usage
TEST: Once the tor and flask application is up and running according to your configs, simply go to http://127.0.0.1:5000/v1/get?url=http://ip-api.com/json/ .If everything is working correctly you should see your tor's IP address info.

- to make a 'get' requests to 'https://somesite.com/somepath':
```url
http://127.0.0.1:5000/v1/get?url=https://somesite.com/somepath
```

- to make a 'post' requests to 'https://somesite.com/somepath' with data '{"somedata": 1}' and headers '{"Content-Type": "application/json"}'
```js
// js fetch
fetch("http://127.0.0.1:5000/v1/post", {
    method: "post",
    headers: {"content-type": "application/json"},
    body: JSON.stringify({"url": "https://somesite.com/somepath", "body": {"somedata": 1}, "headers": {"Content-Type": "application/json"}})
}).then(async res => {
    console.log(await res.text())
})
```


In case you are haveing some issues, raise an issue :stuck_out_tongue_winking_eye:
