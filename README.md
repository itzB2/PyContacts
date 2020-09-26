##### Bascically i guess it is a Python Library for contacts like gmail vcard and and stuff.

##### Like when bass go boom boom.

##### U, not me. import the module named vcard by just importinig it easy as it sounds like this example

```from contacts import vcard```
to create a card you simply write:
```python
from contacts import vcard

card = vcard.VCard(path)
card.create(display_name:list, full_name:str, number:str, email:str=None)
```
to read a card you simply write:
```python
from contacts import vcard

card = vcard.VCard(path)
card.read(att:str)
```
The (attributes or att) are
```python
{"name":"The display name", "full_name":"The full name", "number":"the number", "email":" the email"}
```
or you can do the dot value
```python
from contacts import vcard

card = vcard.VCard(path)
theName = card.name
theNumber = card.number
theFullName = card.fullName
theEmail = card.email
```

##### Gmail thing

```python
from contacts import gmail

mail = gmail.Gmail(email, password)
```
You can register stuff, no worries everything is pickled
```python
from contacts import gmail

mail = gmail.Gmail(email, password)
mail.register('name')
```
and then u can load the the email and password with the load command
```python
from contacts import gmail

mail = gmail.Gmail()
mail.load('name')
```
u can get all the registerd members by doing
```python
from contacts import gmail

mail = gmail.Gmail()
mail.memberList()
```
add messages by doing
```python
from contacts import gmail

mail = gmail.Gmail()
mail.load('name')
mail.setMessage(subject, to)
```
content by doing
```python
from contacts import gmail

mail = gmail.Gmail()
mail.setContent(content)
```
attachment by
```python
from contacts import gmail

mail = gmail.Gmail()
mail.load('name')
mail.addAttachment(path:list, types:list)
```
path is obviously the path. in types you can only put images or pdf in uppercase or lowercase like this example
```python
from contacts import gmail

mail = gmail.Gmail()
mail.addAttachment(["test.jpg", "test.pdf"], ["image", "PDF"])
```
add html i think you know this already but you are only allowed to use inline styles or in html css
```python
from contacts import gmail

mail = gmail.Gmail()
mail.load('name')
mail.addHTML(path)
```
login this is obvious 
```python
from contacts import gmail

mail = gmail.Gmail()
mail.load('name')
mail.login()
```
send message just send it
```python
from contacts import gmail

mail = gmail.Gmail()
mail.load('name')
mail.login()
mail.sendMessage()
```