from datetime import datetime
import ssl
import OpenSSL

#thekey
key='MysecretMzZzH'

# encrypt
def encryptpass(text ,keys):
    if len(text)!=1:
        if len(keys)!=0:
            return (text[0]+keys[0]) + encryptpass(text[1:],keys[1:])
        elif len(text)!=0:
            keys=key
            return (text[0]+keys[0]) + encryptpass(text[1:],keys[1:])
        else:
            return keys
    else:                
        return text    

#getexpiredate
def getexpiredate(url):
    try:
        cert=ssl.get_server_certificate((url, 443))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        bytes=x509.get_notAfter()
        timestamp = bytes.decode('utf-8')
        expiredate=datetime.strptime(timestamp[0:timestamp.index('Z')], '%Y%m%d%H%M%S').strftime("%Y-%m-%d %H:%M")
        expiredate=datetime.strptime(expiredate,'%Y-%m-%d %H:%M')
        return expiredate
    except Exception as e:
        return None