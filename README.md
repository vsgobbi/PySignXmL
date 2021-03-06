## Description
This lib was created in order to help users dealing with signed XML SOAP envelopes. PySignXML is intended to use with WebServices that requires certificate signatures values amongst the xml body.
It's features are extracting .CERT or .PEM files and PrivateKeys to add values on Signatures elements as ***SignatureValue*** and ***X509Certificate*** with ***rsa-sha1*** type, compliance with http://www.w3.org/2000/09/xmldsig. 
Sign a XML file or buffered String using A1 or A3 certificate. Serializes the data to request SOAP services. Creates POST requests on WebServices as NFe or NFSe.

## Table of Contents


- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)



<a href="https://gnu.org"><img src="https://www.gnu.org/graphics/gplv3-127x51.png" title="FVCproductions" alt="GPL"></a>

<!-- [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) -->
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger)
[![Coverage Status](http://img.shields.io/coveralls/badges/badgerbadgerbadger.svg?style=flat-square)](https://coveralls.io/r/badges/badgerbadgerbadger) 
[![Code Climate](http://img.shields.io/codeclimate/github/badges/badgerbadgerbadger.svg?style=flat-square)](https://codeclimate.com/github/badges/badgerbadgerbadger) 


---


## Installation

### Clone

### CLONE PROJECT
- Firstly, clone this repo to your local machine

```shell
git clone https://github.com/vsgobbi/PySignXmL.git
```
---

### INSTALL REQUIRED LIBS

- Install main libs
```shell     
pip install -r requirements.txt
``` 

## Features
> Using the following libs: 
- signxml, lxml, ElementTree

---


## Setup

### CREATE VENV

- Create virtualenv using Python2.7
```shell     
virtualenv -p python2.7 venv
```
- Activate the virtualenv
```shell     
source venv/bin/activate
```
- Verify if version is correct
```shell     
python --version #expected return: Python2.7
pip --version
```

---
## Usage

### Using PySignXML to sign a xml

#### How to use library:
```python
from SignXML import SignCert
# Works with .crt and .pem files
certificateFile = "path/To/Certificate/file.crt"
privatekeyFile = "path/To/Key/Key.pem"
cnpj = "012345678901"
objSignCert = SignCert()
# objSignCert.generateCert()
objSignCert.loadPem()
certContent = objSignCert.loadCert()
keyContent = objSignCert.loadKey()
```

#### How to sign a new xml:
```python
xmlEnvelope = "file.xml"
with open(xmlEnvelope, 'rb') as xmlEnvelope:
    xmlEnvelope=xmlEnvelope.read()
    # Simply sign
    objSignCert.signXML(xmlEnvelope)
# Sign with extended A1 certificate
signedRoot = objSignCert.signA1Cert(xmlEnvelope)
```


#### How to verify the signed xml file
```python
objSignCert.verifySignature(signedRoot)
```

#### How to post using signed xml:
```python
objRequestPost = PostXML("SP", cert=certificateFile, key=keyFile)
objRequestPost.consulta_cadastro(cnpj=cnpj)
objRequestPost.status_servico()
# In case of using "PREFEITURA Web Service"
objPostXMLPrefeitura = PostXML("PREFEITURA", cert=certificateFile, key=keyFile)
objPostXMLPrefeitura.consulta_cadastro(cnpj=cnpj)


# How to post using signed xml:

objRequestPost = PostXML("SP", cert=certificateFile, key=privatekeyFile)
objRequestPost.consulta_cadastro(cnpj=cnpj)

objPostXMLPrefeitura = PostXML("PREFEITURA", cert=certificateFile, key=privatekeyFile)
objPostXMLPrefeitura.consulta_cadastro(cnpj=cnpj)
```

---

## Contributing

#### Get started

- **Step 1**
    - 🍴 Fork this repo!

- **Step 2**
    - 🔨🔨 Clone this repo to your local machine using `https://github.com/vsgobbi/PySignXmL`

- **Step 3**
    - 🔃 Create a new pull request using <a href="https://github.com/vsgobbi/PySignXmL/compare/" target="_blank">`https://github.com/vsgobbi/PySignXmL/compare/`</a>

---

## FAQ

- **Questions?**
    - Direct me

---

## Support

Reach out to me at one of the following places!
### Vitor Sgobbi, 2019 
- E-mail at <a href="mailto:" target="_blank">`sgobbivitor@gmail.com`</a>
- Instagram at <a href="https://www.instagram.com/vsgobbi/" target="_blank">`@vsgobbi`</a>
- Facebook at <a href="https://www.facebook.com/vsgobbi" target="_blank">`@vsgobbi`</a>

---

## License

 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- **[GPL license](https://www.gnu.org/licenses/gpl-3.0)**
- Copyright 2019 © <a href="https://github.com/vsgobbi" target="_blank">Vitor Sgobbi</a>.
