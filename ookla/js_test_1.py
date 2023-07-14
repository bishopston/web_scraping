import re

from bs4 import BeautifulSoup

data = """
<script>
[other code]
var my = 'hello';
var name = 'hi';
var is = 'halo';
[other code]
</script>
"""

soup = BeautifulSoup(data, "html.parser")

pattern = re.compile(r"var name = '(.*?)';$", re.MULTILINE | re.DOTALL)
script = soup.find("script", text=pattern)

print(pattern.search(script.text).group(1))
