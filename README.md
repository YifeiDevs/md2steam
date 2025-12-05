[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YifeiDevs/md2steam/blob/main/md2steam_demo.ipynb)

### Installing
```
pip install git+https://github.com/YifeiDevs/md2steam.git
```

### Example
```python
from md2steam import markdown_to_steam_with_tables

md_text = """
# Example Header

Text with **bold**, *italic* and [link](https://example.com).

| A | B |
|---|---|
| 1 | 2 |
"""

bbcode_text = markdown_to_steam_with_tables(md_text)
print(bbcode_text)
```

### Output
```
[h1]Example Header[/h1]

Text with [b]bold[/b], [i]italic[/i] and [url=https://example.com]link[/url].

[table]
[tr]
[th]A[/th]
[th]B[/th]
[/tr]
[tr]
[td]1[/td]
[td]2[/td]
[/tr]
[/table]
```
